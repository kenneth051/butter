# butter
Clone the repo to your local machine using the command `git clone https://github.com/kenneth051/butter.git`

Setup using docker
-------------------
download and install docker on your computer,

in the project root folder, run the command `docker-compose build` to build all images

run the command  `docker-compose up` to start the containers

to stop the containers run the command `docker-compose down`

Setup without docker
---------------------
after clonning the repo

create a `.env` file in root of the project and add a database url example is in `env_sample` file.

install pipenv by running the command `pip3 install pipenv` to create ana enviroment

in the pipenv enviroment install the requirements by running the command `pip install -r requirements.txt`

make sure you have postgres installed.

make migrations by running the command `python manage.py migrate`

start the app by running the command `python manage.py runserver`

Using the app.
--------------
on postman go the endpoint  `http://127.0.0.1:8000/butter/agreement/` to see the user agreement contract to be signed.

open another postman tab then go to the endpoint `http://127.0.0.1:8000/butter/sign_agreement/` to sign the agreement by passing in the various data feilds with there data

    {
      "first_name":",
      "last_name":"",
      "email":"",
      "password":"",
      "street":"",
      "post_code":" "
    }
    
by sending this data, you agree to the terms of the product/ company.

after go to the endpoint `http://127.0.0.1:8000/butter/agreement/`.

This time pass in the token you have recieved after signing the agreement.pass this token under the Headers' tab on postman using a key `Authorization`.
send the request, then you will see the html agreement you have signed  displayed in html.

make sure the token is correct and you paste it in fully without any other word appended to it.

To run the sample tests
-----------------------
Run the command `python3 manage.py test`


