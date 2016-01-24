# from django.conf import settings
# settings.configure()
# import django
# django.setup()
# from vewTrak.models import RelationalHits
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'theRealPOD.settings')
django.setup()

from vewTrak.models import RelationalHits

def rds_increase():
	hit = RelationalHits.objects.get(id=1)
	hit.hits = hit.hits + 1
	hit.save()
