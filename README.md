# news_api

API Service with custom token authorization, and News model.

Project aviable in http://51.250.103.147


#### Stack: 
Python 3, Django, gunicorn, PostgreSQL, nginx

## How start project:

Clone a repository and go to command line:

```sh
git clone https://github.com/menyanet73/news_api.git
```

```sh
cd news_api/
```

Create .env file.

```sh
touch .env
```

Fill it in with your data. 

```sh
SECRET_KEY='django-insecure-***django-secret-key***'
ALLOWED_HOSTS=['*']
POSTGRES_NAME=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
PGHOST=database
PGPORT=5432
DEBUG=0
```

```sh
cd infra
```

Create/download docker-compose images and containers

```sh
docker-compose up
```


Done!

### Endpoints

http://51.250.103.147/users/ - Allowed methods [POST] - {"username":"user", "password":"pass"}, for create user. <br/>
http://51.250.103.147/users/{id}/ - Allowed methods [DELETE], for delete user.<br/>
http://51.250.103.147/auth/ - Allowed methods [POST] - {"username":"user", "password":"pass"}, for create token.<br/>
Token must be transmissed to header of request (Authorization - Token ***token***<br/>
http://51.250.103.147/news/ - Allowed methods [GET, POST] - {"title":"Title of news", "text": "text of news, and description for photos of Spider Man."}, for create news and get list of it.<br/>
http://51.250.103.147/news/{id}/ - Allowed methods [GET, DELETE, PUT, PATCH], retrieve, delete or update news.

### Author
##### https://github.com/menyanet73
