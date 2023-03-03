from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Books, Members
from .serializers import MembersSerializer, BooksSerializer


# Create your views here.

# CRUD              Create,     Read,       Update         Delete


class MembersAPI(APIView):
    def get(self, request):
        # Zemanje na site podatoci
        # members = Members.objects.all()
        # members_serializer = MembersSerializer(members,many=True)
        # return Response(members_serializer.data)

        # Zemanje na eden podatok / unikaten podatok
        # member = Members.objects.get(ime_prezime="Marjan Shuplinoski")
        # members_serializer = MembersSerializer(member)
        # return Response(members_serializer.data)

        #  filtriranje na podatoci
        member = Members.objects.filter(zemeno=False, godini__gt=10,plateno=False).order_by("datum_zaclenuvanje")
        members_serializer = MembersSerializer(member, many=True)
        return Response(members_serializer.data)


class BooksAPI(APIView):
    def get(self, request):
        books = Books.objects.all()
        books_serializer = BooksSerializer(books, many=True)
        return Response(books_serializer.data)


class OneMember(APIView):
    def get(self, request):
        if request.GET.get('id', None):
            member_id = int(request.GET.get('id', 0))
            member = Members.objects.get(id=member_id)
            member_serializer = MembersSerializer(member)
            return Response(member_serializer.data)
        else:
            return Response({"error":"Greska"})

class Books_Zanr(APIView):
    def get(self, request):
        if request.GET.get('zanr', None):
            zanr = request.GET.get('zanr', '')
            book = Books.objects.get(zanr=zanr)
            book_serializer = BooksSerializer(book)
            return Response(book_serializer.data)
        else:
            return Response({"error": "Greska"})

class Books_Jazik(APIView):
    def get(self, request):
        if request.GET.get('jazik', None):
            jazik = request.GET.get('jazik', '')
            book = Books.objects.get(jazik=jazik)
            book_serializer = BooksSerializer(book)
            return Response(book_serializer.data)
        else:
            return Response({"error": "Greska"})

class Member_Grad(APIView):
    def get(self, request):
        if request.GET.get('grad', None):
            grad = request.GET.get('grad', '')
            member = Members.objects.filter(grad=grad)
            member_serializer = MembersSerializer(member,many=True)
            return Response(member_serializer.data)
        else:
            return Response({"error": "Greska"})

class Books_Dostapni(APIView):
    def get(self, request):
        if request.GET.get('dostapni_izdanija', None):
            dostapni_izdanija = int(request.GET.get('dostapni_izdanija', ''))
            book = Books.objects.filter(dostapni_izdanija__gt=dostapni_izdanija)
            book_serializer = BooksSerializer(book, many=True)
            return Response(book_serializer.data)
        else:
            return Response({"error": "Greska"})