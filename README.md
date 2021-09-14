# DMS

DMS is a web based utility which can migrate data between different datasources. It does so by taking source and target configuration on UI and running the job on [Apache Spark](https://github.com/apache/spark) backend.

# How to run DMS

To run DMS you have the following options:
1. Run using docker-compose
2. Run on Kubernetes (WIP)

## Run using docker-compose

To the code using docker-compose in local, make you have `git` , `docker` and  `docker-compose` installed.

Clone the code in your local system
```
git clone git@github.com:sandeep-krp/dms.git
```

Go to the deploy/docker-compose directory
```
cd deploy/docker-compose
```

Run the docker-compose
```
docker-compose.yml up -d
```

Once the docker-compose is successful, you can check open the DMS app on the browser at http://localhost:3000

## Run on Kubernetes (WIP)