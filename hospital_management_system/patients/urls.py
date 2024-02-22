from django.urls import path
from patients import views

urlpatterns = [    
    path('patients/', views.PatientViewSet.as_view({'get': 'patients'}), name='patients'),
    path('patients/<int:patient_id>/', views.PatientViewSet.as_view({'get': 'patient_detail'}), name='patient_detail'),
    path('patients/create/', views.PatientViewSet.as_view({'post': 'patient_create'}), name='patient_create'),
    path('patients/update/<int:id>', views.PatientViewSet.as_view({'post': 'patient_update'}), name='patient_update'),
    path('patients/delete/<int:id>', views.PatientViewSet.as_view({'post': 'patient_delete'}), name='patient_delete'),
    
    path('appointments/', views.AppointmentViewSet.as_view({'get': 'list', 'post': 'create'}), name='appointment_list'),
    path('appointments/<int:id>/', views.AppointmentViewSet.as_view({'get': 'retrieve', 'put': 'update', 'delete': 'destroy'}), name='appointment_detail'),
]
