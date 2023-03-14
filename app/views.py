from django.shortcuts import render

# Create your views here.
def conditional(request):
    d={'a':101, 'b':201, 'c':300}
    return render(request,'conditional.html',context=d)

def loops(request):
    d={'Name':'Naveen'}
    return render(request,'loops.html',context=d)