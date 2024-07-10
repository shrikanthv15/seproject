from flask import Flask
from func.auth import auth_bp, configure_auth
from func.models import configure_database, db
from flask_restful import Api
from func.announcements import announcements_bp
from func.lectures import lectures_bp
from func.documents import documents_bp
from func.user import user_bp
from func.admin import admin_bp
from func.support import support_bp
from flask_cors import CORS
from celery import Celery   
from func.configmail import configure_mail

# def make_celery(app):
#     celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
#     celery.conf.update(app.config)
#     celery.conf.imports = ('func.reports',)
#     TaskBase = celery.Task

#     class ContextTask(TaskBase):
#         abstract = True

#         def __call__(self, *args, **kwargs):
#             with app.app_context():
#                 return TaskBase.__call__(self, *args, **kwargs)
#     celery.Task = ContextTask
#     return celery

app = Flask(__name__)
CORS(app)
app.register_blueprint(auth_bp)
app.register_blueprint(announcements_bp)
app.register_blueprint(lectures_bp)
app.register_blueprint(documents_bp)
app.register_blueprint(user_bp)
app.register_blueprint(admin_bp)
app.register_blueprint(support_bp)
app.config.update(
    CELERY_BROKER_URL='redis://localhost:6379/1',
    result_backend='redis://localhost:6379/2',
    broker_connection_retry_on_startup=True,
    timezone="Asia/Kolkata"
)

with app.app_context():
    configure_auth(app)
    configure_database(app)
    configure_mail(app)
    celery_app = make_celery(app)
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)
