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
# Django Framework views - HTTP-oriented functions that will make our app talk to the outside world root@ianlawrence.info
#
#
#===========================================================================


from django.shortcuts import render_to_response

def index(request):
    return render_to_response('base.html','' )
  
def main(request):
    return render_to_response('base.html','' )
