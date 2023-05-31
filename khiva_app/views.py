from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView

from khiva_app.models import Khiva, Images, Contact, KhivaNews, Restaurant
from .forms import ContactForm


def khiva_list(request):
    khiva_list = Khiva.published.all()

    context = {
        'khiva_list': khiva_list
    }
    return render(request, 'khiva/khiva_list.html', context)


def khiva_detail(request, khiva):
    khiva_detail = get_object_or_404(Khiva, slug=khiva, status=Khiva.Status.Published)
    context = {
        'khiva_detail': khiva_detail
    }

    return render(request, 'khiva/khiva_detail.html', context)

def khiva_course_single(request):
    context = {

    }
    return render(request,'khiva/course-single.html', context)


def HomePage(request):
    khiva_news = Khiva.objects.all().filter(status=Khiva.Status.Published).order_by()[:5]
    image_news = Images.objects.all()
    users = Contact.objects.all()
    khiva_new = KhivaNews.objects.all()
    restaurant = Restaurant.objects.all()
    context = {
        'khiva_news': khiva_news,
        'image_news': image_news,
        'users':users,
        'khiva_new':khiva_new,
        'restaurant':restaurant
    }

    return render(request, 'khiva/home.html', context)


def GalleryPage(request):
    image_news = Images.objects.all()
    context = {
        'image_news': image_news
    }
    return render(request, 'khiva/gallery2.html', context)


def aboutPage(request):
    context = {

    }
    return render(request, 'khiva/about.html', context)


# def ContactPageView(request):
#     form = ContactForm(request.POST or None)
#     if request.method == 'POST' and form.is_valid(): # yani inputlarning hammasi toldirilganmi yo yo'qmi sh
#         form.save()
#         return HttpResponse("<h2>Biz bilan bog'langaningizdan hursandmiz!!!</h2>")
#
#     context = {
#         'form':form
#     }
#     return render(request, 'khiva/contact.html', context)
class ContactPageView(TemplateView):
    template_name = 'khiva/contact.html'

    def get(self, request, *args, **kwargs):
        form = ContactForm()
        context = {
            'form': form
        }
        return render(request, 'khiva/contact.html', context)

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if request.method == 'POST' and form.is_valid():
            form.save()
            return HttpResponse("<h2> Biz bilan bog'langaningiz uchun raxmat!!!!</h2>")
        context = {
            'form': form
        }

        return render(request, 'khiva/contact.html', context)





