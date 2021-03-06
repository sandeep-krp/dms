from flask_restful import Resource
from flask import request, jsonify
from app import db
from app.target.models import Target, target_schema, targets_schema
from flask_apispec.views import MethodResource
from flask_apispec import doc, marshal_with
from app.target.models import TargetSchema
import uuid


class TargetManager(MethodResource, Resource):

    @marshal_with(TargetSchema)
    @doc(description='Get targets', tags=['Target'])
    def get(self):
        try: id = request.args['id']
        except Exception as _: id = None

        if not id:
            targets = Target.query.all()
            res = jsonify(targets_schema.dump(targets))
            res.headers.add("Access-Control-Allow-Origin", "*")
            return res
        target = Target.query.get(id)
        res = jsonify(target_schema.dump(target))
        res.headers.add("Access-Control-Allow-Origin", "*")
        return res

    @doc(description='Create a new target', tags=['Target'])
    def post(self):
        id = 'trg-' + str(uuid.uuid4())
        name = request.json['name']
        connection_id = request.json['connection_id']
        conf_blob = request.json['conf_blob']

        target = Target(id, name, conf_blob, connection_id)
        db.session.add(target)
        db.session.commit()
        return jsonify({
            'Message': f'Target [{name}] inserted.'
        })


class TargetManagerById(MethodResource, Resource):

    @marshal_with(TargetSchema)
    @doc(description='Get target details', tags=['Target'])
    def get(self, id):
        target = Target.query.get(id)
        res = jsonify(target_schema.dump(target))
        res.headers.add("Access-Control-Allow-Origin", "*")
        return res

    @doc(description='Update an existing target', tags=['Target'])
    def put(self, id):
        target = Target.query.get(id)

        name = request.json['name']
        connection_id = request.json['connection_id']
        conf_blob = request.json['conf_blob']

        target.name = name
        target.connection_id = connection_id
        target.conf_blob = conf_blob

        db.session.commit()
        return jsonify({
            'Message': f'Target [{name}] altered.'
        })

    @doc(description='Delete an existing target', tags=['Target'])
    def delete(self, id):
        target = Target.query.get(id)

        db.session.delete(target)
        db.session.commit()

        return jsonify({
            'Message': f'Target [{str(id)}] deleted.'
        })
