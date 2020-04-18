from app_django.models import Admin

def valid_token(request):
    try:
        admin = Admin.objects.get(id=1)
        token = request.META.get("HTTP_TOKEN")
    except:
        return False
    if not(admin and admin.token == token and admin.validate_token()):
        return False
    return True
