from django.shortcuts import render,redirect
from django.views import View
from .models import *
from .forms import *
from django.core.mail import send_mail
import smtplib
from django.contrib.auth import authenticate, login





class IndexView(View):
    def get(self,request):
        data = {"asosiysahifa":AsosiySahifa.objects.all()}
        return render(request,'index.html',data)



class ProductsView(View):
    def get(self,request):
        data = {"telefons": Telefonlar.objects.all(), "soats": Soatlar.objects.all(), "boshqas": BoshqaMahsulotlar.objects.all()}
        return render(request,'products.html',data)



class AboutView(View):
    def get(self,request):
        data = {'sahifa':WebSahifalar.objects.all()}
        return render(request,'about.html',data)



class ContactView(View):
    def get(self,request):
        return render(request,'contact.html')

    def post(self, request):
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']

            # Tashqi pochta serverning host va port ma'lumotlarini o'rnating
            host = 'smtp.gmail.com'
            port = 465

            # Tashqi pochta serveriga ulanishni tekshirish
            def test_smtp_connection():
                try:
                    server = smtplib.SMTP(host, port)
                    server.close()
                    return True
                except Exception as e:
                    print(f"Ulanishda xatolik yuz berdi: {str(e)}")
                    return False

            if test_smtp_connection():
                send_mail(
                    name,
                    subject,
                    email,  # Absenderingizning email manzili
                    ['xayrullajonovozodbek@gmail.com'],  # Adminning email manzili
                    fail_silently=False,
                )

                return render(request, 'success.html')

            else:
                print(form.errors)
                print(form.non_field_errors)
                # Xatolik bilan qaytaring

        return render(request, 'contact.html', {'form': form})



class PrDetailView(View):
    def get(self,request,pk):
        data = {'product':AsosiySahifa.objects.get(id=pk), 'asosiysah':AsosiySahifa.objects.all()}
        return render(request,'product-detail.html',data)



class SignUpView(View):
    def get(self,request):
        return render(request,'sign-up.html')
    def post(self,request):
        if request.POST.get('password')==request.POST.get('confirm_password'):
            User.objects.create_user(
                username = request.POST.get('email'),
                password = request.POST.get('password')
            )
            return redirect('/signin/')
        else:
            return redirect('/signup')



class SignInView(View):
    def get(self, request):
        return render(request,'sign-in.html')
    def post(self,request):
            user = authenticate(username=request.POST.get('email'),
                         password=request.POST.get('password'))
            if user:
                login(request, user)
                return redirect('/')
            return redirect('/signin/')




