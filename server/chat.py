from flask_restful import request, Resource
from werkzeug.exceptions import BadRequest


class Chat(Resource):

    dbhelper = None
    reqparser = None

    def __init__(self, **kwargs):
        self.dbhelper = kwargs['db']

    def get(self):
        sql = "SELECT id, author, text, date FROM messages ORDER BY date ASC"
        results = self.dbhelper.fetch_records(sql)

        return results

    def post(self):
        resp_code = 400
        response = {'msg': 'Validation error. Check input data'}

        try:
            msg = request.get_json(silent=False)
        except BadRequest as e:
            response = {'msg': e.description}
            return response, resp_code

        if self._validate_data(msg):
            sql = "INSERT INTO messages (author, text) VALUES (%s, %s)"
            record_id = self.dbhelper.execute_query(sql, (msg['author'], msg['text']))

            if record_id:
                msg['id'] = record_id
                resp_code = 201
                response = {'result': msg}

        return response, resp_code

    @staticmethod
    def _validate_data(data):
        res = True
        req_keys = ("author", "text")

        for key in req_keys:
            if key not in data:
                res = False
                break

            if data[key] == "":
                res = False
                break

        return res

