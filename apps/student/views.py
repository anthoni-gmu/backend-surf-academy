from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions

from .models import Student
from .serializers import StudentSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated

class GetStudentsView(generics.ListAPIView):
    serializer_class = StudentSerializer
    pagination_class = PageNumberPagination
    permission_classes = (permissions.AllowAny, )

    def get(self, request, format=None, *args, **kwargs):
        students = Student.objects.all()
        page = self.paginate_queryset(students)
        if students and page is not None:
            return self.get_paginated_response(self.serializer_class(students, many=True).data)
        return Response('Not found', status=status.HTTP_404_NOT_FOUND)


class AddStudentView(generics.CreateAPIView):
    serializer_class = StudentSerializer
    pagination_class = PageNumberPagination
    def post(self, request, format=None):
        data = self.request.data
        
        try: 
            print(data)
            for i in data:
                print(i)
            first_name = data['first_name']
            last_name = data['last_name']
            email = data['email']
            phone = data['phone']
            dni = data['dni']
            
            print(dni)
            print(dni)
            
            if Student.objects.filter(dni__iexact=dni).exists():
                return Response(
                    {'dni': 'existing DNI'},
                    status=status.HTTP_404_NOT_FOUND
                )

            if Student.objects.filter(email__iexact=email).exists():
                return Response(
                    {'email': 'existing email'},
                    status=status.HTTP_404_NOT_FOUND
                )
                
            try:
                Student.objects.create(
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    phone=phone,
                    dni=dni
                )
                students = Student.objects.all()
                page = self.paginate_queryset(students)
                if students and page is not None:
                    return self.get_paginated_response(self.serializer_class(students, many=True).data)
            
            except:
                return Response(
                    {'error': 'Error create student'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        except:
            return Response(
                    {'error': 'Error create studentadsa'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )