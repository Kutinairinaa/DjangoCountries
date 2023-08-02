# -*- coding: utf-8 -*-
########################################################################
#                                                                      #
# Main router                                                          #
#                                                                      #
# MIT License                                                          #
# Copyright (c) 2023 Irina                                             #
#                                                                      #
########################################################################


from django.contrib import admin
from django.urls import path, include

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('countries', include('countries.urls')),
]
