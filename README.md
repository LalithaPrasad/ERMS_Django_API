This is again the app 'Employee record management system'. It uses Django
rest_framework to provide the api. It uses token based authentication.

To run it first initialise the database with:

    ./manage.py makemigrations app_django
    ./manage.py migrate

Then:

    ./manage.py runserver

To access the api, you can use a http client like postman or httpie. Below I am
showing the commands for httpie:

    http post http://localhost:8000/create_admin/ username=<username> password=<password>

    http get http://localhost:8000/get_token/ username=<username> password=<password>

    http post http://localhost:8000/add_employee/ token:<token> name=<name>
                                                age=<age> ed=<education> role=<role>

    http put http://localhost:8000/modify_employee/ token:<token> id=<id>
                                                            ed=<new ed> role=<new role>

    http delete http://localhost:8000/delete_employee/ token:<token> id=<id>

    http get http://localhost:8000/display_employees/ token:<token>

Remember to add a / at the the end of the url. Django rest_framework requires
it.
