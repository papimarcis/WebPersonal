import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mi_web.settings")

import django
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
User.objects.create_superuser('admin', 'admin@gmail.com', os.environ.get('DJANGO_SUPERUSER_PASSWORD'))