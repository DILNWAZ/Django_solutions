from django.http import HttpResponse
from django.template import loader
from .models import Member

def members(request):
  mymember = Member.objects.all().values()
  template = loader.get_template('contact_us.html')
  content = {
    "mymember" : mymember
  }
  return HttpResponse(template.render(content,request))