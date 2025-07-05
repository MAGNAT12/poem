from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import ListPoem
# Create your views here.

def verse_list(request):
    return render(request, 'poem.html')

def poem_list(request):
    poems = ListPoem.objects.order_by('-created_at')
    return render(request, 'poem_list.html', {'poems': poems})

def like_poem(request, poem_id):
    poem = get_object_or_404(ListPoem, id=poem_id)
    voted = request.session.get(f'voted_poem_{poem_id}')

    if voted is None:
        poem.likes += 1
        poem.save()
        request.session[f'voted_poem_{poem_id}'] = 'like'

    messages.success(request, "Спасибо за ваш лайк!")
    return redirect('poem_list')


def dislike_poem(request, poem_id):
    poem = get_object_or_404(ListPoem, id=poem_id)
    voted = request.session.get(f'voted_poem_{poem_id}')

    if voted is None:
        poem.dislikes += 1
        poem.save()
        request.session[f'voted_poem_{poem_id}'] = 'dislike'

    messages.success(request, "Спасибо за ваш дислайк!")
    return redirect('poem_list')
