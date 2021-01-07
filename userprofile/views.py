from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse, QueryDict
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.hashers import make_password
from django.utils.decorators import method_decorator
from django.views import View
import json
from .forms import UserForm






# Create your views here.
@csrf_exempt
def user_create(request):
	print(request)
	username = request.GET.get('username')
	print(username)
	email = request.GET.get('email')
	print(email)
	password = make_password(request.GET.get('password'))
	print(password)
	first_name = request.GET.get('first_name')
	print(first_name)
	last_name = request.GET.get('last_name')
	print(last_name)

	user = User.objects.create(username = username,email =email,password =password,first_name =first_name,last_name = last_name)
	return JsonResponse({'success':True},safe=False)

def signup(request):
    return render(request,'signup.html')


@method_decorator(csrf_exempt, name='dispatch')
class UserView(View):
    # def get(self,request,*args, **kwargs):
    #     todos =list(Todo.objects.all().values())
    #     print(todos)
    #     return JsonResponse(todos,safe=False)

    def post(self, request, *args, **kwargs):
        json_request = QueryDict('', mutable=True)
        json_request.update(json.loads(request.body))
        print(json_request)
        json_request['password'] = make_password(json_request['password'])
        form = UserForm(json_request)
        print(form)
        if form.is_valid():
            model = form.save()
            model.save()
        return JsonResponse(data={"valid": True},safe=False)