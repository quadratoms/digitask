from django.shortcuts import render, redirect
from .forms import Entryform
from .models import Voter, Votes
from django.contrib.auth.models import auth, User


def home(request):
    if request.user in User.objects.all():
        return redirect('vote')
    else:
        return redirect('entry')


def logout(request):
    auth.logout(request)
    return redirect('entry')


def entry(request):
    form = Entryform()
    print(2)
    if 'submit' in request.POST:
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['secure_pin']
        age = request.POST['birthday']
        print(form)

        print(1)
        username = first_name+last_name
        if User.objects.filter(username=username).exists():
            user = auth.authenticate(
                request, username=username, password=password)
            auth.login(request, user)
            return redirect('vote')

        else:

            user = User.objects.create_user(
                username=username, first_name=first_name, last_name=last_name, password=password, age=age, email=email)
            user.save()
            user = auth.authenticate(
                request, username=username, password=password)
            auth.login(request, user)
            form.user_id = request.user

            return redirect('vote')

    return render(request, 'entry.html', {'form': form})


def vote(request):
    user = request.user
    print(user)
    #profile = Voter.objects.get(user=user)
    allow = True
    choice = None
    a = Votes.objects.filter(user=user)
    print(len(a))
    l=[len(Votes.objects.filter(vote='Donald Trump')), len(Votes.objects.filter(vote='Joe Biden'))]
    if len(a) == 0:

        if 'biden' in request.POST:
            v = Votes()
            v.user = user
            v.vote = 'Joe Biden'
            v.save()
            return redirect('entry/')

        if 'trump' in request.POST:
            v = Votes()
            v.user = user
            v.vote = 'Donald Trump'
            v.save()
            return redirect('entry')

    else:
        allow = False
        choice = Votes.objects.get(user=user)
        

    return render(request,  'vote.html', {'choice': choice, 'l':l})


# Create your views here.
