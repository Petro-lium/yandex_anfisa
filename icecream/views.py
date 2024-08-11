from django.shortcuts import render, get_object_or_404
from .models import IceCream


def icecream_detail(request, pk):
    ice_cream = get_object_or_404(IceCream, pk=pk)

    context = {
            'name': ice_cream.name,
            'description': ice_cream.description,
    }

    return render(request, "icecream/icecream-detail.html", context)
