from app import db, ma

class Connection(db.Model):
    id = db.Column(db.String(128), primary_key=True)
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
