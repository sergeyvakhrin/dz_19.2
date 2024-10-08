# Generated by Django 5.1 on 2024-08-24 10:59

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "category_name",
                    models.CharField(
                        help_text="Введите название категории",
                        max_length=100,
                        verbose_name="Категория",
                    ),
                ),
                (
                    "category_description",
                    models.TextField(
                        blank=True,
                        help_text="Введите описание категории",
                        null=True,
                        verbose_name="Описание категории",
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
                "ordering": ("category_name",),
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "product_name",
                    models.CharField(
                        help_text="Введите ниаменование продукта",
                        max_length=100,
                        verbose_name="Наименование",
                    ),
                ),
                (
                    "product_description",
                    models.TextField(
                        blank=True,
                        help_text="Введите описание продукта",
                        null=True,
                        verbose_name="Описание продуктв",
                    ),
                ),
                (
                    "product_image",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите фото продукта",
                        null=True,
                        upload_to="product/",
                        verbose_name="Фото",
                    ),
                ),
                (
                    "price",
                    models.IntegerField(help_text="Введите цену", verbose_name="Цена"),
                ),
                (
                    "created_at",
                    models.DateTimeField(
                        blank=True,
                        help_text="Введите дату создания",
                        null=True,
                        verbose_name="Дата создания",
                    ),
                ),
                (
                    "created_up",
                    models.DateTimeField(
                        help_text="Введите дату изменения",
                        verbose_name="Дата изменения",
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        blank=True,
                        help_text="Введите категорию",
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="Products",
                        to="catalog.category",
                        verbose_name="Категория",
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
                "ordering": ("product_name",),
            },
        ),
    ]
