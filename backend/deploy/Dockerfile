FROM python:3.9
COPY ./app /dms/app
COPY requirements.txt /dms/
COPY run.py /dms/
COPY config.py /dms
WORKDIR /dms

RUN pip install -r requirements.txt

# Set up spark
RUN wget https://dlcdn.apache.org/spark/spark-3.2.0/spark-3.2.0-bin-hadoop3.2.tgz && \
    tar -xvzf spark-3.2.0-bin-hadoop3.2.tgz && \
    rm spark-3.2.0-bin-hadoop3.2.tgz
ENV SPARK_HOME=/dms/spark-3.2.0-bin-hadoop3.2/

# Set up Java
RUN wget https://corretto.aws/downloads/latest/amazon-corretto-8-x64-linux-jdk.tar.gz && \
    tar -xvzf amazon-corretto-8-x64-linux-jdk.tar.gz
ENV JAVA_HOME=/dms/amazon-corretto-8.312.07.1-linux-x64/

EXPOSE 8080
ENTRYPOINT [ "python"]
CMD [ "run.py" ]
