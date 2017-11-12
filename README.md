# googleVisionTest project

This is a simple image hosting application that additionally performs computer vision analysis via the Google Vision API.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites

- Python2.7
- pip
- PostreSQL database (9.4 - 9.6.2)
- Redis (3.2.5)
- Node.js (8.2.1)
- Google Vision API secret key (https://cloud.google.com/vision/docs/quickstart)

### Installing

1. Clone project from repository

2. Create virtualenv
```
virtualenv <your_env_name>
```

3. Run virtualenv
```
source <your_env_name>/bin/activate
```

4. Go to the project folder and install requirements
```
pip install -r requirements.txt
```

5. Copy google_vision_api_key.json to the <your_project_path>/googlevisiontest/google/

6. Create/download simple .jpeg/.png test image, and move it to the <your_project_path>/googlevisiontest/google/

7. Go to the <your_project_path>/googlevisiontest/

8. Create localsettings.py
```
cp localsettings.default localsettings.py
```

9. Update localsettings.py
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<database_name>',
        'USER': '<username>',
        'PASSWORD': '<password>',
        'HOST': '<host>',
        'PORT': '',
    }
}

DEBUG = True
API_KEY_PATH = <api_key_path> #example: os.path.join(BASE_DIR, 'google', 'api_key.json')
API_TEST_IMAGE_PATH = <api_test_image_path> #example os.path.join(BASE_DIR, 'google', 'test.png')

ALLOWED_HOSTS = []

BROKER_URL = '<your borker url>' #example: redis://localhost:6379/0
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json
,,,

10. If you don't have postgres user and database, create it

11. You need to export GOOGLE_APPLICATION_CREDENTIALS environment variable
```
export GOOGLE_APPLICATION_CREDENTIALS='<path_to_your_project>/googlevisiontest/google/api_key.json'
```

12. Run migrations
```
python manage.py migrate
```

13. Application is using thumbnail to cache images, so you need to generate thumbnail migration
```
manage.py makemigrations thumbnail
python manage.py migrate
```

14. Try to run application
```
python manage.py runserver
```
and go to the localhost:8000


15. Now you can test your google cloud connection
```
python manage.py test utils.tests
```
If tests didn't passed, check your GOOGLE_APPLICATION_CREDENTIALS variable and localsetting.py

16. If tests passed, run celery in other tab
```
celery --app=googlevisiontest.celery:app worker --loglevel=INFO -P solo
```

17. Now, your application should work !!
