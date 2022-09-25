from django.shortcuts import render, redirect


def counter(request):
    if "ctimes" in request.session:
        request.session["ctimes"] += 1
    else:
        request.session["ctimes"] = 1

    return render(request, "index.html")


def destroy_session(request):
    del request.session["ctimes"]
    return redirect("/")
