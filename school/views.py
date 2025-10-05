from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Student

class StudentCreateView(APIView):
    def post(self, request):
        data = request.data
        try:
            student = Student.objects.create(
                name=data.get('name'),
                cpf=data.get('cpf'),
                email=data.get('email'),
                phone=data.get('phone')
            )
            return Response({
                "id": student.id,
                "name": student.name,
                "cpf": student.cpf,
                "email": student.email,
                "phone": student.phone
            }, status=status.HTTP_201_CREATED)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class StudentListView(APIView):
    def get(self, request):
        students = Student.objects.all()
        student_list = [{
            "id": student.id,
            "name": student.name,
            "cpf": student.cpf,
            "email": student.email,
            "phone": student.phone
        } for student in students]
        return Response(student_list, status=status.HTTP_200_OK)
    
    