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
# Django imports
from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template


# Local imports


# urls for ui
urlpatterns = patterns('',
    (r'^$', direct_to_template,{ 'template': 'ui/index.html' }, 'index'),
    (r'^main/', 'ndg.ui.views.main'),
)
     

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/home/roda/Web/django_projects/ndg/media'}),
    )
