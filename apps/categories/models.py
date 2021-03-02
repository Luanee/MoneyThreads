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
    name = models.CharField(max_length=50)
    amount = models.FloatField(default=0)
    type = models.CharField(max_length=8, choices=CATEGORY_TYPES, default=INCOME)
    main_category = models.CharField(max_length=50)
