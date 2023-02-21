from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.

# CBW - Class Based Views

# FBW - Function Based Views

@api_view(["GET"])
def helloWorld(request):
    ime = request.GET['ime']
    prezime = request.GET.get("prezime", "Shuplinoski")
    print(ime)
    data = {"info": "Dobrodojdovte {} {}".format(ime, prezime)}
    return Response(data)


@api_view(["GET"])
def zbir_na_broevi(request):
    broj1 = int(request.GET.get('broj1', 0))
    broj2 = int(request.GET.get('broj2', 0))
    zbir = broj1 + broj2
    data = {"poraka": "Zbirot na {} i {} e {}".format(broj1, broj2, zbir),
            "broj1": broj1,
            "broj2": broj2,
            "zbir": zbir
            }
    return Response(data)


@api_view(["GET"])
def odzemanje_na_broevi(request):
    broj1 = int(request.GET.get('broj1', 0))
    broj2 = int(request.GET.get('broj2', 0))
    odzemanje = broj1 - broj2
    data = {
        "poraka": "Odzemanje na {} i {} = {}".format(broj1, broj2, odzemanje)
    }
    return Response(data)


@api_view(["GET"])
def mnozenje_na_broevi(request):
    broj1 = int(request.GET.get('broj1', 0))
    broj2 = int(request.GET.get('broj2', 0))
    mnozenje = broj1 * broj2
    data = {
        "poraka": "Mnozenje na {} i {} = {}".format(broj1, broj2, mnozenje)
    }
    return Response(data)


@api_view(["GET"])
def delenje_na_broevi(request):
    broj1 = int(request.GET.get('broj1', 0))
    broj2 = int(request.GET.get('broj2', 0))
    delenje = broj1 / broj2
    data = {
        "poraka": "Delenje na {} i {} = {}".format(broj1, broj2, delenje)
    }
    return Response(data)


@api_view(["GET"])
def mat_operacija(request):
    broj1 = int(request.GET.get('broj1', 0))
    broj2 = int(request.GET.get('broj2', 0))
    operacija = request.GET.get('operacija', None)
    if (operacija == 'sobiranje'):
        rezultat = broj1 + broj2
        return Response(rezultat)
    elif (operacija == 'odzemanje'):
        rezultat = broj1 - broj2
        return Response(rezultat)
    elif (operacija == 'mnozenje'):
        rezultat = broj1 * broj2
        return Response(rezultat)
    elif (operacija == 'delenje'):
        rezultat = broj1 / broj2
        return Response(rezultat)
    else:
        return Response('error')


@api_view(['POST'])
def prv_post(request):
    print(request.data)
    ime = request.data.get('ime', None)
    prezime = request.data.get('prezime', None)
    return Response({'info': "uspesno"})


@api_view(["POST"])
def mat_operacija2(request):
    broj1 = int(request.data.get('broj1', 0))
    broj2 = int(request.data.get('broj2', 0))
    operacija = request.data.get('operacija', None)
    if (operacija == 'sobiranje'):
        rezultat = broj1 + broj2
        return Response(rezultat)
    elif (operacija == 'odzemanje'):
        rezultat = broj1 - broj2
        return Response(rezultat)
    elif (operacija == 'mnozenje'):
        rezultat = broj1 * broj2
        return Response(rezultat)
    elif (operacija == 'delenje'):
        rezultat = broj1 / broj2
        return Response(rezultat)
    else:
        return Response('error')


@api_view(["POST"])
def proverka_godini(request):
    ime = request.data.get('ime', None)
    godini = int(request.data.get('godini', None))
    if (godini > 18):
        return Response("{} e polnoleten".format(ime))
    else:
        return Response("{} e maloleten".format(ime))
