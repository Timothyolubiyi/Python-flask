FROM python:alpine
RUN mkdir /app
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
# RUN pip install --upgrade
EXPOSE 5008
CMD ["python","app.py"]