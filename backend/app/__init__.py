from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_restful import Api
from prometheus_flask_exporter import PrometheusMetrics

app = Flask(__name__)

app.config.from_object('config')

api = Api(app)

# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

ma = Marshmallow(app)

from app.connection.controller import ConnectionManager
api.add_resource(ConnectionManager, '/api/v1/connection')

# Build the database:
# This will create the database file using SQLAlchemy

metrics = PrometheusMetrics(app)
metrics.info('app_info', 'DMS', version='0.1')

db.create_all()