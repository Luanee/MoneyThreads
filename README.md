# MoneyThreads

You often ask yourself where your money has gone? Follow the money threads and find out what you have done with your money.

### Development

#### Project Pre-Installations
Create a virtual environment in which to install Python pip packages. With [virtualenv](https://virtualenv.pypa.io),
```bash
virtualenv <dir_name>            # create a virtualenv
source <dir_name>/bin/activate   # activate the Python virtualenv
```
Install development dependencies,
```bashs
pip install -r requirements.txt
```

#### Create Django App

```bash
user@pc MoneyThreads ~ % python manage.py startapp <app_name> <root/app_name>
```

#### Add Migrations to App
  Creates new migrations based on the changes detected to your models. Migrations, their relationship with apps and more are covered in depth in the [migrations documentation](https://docs.djangoproject.com/en/3.1/topics/migrations/).

```bash
user@pc MoneyThreads ~ % python manage.py makemigrations <app_name>
```

#### Synchronizes App
Synchronizes the database state with the current set of models and migrations. Migrations, their relationship with apps and more are covered in depth in the [migrations documentation](https://docs.djangoproject.com/en/3.1/topics/migrations/).

```bash
user@pc MoneyThreads ~ % python manage.py migrate
```
