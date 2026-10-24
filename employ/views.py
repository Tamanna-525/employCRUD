# from rest_framework import viewsets
# from .models import employ
# from .serializers import employSerializer


# class employViewSet(viewsets.ModelViewSet):
#     queryset =employ.objects.all().order_by('id')
#     serializer_class = employSerializer

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.views.decorators.http import require_POST

from .models import employ
from .forms import EmployForm, RegisterForm


def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('employ_list')
        else:
            print(form.errors)
    else:
        form = RegisterForm()

    return render(request, 'employ/register.html', {'form': form})


class UserLoginView(LoginView):
    template_name = 'employ/login.html'
    redirect_authenticated_user = True


class UserLogoutView(LogoutView):
    pass


@login_required
def employ_list(request):
    employs = employ.objects.all().order_by('id')
    print(employs)
    return render(
        request,
        'employ/employ_list.html',
        {'employs': employs}
    )


@login_required
def employ_add(request):
    form = EmployForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('employ_list')

    return render(request, 'employ/employ_form.html', {
        'form': form,
        'title': 'Add Employee'
    })


@login_required
def employ_edit(request, pk):
    employe = get_object_or_404(employ, pk=pk)
    form = EmployForm(request.POST or None, instance=employe)

    if request.method == 'POST' and form.is_valid():
        form.save()
        return redirect('employ_list')

    return render(request, 'employ/employ_form.html', {
        'form': form,
        'title': 'Edit Employee'
    })


@login_required
def employ_delete(request, pk):
    employe = get_object_or_404(employ, pk=pk)

    if request.method == 'POST':
        employe.delete()
        return redirect('employ_list')

    return render(request, 'employ/employ_confirm_delete.html', {
        'employ': employe
    })