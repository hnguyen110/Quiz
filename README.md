
# Quizzes

Quizzes is a private platform for learning computer science by practicing mock exams and watching hands-on videos. 
## Authors

- [hnguyen110](https://github.com/hnguyen110)
- [cindy-jang](https://github.com/CindyJang1)


## Installation
Please ensure you have installed these components on your computer before running the application.

- Docker
- Local MySQL server
- Python, version 3.10.6
- Pipenv, version 2022.9.4

Clone the project from GitHub.
```bash
git clone git@github.com:hnguyen110/Quiz.git
```

Go inside the project and run pipenv shell to create an environment for the application.
```bash
pipenv shell
```

Install the application dependencies.
```bash
pipenv install
```

Set up the environment variables in the development environment.
```bash
chmod +x set_up_local_environment.sh
source ./set_up_local_environment.sh
```

Create database migrations and apply the migrations to create a local database if you have not set up the database yet.
```bash
python manage.py makemigrations
python manage.py migrate
```

Start Docker and set up the local S3 server.
```bash
./local-stack.sh
```

Start the local development server.
```bash
python manage.py runserver 
```

## Documentation

The application uses Swagger and the internal interactive API dashboard from DRF. You can generate the API documentation that can be imported to Postman to perform API requests to the server using Swagger. Swagger also shows all the APIs supported by the application at a higher level. Or you can use the internal API dashboard in case of SQL command inspection.

View the Swagger documentation by visiting the following location.
```bash
http://127.0.0.1:8000/swagger/
```

View the Redoc documentation by visiting the following location.
```bash
http://127.0.0.1:8000/redoc/
```

Generate the API specification to use with Postman or Insomnia by visiting the following location.
```bash
http://127.0.0.1:8000/swagger.json
```
## Environment Variables

The application requires some environment variables before it can run. You can customize these variables in the set_up_local_environment.sh file and then run the bash file again to apply the changes to your computer.

`DEBUG` - development mode set to True by default for local development.

`SECRET_KEY` - JWT secret key.

`ALLOWED_HOSTS` - the IP address, domain name or the hostname of the server that runs the application.

`DATABASE_NAME` - the database name or the schema name where you want to store all the data of the application.

`DATABASE_HOST` - the IP address, domain name or hostname of the database server.

`DATABASE_USER` - the username to access the database server.

`DATABASE_PASSWORD` - the password to access the database server.

`CORS_ALLOWED_ORIGINS` - the IP address, domain name or hostname of the front-end server
    
`EMAIL_HOST` - the IP address, domain name or hostname of the SMTP server

`EMAIL_HOST_USER` - the username to access the SMTP server.
    
`EMAIL_HOST_PASSWORD` - the password to access the SMTP server.

`EMAIL_PORT` - the port of the SMTP server.

`DEFAULT_FROM_EMAIL` - the default sender email address for the application  

`AWS_S3_ENDPOINT_URL` - the IP address, domain name or the hostname of the S3 server (do not set this variable in production)

`AWS_ACCESS_KEY_ID` - the AWS IAM username to access the S3 server.

`AWS_SECRET_ACCESS_KEY` - the AWS IAM password to access the S3 server.
    
`AWS_STORAGE_BUCKET_NAME` - the bucket name of the S3 server to specify where to store the media contents

