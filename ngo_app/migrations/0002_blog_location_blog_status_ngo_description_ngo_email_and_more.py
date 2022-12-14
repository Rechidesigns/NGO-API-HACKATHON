# Generated by Django 4.1.2 on 2022-10-28 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ngo_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='location',
            field=models.CharField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='status',
            field=models.CharField(choices=[('unpublished', 'Unpublished'), ('published', 'Published')], default='published', max_length=50),
        ),
        migrations.AddField(
            model_name='ngo',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='ngo',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='ngo',
            name='website',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='ngo',
            name='reg_num',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
