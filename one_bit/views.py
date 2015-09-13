from django.views.generic import TemplateView
from django.http import HttpResponse
import datetime
import models
import os

def current_datetime(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)

def foo(request):
    html = "<html><body>foo=%s.</body></html>" % request.REQUEST['foo']
    return HttpResponse(html)

def set(request):
    userName = request.REQUEST['username']
    atCafe = True if 'atcafe' in request.REQUEST and request.REQUEST['atcafe'] == 'True' else False
    description = request.REQUEST['description'] if 'description' in request.REQUEST else ''
    teach = True if 'teach' in request.REQUEST and request.REQUEST['teach'] == 'True' else False
    objs = models.UserStatus.objects.filter(userName = userName)
    if len(objs) == 0:
        obj = models.UserStatus(userName = userName, atCafe = atCafe, description = description, teach = teach)
        obj.save()
    else:
        obj = objs[0]
        if 'atcafe' in request.REQUEST:
            if obj.atCafe == False and atCafe == True and userName == 'shimizu':
                post_to_mythings()
            obj.atCafe = atCafe;
        if 'description' in request.REQUEST:
            obj.description = description
        if 'teach' in request.REQUEST:
            obj.teach = teach
        obj.save()
    obj = models.UserStatus.objects.filter(userName = userName)[0]
#    return HttpResponse('{"username" : "%s", "atcafe" : "%s", "description": "%s", "teach" : "%s"}' % (obj.userName, str(obj.atCafe), obj.description, str(obj.teach)));
    return HttpResponse('done. <a href="form">back to form</a>')

def get(request):
    userName = request.REQUEST['username']
    objs = models.UserStatus.objects.filter(userName = userName)
    if len(objs) == 0:
        return HttpResponse('{"username" : "%s", "atcafe" : "False"}' % userName)
    obj = objs[0]
    return HttpResponse('{"username" : "%s", "atcafe" : "%s", "description": "%s", "teach" : "%s"}' % (obj.userName, str(obj.atCafe), obj.description, str(obj.teach)));

def delete(request):
    userName = request.REQUEST['username']
    objs = models.UserStatus.objects.filter(userName = userName)
    if len(objs) == 0:
        return HttpResponse('done. <a href="form">back to form</a>')
    obj = objs[0]
    obj.delete()
    return HttpResponse('done. <a href="form">back to form</a>')

def get_people(request):
    teachers = models.UserStatus.objects.exclude(description__exact = '').filter(teach = True)
    students = models.UserStatus.objects.exclude(description__exact = '').filter(teach = False)
    return HttpResponse('{"teachers" : [%s], "students" : [%s]}' % \
                        (people_json(teachers), people_json(students)))
#'", "'.join([obj.userName for obj in teachers]), '", "'.join([obj.userName for obj in students])))

def people_json(people):
    ret = []
    for obj in people:
        ret.append('{"username" : "%s", "atcafe" : "%s", "description": "%s", "teach" : "%s"}' % (obj.userName, str(obj.atCafe), obj.description, str(obj.teach)))
    return ', '.join(ret)

def post_to_mythings():
    auth_uuid = '73659b62-80e7-46b5-aff4-c1644f3ce194'
    auth_token = 'e557062f'
    cmd = 'curl -X POST "http://210.140.71.170/data/%s" -d "temperature=over" --header "meshblu_auth_uuid: %s" --header "meshblu_auth_token: %s"' % (auth_uuid, auth_uuid, auth_token)
    os.system(cmd)

class WhiteboardView(TemplateView):
    template_name = "whiteboard.html"

class FormView(TemplateView):
    template_name = "form.html"

class APIDescriptionView(TemplateView):
    template_name = "api_description.html"
