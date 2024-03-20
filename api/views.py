from django.core.mail import send_mail
from datetime import datetime
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee, Event, EmailTemplate, EmailLog
from django.db import transaction
from rest_framework import generics
from .serializers import EmployeeSerializer, EventSerializer, EmailLogSerializer, EmailTemplateSerializer

class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EmployeeRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class EventListCreateView(generics.ListCreateAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EventRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer

class EmailTemplateListCreateView(generics.ListCreateAPIView):
    queryset = EmailLog.objects.all()
    serializer_class = EmailTemplateSerializer

class EmailTemplateRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmailTemplate.objects.all()
    serializer_class = EmailTemplateSerializer
    
class EmailLogListCreateView(generics.ListCreateAPIView):
    queryset = EmailTemplate.objects.all()
    serializer_class = EmailLogSerializer

class EmailLogRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = EmailLog.objects.all()
    serializer_class = EmailLogSerializer


@api_view(['POST'])
def send_event_emails_view(request):
    today = datetime.today().date()
    events = Event.objects.filter(event_date=today)
    
    for event in events:
        try:
            employee = event.employee
            email_template = EmailTemplate.objects.get(event_type=event.event_type)
            
            # Personalize email template with employee name
            email_content = email_template.template.replace('{employee_name}', employee.name)
            
            send_mail(
                f'Happy {event.event_type}!',
                email_content,
                'shaheenansari1906@gmail.com',
                [employee.email],
                fail_silently=False,
            )

            # Create EmailLog instance within a transaction
            with transaction.atomic():
                email_log = EmailLog.objects.create(employee=employee, event=event, success=True)
                email_log.save()
        except Exception as e:
            # Log the error and continue to the next event
            EmailLog.objects.create(employee=employee, event=event, success=False, error_message=str(e))
            continue

    return Response({'message': 'Event emails sent successfully'})
