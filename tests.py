from django.test import TestCase
from django.db import connection
from pytest import mark

class DatabaseTest(TestCase):
    @mark.django_db
    def test_connection(self):
        # Test if the database is accessible
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            self.assertE
