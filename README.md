# Running Project locally:

### TO TRY THE DEPLOYED WEB APP GO [HERE](https://demo-task-app.herokuapp.com/)

![APP SCREENSHOT](https://raw.githubusercontent.com/ashlyjustin/movieDbAPI/master/SS.png)

`git clone https://github.com/ashlyjustin/movieDbAPI.git`

### Create a virtual envirornment and activate it

### Run in terminal
`cd movieDbAPI`

### Install requirements

`pip install -r requirements.txt`

### Create a `.ENV` file in the `root` directory

### Add the following lines to the .env file

`MovieDB_APP_Key=958038249ce6d4ddc29c531ce3164df3`

`SECRET_KEY=zs-*8pb5k7n%&_#s4x56avou-ulza+p*ma_*k6-vh+k1gete@w`

### Go to `settings.py`

_Change `ALLOWED HOSTS AS SHOWN:` -> `ALLOWED HOSTS = []`_

### From project `root` directory terminal

RUN `python manage.py -runserver`

### It will run locally at `localhost:8000`

## You're good to go!
