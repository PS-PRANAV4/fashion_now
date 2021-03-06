# Generated by Django 4.0.4 on 2022-06-08 06:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0010_remove_category_main_cate_delete_maincategory'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('MEN', 'MEN'), ('WOMEN', 'WOMEN'), ('KIDS', 'KIDS')], default='MEN', max_length=20)),
                ('main_category_image', models.ImageField(blank=True, upload_to='photos/maincategory')),
            ],
        ),
        migrations.AddField(
            model_name='category',
            name='main_cate',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='product.maincategory'),
        ),
    ]
