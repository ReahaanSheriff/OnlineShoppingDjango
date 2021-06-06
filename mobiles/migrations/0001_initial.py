# Generated by Django 3.0.6 on 2020-06-09 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='accessories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img1', models.ImageField(upload_to='pics')),
                ('img2', models.ImageField(upload_to='pics')),
                ('img3', models.ImageField(upload_to='pics')),
                ('img4', models.ImageField(upload_to='pics')),
                ('category', models.CharField(max_length=50)),
                ('o_price', models.IntegerField()),
                ('price', models.IntegerField()),
                ('offer', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='mobiles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('img1', models.ImageField(upload_to='pics')),
                ('img2', models.ImageField(upload_to='pics')),
                ('img3', models.ImageField(upload_to='pics')),
                ('img4', models.ImageField(upload_to='pics')),
                ('brand', models.CharField(max_length=50)),
                ('o_price', models.IntegerField()),
                ('price', models.IntegerField()),
                ('offer', models.BooleanField(default=False)),
                ('ram', models.IntegerField()),
                ('rom', models.IntegerField()),
                ('battery', models.IntegerField()),
                ('processor', models.CharField(max_length=50)),
                ('os', models.CharField(max_length=50)),
                ('f_camera', models.IntegerField()),
                ('r_camera', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('image', models.ImageField(upload_to='products/')),
                ('price', models.IntegerField()),
            ],
        ),
    ]