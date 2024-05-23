import os
import django
from django.contrib.auth import get_user_model

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eps.settings')
django.setup()

User = get_user_model()
User.objects.create_superuser('admin', 'admin@myproject.com', '123456')

