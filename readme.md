# Plat-nner
MAS-RAD CAS-IDD 2025 Deployment of software solutions

Rafael Teixeira

## Description
Plat-nner is a simple planning app allowing users to add events, event posts and a list of person for each post.

The goal is to have a small dockable app usable by small teams. All the members of the team that access the app see the same events displayed.

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

Customized for needs of the project

Docker-compose builds 4 containers :
- Backend (flaskr)
- Db : mariaDB
- Proxy : Nginx
- Phpmyadmin

## Install locally
1. Install Python. The app is build on Python 3.13
2. Clone the repository
3. Go to the created folder and run the commands :
```bash
docker compose -f compose.yaml -f compose.dev.yaml build
docker compose -f compose.yaml -f compose.dev.yaml up -d
```
4. In a browser, go to localhost
5. Start using the app
6. To use phpmyadmin, go to localhost:8080

The compose.dev.yaml file defines development config. For production, don't use it and create dedicated file replacing the values and replacing compose.dev.yaml in the above commands

## Setup docker files
### Create files with environment variables
The build needs two files with env variables to work properly.

#### Files
1. Create a db folder in project root folder. Inside it, create a password.txt file. Edit the file and write your password on the first line. This file is used by the compose.yaml file as a secret to set the password credentials for these containers : backend, db and phpmyadmin

2. In the project root folder, create a .env file. The format is VARNAME=YOUR_VALUE, one per line. In the .env file, define the following env var :

    - REGISTER_SECRET_CODE

    This var is needed in the app to create new users.
