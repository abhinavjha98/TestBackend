from django.contrib.auth import login, authenticate
from rest_framework_simplejwt.tokens import RefreshToken
# from django.contrib.auth import get_user_model
# User = get_user_model()
from account.models import User
def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
def validate_data(data):
    mobile = data.get("mobile")
    print(mobile)
    
    required_fields = ['name', 'username', 'mobile', 'password']
    flag = True
    msg = []
    for i in required_fields:
        v = data.get(i, None)
        if v is None or v == '':
            flag = False
            msg.append(f'{i} is required!')

    print(flag,msg)
    return flag,msg

def register_user(**kwargs):
    try:
        name = kwargs.pop("name")
        print(name[0])
        username = kwargs.pop("username")
        password = kwargs.pop("password")
        dob = kwargs.pop("dob")
        mobile = kwargs.pop("mobile")
        print(mobile)
        email = kwargs.pop("email")
        user = User(
            name=name[0],
            email=email[0],
            username=username[0],
            mobile=mobile[0],
            dob=dob[0],
            password=password[0]
        )
        print(user)
        user.save()
        user.set_password(password[0])
        user.save()
        return user
    except Exception as e:
        print(e)
        return None
    
    
