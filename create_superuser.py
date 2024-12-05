import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mi_web.settings")

import django
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'admin@admin.com', os.environ.get('DJANGO_SUPERUSER_PASSWORD', 'admin'))
    print('Superuser created!')
else:
    print('Superuser already exists.')