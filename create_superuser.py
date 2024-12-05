import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mi_web.settings")

import django
django.setup()

from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@admin.com', settings.SUPERUSER_PASSWORD)
    print('Superuser created!')
else:
    print('Superuser already exists.')