from django.shortcuts import render

def project_view(request, flower, month):
    context = {
        "flower": flower,
        "month": month,
    }
    return render(request, "project.html", context)