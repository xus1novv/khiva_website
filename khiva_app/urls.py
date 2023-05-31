from django.urls import path
from .views import khiva_list, khiva_detail, HomePage, ContactPageView, GalleryPage, aboutPage, khiva_course_single

urlpatterns = [
    path('', HomePage, name = 'home_page' ),
    path('khiva/', khiva_list, name = 'khiva_list_page'),
    path('khiva/<slug:khiva>/', khiva_detail, name = 'khiva_detail_page' ),
    path('course_single', khiva_course_single, name = 'khiva_course_single'),
    path('aboutkhiva/', aboutPage, name = 'about_page_detail'),
    path('gallery/', GalleryPage, name = 'gallery_page'),
    path('contact/', ContactPageView.as_view(), name = 'contact_page')
]