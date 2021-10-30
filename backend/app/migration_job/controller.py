from flask_restful import Resource
from flask import request, jsonify
from app import db
from app.migration_job.models import MigrationJob, migration_job_schema, migration_jobs_schema
from flask_apispec import doc, marshal_with
from flask_apispec.views import MethodResource
from app.migration_job.models import MigrationJobSchema
import uuid



class MigrationJobManager(MethodResource, Resource):

    @doc(description='Get migration_jobs', tags=['MigrationJob'])
    @marshal_with(MigrationJobSchema)
    def get(self):
        try: id = request.args['id']
        except Exception as _: id = None

        if not id:
            migration_jobs = MigrationJob.query.all()
            res = jsonify(migration_jobs_schema.dump(migration_jobs))
            res.headers.add("Access-Control-Allow-Origin", "*")
            return res
        migration_job = MigrationJob.query.get(id)
        res = jsonify(migration_job_schema.dump(migration_job))
        res.headers.add("Access-Control-Allow-Origin", "*")
        return res

    @marshal_with(MigrationJobSchema)
    @doc(description='Create a new MigrationJob', tags=['MigrationJob'])
    def post(self):
        id = 'mj-'+str(uuid.uuid4())
        name = request.json['name']
        source_id = request.json['source_id']
        target_id = request.json['target_id']

        migration_job = MigrationJob(id, name, source_id, target_id)
        db.session.add(migration_job)
        db.session.commit()
        return jsonify({
            'Message': f'MigrationJob [{name}] inserted.'
        })

    @doc(description='Update an existing migration_job', tags=['MigrationJob'])
    def put(self):
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({ 'Message': 'Must provide the migration_job ID' })
        migration_job = MigrationJob.query.get(id)

        name = request.json['name']
        source_id = request.json['source_id']
        target_id = request.json['target_id']

        migration_job.name = name
        migration_job.source_id = source_id
        migration_job.target_id = target_id

        db.session.commit()
        return jsonify({
            'Message': f'MigrationJob [{name}] altered.'
        })

    @doc(description='Delete an existing source', tags=['MigrationJob'])
    def delete(self):
        try: id = request.args['id']
        except Exception as _: id = None
        if not id:
            return jsonify({ 'Message': 'Must provide the migration_job ID' })
        migration_job = MigrationJob.query.get(id)

        db.session.delete(migration_job)
        db.session.commit()

        return jsonify({
            'Message': f'MigrationJob [{str(id)}] deleted.'
        })
