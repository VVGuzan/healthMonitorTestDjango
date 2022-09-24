from django.shortcuts import render
from django.views import generic
from .models import TestInstance, UserSimple


# Create your views here.
def index(request):
    """
    Rendering function for home page.
    """
    # number of tests performed
    num_tests = TestInstance.objects.all().count()
    # number of users registered
    num_users = UserSimple.objects.all().count()

    num_visits = request.session.get("num_visits", 0)
    request.session["num_visits"] = num_visits + 1

    return render(
        request,
        "index.html",
        context={
            "num_tests": num_tests,
            "num_users": num_users,
            "num_visits": num_visits,
        },
    )


class UsersListView(generic.ListView):
    model = UserSimple
    paginate_by = 10


class UserDetailView(generic.DetailView):
    model = UserSimple


class TestListView(generic.ListView):
    model = TestInstance
    paginate_by = 10


class TestDetailView(generic.DetailView):
    model = TestInstance
