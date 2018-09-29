import datetime
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import UpdateView, DeleteView, ListView
from basic_app.forms import UserForm, OrderForm, AddressForm
from basic_app.models import Order, Address
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.
def index(request):
    return render(request, 'basic_app/index.html')


@login_required
def home(request):
    order = OrderForm()
    return render(request, 'basic_app/home.html', {'order': order})


def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()

    return render(request, 'basic_app/registration.html',
                  {'user_form': user_form,
                   'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('basic_app:home'))
            else:
                return HttpResponse("Account not active")
        else:
            print("someone tried to login and failed")
            print("Username: {} and password {}".format(username, password))
            return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'basic_app/login.html', {})


class UserUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UserForm
    model = User

    def get_success_url(self):
        return reverse('index')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


@login_required
def address(request):
    form = AddressForm()
    if request.method == "POST":
        address_form = AddressForm(request.POST)
        if address_form.is_valid():
            address = address_form.save(commit=False)
            user = User.objects.get(id=request.user.id)
            address.user = user
            address.save()
            return HttpResponseRedirect(reverse('basic_app:address_list'))
    return render(request, 'basic_app/address_list.html', {'form': form})


class AddressListView(LoginRequiredMixin, ListView):
    model = Address
    def get_queryset(self):
        return Address.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super(AddressListView, self).get_context_data(**kwargs)
        context['address'] = AddressForm()
        context['order'] = OrderForm()
        return context

class AddressUpdateView(LoginRequiredMixin, UpdateView):
    form_class = AddressForm
    model = Address

    def get_success_url(self):
        return reverse('basic_app:address_list')


class AddressDeleteView(LoginRequiredMixin, DeleteView):
    model = Address
    success_url = reverse_lazy('basic_app:address_list')


@login_required
def order(request):
    form = OrderForm()
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            user = User.objects.get(id=request.user.id)
            order.orderedBy = user
            order.save()
            return HttpResponseRedirect(reverse('basic_app:order_list'))
    return render(request, 'basic_app/order.html', {'form': form})


class OrderDeleteView(LoginRequiredMixin, DeleteView):
    model = Order
    success_url = reverse_lazy('basic_app:order_list')


class OrderListView(LoginRequiredMixin, ListView):
    model = Order

    def get_queryset(self):
        return Order.objects.filter(date_placed__lte=datetime.datetime.now()).order_by('-date_placed')
