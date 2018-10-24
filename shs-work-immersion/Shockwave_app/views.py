from django.shortcuts import render
from django.views.generic import TemplateView 

# Create your views here.

class NamePageView(TemplateView):
    template_name = "name.html"

    def get_context_data(self):
        data = {"favquote" : "Pano mo nasabi?  !!",
        }
        return data

class ResumePageView(TemplateView):
    template_name = "resume.html"

    def get_context_data(self):
        data = {"shs" : "Camarines Sur National High School",
                "jhs": "Camarines Sur National High School",
                "elem": "Pamplona Camarines Sur"}
        return data

class ContactPageView(TemplateView):
    template_name = "contact.html"

    def get_context_data(self):
        data = {"name" : "danmark Rabano",
                "address": "Z-2 Tambo Pamplona Camarines Sur",
                "email": "danmark.rabano14@gmail.com",
                 "contact": "09152505011"}

        return data
