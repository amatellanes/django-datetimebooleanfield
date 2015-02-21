from django.db import models
from django.test import TestCase
from django.utils import timezone

from freezegun.api import freeze_time

from .fields import DateTimeBooleanField


class SimpleModel(models.Model):
    created = DateTimeBooleanField(auto_now_add=True)
    verified = DateTimeBooleanField(null=True, blank=True)


class AnotherSimpleModel(models.Model):
    created = DateTimeBooleanField(property='was_created')  # Sets a custom property name.


class DateTimeBooleanFieldTestCase(TestCase):
    def test_returns_internal_type(self):
        field = DateTimeBooleanField()

        self.assertEqual(field.get_internal_type(), "DateTimeField")

    def test_exists_boolean_property(self):
        model = SimpleModel()

        self.assertIsInstance(model.is_verified, bool)
        self.assertIsInstance(model.is_created, bool)
        self.assertFalse(model.is_created)
        self.assertFalse(model.is_verified)

    def test_exists_boolean_property_using_custom_property_name(self):
        model = AnotherSimpleModel()

        self.assertIsInstance(model.was_created, bool)
        self.assertFalse(model.was_created)

    def test_sets_true_value_if_datetime_field_are_specified(self):
        model = SimpleModel(created=timezone.now(), verified=timezone.now())

        self.assertTrue(model.is_created)
        self.assertTrue(model.is_verified)

    def test_exists_boolean_property_after_retrieve_object_from_database(self):
        model = SimpleModel.objects.create(verified=timezone.now())
        model = SimpleModel.objects.get(pk=model.pk)

        self.assertIsInstance(model.is_verified, bool)
        self.assertIsInstance(model.is_created, bool)
        self.assertTrue(model.is_created)
        self.assertTrue(model.is_verified)

    @freeze_time(timezone.now())
    def test_sets_datetime_field_to_now_if_boolean_poperty_is_set_as_true(self):
        model = SimpleModel()
        model.is_verified = True

        self.assertTrue(model.is_verified)
        self.assertEqual(model.verified, timezone.now())