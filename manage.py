
from flask import Flask,session
from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager
from apis.analysisapi import analysis
from apis.noteapi import note
from database import db,User
import config
from apis.userapi import user
from apis.indexapi import index
from apis.crawlapi import crawl


app = Flask(__name__)
#设置
app.config.from_object(config)
#数据库
db.init_app(app)

# db.create_all(app=app)

#用于数据迁移，生成表，更新
migrate = Migrate()
migrate.init_app(app=app, db=db)
#蓝图注册，初始化
app.register_blueprint(blueprint=user)
app.register_blueprint(blueprint=index)
app.register_blueprint(blueprint=crawl)
app.register_blueprint(blueprint=analysis)
app.register_blueprint(blueprint=note)
#管理
manager = Manager(app=app)

manager.add_command('db', MigrateCommand)


@app.context_processor
def my_context_processor():
    user_id = session.get('user_id')
    if user_id:
        user = User.query.filter(User.id == user_id).first()

        if user:
            return {'user':user}
    return {}


if __name__ == '__main__':
    manager.run()



