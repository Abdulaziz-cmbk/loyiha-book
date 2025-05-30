# Generated by Django 5.2 on 2025-05-31 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_author_is_deleted_book_is_deleted_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='quantity',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='created_at',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='expence',
            name='created_at',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='output',
            name='created_at',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='references',
            name='type',
            field=models.CharField(choices=[('kitob_turi', 'kitob_turi'), ('jinsi', 'jinsi'), ('chiqim_turi', 'chiqim_turi')], max_length=255, verbose_name='Malumotnoma turi'),
        ),
        migrations.AlterField(
            model_name='references',
            name='value',
            field=models.CharField(max_length=255, verbose_name="Ma'lumotnoma qiymati"),
        ),
        migrations.AlterField(
            model_name='sell',
            name='created_at',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='staff',
            name='birthdate',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='staff',
            name='created_at',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='staff_payment',
            name='created_at',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='staff_work',
            name='created_at',
            field=models.DateField(),
        ),
    ]
