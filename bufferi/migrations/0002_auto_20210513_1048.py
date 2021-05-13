# Generated by Django 3.2.2 on 2021-05-13 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bufferi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140)),
                ('balance', models.IntegerField()),
                ('deleted', models.BooleanField(default=False)),
                ('mobilepay_id', models.CharField(blank=True, max_length=140, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='deleted',
        ),
        migrations.AddField(
            model_name='transaction',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='bufferi.customer'),
        ),
    ]