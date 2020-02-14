from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    # return HttpResponse("hello Ritik")
    params={'name': 'ritik', 'place':'noida'}
    return render(request,'index.html',params)

def about(request):
    return HttpResponse(''' <h1> This is my first DJANGO WEBSITE </h1> <a href="/">HOME</a><br>
                            1. <a href="https://www.youtube.com/"> YouTube Site  </a><br>
                            2. <a href="https://www.facebook.com/"> Facebook Site  </a><br>
                            3. <a href="https://www.instagram.com/"> Instagram Site  </a><br>
                            4. <a href="https://www.google.com/"> Google Site  </a><br>
                            5. <a href="https://www.uber.com/"> UBER Site  </a><br> ''')

def read(request):
    f=open("D:\\DJANGO-Project\\mysite\\mysite\\kk.txt", "r+")
    return HttpResponse(f.readlines())

def analyze(request):
    #GET THE TEXT
    djtext=request.POST.get('text','default')
    removepunc=request.POST.get('removepunc', 'off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover=request.POST.get('newlineremover', 'off')
    spaceremover=request.POST.get('spaceremover', 'off')
    charcounter=request.POST.get('charcounter', 'off')
    
    if removepunc=='on':
        analyzed=""
        punctuations='''\-[]{}()*+?^.$|#/,'!@$&";'''
        for char in djtext:
            if char not in punctuations:
                analyzed+=char
        params={'purpose':'Changed to Upper Case', 'analyzed_text':analyzed}
        djtext=analyzed
        #ANALYZE THE TEXT
        # return render(request,'analyze.html', params)
    
    if(fullcaps=='on'):
        analyzed=""
        for char in djtext:
            analyzed=analyzed+char.upper()
        params={'purpose':'Changed to Upper Case', 'analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html', params)

    if(newlineremover=='on'):
        analyzed=""
        for char in djtext:
            if char !='\n' and char !='\r':
                analyzed=analyzed+char.upper()
        params={'purpose':'Removed NEW LINES', 'analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html', params)

    if(spaceremover=='on'):
        analyzed=""
        for index,char in enumerate(djtext):
            if not(djtext[index] ==' ' and djtext[index+1]==' '):
                analyzed=analyzed+char.upper()

        params={'purpose':'Removed NEW LINES', 'analyzed_text':analyzed}
        djtext=analyzed
        # return render(request,'analyze.html', params)

    if(charcounter=='on'):
        analyzed=""
        count=0
        punctuations='''\-[]{}()*+?^.$|#/,'!@$&";'''
        for index,char in enumerate(djtext):
            if not(djtext[index] ==' ' or djtext[index] in punctuations or djtext[index]=='\n'  ):
                analyzed=analyzed+char.upper()
                count+=1
        
        params={'purpose':'Removed NEW LINES', 'analyzed_text':analyzed, 'count':count}
        djtext=analyzed
        # return render(request,'analyze.html', params)

    if(charcounter!='on' and spaceremover!='on' and newlineremover!='on' and fullcaps!='on' and removepunc!='on'):
        return HttpResponse("Please select any operation")

    return render(request,'analyze.html', params)
    