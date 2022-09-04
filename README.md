<p align="center">
<img src="https://github.com/Checkmarx/capital/blob/capital-dev/.github/assets/capital-logo-white.PNG#center" width="600" height="300" />
</p>

[![Docker](https://img.shields.io/badge/docker-support-%2300D1D1)](https://github.com/Checkmarx/capital/tree/capital-dev#quickstart) 
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

Quick facts
----------

   - **Name**:      'c{api}tal'
   - **Type**:      Vulnerable API Security application
   - **License**:   MIT
   - **Language**:  Python, JS
   - **Author**:    Checkmarx
   
Description
----------
The Checkmarx research team created c{api}tal to provide users with an active playground in which they hone their API Security skills. <br> The c{api}tal application contains 10 API challenges which map to the <a href="https://owasp.org/www-project-api-security/" target="_blank">OWASP top 10 API risks</a>. <br> It is built with Python (FastAPI) and JS (React).

c{api}tal can also be used for conducting your own API Security CTF event.

Visit [capital-ctf.com](https://www.capital-ctf.com/) to learn about the vulnerabilities and the challenges.

Features:
----------
Contains 10 challenges based on the <a href="https://owasp.org/www-project-api-security/" target="_blank">OWASP top 10 API risks</a>

* Built on FastAPI (backend) and React (frontend) 
* UI - Blogging website (i.e medium) 
* OpenAPI3 API JSON specification file that can be imported as a POSTMAN collection 
* JWT token based authentication (lifetime can be adjusted in app) 


c{api}tal is a blogging application which allow users to register, create and delete posts, 
create and delete comments, follow other users, and more.

<p align="center">
<img src="https://github.com/Checkmarx/capital/blob/capital-dev/postman/API%20endpoints.PNG#center" width="1000" height="850" />
</p>

# Quickstart

Run the full application using docker-compose:
 
    docker-compose up -d


The backend will be running on http://localhost:8000/ <br>
The frontend will be running on http://localhost:4100/ <br>
Check out the API endpoints specification page at http://localhost:8000/docs <br>

Generate API requests to http://localhost:8000/api (via POSTMAN/Burp for example) <br>
Import the API collection JSON file to POSTMAN and start generating API requests: <br>
[click here to download the c{api}tal API json collection file](https://www.capital-ctf.com/files/de1ad03a48959f38c7f131f81f95d42e/capital.postman_collection.json)

<p align="center">
<img src="https://github.com/Checkmarx/capital/blob/capital-dev/.github/assets/postman%20-%20register%20user%20request.PNG#center" width="1000" height="300" />
</p>

To run the web application in debug:
----------

First, run ``PostgreSQL``, set environment variables and create database:

    export POSTGRES_DB=rwdb POSTGRES_PORT=5432 POSTGRES_USER=postgres POSTGRES_PASSWORD=postgres
    docker run --name pgdb --rm -p 5432:5432 -e POSTGRES_USER="$POSTGRES_USER" -e POSTGRES_PASSWORD="$POSTGRES_PASSWORD" -e POSTGRES_DB="$POSTGRES_DB" postgres
    export POSTGRES_HOST=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' pgdb)
    createdb --host=$POSTGRES_HOST --port=$POSTGRES_PORT --username=$POSTGRES_USER $POSTGRES_DB

[Option 1] Run locally 

Then run the following commands to bootstrap your environment:

    git clone https://github.com/Checkmarx/capital
    cd capital
    pip install -r requirements.txt
    

Then create ``.env`` file in project root and set environment variables for application:
    
    export POSTGRES_DB=rwdb POSTGRES_PORT=5432 POSTGRES_USER=postgres POSTGRES_PASSWORD=postgres
    export POSTGRES_HOST=localhost
    export DATABASE_URL=postgresql://$POSTGRES_USER:$POSTGRES_PASSWORD@$POSTGRES_HOST:$POSTGRES_PORT/$POSTGRES_DB
    touch .env
    echo APP_ENV=dev
    echo DATABASE_URL=postgresql://$POSTGRES_USER:$POSTGRES_PASSWORD@$POSTGRES_HOST:$POSTGRES_PORT/$POSTGRES_DB >> .env
    echo SECRET_KEY=$(openssl rand -hex 32) >> .env

Then run the backend server:

    python3 main.py

[Option 2] Run backend using docker
Run the backend using docker build:
 
    docker build . -t capital
    docker run -p 8000:8000  -e DATABASE_URL=postgresql://postgres:postgres@host.docker.internal:5432/rwdb --rm --name backend-capital capital


Run tests
---------

Tests for this project are defined in the ``tests/`` folder.

Set up environment variable ``DATABASE_URL`` or set up ``database_url`` in ``app/core/settings/test.py``

This project uses `pytest
<https://docs.pytest.org/>`_ to define tests because it allows you to use the ``assert`` keyword with good formatting for failed assertations.


To run all the tests of a project, simply run the ``pytest`` command: ::

    $ pytest
    ================================================= test session starts ==================================================
    platform linux -- Python 3.8.3, pytest-5.4.2, py-1.8.1, pluggy-0.13.1
    rootdir: /home/some-user/user-projects/fastapi-realworld-example-app, inifile: setup.cfg, testpaths: tests
    plugins: env-0.6.2, cov-2.9.0, asyncio-0.12.0
    collected 90 items

    tests/test_api/test_errors/test_422_error.py .                                                                   [  1%]
    tests/test_api/test_errors/test_error.py .                                                                       [  2%]
    tests/test_api/test_routes/test_articles.py .................................                                    [ 38%]
    tests/test_api/test_routes/test_authentication.py ..                                                             [ 41%]
    tests/test_api/test_routes/test_comments.py ....                                                                 [ 45%]
    tests/test_api/test_routes/test_login.py ...                                                                     [ 48%]
    tests/test_api/test_routes/test_profiles.py ............                                                         [ 62%]
    tests/test_api/test_routes/test_registration.py ...                                                              [ 65%]
    tests/test_api/test_routes/test_tags.py ..                                                                       [ 67%]
    tests/test_api/test_routes/test_users.py ....................                                                    [ 90%]
    tests/test_db/test_queries/test_tables.py ...                                                                    [ 93%]
    tests/test_schemas/test_rw_model.py .                                                                            [ 94%]
    tests/test_services/test_jwt.py .....                                                                            [100%]

    ============================================ 90 passed in 70.50s (0:01:10) =============================================
    $

If you want to run a specific test, you can do this with `this
<https://docs.pytest.org/en/latest/usage.html#specifying-tests-selecting-tests>`_ pytest feature: ::

    $ pytest tests/test_api/test_routes/test_users.py::test_user_can_not_take_already_used_credentials

Web routes
----------

All routes are available on ``/docs`` or ``/redoc`` paths with Swagger or ReDoc.


Project structure
-----------------

Files related to application are in the ``app`` or ``tests`` directories.
Application parts are:

    app
    ├── api              - web related stuff.
    │   ├── dependencies - dependencies for routes definition.
    │   ├── errors       - definition of error handlers.
    │   └── routes       - web routes.
    ├── core             - application configuration, startup events, logging.
    ├── db               - db related stuff.
    │   ├── migrations   - manually written alembic migrations.
    │   └── repositories - all crud stuff.
    ├── models           - pydantic models for this application.
    │   ├── domain       - main models that are used almost everywhere.
    │   └── schemas      - schemas for using in web routes.
    ├── resources        - strings that are used in web responses.
    ├── services         - logic that is not just crud related.
    ├── credentials      - list of common strings for Brute Force.
    ├── postman          - api json file for postman.
    ├── redis            - redis docker file and conf file.
    ├── scripts         
    ├── tests         
    └── main.py          - FastAPI application creation and configuration.
    
Referrences
----------
c{api}tal CTF event on AppSec Village at DefCon30: <br>
https://www.appsecvillage.com/events/dc-2022/c%7Bapi%7Dtal-api-security-ctf

Write-up (Credit to <a href="https://medium.com/@maor_59001" target="_blank">Maor Tal</a>): <br>
Part 1: <br>
https://medium.com/@maor_59001/defcon-30-appsec-villiage-ctf-writeup-part-1-1730de791f50 <br>
Part 2: <br>
https://medium.com/@maor_59001/defcon-30-c-api-tal-ctf-writeup-part-2-ef99a0fc8d28

c{api}tal CTF event sum-up blog: <br>
TBD

Stickers from DefCon30: <br>
<img src="https://github.com/Checkmarx/capital/blob/capital-dev/.github/assets/sticker1.png" width="300" height="150" />
<img src="https://github.com/Checkmarx/capital/blob/capital-dev/.github/assets/sticker2.png" width="300" height="150" />
<img src="https://github.com/Checkmarx/capital/blob/capital-dev/.github/assets/sticker3.jpeg" width="300" height="150" />


Development and Bugs
----------
Found an issue, or have a great idea? Let us know:

* E-mail - ResearchTeam@checkmarx.com

Contributions are appreciated and can be done via GitHub. 

See CONTRIBUTING.md for more information about how to submit them.

Thanks
----------

The application was built base on ``real-world-app`` , we used these awesome repos: <br>
<a href="https://github.com/nsidnev/fastapi-realworld-example-app" target="_blank">Backend - FastAPI (Python)</a>  <br>
<a href="https://github.com/khaledosman/react-redux-realworld-example-app" target="_blank">Frontend - React (JS)</a>  <br>
Thanks again for contributing to the open-source community! <br>
