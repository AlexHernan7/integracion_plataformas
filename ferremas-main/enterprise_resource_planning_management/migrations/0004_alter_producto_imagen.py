# Generated by Django 4.2.13 on 2024-05-19 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterprise_resource_planning_management', '0003_alter_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(default='productos/no-image.jpg', upload_to='productos/', verbose_name='Imagen'),
        ),
    ]