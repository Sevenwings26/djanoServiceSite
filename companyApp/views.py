from django.shortcuts import render, redirect
from . import models
from companyApp.models import GeneralInfo, Service, Testimonial, FrequentlyAskedQuestion
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

# # to store queries executed by django ... 
# from django.db import connection
# file_path = 'sql_queries.txt'
# def write_sql_queries_to_file(file_path):
#     with open(file_path, 'w') as file_object:
#         sql_queries = connection.queries
#         for query in sql_queries:
#             sql = query['sql']
#             file_object.write(f"{sql}\n")


# Create your views here.
# landing page 
def index(request):

    general_info = GeneralInfo.objects.first()
    # write_sql_queries_to_file(file_path=file_path)
    # print(general_info.location)

    services = Service.objects.all()
    testimonials = Testimonial.objects.all()
    faqs = FrequentlyAskedQuestion.objects.all()

    context = {
        "company_name": general_info.company_name,
        "location":general_info.location,
        "email":general_info.email,
        "phone":general_info.phone,
        "open_hours":general_info.open_hours,
        "video_url":general_info.video_url,
        "twitter":general_info.twitter_url,
        "facebook":general_info.facebook_url,
        "instagram":general_info.instagram_url,
        "linkedin":general_info.linkedin_url,

        "services":services,
        "testimonials":testimonials,
        "faqs":faqs,
    }

    return render(request, "index.html", context)


# Contact form creation 
def contact_form(request):
    # using post request, to enable user to send mail 
    if request.method == "POST":
        print('\nContact form submitted by user...')
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # # console print 
        # print(f'request POST: {request.POST}')
        # print(f'name: {name}')
        # print(f'request POST: {email}')
        # print(f'request POST: {subject}')
        # print(f'request POST: {message}')

        # Styling sent contact message
        context = {
            "name":name,
            "email":email,
            "subject":subject,
            "message":message,
        }
        html_context = render_to_string('email.html', context)
        
        # send mail .... 
        send_mail(
            subject=subject,
            # message=f"{name} - {email} - {message}",
            message=None,
            html_message=html_context,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=[settings.EMAIL_HOST_USER],
            fail_silently=False, # True is default
        )

    return redirect('home')
