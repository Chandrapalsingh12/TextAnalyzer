from django.http import HttpResponse
from django.shortcuts import render

def index(request):

    return render(request, "index.html")

def analyze(request):

    djtext = request.POST.get("text", "off")

    removepunc = request.POST.get("removepunc", "off")

    fullcaps = request.POST.get("fullcaps", "off")

    charcount = request.POST.get("countchar", "off")

    if removepunc == "on":
        punctuation = ''' ~!@#$%^&*()_+{}|:"<>?/.,'\;][=- '''
        analyzed = ""
        for char in djtext:
            if char not in punctuation:
                analyzed = analyzed + char

        luci = {"my": "Remove Punctuations", "my_text": analyzed}
        djtext = analyzed

    if fullcaps == "on":
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()
        luci = {"my": "Change To Uppecase", "my_text": analyzed}
        djtext = analyzed

    if charcount == "on":
        analyzed = len(djtext)
        luci = {"my": "Count Of your Text is: ", "my_text": analyzed}
        djtext = analyzed

    if (removepunc != "on" and fullcaps != "on" and charcount != "on"):
        return HttpResponse("Error")

    return render(request,"analyze.html", luci)

