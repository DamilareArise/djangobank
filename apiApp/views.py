from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from app.models import Example
from .serializers import ContactSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def contact_list(request):
    contacts = Example.objects.all()
    
    if request.method == 'POST':
        serializer = ContactSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    else:
        
        serializer = ContactSerializer(contacts, many=True)
        print(serializer)
        return Response(serializer.data, status=status.HTTP_200_OK)
    

@api_view(['GET', 'PUT', 'DELETE'])
def contact_detail(request, id):
    try:
        contact = Example.objects.get(id=id)
    except Example.DoesNotExist as e:
        return Response({'error': 'Not Found'}, status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ContactSerializer(contact)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serializer = ContactSerializer(contact, data = request.data)
        if serializer.is_valid():
            serializer.save()
            
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    elif request.method == 'DELETE':
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)