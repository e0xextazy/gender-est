FROM python:3.8

WORKDIR /app

RUN mkdir -p model_files

ADD model_files/gender_v1.pth model_files/gender_v1.pth
ADD run.py run.py
ADD requirements.txt requirements.txt
ADD model.py model.py
ADD utils.py utils.py

RUN apt-get update && apt-get install -y python3-opencv
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000

CMD [ "gunicorn", "--bind", "0.0.0.0:5000", "run:app" ]
