FROM python:3.9
COPY app.py /dms/
COPY requirements.txt /dms/
COPY deploy/dbinit.py /dms/
WORKDIR /dms
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python"]
RUN python dbinit.py
CMD [ "app.py" ]
