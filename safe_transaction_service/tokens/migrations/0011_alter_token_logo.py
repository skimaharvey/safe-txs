# Generated by Django 4.2 on 2023-05-03 11:04

from django.db import migrations

import imagekit.models.fields

import safe_transaction_service.tokens.models


class Migration(migrations.Migration):
    dependencies = [
        ("tokens", "0010_tokenlist"),
    ]

    operations = [
        migrations.AlterField(
            model_name="token",
            name="logo",
            field=imagekit.models.fields.ProcessedImageField(
                blank=True,
                default="",
                storage=safe_transaction_service.tokens.models.get_file_storage,
                upload_to=safe_transaction_service.tokens.models.get_token_logo_path,
            ),
        ),
    ]
