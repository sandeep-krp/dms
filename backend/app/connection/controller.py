from flask_restful import Resource
from flask import request, jsonify
from app import db, api
from app.connection.models import Connection, connection_schema, connections_schema
from flask_apispec import doc, marshal_with
from flask_apispec.views import MethodResource
from app.connection.models import ConnectionSchema
import uuid



class ConnectionManager(MethodResource, Resource):

    @doc(description='Get connections', tags=['Connection'])
    @marshal_with(ConnectionSchema)
    def get(self):
        try: id = request.args['id']
        except Exception as _: id = None

        if not id:
            connections = Connection.query.all()
            res = jsonify(connections_schema.dump(connections))
            res.headers.add("Access-Control-Allow-Origin", "*")
            return res
        connection = Connection.query.get(id)
        res = jsonify(connection_schema.dump(connection))
        res.headers.add("Access-Control-Allow-Origin", "*")
        return res

    @marshal_with(ConnectionSchema)
    @doc(description='Create a new Connection', tags=['Connection'])
    def post(self):
        id = 'con-'+str(uuid.uuid4())
        name = request.json['name']
        version = request.json['version']
        type = request.json['type']
        format = request.json['format']
        schema_blob = request.json['schema_blob']

        connection = Connection(id, name, version, schema_blob, format, type)
        db.session.add(connection)
        db.session.commit()
        return jsonify({
            'Message': f'Connection {name} inserted.'
        })

    @doc(description='Update an existing connection', tags=['Connection'])
    def put(self):
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({ 'Message': 'Must provide the connection ID' })
        connection = Connection.query.get(id)

        name = request.json['name']
        version = request.json['version']
        type = request.json['type']
        format = request.json['format']
        schema_blob = request.json['schema_blob']

        connection.name = name
        connection.version = version
        connection.type = type
        connection.format = format
        connection.schema_blob = schema_blob

        db.session.commit()
        return jsonify({
            'Message': f'Connection {id} {name} altered.'
        })

    @doc(description='Delete an existing source', tags=['Connection'])
    def delete(self):
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({ 'Message': 'Must provide the connection ID' })
        connection = Connection.query.get(id)

        db.session.delete(connection)
        db.session.commit()

        return jsonify({
            'Message': f'Connection {str(id)} deleted.'
        })
