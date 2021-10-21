FROM python:3.9
COPY ./app /dms/app
COPY requirements.txt /dms/
COPY deploy/dbinit.py /dms/
COPY run.py /dms/
COPY config.py /dms
WORKDIR /dms
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT [ "python"]
CMD [ "run.py" ]
