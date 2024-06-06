FROM nginx:stable-alpine
COPY nginx.conf /etc/nginx/conf.d
FROM python:3.10-alpine
WORKDIR /app
COPY . /app
EXPOSE 8000
RUN pip install -r requirements.txt
CMD python app.py
