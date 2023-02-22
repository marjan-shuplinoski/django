from django.urls import path
from .views import helloWorld, zbir_na_broevi, odzemanje_na_broevi, mnozenje_na_broevi, delenje_na_broevi, \
    mat_operacija, prv_post, mat_operacija2, proverka_godini, PrvView, ime, ime_god, najgolem_broj,limit

urlpatterns = [
    path("hello-world", helloWorld),
    path("zbir-na-broevi", zbir_na_broevi),
    path("odzemanje-na-broevi", odzemanje_na_broevi),
    path("mnozenje-na-broevi", mnozenje_na_broevi),
    path("delenje-na-broevi", delenje_na_broevi),
    path("mat_operacija", mat_operacija),
    path("prv_post", prv_post),
    path("mat_operacija2", mat_operacija2),
    path("proverka_godini", proverka_godini),
    path("prva_klasa", PrvView.as_view()),
    path("ime",ime.as_view()),
    path("ime_god",ime_god.as_view()),
    path("najgolem_broj",najgolem_broj.as_view()),
    path("limit",limit.as_view()
]
