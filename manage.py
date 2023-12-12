#!/usr/bin/env python
"""Django's command-line utility for administrative tasks.
 
This module is the entry point for many Django commands. Running
`python manage.py [command]` executes the specified command.
 
For more information on this file, see
https://docs.djangoproject.com/en/stable/ref/django-admin/
"""
import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'projectgreen.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)
    
