from django.contrib import admin
from django.urls import path
from account import views
from .views import PhishingView,PhishingUnView

urlpatterns = [
  path('checkurl/',PhishingView.as_view({'post':'check_url'})),
  path('checkurls/',PhishingUnView.as_view({'post':'check_urls'})),
  path('checktext/',PhishingView.as_view({'post':'check_text'})),
  path('smsurls/',PhishingUnView.as_view({'post':'check_sms'})),
  path('test/',PhishingUnView.as_view({'get':'print_hello'})),
  path('attachment/',PhishingView.as_view({'post':'check_attachment'})),
]