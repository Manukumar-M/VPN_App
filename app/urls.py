"""Generate URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""


# from django.urls import path
# from . import views

# urlpatterns = [
#     # Other URL patterns...
#     path('generate_ovpn/', views.generate_ovpn_certificate, name='generate_ovpn_certificate'),
#     path('generate_person/', views.generate_person_certificate, name='generate_person_certificate'),
# ]


from django.urls import path
from . import views

urlpatterns = [
    # Other URL patterns...
    path('generate_certificate/device/', views.generate_device_certificate, name='generate_device_certificate'),
    path('generate_certificate/person/', views.generate_person_certificate, name='generate_person_certificate'),
]
