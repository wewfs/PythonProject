from django.urls import path
from .views import NamePageView, ResumePageView, ContactPageView


urlpatterns = [
    path('name/', NamePageView.as_view(), name="name_view"), 
    path('resume/', ResumePageView.as_view(), name="resume_view"),
    path('contact/', ContactPageView.as_view(), name="contact_view")
]