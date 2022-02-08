from django.shortcuts import render, get_object_or_404, redirect
from .models import Post
from django.utils import timezone
from .forms import PostForm


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):  #После заполнения формы(не дает отправить пустую форму) и нажатия клавиши submit форма отправляется
    if request.method == 'POST': #к функции post_new, где определяется тип запроса, здесь он POST тк отправили форму в нем
        form = PostForm(request.POST) #Берется не пустая форма а заполненная из запроса
        if form.is_valid():
            post = form.save(commit=False)  #сохранение полей text и title
            post.author = request.user      #сохранение в посте поля автора не из request.POST а из request.user
            post.published_date = timezone.now()
            post.save() #сохранение записи в бд
            return redirect('blog:post_detail', pk=post.pk)  #перенаправление на созданный и отрендеренную запись
    else:
        form = PostForm()  # если метод запроса Get(при переходе со списка блога по кнопке плюсика) то рендерится
        print(request.method)  # страница с пустой формой и клавишей сабмит
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk) #получаем pk из url
    if request.method == 'POST':  #если метод запроса POST
        form = PostForm(request.POST, instance=post) #отличие от post_new(2 аргумент добавился instance=post (не добавляет новую а изменяет выбранную)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post) #при нажатии на карандаш и попадании в edit формы уже заполнены предыдущим контентом
    return render(request, 'blog/post_edit.html', {'form': form})
