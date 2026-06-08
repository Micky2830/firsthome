from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import ProjectForm
from .models import Projects

STATE_CITY_MAP = {
    "PERAK": ["Ipoh", "Taiping", "Teluk Intan", "Batu Gajah"],
    "SELANGOR": ["Shah Alam", "Klang", "Petaling Jaya"],
    "JOHOR": ["Johor Bahru", "Batu Pahat", "Muar"],
    "KEDAH": ["Alor Setar", "Sungai Petani"],
    "KELANTAN": ["Kota Bharu", "Pasir Mas"],
    "MELAKA": ["Melaka City", "Alor Gajah"],
    "PAHANG": ["Kuantan", "Temerloh"],
    "PENANG": ["George Town", "Butterworth"],
    "PERLIS": ["Kangar"],
    "TERENGGANU": ["Kuala Terengganu", "Dungun"],
    "SABAH": ["Kota Kinabalu", "Sandakan"],
    "SARAWAK": ["Kuching", "Miri"],
    "NEGERI_SEMBILAN": ["Seremban", "Port Dickson"],

    "KUALA_LUMPUR": ["Kuala Lumpur City Centre", "Bangsar", "Cheras"],
    "PUTRAJAYA": ["Presint 1", "Presint 2", "Presint 3"],
    "LABUAN": ["Victoria", "Rancha-Rancha"],
}

def home(request):
    return render(request, "home/index.html")

def createProject(request):
    if request.method == "POST":
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("home")

        else:
            print(form.errors)
    else:
        form = ProjectForm()

    return render(request, "home/create_project.html", {"form": form})

def get_cities(request):
    state = request.GET.get("state")
    cities = STATE_CITY_MAP.get(state, [])
    return JsonResponse({"cities": cities})

def projectList(request):
    projects = Projects.objects.filter(status='Published')

    states = (
        Projects.objects
        .values_list('project_state', flat=True)
        .distinct()
        .order_by('project_state')
    )
    
    return render(
        request,
        "home/project_list.html",
        {
            "projects": projects,
            "states": states,
        }
    )