from django.shortcuts import render, redirect
from .models import Room, Topic
from .forms import RoomForm

# Create your views here.

#rooms = [
#    {'id': 1, 'name': 'Lets Learn Python!'},
#    {'id': 2, 'name': 'Design with me'},
#    {'id': 3, 'name': 'Frontend developers'},
#]

def home(request):
    rooms = Room.objects.all()

    topics = Topic.objects.all()
    

    context = {'rooms': rooms, 'topics': topics}
    
    return render(request, 'dreams/home.html', context)

def room(request, pk):
    room = Room.objects.get(id = pk)
    context = {'room': room}
    
    return render(request, 'dreams/room.html', context)

def create_room(request):
    form = RoomForm()
    
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dreams:home') 

    context = {'form': form}
    return render(request, 'dreams/room_form.html', context)

def update_room(request, pk):
    room = Room.objects.get(id = pk)
    form = RoomForm(instance = room)
    
    if request.method == 'POST':
        form = RoomForm(request.POST, instance = room)
        if form.is_valid():
            form.save()
            return redirect('dreams:home')
    
    context = {'form': form}

    return render(request, 'dreams/room_form.html', context)

def delete_room(request, pk):
    room = Room.objects.get(id = pk)
    
    if request.method == 'POST':
        room.delete()
        return redirect('dreams:home')

    return render(request, 'dreams/delete.html', {'obj': room})

