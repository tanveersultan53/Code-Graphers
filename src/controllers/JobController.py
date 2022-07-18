from src.models.job import Job
from flask_restful import Api, Resource, url_for,reqparse,fields, marshal_with,marshal
from flask import request
from src import api_job
from src.common.decorators import token_required,current_user_login
from src.common.response import ResponseCodes, Response, ResponseMessage
from src.common.helper import ProjectHelper
api = Api(api_job)

class JobList(Resource):
    @token_required
    def get(self,current_user):
        """
        It works also with swag_from, schemas and spec_dict
        ---
        parameters:
          - in: query
            name: longitude
            type: string
            required: false
          - in : path
            name: latitude
            type: string
            required: false
        responses:
          200:
            description: A single user item
            schema:
              id: User
              properties:
                username:
                  type: string
                  description: The name of the user
                  default: Steven Wilson
        """
        try:
            query = Job.job_listing()
            data_details = []
            for item in query:
                data = {'id': item.id, 'job_title': item.job_title,'job_description':item.job_description,
                       'job_rate':item.job_rate,'latitude':item.latitude,'longitude':item.longitude,
                        'user_id':item.user_id,'is_active':item.is_active}
                data_details.append(data)
            response = Response.success(message=ResponseMessage.get_success_message.value,
                                        data=data_details)
        except Exception as e:
            response = Response.error(message=ResponseMessage.exception_message.value + str(e))
        return response

    @token_required
    def post(self,current_user):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('job_title', type=str, location='json', required=True,
                                help="job_title not be blank!")
            parser.add_argument('job_description', type=str, location='json', required=True,
                                help="job_description not be blank!")
            parser.add_argument('job_rate', type=int, location='json', required=True,
                                help="job_rate not be blank!")
            parser.add_argument('latitude', type=str, location='json', required=True,
                                help="latitude not be blank!")
            parser.add_argument('longitude', type=str, location='json', required=True,
                                help="longitude not be blank!")
            parser.add_argument('user_id', type=int, required=True)
            parser.add_argument('is_active', type=bool, location='josn')

            args = parser.parse_args()
            job = Job(**args)
            job.user_id = current_user_login().id
            job.save()
            response = Response.success(message=ResponseMessage.add_records_success_message.value,
                                        code=ResponseCodes.created.value)
        except Exception as e:
            response = Response.error(message=ResponseMessage.exception_message.value + str(e))
        return response

class JobItem(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('job_title', type=str, location='json', required=True,
                        help="job_title not be blank!")
    parser.add_argument('job_description', type=str, location='json', required=True,
                        help="job_description not be blank!")
    parser.add_argument('job_rate', type=int, location='json', required=True,
                        help="job_rate not be blank!")
    parser.add_argument('latitude', type=str, location='json', required=True,
                        help="latitude not be blank!")
    parser.add_argument('longitude', type=str, location='json', required=True,
                        help="longitude not be blank!")
    parser.add_argument('user_id', type=int, required=True)
    parser.add_argument('is_active', type=bool, location='josn')

    @token_required
    def get(self, current_user,job_id):
        try:
            if job_id:
                job_item = Job.get_job_by_id(job_id)
                data = {'id': job_item.id, 'job_title': job_item.job_title, 'job_description': job_item.job_description,
                        'job_rate': job_item.job_rate, 'latitude': job_item.latitude, 'longitude': job_item.longitude,
                        'user_id': job_item.user_id, 'is_active': job_item.is_active}
                response = Response.success(message=ResponseMessage.get_success_message.value,
                                            data=data)
        except Exception as e:
            response = Response.error(message=ResponseMessage.exception_message.value + str(e))
        return response

    @token_required
    def delete(self, current_user,job_id):
        try:
            if job_id:
                Job.update_job(job_id, updated_data={'is_active':False})
                response = Response.success(message=ResponseMessage.delete_record_success_message.value,
                                            )
        except Exception as e:
            response = Response.error(message=ResponseMessage.exception_message.value + str(e))
        return response

    @token_required
    def put(self,current_user, job_id):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('job_title', type=str, location='json')
            parser.add_argument('job_description', type=str, location='json')
            parser.add_argument('job_rate', type=int, location='json')
            parser.add_argument('latitude', type=str, location='json')
            parser.add_argument('longitude', type=str, location='json')
            parser.add_argument('user_id', type=int)
            parser.add_argument('is_active', type=bool, location='josn')
            args = parser.parse_args()

            data = {
                key: value
                for key, value in args.items()
                if value is not None
            }



            Job.update_job(job_id,data)
            response = Response.success(message=ResponseMessage.update_data_success_message.value)
        except Exception as e:
            response = Response.error(message=ResponseMessage.exception_message.value + str(e))
        return response

api.add_resource(JobItem, '/JobItem/<int:job_id>')
api.add_resource(JobList, '/job-list')
