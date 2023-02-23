from django.shortcuts import render

# Create your views here.

rooms = [
    {'id': 1, 'name': 'Lets Learn Python!'},
    {'id': 2, 'name': 'Design with me'},
    {'id': 3, 'name': 'Frontend developers'},
]

def home(request):
    context = {'rooms': rooms}
    return render(request, 'dreams/home.html', context)

def room(request, pk):
    room = None
    for i in rooms:
        if i['id'] == int(pk):
            room = i
    context = {'room': room}
    return render(request, 'dreams/room.html', context)
