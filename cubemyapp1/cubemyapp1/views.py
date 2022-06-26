from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    params = {"name": "harry pratap ", 'place': 'mars kumar','title': 'Removed Punctuation', 'analysed_text': 'ana', 'cli': ['how ', 'are ' ,'you.'],
              'student_details':[
                  {'name':'pradeep','phone':99999999999},
                  {'name':'sanddep','phone':91999919199},
                  {'name':'sanddep','phone':91999919199},
                  {'name':'sanddep','phone':91999919199},
                  {'name':'sanddep','phone':91999919199},
                  {'name':'sanddep','phone':91999919199},
                  {'name':'sanddep','phone':91999919199},

              ],
              'number':{1,2,3,4,5,6,7,8,9}
              }
    #param = {'title': 'Removed Punctuation', 'analysed_text': 'ana'}
    return render(request, 'index.html', params)
    # param = {'title': 'Removed Punctuation', 'analysed_text': 'ana'}
    # return render(request, 'index.html', param)
    #return HttpResponse("welcome to aboutus")
def intro(request):
    return render(request, 'intro.html')
def services(request):
    return render(request, 'services.html')
def cv(request):
    return render(request, 'cv.html')
def blog(request):
    return render(request, 'blog.html')
def contact(request):
    return render(request, 'contact.html')
    #return HttpResponse("welcome to aboutus")
# def course(request):
#     return HttpResponse("<b>welcome to course</b>")
def courseDetails(request,courseid):
    return HttpResponse(courseid)

