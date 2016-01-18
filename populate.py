import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'theRealPOD.settings')
django.setup()

from vewTrak.models import RelationalHits

def create_tracking_object():
	hit = RelationalHits()
	hit.hits = 0
	hit.save()

if __name__ == '__main__':
	create_tracking_object()