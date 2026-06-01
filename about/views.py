from django.shortcuts import render


def about_page(request):
    return render(request, 'about/about.html')


def privacy_policy(request):
    return render(request, 'about/privacy_policy.html')


def terms_conditions(request):
    return render(request, 'about/terms_conditions.html')


def disclaimer(request):
    return render(request, 'about/disclaimer.html')