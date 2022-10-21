
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
docker run --rm -it -d -p 4566:4566 -p 4510-4559:4510-4559 localstack/localstack
./local-stack.sh
```

Start the local development server.
```bash
python manage.py runserver 
```

## Documentation

The application uses Swagger and the internal API dashboard from DRF for documentation. You can use Swagger to generate the API specification file and import it to Postman to make API requests to the server. Swagger also shows all the APIs of the application at a higher level. Or you can use the internal API dashboard if you need to debug the API and profile the SQL commands.

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

## Application Demo

<img width="1440" alt="Screen Shot 2022-10-21 at 12 53 03 PM" src="https://user-images.githubusercontent.com/80547043/197249988-bf3f4f2e-0653-439e-90e3-cc815710472e.png">

<img width="1440" alt="Screen Shot 2022-10-21 at 12 54 32 PM" src="https://user-images.githubusercontent.com/80547043/197250013-b04e5ad2-5c60-4e10-b95f-5dd32624b02c.png">

<img width="1440" alt="Screen Shot 2022-10-21 at 12 54 54 PM" src="https://user-images.githubusercontent.com/80547043/197250050-d021df99-ca59-40d9-8e3f-27e9ef33676d.png">

<img width="1440" alt="Screen Shot 2022-10-21 at 12 55 07 PM" src="https://user-images.githubusercontent.com/80547043/197250079-524ec3ca-9431-453b-9327-ffdf0a033ece.png">

<img width="1440" alt="Screen Shot 2022-10-21 at 12 55 17 PM" src="https://user-images.githubusercontent.com/80547043/197250097-78929972-b2e0-45bd-96c2-46ab4a1fefca.png">

<img width="1440" alt="Screen Shot 2022-10-21 at 12 56 05 PM" src="https://user-images.githubusercontent.com/80547043/197250158-8d760dba-0b8d-4196-bcd2-ea579e2600b6.png">

<img width="1440" alt="Screen Shot 2022-10-21 at 12 56 50 PM" src="https://user-images.githubusercontent.com/80547043/197250184-1024161a-c4fe-469d-b9fe-9438ab16a6d8.png">

<img width="1440" alt="Screen Shot 2022-10-21 at 12 55 42 PM" src="https://user-images.githubusercontent.com/80547043/197250119-453326a3-add6-4634-8f80-fa3b9bede20e.png">

<img width="1440" alt="Screen Shot 2022-10-21 at 12 57 15 PM" src="https://user-images.githubusercontent.com/80547043/197250205-ae763c6e-1544-4d12-83ec-ad154997ddf3.png">

<img width="1440" alt="Screen Shot 2022-10-21 at 12 57 45 PM" src="https://user-images.githubusercontent.com/80547043/197250218-fba7bbb3-f09e-46f5-aa63-b22d4a272913.png">

<img width="1440" alt="Screen Shot 2022-10-21 at 12 59 48 PM" src="https://user-images.githubusercontent.com/80547043/197250236-9ed07e2e-71f1-41b1-b82b-5dbc9b52e1c9.png">
