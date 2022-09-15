from django.urls import path, re_path
from . import views

# from django.conf.urls import url

urlpatterns = [
    # path("", views.index, name="index"),
    re_path(r"^$", views.index, name="index"),
    re_path(r"^users/$", views.UsersListView.as_view(), name="users"),
    re_path(
        r"^users/(?P<pk>[-\d\w]+)$",
        views.UserDetailView.as_view(),
        name="user-detail",
    ),
    re_path(r"^tests/$", views.TestListView.as_view(), name="tests"),
    re_path(
        r"^tests/(?P<pk>[-\d\w]+)$",
        views.TestDetailView.as_view(),
        name="test-detail",
    ),
]
