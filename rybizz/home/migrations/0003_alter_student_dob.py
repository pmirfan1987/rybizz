# Generated by Django 4.2.7 on 2024-01-15 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_student_delete_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='DOB',
            field=models.DateField(blank=True, default='', max_length=30, null=True),
        ),
    ]
