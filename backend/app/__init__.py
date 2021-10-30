from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api
from prometheus_flask_exporter import PrometheusMetrics
from flask_apispec import FlaskApiSpec

app = Flask(__name__)

app.config.from_object('config')

api = Api(app)

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

ma = Marshmallow(app)

from app.connection.controller import ConnectionManager, ConnectionManagerById
from app.source.controller import SourceManager, SourceManagerById
from app.target.controller import TargetManager, TargetManagerById
from app.migration_job.controller import MigrationJobManager, MigrationJobManagerById
api.add_resource(ConnectionManager, '/api/v1/connection')
api.add_resource(SourceManager, '/api/v1/source')
api.add_resource(TargetManager, '/api/v1/target')
api.add_resource(MigrationJobManager, '/api/v1/migrationjob')

api.add_resource(ConnectionManagerById, '/api/v1/connection/<string:id>')
api.add_resource(SourceManagerById, '/api/v1/source/<string:id>')
api.add_resource(TargetManagerById, '/api/v1/target/<string:id>')
api.add_resource(MigrationJobManagerById, '/api/v1/migrationjob/<string:id>')
docs = FlaskApiSpec(app)

docs.register(ConnectionManager)
docs.register(SourceManager)
docs.register(TargetManager)
docs.register(MigrationJobManager)

docs.register(ConnectionManagerById)
docs.register(SourceManagerById)
docs.register(TargetManagerById)
docs.register(MigrationJobManagerById)

# Build the database:
# This will create the database file using SQLAlchemy

metrics = PrometheusMetrics(app)
metrics.info('app_info', 'DMS', version='0.1')

db.create_all()