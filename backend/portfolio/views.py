from django.shortcuts import render
from django.http import JsonResponse
from .models import Profile, Project, Skill, Education, Experience
from .forms import ContactForm

def home(request):
    profile = Profile.objects.first()
    projects = Project.objects.all().order_by('-created_at')
    skills = Skill.objects.all().order_by('-proficiency')
    education = Education.objects.all().order_by('-order')
    experience = Experience.objects.all()
    form = ContactForm()
    
    context = {
        'profile': profile,
        'projects': projects,
        'skills': skills,
        'education': education,
        'experience': experience,
        'form': form,
    }
    return render(request, 'portfolio/home.html', context)

def contact_submit(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success', 'message': 'Message sent successfully!'})
        else:
             return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid method'}, status=405)
