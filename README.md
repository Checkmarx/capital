<p align="center">
<img src="https://github.com/Checkmarx/capital/blob/capital-dev/.github/assets/capital-logo.png#center" width="600" height="300" />
</p>

[![License: AGPL v3](https://img.shields.io/badge/License-AGPL%20v3-blue.svg)](https://www.gnu.org/licenses/agpl-3.0)

Quick facts
----------

   - **Name**:      'c{api}tal'
   - **Type**:      Vulnerable API Security application
   - **License**:   GNU AFFERO GENERAL PUBLIC LICENSE
   - **Language**:  Python, JS
   - **Author**:    CheckMarx Research team
   
Description
----------
c{api}tal is a vulnerable API application based on the OWASP top 10 API risks.
It is built with Python (FastAPI) and JS (React) and it includes 10 API challenges. 
c{api}tal was created by CheckMarx Research team in order to provide users with a playground in which they could learn and develop their API Security skills.
You can use c{api}tal to learn and exploit API Security vulnerabilities!

c{api}tal can also be used for conducting your own API Security CTF event.

Visit [capital-ctf.com](https://www.capital-ctf.com/) to learn about the vulnerabilities and the challenges.
<p align="center">
<img src="https://github.com/Checkmarx/capital/blob/capital-dev/.github/assets/challange.PNG#center" width="800" height="600" />
</p>

Features:
----------

* Contains 10 challenges based on the OWASP top 10 API risks
* The application is built on FastAPI (backend) and React (frontend)
* UI - Blogging website (i.e medium)
* OpenAPI3 API json specification file that can be imported as a POSTMAN collection
* JWT token based authentication (lifetime can be adjusted in app)

c{api}tal is a blogging application which allow users to register, create and delete posts, 
create and delete comments, follow other users, and more.

<p align="center">
<img src="https://github.com/Checkmarx/capital/blob/capital-dev/postman/API%20endpoints.PNG#center" width="1000" height="850" />
</p>

Quickstart
----------

Run the application using docker-compose:
 
    docker-compose up -d

To run the web application in debug:

First, run ``PostgreSQL``, set environment variables and create database:

    export POSTGRES_DB=rwdb POSTGRES_PORT=5432 POSTGRES_USER=postgres POSTGRES_PASSWORD=postgres
    docker run --name pgdb --rm -e POSTGRES_USER="$POSTGRES_USER" -e POSTGRES_PASSWORD="$POSTGRES_PASSWORD" -e POSTGRES_DB="$POSTGRES_DB" postgres
    export POSTGRES_HOST=$(docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' pgdb)
    createdb --host=$POSTGRES_HOST --port=$POSTGRES_PORT --username=$POSTGRES_USER $POSTGRES_DB

Then run the following commands to bootstrap your environment:

    git clone https://github.com/Checkmarx/capital
    cd capital
    pip install -r requirements.txt
    python3 main.py

Then create ``.env`` file in project root and set environment variables for application:

    touch .env
    echo APP_ENV=dev
    echo DATABASE_URL=postgresql://$POSTGRES_USER:$POSTGRES_PASSWORD@$POSTGRES_HOST:$POSTGRES_PORT/$POSTGRES_DB >> .env
    echo SECRET_KEY=$(openssl rand -hex 32) >> .env

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

Development and Bugs
----------
Found an issue, or have a great idea? Let us know:

* E-mail - ResearchTeam@checkmarx.com

Contributions are appreciated and can be done via GitHub. 

See CONTRIBUTING.md for more information about how to submit them.

Thanks
----------

Thanks to the community for using and supporting open source software.
