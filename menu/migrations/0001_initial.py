# Generated by Django 4.1.4 on 2023-01-01 13:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
            ],
            options={
                'verbose_name': 'Menu',
                'verbose_name_plural': 'Menus',
            },
        ),
        migrations.CreateModel(
            name='MenuItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=128)),
                ('menu', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='menu_items', to='menu.menu')),
                ('parent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_items', to='menu.menuitem')),
            ],
            options={
                'verbose_name': 'Menu Item',
                'verbose_name_plural': 'Menu Items',
            },
        ),
    ]
