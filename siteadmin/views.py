from django.shortcuts import render


def siteadmin(request):
    return render(request, "siteadmin/siteadmin.html")
