from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Resource, Api
from prometheus_flask_exporter import PrometheusMetrics


app = Flask(__name__)
metrics = PrometheusMetrics(app)
metrics.info('app_info', 'DMS', version='0.1')
api = Api(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///dms.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
ma = Marshmallow(app)


class Connection(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(1024), unique=True)
    version = db.Column(db.String(128))
    schema_blob = db.Column(db.Text())
    format = db.Column(db.String(128))
    type = db.Column(db.String(128))


    def __init__(self, id, name, version, schema_blob, format, type):
        self.id = id
        self.name = name
        self.version = version
        self.schema_blob = schema_blob
        self.format = format
        self.type = type


class ConnectionSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'version', 'type', 'format', 'schema_blob')

connection_schema = ConnectionSchema()
connections_schema = ConnectionSchema(many=True)


class ConnectionManager(Resource):
    @staticmethod
    def get():
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

    @staticmethod
    def post():
        id = request.json['id']
        name = request.json['name']
        version = request.json['version']
        type = request.json['type']
        format = request.json['format']
        schema_blob = request.json['schema_blob']

        connection = Connection(id, name, version, schema_blob, format, type)
        db.session.add(connection)
        db.session.commit()
        return jsonify({
            'Message': f'Connection {id} {name} inserted.'
        })

    @staticmethod
    def put():
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

    @staticmethod
    def delete():
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


api.add_resource(ConnectionManager, '/api/v1/connection')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=80)