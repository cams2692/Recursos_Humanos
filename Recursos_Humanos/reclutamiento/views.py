from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.contrib.auth.models import User
from django.db.models import Q
from datetime import *

def view_test(request):
	return render_to_response("test.html",{},context_instance=RequestContext(request))
