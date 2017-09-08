from django.views import generic
from braces import views

from django.core.urlresolvers import reverse_lazy

from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from . import forms


class HomePageView(generic.TemplateView):
    """
        Class based view for Home Page
    """

    template_name = 'home.html'

    active_link = "Home"
    hide_application_links = True


class SignUpView(views.AnonymousRequiredMixin, views.FormValidMessageMixin, generic.CreateView):

    form_class = forms.RegistrationForm
    form_valid_message = 'Thanks for registration! You are ready to log in!'
    model = User
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')


class LoginView(views.AnonymousRequiredMixin, views.FormValidMessageMixin, generic.FormView):

    form_class = forms.LoginForm
    form_valid_message = 'Successfully logged in!'
    template_name = 'accounts/login.html'
    # redirect to login page after registration
    success_url = reverse_lazy('home')

    def form_valid(self, form):

        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user = authenticate(username=username, password=password)

        if user is not None and user.is_active:
            login(self.request, user)
            return super(LoginView, self).form_valid(form)
        else:
            return self.form_invalid(form)


class LogOutView(views.LoginRequiredMixin, views.FormValidMessageMixin, generic.RedirectView):

    url = reverse_lazy('home')
    # form_valid_message doesn't work on RedirectView
    form_valid_message = 'Successfully logged out!'

    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogOutView, self).get(request, *args, **kwargs)