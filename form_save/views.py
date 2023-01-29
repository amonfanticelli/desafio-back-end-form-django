from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadFileForm
from rest_framework.views import APIView, Response
from .models import Form
from .serializers import FormSerializer
import ipdb
from django.db.models import Sum


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
        contents = f.readlines()

        for content in contents:
            content = {
                "type": content[:1],
                "date": f"{content[1:5]}-{content[5:7]}-{content[7:9]}",
                "value": int(content[9:20]) / 100,
                "cpf": content[20:30],
                "creditCard": content[31:42],
                "time": f"{content[43:44]}:{content[45:46]}:{content[47:48]}",
                "storeOwner": content[47:60],
                "storeName": content[60:80],
            }

            Form.objects.create(**content)


class listStores(APIView):
    def get(self, request):
        transactions = Form.objects.values("storeName").annotate(
            totalValue=Sum("value")
        )
        return Response(transactions)
        # transactions = Form.objects.all()
        # serializer = FormSerializer(transactions, many=True)
        # return Response(serializer.data, status=201)
