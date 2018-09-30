from django.shortcuts import render


def main(request):
    title = 'Главная'

    content = {'title': title}
    return render(request, 'mainapp/index.html', content)


def catalog(request):
    title = 'Каталог'

    content = {'title': title}
    return render(request, 'mainapp/catalog.html', content)


def contacts(request):
    title = 'Контакты'

    content = {'title': title}
    return render(request, 'mainapp/contacts.html', content)


def products(request):
    title = 'Продукт'

    content = {'title': title}
    return render(request, 'mainapp/products/1.html', content)
