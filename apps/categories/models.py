from django.db import models


class Category(models.Model):
    INCOME = "income"
    EXPENSES = "expenses"
    SAVINGS = "savings"
    CATEGORY_TYPES = [
        (INCOME, 'income'),
        (EXPENSES, 'expenses'),
        (SAVINGS, 'savings'),
    ]
    name = models.CharField(max_length=50, default="Category name")
    main_category = models.CharField(max_length=50)
    type = models.CharField(max_length=8, choices=CATEGORY_TYPES, default=INCOME)
    amount = models.FloatField(default=0)
    symbol = models.CharField(max_length=10, default="Symbol")
