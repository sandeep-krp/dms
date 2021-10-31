from pyspark.sql.dataframe import DataFrame
from app.migration_job.models import MigrationJob
from app.source.models import Source
from app.target.models import Target
from app.connection.models import Connection
from pyspark.sql import SparkSession


class MigrationJobService():

    @staticmethod
    def start(migration_job: MigrationJob):
        spark_builder = SparkSession.builder
        print(migration_job.conf_blob)
        configs = next((x for x in migration_job.conf_blob['fields'] if x['name'] == 'config'), None)['value']
        for config in configs:
            spark_builder.config(config['key'], config['value'])
        spark = spark_builder.getOrCreate()
        source = Source.query.get(migration_job.source_id)
        source_connection_type = Connection.query.get(source.connection_id).type

        target = Target.query.get(migration_job.target_id)
        target_connection_type = Connection.query.get(target.connection_id).type
        # TODO Replace with enums maybe?
        if source_connection_type == 'rdbms':
            df = MigrationJobService.handle_rdbms_source(source, spark)
        else:
            raise ValueError (f'The source type [{source_connection_type}] is not supported')

        if target_connection_type == 'rdbms':
            df = MigrationJobService.handle_rdbms_target(target, df)
        else:
            raise ValueError(f'The target type [{target_connection_type}] is not supported')

        print(f'To-Do : Start the actual job [{migration_job.name}]')

    def kill(migration_job):
        print(f'To-Do : Kill the actual job [{migration_job.name}]')

    @staticmethod
    def handle_rdbms_source(source, spark:SparkSession):
        dfr = spark.read.format('jdbc')
        conf = source.conf_blob
        options = next((x for x in conf['fields'] if x['name'] == 'options'), None)['value']
        for option in options:
            dfr.option(option['key'],option['value'])
        return dfr.load()

    def handle_rdbms_target(target, df:DataFrame):
        dfw = df.write.format('jdbc')
        conf =target.conf_blob
        options = next((x for x in conf['fields'] if x['name'] == 'options'), None)['value']
        for option in options:
            dfw.option(option['key'],option['value'])
        dfw.save()

