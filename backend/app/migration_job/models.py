from app import db, ma

class MigrationJob(db.Model):
    id = db.Column(db.String(128), primary_key=True)
    name = db.Column(db.String(1024), unique=True)
    source_id = db.Column(db.String(128))
    target_id = db.Column(db.String(128))
    conf_blob = db.Column(db.JSON)


    def __init__(self, id, name, source_id, target_id, conf_blob):
        self.id = id
        self.name = name
        self.source_id = source_id
        self.target_id = target_id
        self.conf_blob = conf_blob

class MigrationJobSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'source_id', 'target_id', 'conf_blob')

migration_job_schema = MigrationJobSchema()
migration_jobs_schema = MigrationJobSchema(many=True)
