from flask_restful import Api
from .qr_resource import QRResource
from .qr_make_resource import QRMakeResource


api = Api()

api.add_resource(QRResource, QRResource.path)
api.add_resource(QRMakeResource, QRMakeResource.path)
