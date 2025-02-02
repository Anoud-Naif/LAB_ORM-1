# Generated by Django 4.2.7 on 2023-11-25 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0003_blog_delete_blogg'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='category',
            field=models.CharField(choices=[('Health', 'Health'), ('Stories', 'Stories'), ('Science', 'Science')], default='Health', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='images/default.jpeg', upload_to='images/'),
        ),
    ]
