# cau-anseong-21-spring-festival

중앙대학교 안성캠퍼스 봄축제 웹사이트

## Installation

### Set up `.env` file

Create `.env` file with the template `.env.template`.

```
SECRET_KEY= # Your secret key
DEBUG= # 0 or 1
ALLOWED_HOSTS= # localhost, server domains, ...
```

### Activate Python virtual environment

All of the commands are to be run with virtual environment activated.

```sh
$ python3 -m venv ./venv
$ source ./venv/bin/activate
(venv) $ pip install -r requirements.txt
```

### Run the development server

```sh
$ (venv) python manage.py runserver [port number]
```
