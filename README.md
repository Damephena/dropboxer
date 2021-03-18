# Dropboxer

A simple file uploading application to desmonstrate how AWS S3 can be integrated into a Django Rest Framework Application.

This application is a tutorial codebase for [the section.io engineering blog](https://section.io/engineering-blog/).

## How to run this repository on your local machine:

1.

```bash
pip install -r requirements.txt
```

2. Replace placeholders in settings.py with your own

```python
AWS_ACCESS_KEY_ID = <YOUR AWS ACCESS KEY>
AWS_SECRET_ACCESS_KEY = <YOUR AWS SECRET KEY>
AWS_STORAGE_BUCKET_NAME = <YOUR AWS S3 BUCKET NAME>
AWS_S3_REGION_NAME = <YOUR AWS S3 BUCKET LOCATION>
```
3. Make migrations

```bash
pip manage.py makemigrations
pip manage.py migrate
```

4. Start local server

```bash
python manage.py runserver
```

That's it!😎

