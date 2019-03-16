from flask import (
    Blueprint, jsonify, request
)
from flask_restplus import Api, Resource, fields
from werkzeug.exceptions import abort
from . import service

bp = Blueprint('clients', __name__, url_prefix='/clients/v1')
     
@bp.route('/') 
def query():
    clients = service.search_clients(request.args.get('q'))
    return jsonify(list(map(lambda x: x.name, clients)))