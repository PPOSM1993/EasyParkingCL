# locations/tests.py

from django.test import TestCase
from .models import LocationZone
from django.contrib.gis.geos import Polygon

class LocationZoneTest(TestCase):
    def test_create_zone(self):
        poly = Polygon((
            (0.0, 0.0),
            (0.0, 1.0),
            (1.0, 1.0),
            (1.0, 0.0),
            (0.0, 0.0),
        ))
        zone = LocationZone.objects.create(name="Zona Test", polygon=poly)
        self.assertEqual(zone.name, "Zona Test")
