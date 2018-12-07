from django.shortcuts import render
from basic import forms
# Create your views here.

def calc(request):
    if request.method=='POST':
        form = forms.FormName(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            n1 = cd['num1']
            n2 = cd['num2']
            c = n1+n2
            return render(request,'out.html',{'form':form,'insert':c})
    else:
        form = forms.FormName()
    return render(request, 'index.html', {'form': form })
