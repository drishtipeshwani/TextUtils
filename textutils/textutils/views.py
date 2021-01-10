from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')


def analyse(request):
    text = request.POST.get('text')
    removepunc = request.POST.get('removepunc')
    capitalize = request.POST.get('capitalize')
    newlineremover = request.POST.get('newlineremover')
    extraspaceremover = request.POST.get('extraspaceremover')
    charcount = request.POST.get('charcount')
    if removepunc == "on":
        punctuations = '''’'()[]{}<>:,!.?;/'''
        analyzed = "";
        for char in text:
            if char not in punctuations:
                analyzed = analyzed + char;
        params = {'purpose': 'Removed Punctuations', 'analyzed_text': analyzed}
        text = analyzed
    if capitalize == "on":
        analyzed = ""
        for char in text:
            analyzed = analyzed + char.upper();
        params = {'purpose': 'Capitalize all characters', 'analyzed_text': analyzed}
        text = analyzed
    if newlineremover == "on":
        analyzed = ""
        for char in text:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char;
            else:
                analyzed = analyzed + " " ;
        params = {'purpose': 'New Line Remover', 'analyzed_text': analyzed}
        text = analyzed
    if extraspaceremover == "on":
        analyzed = ""
        for i, char in enumerate(text):
            if not (text[i] == " " and text[i + 1] == " "):
                analyzed = analyzed + char;
        params = {'purpose': 'Extra Space Remover', 'analyzed_text': analyzed}
        text = analyzed
    if charcount == "on":
        c = 0;
        dtext = "";
        for char in text:
            if char != "\n" and char != "\r":
                dtext = dtext + char;
        for char in dtext:
            if char != " ":
                print(c);
                c = c + 1;
        analyzed = "Number of characters are " + str(c);
        params = {'purpose': 'Character counter', 'analyzed_text': text + "\n" + analyzed}

    if (
            removepunc != "on" and charcount != "on" and extraspaceremover != "on" and newlineremover != "on" and capitalize != "on"):
        m = {'message': "No Change in Text ! Please select a valid option"};
        return render(request, 'error.html', m);
    if (text == ""):
        m = {'message': "Empty Text-Field !"}
        return render(request, 'error.html', m);

    return render(request, 'analyse.html', params)
