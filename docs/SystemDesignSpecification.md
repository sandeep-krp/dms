# DMS

## What does the system do?

The DMS (Data Migration Service) is a web based application which can be used to migrate data between different Data Sources by configuring source and targets on the GUI.

It uses Apache Spark as the migration engine to do all the heavy lifting.

## Tech stack

The system uses python 3.9 to do all the work at the backend. This includes exposing REST endpoints to manage Connection, Source & Targets, Migration Jobs, etc. The python code also manages scheduling of Migration Jobs.

The actual job is run on Apache Spark. But the submission of the job is done by python code.

Reactjs is used for the present user with the user interface on the web browser.


## Software Components

1. **Connections**: \
   To migrate data between data stores we need to define the connection details of the Source and Targets. For example if we are going to use an RDBMS as a source, the source connection configuration will contain the jdbcURL, username, password, database, schema, etc. But defining a new set of these configurations for each source is a bit overwhelming. For example, we might want to migrate 10 different databases from the same database instance. In that case we don't want to configure the same jdbc url for all the sources.
   That's why we create Connections on the top level where we define the jdbc url once, and then specific sources can extend this connection.

2. **Source and Targets** \
   Sources and Targets define the final configuration will be used to pull data from source and push to a target. As discussed in the Connections section, the source and targets extend Connections to inherit all the configuration and then override them and define their own configs.

3. **Migration Jobs** \
   Migration job is configuration which defines from which source we want to pull data and which target to push it to.

4. **Migration Job Run** \
   When a migration job runs, we store all the metadata related to that run in a Migration Job Run. For example if we run a Migration job twice, two Migration Job Run are created and each of them can be viewed individually.

5. **Scheduler** \
   Scheduler is the component which is responsible for looking at the available jobs to run and kick them off when they have to.

6. **Namespace**
   Namespace is just a simple tag attached to all the resources to sperate out resources. For example for different clients, we can create different namespaces so that no unrelated resources are shown at one place.

## Represntation
1. **Connection** \
   A connection contains the following metadata: \
   1.1 `id` : A unique identifire for the connection
   1.2 `name` : This this is unique field accross all the connections and represents the name of the connection. \
   1.3 `type` : It is a string feild representing the type of the connection. For example it could be RDBMS, S3, Hive, etc. \
   1.4 `version` : This represents the version of connection. If we change the schema of the connection, we should update the version as well. This helps rendering old schemas on the UI. \
   1.5 `schema` : This will be a JSON object that contains all the connection details like database hosts, names, passwords, etc. \
   1.6 `namespace` : Represents the namespace

2. **Source** \
   A Source contains the following metadata: \
   2.1 `id` : A unique identifire for the source
   2.1 `name` : The name of the Source. e.g `production-app-db`. \
   2.2 `connectionId` : Id of the connection this source was derived from
   2.3 `conf` : A JSON representing the configurations of the source. Note that all fields from the `Connection` should be present here as source conf is inherited from the schema of connection. \
   2.4 `namespace` : Rerpresents the name of the namespace this source belongs to.

3. **Target** \
   A Target contains the following metadata: \
   3.1 `id` : A unique identifire for the target \
   3.1 `name` : The name of the Target. e.g `production-app-db`. \
   3.2 `connectionId` : Id of the connection this target was derived from \
   3.3 `conf` : A JSON representing the configurations of the target. Note that all fields from the `Connection` should be present here as target conf is inherited from the schema of connection. \
   3.4 `namespace` : Rerpresents the name of the namespace this target belongs to.

4. **Migration Job** \
   A Migration job has the following metadata: \
   4.1 `id` : Represents a unique id of the Migration Job \
   4.1 `sourceId` : Represents the source-id. \
   4.2 `targetId` : Represents the target-id. \
   4.3 `namespace` : Represents the namespace

5. **Migration job Run** \
   5.1 `id` : Repersents a unique identifire for the Migration Job Run \
   5.2 `migrationJobId` : The Migration Job Id this MJR belongs to. \
   5.3 `state` : Represents the current state of the migration job. It can be one of the following: `fresh`, `queued`, `running`, `failed`. \
   5.4. `startTime` : The unix timestamp when MJR started. Null if the job has not started yet. \
   5.5 `endTime` : The unix timestamp when the MJR ended (failed or succeeded). Null if the job has not ended yet.



