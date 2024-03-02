from .models import Client


def auth(credentials):
    try:
        user  = Client.objects.get(email=credentials['email'])
        return credentials["password"] == user.password
    except Client.DoesNotExist:
        return False
