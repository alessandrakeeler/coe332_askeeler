FROM python:3.9

RUN mkdir /app
WORKDIR /app
COPY ML_Data_Sample.json /app
COPY requirements.txt /app/requirements.txt
RUN pip3 install -r /app/requirements.txt
COPY . /app

ENTRYPOINT ["python"]
CMD ["app.py"]