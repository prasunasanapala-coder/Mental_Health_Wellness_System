from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Yoga, Meditation, Mood
from django.contrib import messages
from django.contrib.auth import login
from .forms import CustomUserCreationForm
from django.contrib.auth import authenticate
from datetime import date

@login_required
def dashboard(request):
    user = request.user

    yoga_count = Yoga.objects.count()
    meditation_count = Meditation.objects.count()
    mood_count = Mood.objects.filter(user=user).count()

    latest_mood = Mood.objects.filter(user=user).order_by('-id').first()

    context = {
        'yoga_count': yoga_count,
        'meditation_count': meditation_count,
        'mood_count': mood_count,
        'latest_mood': latest_mood,
    }

    return render(request, 'dashboard.html', context)



@login_required
def yoga_page(request):
    yoga_sessions = Yoga.objects.all()
    return render(request, 'yoga.html', {'yoga': yoga_sessions})



@login_required
def meditation_page(request):
    meditations = Meditation.objects.all()
    return render(request, 'meditation.html', {'meditations': meditations})



@login_required
def meditation_detail(request, id):
    meditation = get_object_or_404(Meditation, id=id)
    return render(request, 'meditation_detail.html', {'meditation': meditation})




@login_required
def mood_page(request):
    today = date.today()

    if request.method == 'POST':
        existing = Mood.objects.filter(user=request.user, date=today).first()

        if existing:
            messages.error(request, "You have already logged your mood today.")
        else:
            Mood.objects.create(
                user=request.user,
                mood=request.POST['mood'],
                note=request.POST.get('note', '')
            )
            messages.success(request, "Mood saved successfully!")

        return redirect('mood')

    user_moods = Mood.objects.filter(user=request.user).order_by('-date')

    

    happy_count = Mood.objects.filter(user=request.user, mood="Happy").count()
    calm_count = Mood.objects.filter(user=request.user, mood="Calm").count()
    stressed_count = Mood.objects.filter(user=request.user, mood="Stressed").count()
    anxious_count = Mood.objects.filter(user=request.user, mood="Anxious").count()

    context = {
        'user_moods': user_moods,
        'happy_count': happy_count,
        'calm_count': calm_count,
        'stressed_count': stressed_count,
        'anxious_count': anxious_count,
    }

    return render(request, 'mood.html', context)

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('dashboard')
    else:
        form = CustomUserCreationForm()

    return render(request, 'signup.html', {'form': form})
@login_required
def yoga_detail(request, id):
    yoga = get_object_or_404(Yoga, id=id)
    return render(request, 'yoga_detail.html', {'yoga': yoga})
@login_required
def meditation_detail(request, id):
    meditation = get_object_or_404(Meditation, id=id)
    return render(request, 'meditation_detail.html', {'meditation': meditation})