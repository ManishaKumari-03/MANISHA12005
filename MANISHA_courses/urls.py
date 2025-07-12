from django.urls import path

from . import views

urlpatterns = [
    path("signup/", views.MANISHA_lmsSignupUser.as_view()),
    path("getAllUser/", views.MANISHA_lmsGetUserDetails.as_view()),
    path("updateEmail/",views.MANISHA_lmsUpdateEmail.as_view()),
    path("deleteUser/<number>/",views.MANISHA_lmsDeleteUser.as_view())
]
