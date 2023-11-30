from django.shortcuts import render, redirect, get_object_or_404
from store.forms import WearForm
from store.models import Wear, Category


def create_wear(request):
    # создать товар
    categories = Category.objects.all()
    if request.method == 'POST':
        form = WearForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success_page')
    else:
        form = WearForm()

    return render(request,
                  'store/create.html',
                  {'form': form, 'categories': categories})


def update(request, id):
    # Функция для изменений полей товара
    wear = Wear.objects.get(id=id)
    form = WearForm(request.POST, instance=wear)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/crud/')


def edit(request, id):
    # Изменить поля товара
    wear = Wear.objects.get(id=id)
    categories = Category.objects.all()
    return render(request,
                  'store/edit.html',
                  {'wear': wear, 'categories': categories})


def delete(request, id):
    # Удалить товар по его id на главной странице
    wear = Wear.objects.get(id=id)
    wear.delete()
    return redirect('/crud/')


def show(request):
    # Наличие всех товаров в БД
    wear = Wear.objects.all()
    return render(request,
                  'store/show.html',
                  {'wear': wear})


def success_page(request):
    # Код для страницы успешного создания товара
    return render(request,
                  'store/success_page.html')
