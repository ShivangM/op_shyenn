# Generated by Django 5.0.1 on 2024-01-27 13:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("posts", "0007_alter_post_id"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="terms",
            field=models.CharField(max_length=2000, null=True),
        ),
    ]