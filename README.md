## Django Test Task

Please follow all instructions to test the app

* Clone the project from this repository
* Go to into `django-test` folder and run the following commands
    * docker-compose pull server
    * docker-compose up server
* Server will start. Now migrate and create superuser. To do run the following commands in another terminal
    * docker-compose exec server bash
    * pipenv run ./manage.py migrate
    * pipenv run ./manage.py createsuperuser


### Add some data

* login in the admin panel `localhost:8000/admin` with username and password
* create another normal user who is not superadmin
* click on the survey app and create some survey with a title


### API endpoints

* to login `/api/v1/rest-auth/login/`
    * it require username and password and will get token for authentication
* to create, get and update question `/api/v1/question/`
    * Only super admin can create, update and view question
* to survey `/api/v1/qanswer/`
    * user can give answer for question to survey`


### Fibonacci solution

* at the root folder there is a file called fiboacci.py
* Run this file and provide a input after running this file.

1000th fibonacci number is `43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875`