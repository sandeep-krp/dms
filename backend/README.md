WIP
The backend exposes REST APIs for managing the core components of the DMS.
Which are:

1. Connections:

- Connections are the different sources and targets for migrations. A connection will define full details of where to connect, how to connect, which creds to use, etc.
- The same connection can be used in multiple migration jobs.
- There are different types of connections and each connection will have a specific schema in which they are defined.
- The schema is stored in a JSON Format internally
- The schema is versioned between different releases
- The UI is dynamically built using the schema information of the connection
- A stored connection will always have a schema version associated with it since we will store each of the schema version, the UI should be able to render the connection details on the UI.
- The behaviour of the UI, rendering the any given version of schema should be backward compatible
- 
