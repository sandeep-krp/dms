from app import db, ma

class Source(db.Model):
    id = db.Column(db.String(128), primary_key=True)
    name = db.Column(db.String(1024), unique=True)
    conf_blob = db.Column(db.Text())
    connectionId = db.Column(db.String(128))


    def __init__(self, id, name, version, conf_blob, connectionId):
        self.id = id
        self.name = name
        self.version = version
        self.conf_blob = conf_blob
        self.connectionId = connectionId
        self.type = type

class SourceSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'version', 'connectionId', 'conf_blob')

source_schema = SourceSchema()
sources_schema = SourceSchema(many=True)
