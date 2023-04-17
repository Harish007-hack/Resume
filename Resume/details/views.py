from django.shortcuts import render,redirect
from .models import *

# Create your views here.

def home(request):

    Info = UserInfo.objects.all()

    projects = Projects.objects.all()

    if request.method == 'POST':
        x = request.POST
        print(x)
        customer = customerinfo()
        # <QueryDict: {'csrfmiddlewaretoken': ['1BeqUfJkapATGZ1OGIjKkWzWDzP1xpMq6BylZ7dyskEDzKz359PNdtQN4t8iywHP'], 'fName': ['Harish'], 'lName': ['Narayana'], 'email': ['g7harish@gmail.com']}>
        customer.first_name = x['fName']
        customer.last_name = x['lName']
        customer.email = x['email']
        customer.save()
        return redirect('home')



    context = {'info':Info,'project':projects}
    return render(request,"details/index.html",context)