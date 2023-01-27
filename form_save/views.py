from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from rest_framework.views import APIView, Response
from .models import Form
from .serializers import FormSerializer


def upload_file(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES["file"])
            return HttpResponseRedirect("success/url/")
    else:
        form = UploadFileForm()
    return render(request, "upload.html", {"form": form})


def handle_uploaded_file(f):

    with open("cnab/cnab.txt", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)
    with open("cnab/cnab.txt", "r") as f:
        contents = f.read()
        transactions = []
        for content in contents:
            content = {
                "type": content[:1],
                # "date",
                # "value",
                # "cpf",
                # "creditCard",
                # "time",
                # "storeOwner",
                # "storeName",
            }
        transactions.append(content)
        print(transactions)


class getAll(APIView):
    def get(self, request):
        transactions = Form.objects.all()
        serializer = FormSerializer(transactions)
        return Response(serializer.data, status=201)
