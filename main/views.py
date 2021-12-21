from django.db.models import Q
from django.shortcuts import render, redirect
# from django.http import HttpResponse
from django.views.generic.list import ListView
# import json
from account.models import Profile
from main.filters import JewelryFilter
from main.models import Jewelry, JewelryShape, StoneType


def home_view(request):
    jewels = [o.shape for o in JewelryShape.objects.all()]
    types = [o.type for o in StoneType.objects.all()]
    context = {'jewels': jewels, 'types': types}
    request.session['username'] = 'session_tom'
    return render(request, 'home.html', context)


# def jewelry_view(request):
#     # if shape_id:
#     #     print('-->', shape_id)
#     jewelries = Jewelry.objects.all()
#     # f = JewelryFilter(request.GET, queryset=Jewelry.objects.filter())
#     # context = {'jewelry': jewelry, 'filter': f}
#     context = {'jewelries': jewelries}
#     return render(request, 'pages/jewelry.html', context)


def about_view(request):
    context = {}
    return render(request, 'pages/about.html', context)


# class JewelryListView(ListView):
#     template_name = 'pages/jewelry_list.html'
#     model = Jewelry
#     context_object_name = 'jewelries'


def jewelry_htmx(request):
    print('---> jewelry_htmx')
    jewelries = Jewelry.objects.all()
    avail = [[o.shape for o in JewelryShape.objects.all()], [o.type for o in StoneType.objects.all()]]

    # get payload
    pressed = [request.POST.get('shape_pressed', ''), request.POST.get('stone_type_pressed', '')]
    displayed = [request.POST.get('shapes_displayed', ''), request.POST.get('stone_types_displayed', '')]

    # translate displayed into lists
    for i in range(len(displayed)):
        t = []
        for j in avail[i]:
            if j in displayed[i]:
                t.append(j)
        displayed[i] = t

    for i in range(len(pressed)):
        if pressed[i]:
            print(pressed[i])
            if pressed[i] in displayed[i]:
                displayed[i].remove(pressed[i])
            else:
                displayed[i].append(pressed[i])

    # remove from jewelries all ,unwanted shapes
    for i in range(len(displayed)):
        if displayed[i]:
            print(displayed[i])
            jewelries = jewelries.filter(Q(jewelryShape__shape__in=displayed[i]) | Q(stoneType__type__in=displayed[i]))

    context = {
        'jewelries': jewelries,
        'shapes_available': avail[0],
        'stone_types_available': avail[1],
        'shapes_displayed': displayed[0],
        'stone_types_displayed': displayed[1],
    }
    return render(request, 'pages/jewelry.html', context)


def jewel_view(request, jewel_id):
    # print('--->', jewel_id)
    jewel = Jewelry.objects.get(id=jewel_id)
    context = {'jewel': jewel}
    return render(request, 'pages/jewel.html', context)


def test_url(request, param):
    print(param)
    return redirect('jewelry_htmx')
