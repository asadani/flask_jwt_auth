from flask import Blueprint, make_response, jsonify

from auth import required_admin, required_viewer

employee_blueprint = Blueprint('report_blueprint', __name__)


# Token not required
@employee_blueprint.route('/employee')
def portal():
    res = {"message": "Welcome to employee portal"}
    return make_response(jsonify(res), 200)


# Token required, with role as admin or viewer
@employee_blueprint.route('/employee/info')
@required_viewer
def info():
    res = {
        "data": [
            {
                "emp_id": 5870,
                "name": "Doga",
                "department": "R&D"
            },
            {
                "emp_id": 5871,
                "name": "Shakti",
                "department": "Engineering"
            }
        ]
    }
    return make_response(jsonify(res), 200)


# Token required, with role as admin
@employee_blueprint.route('/employee/salary')
@required_admin
def salary():
    res = {
        "data": [
            {
                "emp_id": 5870,
                "salary": 55000
            },
            {
                "emp_id": 5871,
                "salary": 55000
            }
        ]
    }
    return make_response(jsonify(res), 200)
