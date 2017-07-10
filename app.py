from datetime import datetime, timedelta
from bottle import run, get, response, abort, error, request
from bson.json_util import dumps, loads
from shemas.models import User


@get("/login/:usuario/:senha")
def index(usuario, senha):
    response.content_type = 'application/json'
    response.status = 200
    data = User.objects(username=usuario, password=senha)
    if data:
        response.set_cookie('usuario', usuario, secret=True, expires=datetime.now() + timedelta(minutes=10))
        response.set_cookie('senha', senha, secret=True)
        print(request.get_cookie('senha', secret=True))
        return dumps(loads(data.to_json()))
    else:
        abort(code=404, text="Nao encontramos dados")


@get("/home")
def index():
    response.content_type = 'application/json'
    data = User.objects()
    if data:
        return dumps(loads(data.to_json()))
    else:
        abort(code=404, text="Nao encontramos dados")


@error(404)
def json_error(error):
    error_data = {
        'error_message': error.body,
        'status': response.status_code
    }
    response.content_type = 'application/json'
    return dumps(error_data)

run(host='127.0.0.1', port=8080, reloader=True)