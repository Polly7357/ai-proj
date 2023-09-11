"""
WSGI config for mblog project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/wsgi/
"""

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mblog.settings")

# application = get_wsgi_application()

# import os

# from django.core.wsgi import get_wsgi_application

# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mblog.settings")

# application = get_wsgi_application()

import os
import sys      # 20230815

# path = "/home/pollyhuang/mblog/"   # 20230815

# if path not in sys.path:            # 20230815
#     sys.path.insert(0, path)        # 20230815

path = "/home/pollyhuang/django_env/lib/python3.10/site-packages" # 整段20230906
if path not in sys.path:
    sys.path.insert(0, path)
path = "/home/pollyhuang/mblog"
if path not in sys.path:
    sys.path.insert(0, path)


from django.core.wsgi import get_wsgi_application       #20230907移至下方
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mblog.settings")

application = get_wsgi_application()
