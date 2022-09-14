from django.shortcuts import render

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

    return render(
        request,
        "index.html",
        context={"num_tests": num_tests, "num_users": num_users},
    )
