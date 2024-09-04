from django.shortcuts import render

def show_main(request):
    context = {
        'npm': '1906350603',
        'name': 'Vander Gerald Sukandi',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)

# Create your views here.
