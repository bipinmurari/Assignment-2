FROM python:3.7.4-stretch 
WORKDIR /assignment
ADD requirements.txt .
ADD quiz.json .
ADD Quiz.py .
RUN pip install update pip
RUN pip install -r requirements.txt

