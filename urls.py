# Copyright (C) 2010 INdT - Instituto Nokia de Tecnologia
#
# NDG is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# NDG is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with NDG. If not, see <http://www.gnu.org/licenses/

# Contact: Ian Lawrence root@ianlawrence.info

#===========================================================================
#
# Django Framework urls - url regex magic root@ianlawrence.info
#
#
#===========================================================================


from django.conf.urls.defaults import *


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Include the NDG UI
    (r'^', include('ndg-django.ui.urls')),


    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    # registration
    (r'^accounts/', include('registration.backends.default.urls'))
)
