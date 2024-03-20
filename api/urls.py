# urls.py

from django.urls import path
from .views import EmployeeListCreateView, EmployeeRetrieveUpdateDestroyView, EventListCreateView, EventRetrieveUpdateDestroyView,EmailLogListCreateView, EmailLogRetrieveUpdateDestroyView, EmailTemplateListCreateView, EmailTemplateRetrieveUpdateDestroyView, send_event_emails_view

urlpatterns = [
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('employees/<int:pk>/', EmployeeRetrieveUpdateDestroyView.as_view(), name='employee-retrieve-update-destroy'),
    path('emailtemplate/', EmailTemplateListCreateView.as_view(), name='emailtemplate-list-create'),
    path('emailtemplate/<int:pk>/', EmailTemplateRetrieveUpdateDestroyView.as_view(), name='emailtemplate-retrieve-update-destroy'),
    path('events/', EventListCreateView.as_view(), name='event-list-create'),
    path('events/<int:pk>/', EventRetrieveUpdateDestroyView.as_view(), name='event-retrieve-update-destroy'),
    path('email-logs/', EmailLogListCreateView.as_view(), name='email-log-list-create'),
    path('email-logs/<int:pk>/', EmailLogRetrieveUpdateDestroyView.as_view(), name='email-log-retrieve-update-destroy'),
    path('', send_event_emails_view, name='send_event_emails_view'),

]
