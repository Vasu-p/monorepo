# Generated by Django 5.1.1 on 2024-09-12 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("notes", "0007_alter_note_options_alter_servicerequest_options_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="moodevent",
            name="id",
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name="noteevent",
            name="id",
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name="notenextstepsevent",
            name="id",
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name="noteprovidedservicesevent",
            name="id",
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name="notepurposesevent",
            name="id",
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name="noterequestedservicesevent",
            name="id",
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name="servicerequestevent",
            name="id",
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name="taskevent",
            name="id",
            field=models.BigIntegerField(),
        ),
    ]