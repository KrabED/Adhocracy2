# Generated by Django 2.2.6 on 2019-10-24 12:31

import adhocracy4.categories.fields
import adhocracy4.images.fields
import apps.moderatorfeedback.fields
import autoslug.fields
import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('a4_candy_moderatorfeedback', '0001_initial'),
        ('a4modules', '0004_description_maxlength_512'),
        ('a4categories', '0002_category_icon'),
        ('a4labels', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Idea',
            fields=[
                ('moderator_feedback', apps.moderatorfeedback.fields.ModeratorFeedbackField(blank=True, choices=[('CONSIDERATION', 'Under consideration'), ('REJECTED', 'Rejected'), ('ACCEPTED', 'Accepted')], default=None, help_text='The editing status appears below the title of the idea in red, yellow or green. The idea provider receives a notification.', max_length=254, null=True, verbose_name='Processing status')),
                ('item_ptr', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, related_name='a4_candy_ideas_idea', serialize=False, to='a4modules.Item')),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='name', unique=True)),
                ('name', models.CharField(max_length=120, verbose_name='Title')),
                ('description', ckeditor.fields.RichTextField(verbose_name='Description')),
                ('image', adhocracy4.images.fields.ConfiguredImageField('idea_image', blank=True, help_prefix='Visualize your idea.', upload_to='ideas/images', verbose_name='Add image')),
                ('category', adhocracy4.categories.fields.CategoryField(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='a4categories.Category', verbose_name='Category')),
                ('labels', models.ManyToManyField(related_name='a4_candy_ideas_idea_label', to='a4labels.Label', verbose_name='Labels')),
                ('moderator_statement', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='a4_candy_moderatorfeedback.ModeratorStatement')),
            ],
            options={
                'ordering': ['-created'],
            },
            bases=('a4modules.item', models.Model),
        ),
    ]
