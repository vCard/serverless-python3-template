# Serverless Python Template

## Deploying service to AWS from command line

Make sure you have the [Serverless Framework](http://www.serverless.com) installed and you're using Node.js v4.0+. 
```
npm install serverless -g
```

Install project dependencies via npm:
```
npm install
```

Run the following command to hydrate the required python libraries
```
pip install -t ./packages -r requirements.txt
```

Setup your environment appropriately by either running the command suitable with your OS or setting up your aws config file with the credentials in the result.

In the serverless.yml file, ensure the `stage` and `region` under `provider` are set like so

```
provider:
  name: aws
  runtime: python3.6

# the following are used for local deployment
  stage: dev
  region: ap-northeast-1
```

Run the following command in your Terminal window

```
serverless deploy
```

Run the following command to show the endpoint urls:

```
serverless info
```

Once you are done with testing, run the following command to **REMOVE** the service:

```
serverless remove
```

## Running tests and Lambda functions locally

Setup virtual environment:

```
$ python -m venv ./venv
```

Activate the env by running the following command:

```
source venv/bin/activate # linux/macos
# or
source ./venv/Script/activate # windows bash
```

Install the followings:

```
pip install nose
pip install python-lambda-local
```

To test a specific function:

```
python-lambda-local -l ./ -f handler -t 5 handlers/handler.py handlers/event.json
```

To run unit tests

```
nosetests -v
```

To exit from the virtual env, run the following command

```
deactivate
```
