from rest_framework.response import Response
from rest_framework.decorators import api_view
from app_django.models import Admin

# Create your views here.

@api_view(["POST"])
def create_admin(request):
    data = request.data
    un = data['username']
    pw = data['password']
    try:
        admin = Admin.objects.filter(username = un).all()
    except Admin.DoesNotExist:
        return Response({"message":"Admin does not exist"})
    if admin:
        return Response({"message":"Admin already exists"})
    else:
        admin = Admin(username = un)
        admin.set_password(pw)
        admin.save()
        return Response({"message":"Admin added"})

@api_view(["GET"])
def fetch_token(request):
    data = request.data
    un = data['username']
    pw = data['password']
    admin = Admin.objects.filter(username = un).first()
    if admin and admin.check_password(pw):
        token = admin.get_token()
        admin.save()
        doc = {"token" : token}
        return Response(doc)
    else:
        return Response({"message":"Invalid admin"})
