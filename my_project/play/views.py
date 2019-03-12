from django.shortcuts import render
from .game import *
from django.http import JsonResponse
from characterinfo.models import *
import json, time

# Create your views here.


map =map = Map(sizex=100, sizey=100, seed=1)#this would need to be fixed later...

def play(request):
     #need to get variables from user TO DO...

     character = Character.objects.filter(user=request.user)[0]
     position = Position.objects.filter(character = character)[0]
     display = Display(x=position.posx, y=position.posy, map=map)

     context = {
          'display':display
     }

     return render(request, 'play/game.html', context)


def update(request):
     #get db stuff
     character = Character.objects.filter(user=request.user)[0]
     position = Position.objects.filter(character=character)[0]

     #handle post info
     x = request.POST['x']
     y = request.POST['y']
     t = request.POST['time']

     #handle time ... think about this more... before implementing
     trigger_time = (int)(t)
     time_stamp = position.timestamp
     elapsed_time = trigger_time - time_stamp

     #initial displayedmap
     display = Display(x=position.posx, y=position.posy, map=map)

     position.timestamp = trigger_time
     position.save()
     #check against map if collisions occur
     if(map.map[position.posx+ (int)(x)][position.posy+ (int)(y)] == 0):
          #update position
          position.posx = position.posx + (int)(x)
          position.posy = position.posy + (int)(y)
          position.save()

     display.update(position.posx,position.posy)




     context = {
          'display': display.displayedMap,
          }

     data = json.dumps(context)


     return JsonResponse(data, safe=False)