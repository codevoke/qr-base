from os import getenv as env
from flask import request
from flask_restful import Resource

from models import QRModel


class QRMakeResource(Resource):
    path = "/api/BBB*CRcb38vb"

    def post(self):
        # test authentication
        auth = request.headers.get("Authorization")
        if auth != env("AUTH_KEY"):
            return "not authed", 200

        # test content type
        json = request.get_json()
        if json is None:
            return "json is None", 400

        # try to get fields
        name = json.get("name")
        manufacture = json.get("manufacture")
        code = json.get("code")

        # check required
        if not all([name, manufacture, code]):
            return "no enough data", 400

        # check if exists
        test_qr = QRModel.get_by_code(code, SYSTEM=True)
        if test_qr:
            return "Already registered", 400
        
        # save
        qr = QRModel(
            name=name, 
            manufacture=manufacture,
            code=code
        )
        qr.save()

        return "success", 200
