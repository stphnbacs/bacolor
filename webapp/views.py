from django.shortcuts import render, redirect
from .models import *
from .forms import GroupForm, MusicianForm, AlbumForm, TrackForm, OrganizerForm, ContractForm, MusicianContractStatusForm

def home(request):
    return render(request, 'pages/home.html')

def about(request):
    return render(request, 'pages/about.html')
def artist(request):
    musicians = Musician.objects.all()
    group = Group.objects.all()
    albums = Album.objects.all()
    contract_status = MusicianContractStatus.objects.all()

    total_musician = musicians.count()
    total_album = albums.count()

    accepted = contract_status.filter(status='A').count()
    pending = contract_status.filter(status='P').count()
    #accepted = contract_status.filter(status='A')

    context = {
        'musicians':musicians,
        'group':group,
        'total_album':total_album,
        'total_musician':musicians.count,
        'accepted':accepted,
        'pending':pending,
    }
    return render(request, 'pages/artist.html', context)

def profile(request, pk):
    musician = Musician.objects.get(id=pk)
    albums = musician.album_set.all()
    track = []
    for albums in albums:
        track.extend(albums.track_set.all())

    form = MusicianForm(instance=musician)

    if request.method == 'POST':
        form = MusicianForm(request.POST, instance=musician)
    if form.is_valid():
        form.save()
        return redirect('artist')
    context = {
        'form':form,
        'track':track
    }
    return render(request, 'pages/profile.html', context)

def deleteProfile(request, pk):
    musician = Musician.objects.get(id=pk)

    if request.method == 'POST':
        musician.delete()
        return redirect('artist')
    context = {
        'musician':musician
    }
    return render(request, 'pages/deleteProfile.html', context)

def addArtist(request):
    form = MusicianForm()
    if request.method == 'POST':
        form = MusicianForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('artist')
    context = {
        'form':form
    }
    return render(request, 'pages/addArtist.html', context)



