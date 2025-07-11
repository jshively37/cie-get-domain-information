# Overview
This Python script queries Palo Alto's Cloud Identity Engine and returns the number of users and groups per configured CIE directory.

## Requirements
```
black==25.1.0
certifi==2025.6.15
charset-normalizer==3.4.2
click==8.2.1
idna==3.10
mypy_extensions==1.1.0
packaging==25.0
pathspec==0.12.1
platformdirs==4.3.8
python-dotenv==1.1.1
requests==2.32.4
urllib3==2.5.0
```

## Creating a service account in Prisma Access

You will need to create a service account in Prisma Access to generate the access token.

The Client ID, Secret ID, and TSG ID will be saved in the .env file.

To create a service account: https://pan.dev/sase/docs/service-accounts/


## Installing and running

Clone down this repo and cd into the directory.

Create a Python virtual environment: python -m venv venv

Activate the virtual environment: \
Windows: .\venv\Scripts\activate \
OSX: source venv/bin/activate \

Install the dependencies using `pip install -r requirements.txt`

Rename `.env.example` to `.env` and populate your variables in this file generated while creating the service account. The .env is included in the .gitignore to ensure it does not accidentally get checked into a git repo.

Run: `python main.py`

The output will be displayed to the screen.
