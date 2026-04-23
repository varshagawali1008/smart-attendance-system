

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_delete_visitor'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedimage',
            name='authorized',
            field=models.BooleanField(default=False),
        ),
    ]
