from json import dumps
from flask import Flask, request, Response
from flask_cors import CORS
from flask_restful import Api, abort
from flask_marshmallow import Marshmallow

from dbhelper import DbHelper
from chat import Chat

import config as c

app = Flask(__name__)
CORS(app)
ma = Marshmallow(app)
api = Api(app)


@api.representation('application/json')
def output_json(data, code, headers=None):
    resp = Response(dumps(data, indent=4, sort_keys=True, default=str))
    resp.headers.extend(headers or {})
    resp.status_code = code

    return resp


db = DbHelper(c.db_user, c.db_host, c.db_password, c.db_name)

api.add_resource(Chat, '/chat', resource_class_kwargs={"db": db})
