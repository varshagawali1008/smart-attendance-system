

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_visitor'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Visitor',
        ),
    ]
