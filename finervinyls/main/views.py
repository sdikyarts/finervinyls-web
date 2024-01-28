from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'title': 'Test',
        'content': 'This is a test. This is only a test.',
        'date_posted': '2021-10-10'
    }

    return render(request, "main.html", context)