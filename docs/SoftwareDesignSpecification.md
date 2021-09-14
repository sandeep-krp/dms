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
