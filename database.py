
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import check_password_hash, generate_password_hash

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    email = db.Column(db.String(50), unique=True)

    username = db.Column(db.String(50), unique=True)

    password = db.Column(db.String(256))

    is_activate = db.Column(db.Boolean, default=False)

    is_delete = db.Column(db.Boolean, default=False)

    def model_to_dict(self):
        return {"id":self.id, "name":self.u_name, "email":self.u_email, "password":self.u_password}

    #flask自带加密编码
    def set_password(self, password):
        self.u_password = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.u_password, password)

    def check_permission(self, permission):
        return self.u_permission & permission == permission


#帖子
class Note(db.Model):
    __tablename__ = 'note'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    title = db.Column(db.String(64), nullable=False)

    content = db.Column(db.Text, nullable=False)

    create_time = db.Column(db.DateTime, default=datetime.now, index=True)

    author_id = db.Column(db.Integer,db.ForeignKey('user.id'))


    author = db.relationship('User', backref=db.backref('notes'))


#评论
class Comment(db.Model):
    __tablename__ = 'comment'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    content = db.Column(db.Text, nullable=False)

    note_id = db.Column(db.Integer, db.ForeignKey('note.id'))

    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))

    create_time = db.Column(db.DateTime, default=datetime.now, index=True)


    note = db.relationship('Note', backref=db.backref('comments', order_by = id.desc()))

    author = db.relationship('User', backref=db.backref('comments'))


class Adcode(db.Model):
    __tablename__ = 'adcode'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    city = db.Column(db.String(50), nullable=False)

    adcode = db.Column(db.Integer, nullable=False)


class Scenecode(db.Model):
    __tablename__ = 'scenecode'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)

    scene = db.Column(db.String(50), nullable=False)

    scenecode = db.Column(db.Integer, nullable=False)


class ScrapeMissions(db.Model):
    __tablename__ = 'scrape_missions'

    id = db.Column(db.Integer, autoincrement=True)

    username = db.Column(db.String(50), nullable=False)

    email = db.Column(db.String(50), nullable=False)

    city = db.Column(db.String(50), nullable=False)

    city_adcode = db.Column(db.String(6), primary_key=True)

    scene = db.Column(db.String(50), nullable=False)

    type_code = db.Column(db.String(6), primary_key=True)

    resolution = db.Column(db.Float, default=0.02)

    status = db.Column(db.String(100), nullable=False)

    final_grid = db.Column(db.Integer, default=0)

    adsl_server_url = db.Column(db.String(100), nullable=False)

    adsl_auth = db.Column(db.String(100), nullable=False)

    keys = db.Column(db.Text, nullable=False)

    create_time = db.Column(db.DateTime, default=datetime.now,onupdate=datetime.now)


class GaodeMapScene(db.Model):
    __tablename__ = 'GaodeMapScene'

    id = db.Column(db.String(20),primary_key=True)

    province = db.Column(db.String(50))

    city = db.Column(db.String(50))

    name = db.Column(db.String(50))

    city_adcode = db.Column(db.String(20))

    district = db.Column(db.String(50))

    address = db.Column(db.String(100))

    longtitude = db.Column(db.Float(scale=10))

    lat = db.Column(db.Float(scale=10))

    type = db.Column(db.String(100))

    typecode = db.Column(db.String(20))

    classify = db.Column(db.String(100))

    area = db.Column(db.Float(scale=10))

    shape = db.Column(db.Text)

    wgs_long = db.Column(db.Float(scale=10))

    wgs_lat = db.Column(db.Float(scale=10))

    wgs_shape = db.Column(db.Text)