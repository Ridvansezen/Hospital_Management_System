from django.urls import path
from patients import views

urlpatterns = [    
    path('patients/', views.PatientListViewSet.as_view(), name='patients'),
    path('patients/<int:patient_id>/', views.PatientDetailViewSet.as_view(), name='patient_detail'),
    path('patients/create/', views.PatientCreateViewSet.as_view(), name='patient_create'),
    path('patients/update/<int:id>', views.UpdatePatientViewSet.as_view(), name='patient_update'),
    path('patients/delete/<int:id>', views.DeletePatientViewSet.as_view(), name='patient_delete'),
    
    path('appointments/', views.AppointmentListView.as_view(), name='appointment_list'),
    path('appointments/<int:appointment_id>/', views.AppointmentDetailView.as_view(), name='appointment_detail'),
    path('appointments/create/', views.CreateAppointmentView.as_view(), name='appointment_create'),
    path('appointments/update/<int:id>/', views.UpdateAppointmentView.as_view(), name='appointment_update'),
    path('appointments/delete/<int:id>', views.DeleteAppointmentView.as_view(), name='appointment_delete'),
]
