from django.shortcuts import render, get_object_or_404
from anfisa.services import what_weather, what_conclusion, what_temperature
from anfisa.models import Friend
from icecream.models import IceCream


def index(request):
    icecreams = ""
    friends = ""
    city_weather = ""
    friend_output = ""
    selected_icecream = ""
    conclusion = ""

    for friend in Friend.objects.all():
        friends += (
                f'<input type="radio" name="friend" required'
                f' value="{friend.name}">{friend.name}<br>'
        )

    icecream_db = IceCream.objects.all()
    for i in range(len(icecream_db)):
        ice_form = (
        f'<input type="radio" name="icecream" required'
        f' value="{icecream_db[i].name}">{icecream_db[i].name}'
        )

        ice_link = f'<a href="icecream/{i}/">Узнать состав</a>'
        icecreams += f"{ice_form} | {ice_link} <br>"

    if request.method == 'POST':
        selected_friend = request.POST["friend"]
        selected_icecream = request.POST["icecream"]

        friend_name = get_object_or_404(Friend, name=selected_friend)
        icecream_name = get_object_or_404(IceCream, name=selected_icecream)
        city = friend_name.city
        weather = what_weather(city)
        parsed_temperature = what_temperature(weather)
        conclusion = what_conclusion(parsed_temperature)
        friend_output = f"{friend_name}, тебе прислали {icecream_name}!"
        city_weather = f"В городе {city} погода :{weather}"

    context = {
        # Передайте значение в шаблон
        "icecreams": icecreams,
        "friends": friends,
        "friend_output": friend_output,
        "city_weather": city_weather,
        "conclusion": conclusion,
    }
    return render(request, "homepage/index.html", context)
