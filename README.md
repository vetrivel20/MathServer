# Ex.04 Design a Website for Server Side Processing
## Date:10-12-2025

## AIM:
To create a web page to calculate vehicle mileage and fuel efficiency using server-side scripts.

## FORMULA:
M = D / F
<br> M --> Mileage (in km/l)
<br> D --> Distance Travelled (in km)
<br> F --> Fuel Consumed (in l)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM:
```
math.html 

html>
    <head>
        <title>MY Milage</title>
        <style>
            .box
            {
                margin-left: 500;
                margin-top: 225;
                padding-bottom: 50px;
                border: solid 5px ;width: 500;color: rgb(0, 0, 0);
                background:linear-gradient(orange,darkgoldenrod)
            }
            h1{
                text-align: center;
                color: black;
            }
            body
            {
                background:linear-gradient(red,gold);
            }
            .box2
            {
                width: 100%;
                background-color:gray;
                padding: 15px;
                text-align: center;
                border: solid 3px;
            }
        </style>
    </head>
    <body>
        <div class="box">
            <h1><u>Calculate Mileage</u></h1>
            <br>
            <form method="post">
                {% csrf_token %}
                <table>
                    <tr>
                        <td><b style="font-size: 25;color: white;">Kilometer :</b></td>
                        <td><input type="number" style="height: 35;width: 250;" name="killometer"></td>
                    </tr>
                    <tr>
                        <td><b style="font-size: 25;color: white;">Liter :</b></td>
                        <td><input type="number" style="height: 35;width: 250;" name="liter"></td>
                    </tr>
                    <tr>
                        <td></td>
                        <td><button style="height: 30;margin-left: 65;margin-top: 15;">Calculate</button></td>
                    </tr>
                    <tr>
                        <td><b style="font-size: 25;color: rgb(255, 255, 255);">Mileage :</b></td>
                        <td>
                            <b>{{mils}}</b>
                        </td>
                    </tr>
                </table>
            </form>
        </div>
        <br>
        <br>
        <div class="box2">
            <h2 style="color: white;">M.Vetrivel (25011461)</h2>
            <h3 style="color: white;">Copy Right Climed &copy;</h3>
        </div>
    </body>
</html>

views.py

from django.shortcuts import render
def milage(request):
    km = int(request.POST.get('killometer','0'))
    l = int(request.POST.get('liter','0'))
    mils = km/l if request.method == 'POST' else 0
    print("killometer=",km)
    print("liter=",l)
    print("milage=",mils)
    return render(request, 'mathapp/math.html', {'km': km, 'l': l, 'mils': mils})

urls.py

from django.urls import path
from mathapp import views
urlpatterns = [
    path('', views.milage, name='milage'),
]


```

## OUTPUT - SERVER SIDE:
![alt text](<Screenshot (25).png>)

## OUTPUT - WEBPAGE:
![alt text](<Screenshot (24).png>)

## RESULT:
The a web page to calculate vehicle mileage and fuel efficiency using server-side scripts is created successfully.
