import datetime
from . import db
from typing import List

class Job(db.Model):
    __tablename__ = 'job'
    role_foreign_key = "user.id"


    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    job_title = db.Column(db.String(), nullable=False)
    job_description = db.Column(db.String(), nullable=False)
    job_rate = db.Column(db.Float, nullable=False)
    latitude = db.Column(db.String(), nullable=False)
    longitude = db.Column(db.String(), nullable=False)
    # user_id = db.Column(db.Integer, db.ForeignKey(role_foreign_key), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'),
              nullable=False)
    is_active = db.Column(db.Boolean, default=False, nullable=False)
    job_created_at = db.Column(db.DateTime)
    job_modified_at = db.Column(db.DateTime)

    def __init__(self, job_title,job_description,job_rate,latitude,longitude,user_id,is_active):
        self.job_title = job_title
        self.job_description = job_description
        self.job_rate = job_rate
        self.latitude = latitude
        self.longitude = longitude
        self.user_id = user_id
        self.is_active = is_active
        self.job_created_at = datetime.datetime.utcnow()
        self.job_modified_at = datetime.datetime.utcnow()


    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def delete_job_by_id(job_id):
        Role.query.filter(Job.id == job_id).delete()
        db.session.commit()

    @staticmethod
    def job_listing():
        return Job.query.filter_by(is_active=True).all()

    @staticmethod
    def get_job_by_id(job_id):
        return Job.query.get(job_id)

    @classmethod
    def find_all(cls) -> List["JobList"]:
        return cls.query.all()


    @staticmethod
    def update_job(job_id, updated_data):
        Job.query.filter(Job.id == job_id).update(updated_data)
        db.session.commit()