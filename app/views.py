from django.shortcuts import render, redirect, get_object_or_404
from .forms import UserForm
from .models import Example
from django.contrib import messages

# Create your views here.

def homeView(request):
    # name = 'Arise Damilare'
    # isAdmin = True
    # permissions = ['can delete', 'can create', 'can edit', 'can read']
    
    form = UserForm()
    
    infos = Example.objects.all() # returns array of object
    # infos = Example.objects.filter(email__contains='arise') # returns array of filterd object
    # info = Example.objects.get(id =1) # return object
    
    # print(infos)
    # for info in infos:
    #     print(info.email)
    
    if request.method == 'POST':
        # fullname = request.POST.get('fullname') 
        # email = request.POST.get('email')
        # image = request.FILES.get('image')
        
        # Example.objects.create(
        #     fullname = fullname,
        #     email = email,
        #     image = image
        # )
    
        
        
        form = UserForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Form submitted successfully')
        else:
            messages.error(request, 'Form submission failed')
    
    return render(
        request=request,
        template_name="index.html",
        context={
            # "name": name,
            # "isAdmin": isAdmin,
            # "permissions": permissions,
            'infos': infos,
            'form': form
        }
    )
    

def aboutView(request):
    return render(
        request,
        'about.html'
    )
    
    
def deleteUser(request, id):
    # user = get_object_or_404(Example, id=id)
    try:
        user = Example.objects.get(id=id)
        # user = get_object_or_404(Example, id=id)
        user.delete()
        messages.success(request, 'User deleted successfully')
    except Example.DoesNotExist:
        messages.success(request, 'User not found')
    
    return redirect('home')


def editUser(request, id):
    user = get_object_or_404(Example, id=id)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'User edited successfully')
        else:
            messages.success(request, 'error occured while editing user')
            
        return redirect('home')
    
    else:
        form = UserForm(instance=user)
        return render(
            request,
            template_name='editForm.html',
            context={
                'form': form
            }
        )