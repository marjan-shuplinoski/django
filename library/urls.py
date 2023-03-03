from django.urls import path
from .views import MembersAPI, BooksAPI, OneMember, Books_Zanr, Books_Jazik, Member_Grad, Books_Dostapni


urlpatterns = [
    path('MembersAPI', MembersAPI.as_view()),
    path("BooksAPI", BooksAPI.as_view()),
    path('OneMember',OneMember.as_view()),
    path('Book_Zanr',Books_Zanr.as_view()),
    path('Book_Jazik',Books_Jazik.as_view()),
    path('Member_Grad',Member_Grad.as_view()),
    path('Books_Dostapni',Books_Dostapni.as_view()),

]