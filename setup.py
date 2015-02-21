try:
    from setuptools import setup, Command
except ImportError:
    from distutils.core import setup, Command


class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import django
        from django.core.management import call_command
        from django.conf import settings

        settings.configure(
            DATABASES={
                'default': {
                    'NAME': ':memory:',
                    'ENGINE': 'django.db.backends.sqlite3'
                }
            },
            INSTALLED_APPS=('datetimebooleanfield',),
            MIDDLEWARE_CLASSES=[],
        )

        if django.VERSION[:2] >= (1, 7):
            django.setup()
        call_command('test', 'datetimebooleanfield')


with open('README.rst') as readme:
    long_description = readme.read()

setup(
    name='django-datetimebooleanfield',
    version='0.0.1',
    license='GNU',
    author='Adrian Matellanes',
    author_email='matellanesadrian@gmail.com',
    url='https://github.com/amatellanes/django-datetimebooleanfield',
    description='',
    long_description=long_description,
    packages=['datetimebooleanfield'],
    install_requires=['Django'],
    tests_require=['Django'],
    cmdclass={'test': TestCommand},
    classifiers=[
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Operating System :: OS Independent',
        'Topic :: Software Development',
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.6",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.2",
        "Programming Language :: Python :: 3.3",
        "Programming Language :: Python :: 3.4",
    ],
)
