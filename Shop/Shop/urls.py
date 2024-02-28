from django.contrib import admin
from django.urls import path
from Asosiy.views import *
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view()),
    path('products/', ProductsView.as_view()),
    path('about/', AboutView.as_view()),
    path('contact/', ContactView.as_view()),
    path('prdetail/<int:pk>/', PrDetailView.as_view()),
    path('signup/', SignUpView.as_view()),
    path('signin/', SignInView.as_view()),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



