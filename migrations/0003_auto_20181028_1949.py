# Generated by Django 2.1.2 on 2018-10-29 02:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_messages', '0002_auto_20160607_0852'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='parent_msg',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='next_messages', to='django_messages.Message', verbose_name='Parent message'),
        ),
        migrations.AlterField(
            model_name='message',
            name='recipient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='received_messages', to=settings.AUTH_USER_MODEL, verbose_name='Recipient'),
        ),
        migrations.AlterField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='sent_messages', to=settings.AUTH_USER_MODEL, verbose_name='Sender'),
        ),
    ]
