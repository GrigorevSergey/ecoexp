import json
from django.core.mail import EmailMessage
from django.http import HttpResponse
from django.shortcuts import render

from config import settings
from .models import Post, PostValue

def post_form(request):
    if request.method == 'POST':
        # Данные для модели Post
        customer = request.POST.get('customer')
        customer_address = request.POST.get('customer_address')
        name_official = request.POST.get('name_official')
        contract = request.POST.get('contract')
        name_of_the_object = request.POST.get('name_of_the_object')
        location_object = request.POST.get('location_object')
        the_presence_of_harmful_factors = request.POST.get('the_presence_of_harmful_factors') == 'on'
        the_purpose_of_the_research = request.POST.get('the_purpose_of_the_research')

        # Создание записи Post
        post = Post.objects.create(
            customer=customer,
            customer_address=customer_address,
            name_official=name_official,
            contract=contract,
            name_of_the_object=name_of_the_object,
            location_object=location_object,
            the_presence_of_harmful_factors=the_presence_of_harmful_factors,
            the_purpose_of_the_research=the_purpose_of_the_research
        )

        # Обработка множественных PostValue
        titles = request.POST.getlist('title[]')
        categories = request.POST.getlist('category[]')
        values = request.POST.getlist('value[]')
        name_of_indicators_list = request.POST.getlist('name_of_indicators[]')

        post_values = []
        for title, category, value, name_of_indicators in zip(titles, categories, values, name_of_indicators_list):
            post_value = PostValue.objects.create(
                title=title,
                category=category,
                value=int(value),
                name_of_indicators=name_of_indicators
            )
            post.indicators.add(post_value)

            # Добавляем данные в JSON
            post_values.append({
                'title': title,
                'category': category,
                'value': value,
                'name_of_indicators': name_of_indicators,
            })

        # Сохранение данных в JSON
        post_data = {
            'customer': customer,
            'customer_address': customer_address,
            'name_official': name_official,
            'contract': contract,
            'name_of_the_object': name_of_the_object,
            'location_object': location_object,
            'the_presence_of_harmful_factors': the_presence_of_harmful_factors,
            'the_purpose_of_the_research': the_purpose_of_the_research,
            'indicators': post_values,
        }

        json_data = json.dumps(post_data, ensure_ascii=False, indent=4)

        # Отправка письма
        email = EmailMessage(
            subject=f"Новая заявка к договору № {post.contract}",
            body="Во вложении JSON с данными формы.",
            from_email=settings.EMAIL_HOST_USER,
            to=["grigoryev0089@yandex.ru"],
        )
        email.attach('form_data.json', json_data.encode('utf-8'), 'application/json')
        email.send()

        return HttpResponse("Форма успешно отправлена!")

    return render(request, 'application/post_form.html')


def home(request):
    return render(request, 'application/home.html')