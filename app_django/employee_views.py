from rest_framework.response import Response
from rest_framework.decorators import api_view
from app_django.auth import valid_token
from app_django.models import Employee

@api_view(["POST"])
def add_employee(request):
    if not valid_token(request):
        return Response({"message":"Invalid user or token"})
    data = request.data
    n = data['name']
    a = data['age']
    e = data['ed']
    r = data['role']
    emp = Employee(name=n, age=a, ed=e, role=r)
    emp.save()
    return Response({"message":"Employee added"})

@api_view(["DELETE"])
def delete_employee(request):
    if not valid_token(request):
        return Response({"message":"Invalid user or token"})
    data = request.data
    id = int(data['id'])
    Employee.objects.get(pk=id).delete()
    return Response({"message":"Employee deleted"})

@api_view(["PUT"])
def modify_employee(request):
    if not valid_token(request):
        return Response({"message":"Invalid user or token"})
    data = request.data
    id = int(data['id'])
    emp=Employee.objects.get(pk=id)
    if 'ed' in data: emp.ed=data['ed']
    if 'role' in data: emp.role=data['role']
    emp.save()
    return Response({"message":"Employee modified"})

@api_view(["GET"])
def display_employees(request):
    if not valid_token(request):
        return Response({"message":"Invalid user or token"})
    employees = Employee.objects.all()
    if employees:
        tmp=[]
        for emp in employees:
            tmp.append(dict(zip(['id','name','age','education','role'],
                [emp.pk,emp.name,emp.age,emp.ed,emp.role])))
        return Response(tmp)
    else:
        return Response({"message":"No employees in database"})
