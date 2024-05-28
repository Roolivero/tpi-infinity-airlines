FROM python:latest


# Set the working directory
WORKDIR /app

# Install dependencies
COPY ./django-project/requirements.txt ./requirements.txt
RUN pip install -r requirements.txt

# Copy the project code into the container
COPY ./django-project .
EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]

#CMD ["tail", "-f", "/dev/null"]
