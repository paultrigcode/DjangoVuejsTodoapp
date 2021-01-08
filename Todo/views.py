from django.shortcuts import render
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse, QueryDict
import json
from .forms import TodoForm
from .models import Todo







# Create your views here.

def home(request):
    return render(request,'todo.html')

@method_decorator(csrf_exempt, name='dispatch')
class TodoView(View):
    permission_required = ('requisitions.can_disburse_requisition','requisitions.can_approve_requisition','requisition.can_view_all_requisition')
    def get(self,request,*args, **kwargs):
        todos =list(Todo.objects.all().values())
        print(todos)
        return JsonResponse(todos,safe=False)

    def post(self, request, *args, **kwargs):
        json_request = QueryDict('', mutable=True)
        json_request.update(json.loads(request.body))
        print(json_request)
        form = TodoForm(json_request)
        if form.is_valid():
            model = form.save()
            model.save()
        return JsonResponse(data={"valid": False,"errors": form.errors},safe=False)

@csrf_exempt
def markComplete(request,id):
    todo = Todo.objects.filter(id=id).update(completed = True)
    response_data = {
                "todo": todo,
            }
    return JsonResponse(response_data,safe=False)

@csrf_exempt
def delete(request,id):
    todo = Todo.objects.filter(id=id).delete()
    response_data = {
                "todo": todo,
            }
    return JsonResponse({'success':True},safe=False)


