# Generated by Django 4.2 on 2024-04-30 11:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_product_is_published'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ('name',), 'permissions': [('can_edit_is_published', 'Может менять публикацию'), ('can_edit_description', 'Может менять описание'), ('can_edit_category', 'Может менять категорию')], 'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
    ]
