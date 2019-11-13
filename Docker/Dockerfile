# our base image
FROM python:3-onbuild

COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# specify the port number the container should expose
EXPOSE 5000

# run the application
CMD ["python", "./app.py"]
