from django.shortcuts import render

def post_list(request):
    return render(request, 'northlandblog/post_list.html', {})
