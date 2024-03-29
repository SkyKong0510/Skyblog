import logging
from flask import Flask
from config import Config#从config模块导入Config类
# from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy#从包中导入类
from logging.handlers import RotatingFileHandler
from flask_moment import Moment
import os

app = Flask(__name__)

db = SQLAlchemy(app)  # 数据库对象
if not app.debug:
    app.config.from_object(Config)
    migrate = Migrate(app, db)  # 迁移引擎对象
    login = LoginManager(app)
    login.login_view = 'login'
    # mail = Mail(app)
    bootstrap = Bootstrap(app)
    moment = Moment(app)
    if not os.path.exists('logs'):
        os.mkdir('logs')
    file_handler = RotatingFileHandler('logs/microblog.log', maxBytes=10240,backupCount=10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('Microblog startup')

from app import routes,models,errors