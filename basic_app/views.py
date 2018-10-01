import datetime
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import UpdateView, DeleteView, ListView
from basic_app.forms import UserForm, OrderForm, AddressForm
from basic_app.models import Order, Address
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages


# Create your views here.
def index(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('basic_app:home'))
    else:
        return render(request, 'basic_app/index.html')


@login_required
def home(request):
    return render(request, 'basic_app/home.html', {})


def register(request):
    registered = False
    if request.method == "POST":
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            cd = user_form.cleaned_data
            user = user_form.save()
            user.set_password(cd['password_raw'])
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

        user = authenticate(request, username=username, password=password)
        if user:
            if user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('basic_app:home'))
            else:
                return HttpResponse("Account not active")
        else:
            messages.error(request, "Invalid login credentials, please try again!")

            return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'basic_app/index.html', {})


class UserUpdateView(LoginRequiredMixin, UpdateView):
    form_class = UserForm
    model = User

    def form_valid(self, form):
        user = form.save()
        user.set_password(form.cleaned_data['password_raw'])
        return redirect(self.get_success_url())

    def get_success_url(self):
        return reverse('logout')

    def user_passes_test(self, request):
        if request.user.is_authenticated:
            self.object = self.get_object()
            return self.object == request.user
        return False

    def dispatch(self, request, *args, **kwargs):
        if not self.user_passes_test(request):
            return HttpResponseRedirect(reverse('basic_app:user_update', kwargs={'pk': request.user.id}))
        return super(UserUpdateView, self).dispatch(
            request, *args, **kwargs)


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
    if request.method == "POST":
        order_form = OrderForm(request.user.id, request.POST)
        if order_form.is_valid():
            order = order_form.save(commit=False)
            user = User.objects.get(id=request.user.id)
            order.orderedBy = user
            order.save()
            return HttpResponseRedirect(reverse('basic_app:order_list'))
    return render(request, 'basic_app/home.html')


class OrderDeleteView(LoginRequiredMixin, DeleteView):
    model = Order
    success_url = reverse_lazy('basic_app:order_list')


class OrderListView(LoginRequiredMixin, ListView):
    model = Order

    def get_queryset(self):
        return Order.objects.filter(orderedBy=self.request.user.id, date_placed__lte=datetime.datetime.now()).order_by(
            '-date_placed')