from django.shortcuts import render
def milage(request):
    km = int(request.POST.get('killometer','0'))
    l = int(request.POST.get('liter','0'))
    mils = km/l if request.method == 'POST' else 0
    print("killometer=",km)
    print("liter=",l)
    print("milage=",mils)
    return render(request, 'mathapp/math.html', {'km': km, 'l': l, 'mils': mils})
