FROM python:3.7-slim
RUN pip install flask
WORKDIR /myapp
COPY . /myapp
CMD ["python", "main.py"]
