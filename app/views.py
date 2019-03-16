from flask import (
    Blueprint, jsonify, request
)
from flask_restplus import Api, Resource, fields
from werkzeug.exceptions import abort
from . import service

bp = Blueprint('clients', __name__, url_prefix='/api/v1')
     
@bp.route('/') 
def query():
    query = request.args.get('q')
    clients = service.search_clients(query)
    return jsonify(list(map(lambda x: x.name, clients)))