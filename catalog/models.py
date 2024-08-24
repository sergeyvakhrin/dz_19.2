from django.db import models

NULLABLE = {"null": True, "blank": True}


class Category(models.Model):
    category_name = models.CharField(
        max_length=100, verbose_name="Категория", help_text="Введите название категории"
    )
    category_description = models.TextField(
        verbose_name="Описание категории",
        help_text="Введите описание категории",
        **NULLABLE
    )

    def __str__(self):
        return f"{self.category_name}"

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ("category_name",)


class Product(models.Model):
    product_name = models.CharField(
        max_length=100,
        verbose_name="Наименование",
        help_text="Введите ниаменование продукта"
    )
    product_description = models.TextField(
        verbose_name="Описание продуктв",
        help_text="Введите описание продукта",
        **NULLABLE
    )
    product_image = models.ImageField(
        upload_to="product/",
        verbose_name="Фото",
        **NULLABLE,
        help_text="Загрузите фото продукта"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        verbose_name="Категория",
        help_text="Введите категорию",
        **NULLABLE,
        related_name="Products"
    )
    price = models.IntegerField(verbose_name="Цена", help_text="Введите цену")
    created_at = models.DateTimeField(
        verbose_name="Дата создания", help_text="Введите дату создания", **NULLABLE
    )
    created_up = models.DateTimeField(
        verbose_name="Дата изменения", help_text="Введите дату изменения"
    )

    def __str__(self):
        return f"{self.product_name}"

    class Meta:
        verbose_name = "Продукт"
        verbose_name_plural = "Продукты"
        ordering = ("product_name",)

# class Student(models.Model):
#     first_name = models.CharField(max_length=100, verbose_name='имя')
#     last_name = models.CharField(max_length=100, verbose_name='фамилия')
#     avatar = models.ImageField(upload_to='students/', verbose_name='аватар', **NULLABLE)
#
#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'
#
#     class Meta:
#         verbose_name = 'студент'
#         verbose_name_plural = 'студенты'
#         ordering = ('last_name',)
