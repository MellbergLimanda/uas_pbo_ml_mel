from django.shortcuts import render, redirect
from .forms import MobilForm
from .models import Jenis
from .models import Mobil
from django.http import JsonResponse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from django.shortcuts import render
from django.contrib.auth.views import LoginView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User  # Import User model
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.contrib.auth import logout
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse
from django.urls import reverse_lazy
import numpy as np
import pickle


class MobilListView(LoginRequiredMixin, ListView):
    model = Mobil
    template_name = 'mobil_list.html'
    context_object_name = 'mobil_list'

    def get_queryset(self):
        # Retrieve all Mobil objects for the currently logged-in user
        mobil_list = Mobil.objects.filter(user=self.request.user)
        
        # If needed, handle the case where no objects are found
        if not mobil_list.exists():
            # You could log this or set a message for the user
            pass
        
        return mobil_list

class CustomLoginView(LoginView):
    template_name = 'login.html'

class CustomLogoutView(LogoutView):
    next_page = '/login/'

class CustomPasswordChangeView(PasswordChangeView):
    template_name = 'registration/changepassword.html'
    success_url = reverse_lazy('login.html')
    
    def form_valid(self, form):
        # Change the password and then logout the user
        response = super().form_valid(form)
        logout(self.request)
        messages.success(self.request, 'Password changed successfully. Please login again.')
        return response

    def get_success_url(self):
        return '/login/'

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')  # Get email from the form
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)  # Authenticate using email
        if user is not None:
            login(request, user)
            return redirect('home')  # Redirect to the home page after successful login
        else:
            messages.error(request, 'Invalid email or password')
            return redirect('login')  # Redirect back to the login page to show error message
    else:
        return render(request, 'login.html')
    
def home_view(request):
    return render(request, 'home.html') 

def about_view(request):
    return render(request, 'about.html')


    
def logout_view(request):
    logout(request)
    return redirect('home')

from django.contrib import messages

# views.py
from django.contrib.auth.models import User
from django.contrib import messages

def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.error(request, 'Registration successful, but login failed.')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/register.html', {'form': form})



from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import MobilForm

@login_required
def tambah_mobil(request):
    if request.method == 'POST':
        model_ml = pickle.load(open("aplikasi/models/model_2.pkl", "rb"))
        features = [request.POST.get('tahun'),request.POST.get('kapasitas_mesin'),request.POST.get('bahanbakar'),request.POST.get('transmisi'),request.POST.get('Penggerakroda'),request.POST.get('odometer'),int(request.POST.get('odometer')) + 20000,request.POST.get('harga'),int(request.POST.get('harga'))+50000000]
        features = np.array([features])  # Reshape to 2D array
        prediction = model_ml.predict(features)
        form = MobilForm(request.POST)
        if form.is_valid():
            mobil = form.save(commit=False)
            mobil.user = request.user  # Assign the current logged-in user
            if prediction[0] == 1:
                mobil.kelayakan = "1"
            else:
                mobil.kelayakan = "0"
            mobil.save()
            return redirect('mobil_list')
    else:
        form = MobilForm()
    
    return render(request, 'aplikasi/tambah_mobil.html', {'form': form})

@login_required
def mobil_list(request):
    """
    View to list Mobil objects for the currently logged-in user.
    
    This view ensures that only authenticated users can access the list of
    Mobil objects that belong to them.
    """
    # Retrieve all Mobil objects for the currently logged-in user
    mobil_list = Mobil.objects.filter(user=request.user)
    
    # If needed, handle the case where no objects are found
    if not mobil_list.exists():
        # You could log this or set a message for the user
        pass
    
    # Render the mobil_list.html template with the filtered Mobil objects
    
    return render(request, 'mobil_list.html', {'mobil_list': mobil_list})


def jenis_ajax(request):
    merek_id = request.GET.get('merek')
    jenis_list = Jenis.objects.filter(merek_id=merek_id).values('id', 'name')
    return JsonResponse(list(jenis_list), safe=False)

def edit_mobil(request, pk):
    mobil = get_object_or_404(Mobil, pk=pk)
    if request.method == "POST":
        form = MobilForm(request.POST, instance=mobil)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data has been edited successfully')
            return redirect(reverse('mobil_list'),pk=pk)  # Redirect to the mobil_list view
    else:
        form = MobilForm(instance=mobil)
    return render(request, 'edit_mobil.html', {'form': form})

def delete_mobil(request, id):
    mobil = get_object_or_404(Mobil, id=id)
    if request.method == 'POST':
        mobil.delete()
        messages.success(request, 'Data has been deleted successfully.')
        return redirect('mobil_list')
    return render(request, 'delete_mobil.html', {'mobil': mobil})

def jenis_by_merek(request):
    merek_id = request.GET.get('merek_id')
    jenis_list = Jenis.objects.filter(merek_id=merek_id).values('id', 'name')
    return JsonResponse({'jenis_list': list(jenis_list)})