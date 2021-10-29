from flask_restful import Resource
from flask import request, jsonify
from app import db
from app.source.models import Source, source_schema, sources_schema
from flask_apispec import doc, marshal_with
from flask_apispec.views import MethodResource

from app.source.models import SourceSchema



class SourceManager(MethodResource, Resource):

    @doc(description='Get sources', tags=['Source'])
    def get(self):
        try: id = request.args['id']
        except Exception as _: id = None

        if not id:
            sources = Source.query.all()
            res = jsonify(sources_schema.dump(sources))
            res.headers.add("Access-Control-Allow-Origin", "*")
            return res
        source = Source.query.get(id)
        res = jsonify(source_schema.dump(source))
        res.headers.add("Access-Control-Allow-Origin", "*")
        return res


    @doc(description='Create a new Source', tags=['Source'])
    @marshal_with(SourceSchema)
    def post(self):
        id = request.json['id']
        name = request.json['name']
        connection_id = request.json['connection_id']
        conf_blob = request.json['conf_blob']

        source = Source(id, name, connection_id, conf_blob)
        db.session.add(source)
        db.session.commit()
        return jsonify({
            'Message': f'Source {id} {name} inserted.'
        })
    @doc(description='Update an existing source', tags=['Source'])
    def put(self):
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({ 'Message': 'Must provide the source ID' })
        source = Source.query.get(id)

        name = request.json['name']
        connection_id = request.json['connection_id']
        conf_blob = request.json['conf_blob']

        source.name = name
        source.connection_id = connection_id
        source.conf_blob = conf_blob

        db.session.commit()
        return jsonify({
            'Message': f'Source {id} {name} altered.'
        })

    @doc(description='Delete an existing source', tags=['Source'])
    def delete(self):
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({ 'Message': 'Must provide the source ID' })
        source = Source.query.get(id)

        db.session.delete(source)
        db.session.commit()

        return jsonify({
            'Message': f'Source {str(id)} deleted.'
        })