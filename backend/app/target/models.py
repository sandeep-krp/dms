from app import db, ma

class Target(db.Model):
    id = db.Column(db.String(128), primary_key=True)
    name = db.Column(db.String(1024), unique=True)
    conf_blob = db.Column(db.JSON)
    connection_id = db.Column(db.String(128))


    def __init__(self, id, name, conf_blob, connection_id):
        self.id = id
        self.name = name
        self.conf_blob = conf_blob
        self.connection_id = connection_id

class TargetSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'connection_id', 'conf_blob')

target_schema = TargetSchema()
targets_schema = TargetSchema(many=True)
