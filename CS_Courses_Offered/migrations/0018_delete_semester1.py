# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CS_Courses_Offered', '0017_offering'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Semester1',
        ),
    ]
