from django.shortcuts import render

# Create your views here.

def homeView(request):
    name = 'Arise Damilare'
    isAdmin = True
    permissions = ['can delete', 'can create', 'can edit', 'can read']
    
    
    return render(
        request=request,
        template_name="index.html",
        context={
            "name": name,
            "isAdmin": isAdmin,
            "permissions": permissions
        }
    )
    

def aboutView(request):
    return render(
        request,
        'about.html'
    )