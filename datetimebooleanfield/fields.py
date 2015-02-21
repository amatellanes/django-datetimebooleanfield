from django.db import models

from .descriptors import DateTimeBooleanDescriptor


class DateTimeBooleanField(models.DateTimeField):
    DEFAULT_PROPERTY_NAME = 'is_{0}'

    def __init__(self, *args, **kwargs):
        self.property_name = kwargs.pop('property', None)

        super(DateTimeBooleanField, self).__init__(*args, **kwargs)

    def contribute_to_class(self, cls, name):
        super(DateTimeBooleanField, self).contribute_to_class(cls, name)

        # Use the defined name as boolean property name.
        # If a name isn't defined, a default one is used.
        property_name = self.property_name or \
                        DateTimeBooleanField.DEFAULT_PROPERTY_NAME.format(name)
        setattr(cls, property_name, DateTimeBooleanDescriptor(self.name))

    def get_internal_type(self):
        return "DateTimeField"

    def south_field_triple(self):
        """ Returns a suitable description of this field for South."""
        # We'll just introspect ourselves, since we inherit.
        from south.modelsinspector import introspector

        field_class = "django.db.models.fields.DateTimeField"
        args, kwargs = introspector(self)

        return field_class, args, kwargs