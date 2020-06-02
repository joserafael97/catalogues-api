# pull official base image
FROM python:3.8.3

# set work directory
WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .

# Install assets
RUN python manage.py collectstatic --noinput --clear


# Run the app.  CMD is required to run on Heroku
CMD gunicorn catalogues.wsgi --log-file -
