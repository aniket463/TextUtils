from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#     return HttpResponse('''<h1>hello<h1>  <a href ='https://www.careerbywell.com/'> job4u</a>''')


def index(request):
    # params={'name':'software devloper','place':'KOLKATA'}
    return render(request, 'index.html')


def contact(request):
    return render(request, 'contact.html')


def about(request):
    return render(request, 'about.html')


def analyze(request):
    # Get the data
    djtext = request.POST.get('text', 'default')
    # Check which function will be execute.
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    if (djtext == ""):
        return HttpResponse('''ERROR!<br> You Must Enter some Text  <a href='/'><br>Back</a>''')
    print(removepunc)
    print(djtext)
    p = ''
    if removepunc == "on":

        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~£'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctuations', 'analyzed_text': analyzed}
        p = 'Remove Punctuations,'
        djtext = analyzed
        # return render(request,'analyze.html',params)
    if (fullcaps == "on"):

        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Upper Case', 'analyzed_text': analyzed}
        params['purpose'] = p + ' Upper Case,'
        p = params['purpose']

        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if (extraspaceremover == "on"):

        analyzed = ""
        for index, char in enumerate(djtext):
            if not (djtext[index] == " " and djtext[index + 1] == " "):
                analyzed = analyzed + char

        params = {'purpose': 'Extra spaceRemoved', 'analyzed_text': analyzed}
        params['purpose'] = p + ' Extra space,'
        p = params['purpose']

        # Analyze the text
        djtext = analyzed
        # return render(request, 'analyze.html', params)

    if (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char != "\r":
                analyzed = analyzed + char

        params = {'purpose': 'NewLines', 'analyzed_text': analyzed}
        params['purpose'] = p + ' NewLines,'
        p = params['purpose']
        # Analyze the text
        djtext = analyzed
        # return render(request, 'analyze.html', params)
    if (charcount == "on"):
        a = str(len(djtext))
        analyzed = djtext + f"               TOTAL CHAR = {a}"
        params = {'purpose': 'No of Char', 'analyzed_text': analyzed}
        params['purpose'] = p + ' No.of Character.'
        p = params['purpose']

    if (
            removepunc != "on" and fullcaps != "on" and extraspaceremover != "on" and newlineremover != "on" and charcount != "on"):
        return HttpResponse('''ERROR!<br> You Must select one operations <a href='/'><br>Back</a>''')

    return render(request, 'analyze.html', params)
