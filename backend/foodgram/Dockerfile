FROM python:3.8-slim
WORKDIR /app
COPY . .
RUN pip3 install --upgrade pip
RUN pip3 install -r /app/requirements.txt 
CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000" ]