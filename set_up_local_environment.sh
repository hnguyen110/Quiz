#!/bin/sh
export DEBUG=True
export SECRET_KEY=O4k6xexA4KgZq5lZdETMdO3xjzuuN2qx3k2Itl5ctSZVgGeoEc
export ALLOWED_HOSTS=0.0.0.0
#export DATABASE_NAME
#export DATABASE_HOST
#export DATABASE_USER
#export DATABASE_PASSWORD
export CORS_ALLOWED_ORIGINS='http://localhost:3000'
export EMAIL_HOST=localhost
#export EMAIL_HOST_USER
#export EMAIL_HOST_PASSWORD
export EMAIL_PORT=1025
export DEFAULT_FROM_EMAIL=administrator@pandadoesquizzes.com
export AWS_S3_ENDPOINT_URL=http://localhost:4566
export AWS_ACCESS_KEY_ID=local_user
export AWS_SECRET_ACCESS_KEY=password
export AWS_STORAGE_BUCKET_NAME=quiz