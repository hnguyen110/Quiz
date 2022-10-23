# Quizzes

Quizzes is a private platform for learning computer science by practicing mock exams and watching hands-on videos. 

## Technology Stack
<a href="https://www.python.org/" title="Python"><img src="https://github.com/get-icon/geticon/raw/master/icons/python.svg" alt="Python" width="40px" height="40px"></a>
<a href="https://www.djangoproject.com/" title="Django"><img src="https://github.com/get-icon/geticon/raw/master/icons/django.svg" alt="Django" width="40px" height="40px"></a>
<a href="https://dev.mysql.com/" title="MySQL"><img src="https://github.com/get-icon/geticon/raw/master/icons/mysql.svg" alt="MySQL" width="40px" height="40px"></a>
<a href="https://nodejs.org/" title="Node.js"><img src="https://github.com/get-icon/geticon/raw/master/icons/nodejs-icon.svg" alt="Node.js" width="40px" height="40px"></a>
<a href="https://prettier.io/" title="Prettier"><img src="https://github.com/get-icon/geticon/raw/master/icons/prettier.svg" alt="Prettier" width="40px" height="40px"></a>
<a href="https://www.typescriptlang.org/" title="Typescript"><img src="https://github.com/get-icon/geticon/raw/master/icons/typescript-icon.svg" alt="Typescript" width="40px" height="40px"></a>
<a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" title="JavaScript"><img src="https://github.com/get-icon/geticon/raw/master/icons/javascript.svg" alt="JavaScript" width="40px" height="40px"></a>
<a href="https://reactjs.org/" title="React"><img src="https://github.com/get-icon/geticon/raw/master/icons/react.svg" alt="React" width="40px" height="40px"></a>
<a href="https://nextjs.org/" title="Next.js"><img src="https://github.com/get-icon/geticon/raw/master/icons/nextjs-icon.svg" alt="Next.js" width="40px" height="40px"></a>
<a href="https://ant.design/" title="Ant Design"><img src="https://github.com/get-icon/geticon/raw/master/icons/ant-design.svg" alt="Ant Design" width="40px" height="40px"></a>
<a href="https://tailwindcss.com/" title="Tailwind CSS"><img src="https://github.com/get-icon/geticon/raw/master/icons/tailwindcss-icon.svg" alt="Tailwind CSS" width="40px" height="40px"></a>
<a href="https://www.w3.org/TR/html5/" title="HTML5"><img src="https://github.com/get-icon/geticon/raw/master/icons/html-5.svg" alt="HTML5" width="40px" height="40px"></a>
<a href="https://www.w3.org/TR/CSS/" title="CSS3"><img src="https://github.com/get-icon/geticon/raw/master/icons/css-3.svg" alt="CSS3" width="40px" height="40px"></a>
<a href="https://yarnpkg.com/" title="Yarn"><img src="https://github.com/get-icon/geticon/raw/master/icons/yarn.svg" alt="Yarn" width="40px" height="40px"></a>
<a href="https://www.npmjs.com/" title="npm"><img src="https://github.com/get-icon/geticon/raw/master/icons/npm.svg" alt="npm" width="40px" height="40px"></a>
<a href="https://aws.amazon.com/" title="AWS"><img src="https://github.com/get-icon/geticon/raw/master/icons/aws.svg" alt="AWS" width="40px" height="40px"></a>
<a href="https://git-scm.com/" title="Git"><img src="https://github.com/get-icon/geticon/raw/master/icons/git-icon.svg" alt="Git" width="40px" height="40px"></a>
<a href="https://stripe.com/" title="Stripe"><img src="https://github.com/get-icon/geticon/raw/master/icons/stripe.svg" alt="Stripe" width="40px" height="40px"></a>

## Authors

- [hnguyen110](https://github.com/hnguyen110)
- [cindy-jang](https://github.com/CindyJang1)

## System Design

![Quiz](https://user-images.githubusercontent.com/80547043/197255121-167c2053-e8dd-4556-a02b-c1c6634143f3.png)

![db](https://user-images.githubusercontent.com/80547043/197254733-bf9eb3ee-a354-48cb-8655-64bfc2350205.png)

## System Requirements

Please ensure you have installed these components on your computer before running the application.

- Docker
- Local MySQL server
- Python, version 3.10.6
- Pipenv, version 2022.9.4
- Nodejs, version v16.17.0
- Npm, version 8.15.0
- Yarn, version 1.22.17
## Frontend Installation

Clone the project from GitHub.
```bash
git clone git@github.com:hnguyen110/Quiz-Client-UI.git
```

Go inside the application folder and install the dependencies.
```bash
yarn install
```

Run the Tailwind script to watch for CSS changes.
```bash
yarn tailwind
```

Start the local development server
```bash
yarn dev
```

## Backend Installation

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

<img width="1440" alt="Screen Shot 2022-10-21 at 1 43 00 PM" src="https://user-images.githubusercontent.com/80547043/197257012-abadf986-d0b3-47b9-8722-ab7ffb95ae74.png">

View the Redoc documentation by visiting the following location.
```bash
http://127.0.0.1:8000/redoc/
```

<img width="1440" alt="Screen Shot 2022-10-21 at 1 42 43 PM" src="https://user-images.githubusercontent.com/80547043/197257072-f5ced53f-be26-4320-9005-8c120a341404.png">

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

`STRIPE_SECRET_KEY` - the stripe private API key

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
