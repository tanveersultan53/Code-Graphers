from enum import Enum


class ResponseMessage(Enum):
    add_records_success_message = "add record successfully!"
    delete_record_success_message = "delete record successfully!"
    update_data_success_message = "update data successfully!"
    exception_message = "An issue encountered : "
    get_success_message = "Records found successfully"
    listing_success_message = "Records found in listing"
    listing_error_message = "Listing records not found"
    method_not_allowed_message = "Only post method is required"
    precondition_failed_message = "data not post in request for further proceedings"
    premission_denied_message = "You don't have permission to access this resource"
    token_missing_message = "a valid token is missing"
    invalid_token_message = "invalid token"


class ResponseCodes(Enum):
    success = 200
    created = 201
    accepted = 202
    bad_request = 400
    un_authorized = 401
    forbidden = 403
    not_found = 404
    method_not_allowed = 405
    conflict = 409
    precondition_failed = 412
    server_error = 500
    service_unavailable = 503


class Response:
    @staticmethod
    def success(code=ResponseCodes.success.value, message="success", data=[], key='data'):
        return {
            'code': code,
            'status': 'success',
            'message': message,
            'data': data
        }

    @staticmethod
    def error(code=ResponseCodes.server_error.value, message="error", status='error'):
        return {
            'code': code,
            'status': status,
            'message': message
        }
