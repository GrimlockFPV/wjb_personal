from django.shortcuts import render


# Create your views here.
def home_view(request, *args, **kwargs):  # *args, **kwargs
    return render(request, "home.html", {})


def resume_view(request, *args, **kwargs):
    return render(request, "resume.html", {})


def about_view(request, *args, **kwargs):
    my_context = {
        "title": "abc this is about us",
        "this_is_true": True,
        "my_number": 123,
        "my_list": [1313, 4231, 312, "Abc"],
        "my_html": "<h1>Hello World</h1>"

    }
    return render(request, "about.html", my_context)


