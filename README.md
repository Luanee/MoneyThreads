# MoneyThreads

You often ask yourself where your money has gone? Follow the money threads and find out what you have done with your money.

### Development

#### Activate Virtualenv


#### Create Django App

```console
user@pc MoneyThreads ~ % python manage.py startapp <app_name> <root/app_name>
```

#### Add Migrations to App
  Creates new migrations based on the changes detected to your models. Migrations, their relationship with apps and more are covered in depth in the [migrations documentation](https://docs.djangoproject.com/en/3.1/topics/migrations/).

```console
user@pc MoneyThreads ~ % python manage.py makemigrations <app_name>
```

#### Synchronizes App
Synchronizes the database state with the current set of models and migrations. Migrations, their relationship with apps and more are covered in depth in the [migrations documentation](https://docs.djangoproject.com/en/3.1/topics/migrations/).

```{shell}
user@pc MoneyThreads ~ % python manage.py migrate
```
