from django.shortcuts import render


def dashboard_view(request):
    """

    """
    context = {}
    return render(request, 'home/home.html', context)
