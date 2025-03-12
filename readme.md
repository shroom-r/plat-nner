# Plat-nner
MAS-RAD CAS-IDD 2025 Deployment of software solutions

Rafael Teixeira

## Description
Plat-nner is a simple planning app allowing users to add events, event posts and a list of person for each post.

The goal is to have a small dockable app usable by small teams.

## Dependencies
### Python packages :
- Flask
- mysql-connector
- Flask-SQLAlchemy
- Flask-Migrate
- Flask-WTF
- Bootstrap-Flask
- Flask-Login

### Docker compose :
Based on awesome-compose nginx-flask-mysql ([LINK](https://github.com/docker/awesome-compose/tree/master/nginx-flask-mysql))

Personalized based on the goals and needs of the project

## Setup docker files
### Create files with environment variables
The build needs two files with env variables to work properly.

#### Files
1. Create a db folder in project root folder. Inside it, create a password.txt file. Edit the file and write your password on the first line. This file is used by the compose.yaml file as a secret to set the password credentials for these containers : backend, db and phpmyadmin

2. In the project root folder, create a .env file. The format is VARNAME=YOUR_VALUE, one per line. In the .env file, define the following env var :

    - REGISTER_SECRET_CODE

    This var is needed in the app to create new users.
