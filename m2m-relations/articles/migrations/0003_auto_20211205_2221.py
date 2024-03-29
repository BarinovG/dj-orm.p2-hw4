# Generated by Django 3.2.9 on 2021-12-05 19:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20211205_2109'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleToTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='article',
            name='scopes',
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, null=True, verbose_name='Тег')),
                ('articles', models.ManyToManyField(related_name='tags', through='articles.ArticleToTag', to='articles.Article')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.AddField(
            model_name='articletotag',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.article'),
        ),
        migrations.AddField(
            model_name='articletotag',
            name='tag',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scopes', to='articles.tag'),
        ),
    ]
