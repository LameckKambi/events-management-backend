# from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import MetaData

from sqlalchemy_serializer import SerializerMixin
from uuid import uuid4

from app import db

import uuid


def get_uuid():
    while True:
        new_id = uuid.uuid4().hex
        if not User.query.filter_by(id=new_id).first():
            return new_id


class Event(db.Model, SerializerMixin):
    __tablename__ = 'events'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    date = db.Column(db.DateTime, nullable=False)
    time = db.Column(db.String(50), nullable=True)
    image = db.Column(db.String(255), nullable=True)
    location = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    attendances = db.relationship('Attendance', back_populates='event')


class User(db.Model, SerializerMixin):
    __tablename__ = 'users'

    id = db.Column(db.String(32), primary_key=True, unique=True, default=get_uuid)
    name = db.Column(db.String)
    password = db.Column(db.String, nullable=False)
    email = db.Column(db.String(345), unique=True)

    attendances = db.relationship('Attendance', back_populates='user')


class Attendance(db.Model, SerializerMixin):
    __tablename__ = 'attendances'

    serialize_rules = ('-event.attendances', '-user.attendances')

    id = db.Column(db.Integer, primary_key=True)
    eventid = db.Column(db.Integer, db.ForeignKey('events.id'))
    userid = db.Column(db.String(32), db.ForeignKey('users.id'))
    attendance = db.Column(db.String)

    event = db.relationship('Event', back_populates='attendances')
    user = db.relationship('User', back_populates='attendances')
