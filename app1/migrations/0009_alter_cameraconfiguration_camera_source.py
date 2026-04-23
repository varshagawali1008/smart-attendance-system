

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_cameraconfiguration_delete_camera'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cameraconfiguration',
            name='camera_source',
            field=models.CharField(help_text='Camera index (0 for default webcam or RTSP/HTTP URL for IP camera)', max_length=255),
        ),
    ]
