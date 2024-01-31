from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from patients.models import Patient
from doctorsApp.models import Doctor
from patients.serializers import PatientSerializer
from doctorsApp.serializers import DoctorSerializer
from rest_framework.views import APIView
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.generics import DestroyAPIView
from patients.models import Appointment
from patients.serializers import AppointmentSerializer
from patients.serializers import CustomAppointmentSerializer



class PatientCreateViewSet(APIView):
    serializer_class = PatientSerializer
    
    def get(self, request):
        serializer = self.serializer_class()
        return Response({'serializer': serializer.data})
    
    def post(self, request):
        serializer = PatientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Patient successfully registered."}, status=status.HTTP_201_CREATED)
        return Response({"message": "Failed to register patient, check the form."}, status=status.HTTP_400_BAD_REQUEST)
    

class PatientListViewSet(APIView):
    def get(self, request):
        patients = Patient.objects.all()
        serializer = PatientSerializer(patients, many=True)
        return Response(serializer.data)
    

class PatientDetailViewSet(APIView):
    def get(self, request, patient_id):
        try:
            patient = Patient.objects.get(id=patient_id)
            serializer = PatientSerializer(patient)
            return Response(serializer.data)
        
        except Patient.DoesNotExist:
            return Response({"error": f"Patient with id {patient_id} does not exist."}, status=status.HTTP_404_NOT_FOUND)
    
  
    
class UpdatePatientViewSet(RetrieveUpdateDestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)
    
    
    
class DeletePatientViewSet(DestroyAPIView):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer
    lookup_field = 'id'
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Patient deleted successfully."}, status=status.HTTP_204_NO_CONTENT)
    
    
    
    
class AppointmentListView(APIView):
    def get(self, request):
        appointments = Appointment.objects.all()
        serializer = CustomAppointmentSerializer(appointments, many=True)
        return Response(serializer.data)



class AppointmentDetailView(APIView):
    def get(self, request, appointment_id):
        try:
            appointments = Appointment.objects.get(id=appointment_id)
            serializer = CustomAppointmentSerializer(appointments)
            return Response(serializer.data)
        except Appointment.DoesNotExist:
            return Response({"error": f"Appointment with id {appointment_id} does not exist."}, status=status.HTTP_404_NOT_FOUND)
        
        

class CreateAppointmentView(APIView):
    serializer_class = AppointmentSerializer

    def get(self, request):
        patients = Patient.objects.all()
        doctors = Doctor.objects.all()

        patient_serializer = PatientSerializer(patients, many=True)
        doctor_serializer = DoctorSerializer(doctors, many=True)


        serializer = self.serializer_class()


        return Response({
            'serializer': serializer.data
        })

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Appointment successfully registered."}, status=status.HTTP_201_CREATED)
        return Response({"message": "Failed to create appointment, check the form."}, status=status.HTTP_400_BAD_REQUEST)
    
    

class UpdateAppointmentView(RetrieveUpdateDestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    lookup_field = 'id'

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        return self.partial_update(request, *args, **kwargs)

    def perform_update(self, serializer):
        instance = serializer.save()
        updated_instance = Appointment.objects.get(id=instance.id)
        updated_serializer = AppointmentSerializer(updated_instance)
        data = updated_serializer.data
        message = {"message": "Appointment successfully updated.", "data": data}
        return Response(message, status=status.HTTP_200_OK)

    
    
class DeleteAppointmentView(DestroyAPIView):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    lookup_field = 'id'
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response({"message": "Appointment deleted successfully."}, status=status.HTTP_204_NO_CONTENT)