# Generated by Django 3.1.3 on 2020-11-17 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('people', '0004_auto_20201116_1034'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='url_cv',
            field=models.URLField(blank=True, help_text='Link to CV, e.g. on LinkedIn', max_length=1024, null=True, verbose_name='Curriculum Vitae'),
        ),
        migrations.AlterField(
            model_name='person',
            name='url_personal',
            field=models.URLField(blank=True, help_text='Link to personal or professional homepage', max_length=1024, null=True, verbose_name='Personal website'),
        ),
        migrations.AlterField(
            model_name='person',
            name='url_publications',
            field=models.URLField(blank=True, max_length=1024, null=True, verbose_name='Link to publications'),
        ),
        migrations.AlterField(
            model_name='person',
            name='url_researchgate',
            field=models.URLField(blank=True, help_text='Link to your profile', max_length=1024, null=True, verbose_name='ResearchGate link'),
        ),
        migrations.AlterField(
            model_name='project',
            name='homepage',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]
