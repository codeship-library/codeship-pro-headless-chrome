FROM python:3.5.7-alpine

RUN pip install -U selenium

COPY script.py .
