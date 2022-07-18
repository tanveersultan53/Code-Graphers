import datetime

from sqlalchemy.sql import expression

from . import db  # dev_schema, table_initial
from sqlalchemy.orm import validates



class User(db.Model):
    __tablename__ = 'user'
    role_foreign_key = "role.id"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    email = db.Column(db.String(), nullable=False,unique=True)
    username = db.Column(db.String(), nullable=False,unique=True)
    first_name = db.Column(db.String(), nullable=True)
    last_name = db.Column(db.String(), nullable=True)
    password = db.Column(db.String(), nullable=False)
    public_id = db.Column(db.String(255), nullable=True)
    is_superuser = db.Column(db.Boolean, server_default=expression.true(), default=False, nullable=False)
    is_admin = db.Column(db.Boolean, server_default=expression.true(), default=False, nullable=False)
    is_active = db.Column(db.Boolean, server_default=expression.true(), default=False, nullable=False)
    created_at = db.Column(db.DateTime)
    modified_at = db.Column(db.DateTime)

    def __init__(self, email,username,first_name, last_name,password,public_id,is_superuser,is_admin, is_active):
        self.email = email
        self.username = username
        self.first_name = first_name
        self.last_name = last_name
        self.is_superuser = is_superuser
        self.password = password,
        self.public_id = public_id,
        self.is_active = is_active
        self.is_admin = is_admin
        self.created_at = datetime.datetime.utcnow()
        self.modified_at = datetime.datetime.utcnow()

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def update_user(user_id, data_to_be_updated):
        User.query.filter(User.id == user_id).update(data_to_be_updated)
        db.session.commit()

    def __repr__(self):
        return '<id {}>'.format(self.id)

    @validates('email')
    def validate_email(self, key, email):
        if '@' not in email:
            raise ValueError("failed simplified email validation")
        return email


