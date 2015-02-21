from django.utils import timezone


class DateTimeBooleanDescriptor(object):
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner=None):
        return instance.__dict__[self.name] is not None

    def __set__(self, instance, value):
        value = bool(value)
        if value != self.__get__(instance):
            instance.__dict__[self.name] = timezone.now() if value else None