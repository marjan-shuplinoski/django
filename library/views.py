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
        member = Members.objects.filter(zemeno=False, godini__gt=10, plateno=False).order_by("datum_zaclenuvanje")
        members_serializer = MembersSerializer(member, many=True)
        return Response(members_serializer.data)

    def post(self, request):
        member_serializer = MembersSerializer(data=request.data)
        if (member_serializer.is_valid()):
            member_serializer.save()
            return Response({'info': 'success', 'data': member_serializer.data})
        else:
            return Response(member_serializer.errors)

    def patch(self, request):
        member_id = request.data.get("id", None)
        try:
            member = Members.objects.get(id=member_id)
            member_serializer = MembersSerializer(member, data=request.data, partial=True)
            if member_serializer.is_valid():
                member_serializer.save()
                return Response(member_serializer.data)
            else:
                return Response(member_serializer.errors)
        except Members.DoesNotExist:
            return Response({"info": "Member does not exists"})

    def delete(self, request):
        member_id = request.data.get("id", None)
        try:
            member = Members.objects.get(id=member_id)
            member.delete()
        except Members.DoesNotExist:
            return Response({"info": "Member does not exists"})
        return Response({"info": "success"})


class BooksAPI(APIView):
    def get(self, request):
        books = Books.objects.all()
        books_serializer = BooksSerializer(books, many=True)
        return Response(books_serializer.data)

    def post(self, request):
        book_serializer = BooksSerializer(data=request.data)
        if (book_serializer.is_valid()):
            book_serializer.save()
            return Response({'info': 'success', 'data': book_serializer.data})
        else:
            return Response(book_serializer.errors)

    def patch(self, request):
        book_id = request.data.get("id", None)
        try:
            book = Books.objects.get(id=book_id)
            book_serializer = BooksSerializer(book, data=request.data, partial=True)
            if book_serializer.is_valid():
                book_serializer.save()
                return Response(book_serializer.data)
            else:
                return Response(book_serializer.errors)
        except Books.DoesNotExist:
            return Response({"info": "Book does not exists"})

    def delete(self, request):
        book_id = request.data.get("id", None)
        try:
            book = Books.objects.get(id=book_id)
            book.delete()
        except Books.DoesNotExist:
            return Response({"info": "Book does not exists"})
        return Response({"info": "success"})


class OneMember(APIView):
    def get(self, request):
        if request.GET.get('id', None):
            member_id = int(request.GET.get('id', 0))
            member = Members.objects.get(id=member_id)
            member_serializer = MembersSerializer(member)
            return Response(member_serializer.data)
        else:
            return Response({"error": "Greska"})


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
            member_serializer = MembersSerializer(member, many=True)
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


class Pozajmi(APIView):
    def post(self, request):
        member = Members.objects.get(id=request.data.get('member_id', None))
        book = Books.objects.get(id=request.data.get('book_id', None))
        if(member.plateno != True):
            return Response({"error": "Nemate plateno"})
        if(member.zemeno == True):
            return Response({"error": "Veke imate zemeno kniga"})
        member.zemeno = True
        member.pozajmeno_kniga = book
        member.save()

        book.dostapni_izdanija -= 1
        book.save()

        member_serializer = MembersSerializer(member)
        return Response ( member_serializer.data)

class VratiKniga(APIView):
    def post(self,request):
        member = Members.objects.get(id=request.data.get('member_id', None))
        member.pozajmeno_kniga.dostapni_izdanija += 1
        member.pozajmeno_kniga.save()

        member.zemeno = False
        member.pozajmeno_kniga = None
        member.save()

        member_serializer = MembersSerializer(member)
        return Response(member_serializer.data)

class Plati(APIView):
    def post(self,request):
        try:
            member = Members.objects.get(id=request.data.get('member_id', None))
            if(member.plateno == True):
                return Response("Imate plateno")
            else:
                member.plateno= True
                member.save()
                return Response("Samo sto plativte")
        except Members.DoesNotExist:
            return Response("Ne postoi takov Member")