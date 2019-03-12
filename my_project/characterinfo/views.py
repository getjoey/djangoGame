from django.shortcuts import render, get_object_or_404
from .models import *
from .forms import CreateCharacter


# Create your views here.
def info(request):
    try:
        user = request.user
        character = Character.objects.filter(user = user)[0]
        position = Position.objects.filter(character = character)[0]

        context = {
            'character': character,
            'position': position
        }
        return render(request, 'characterinfo/info.html', context)
    except:
        return render(request, 'home.html')


def createcharacter(request):
    try:
        user = request.user
        character = Character.objects.filter(user = user)[0]

        context = {
            'character' : character,
        }
        return render(request, 'characterinfo/info.html', context)
    except:
        form = CreateCharacter()
        return render(request, 'characterinfo/createcharacter.html', {'form': form})


def create(request):
    try:
        user = request.user
        object = Character.objects.filter(user = user)

        if(object.exists()):
            return render(request, 'characterinfo/characterinfo.html', {'character': object[0],'message':"AlreadyExist"})
        else:
            #create it
            job = request.POST['job']
            gender = request.POST['gender']
            stats = BaseCharacterList.objects.filter(job_name = job)[0]
            try:
                newCharacter = Character.objects.create(
                    user=request.user,
                    gender = gender,
                    job=stats,
                    level=1,
                    hp = stats.hp,
                    mp = stats.mp,
                    physA=stats.physA,
                    physD=stats.physD,
                    magA=stats.magA,
                    magD=stats.magD,

                    mainE=stats.mainE,
                    offE=stats.offE,
                    armorE=stats.armorE,
                    accE=stats.accE,
                )
                position = Position.objects.create(
                    character=newCharacter,
                    posx=16,
                    posy=16,
                    mapseed=1,
                    timestamp = 1,
                )
                position.save()
                newCharacter.save()
            except:
                return render(request, 'home.html')

            context = {
                'character': newCharacter,
                'position': position
            }

            return render(request, 'characterinfo/info.html', context)
    except:
        return render(request, 'home.html')



















