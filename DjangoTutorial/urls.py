"""
Definition of urls for DjangoTutorial.
"""

from datetime import datetime
from django.conf.urls import url, include
import django.contrib.auth.views

import app.forms
import app.views

# Uncomment the next lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = [
    url(r'^$', include("blog.urls")),
    url(r'^admin/', include(admin.site.urls)),
]
