from django.shortcuts import render
from doctorsApp.serializers import DoctorSerializer
from doctorsApp.models import Doctor
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class DoctorsListPage(APIView):
    def get(self, request):
        doctors = Doctor.objects.all()
        serializer = DoctorSerializer(doctors, many=True)
        data = [{'id': doctor['id'], 'name': doctor['name']} for doctor in serializer.data]
        return Response(data)


class DoctorDetailPage(APIView):
    def get(self, request, doctor_id):
        try:
            doctor = Doctor.objects.get(id=doctor_id)
            serializer = DoctorSerializer(doctor)
            return Response(serializer.data)
        except Doctor.DoesNotExist:
            return Response({"error": f"Doctor with id {doctor_id} does not exist."}, status=status.HTTP_404_NOT_FOUND)