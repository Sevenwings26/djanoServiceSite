from django.shortcuts import render
from . import models
from companyApp.models import GeneralInfo, Service, Testimonial

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
def index(request):

    general_info = GeneralInfo.objects.first()
    # write_sql_queries_to_file(file_path=file_path)
    # print(general_info.location)

    services = Service.objects.all()
    testimonials = Testimonial.objects.all()

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
    }

    return render(request, "index.html", context)


