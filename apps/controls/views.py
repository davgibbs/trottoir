from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from ipware import get_client_ip


def index(request):
    """
    Base index on what to show when user comes to base
    :param request: request object
    :return: redirect to the correct page depending if user is logged in
    """
    return render(request, 'controls/index.html', {})


def about(request):
    """
    Base index on what to show when user comes to base
    :param request: request object
    :return: redirect to the correct page depending if user is logged in
    """
    return render(request, 'controls/about.html', {})


@login_required
def app(request):
    """
    Base index on what to show when user comes to base
    :param request: request object
    :return: redirect to the correct page depending if user is logged in
    """
    client_ip, _ = get_client_ip(request)
    address_matching_user = request.user
    address_matching_user.last_login_ip = client_ip
    address_matching_user.save(update_fields=['last_login_ip'])
    return render(request, 'controls/app.html', {})
