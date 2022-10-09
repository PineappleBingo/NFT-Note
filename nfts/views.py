from django.shortcuts import render

# request -> response
# request handler
# action

def say_hello(request):
    return render(request, 'nfts/hello.html')