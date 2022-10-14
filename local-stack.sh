#!/bin/sh
echo "Setting AWS environment variables for LocalStack"
export AWS_ACCESS_KEY_ID=local_user
export AWS_SECRET_ACCESS_KEY=password
export AWS_DEFAULT_REGION=us-east-1
until (curl --silent http://localhost:4566/health | grep "\"s3\": \"\(running\|available\)\"" > /dev/null); do
    sleep 5
done
aws --endpoint-url=http://localhost:4566 s3api create-bucket --bucket quiz
echo 'LocalStack S3 Ready'