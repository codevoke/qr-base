from flask import request, render_template, make_response
from flask_restful import Resource

from models import QRModel


class QRResource(Resource):
    path = "/"

    def get(self):
        code = request.args.get("c")
        qr = QRModel.get_by_code(code)
        
        headers = {'Content-Type': 'text/html'}

        if qr is None:
            return make_response(render_template("error.html"), 200, headers)

        return make_response(
            render_template("index.html",
                product_name=qr.name,
                manufacturer=qr.manufacture,
                code=qr.code,
                counter=qr.counter
            ), 200, headers)
