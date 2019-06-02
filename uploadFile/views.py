from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.



def upload(request):
    if request.method == "POST":
        print(request.POST)
        print(request.FILES)

        obj = request.FILES.get('avatar')
        with open(obj.name, 'wb') as f:
            for line in obj:
                f.write(line)
        return HttpResponse("OK")
    return render(request,'l_upload.html')