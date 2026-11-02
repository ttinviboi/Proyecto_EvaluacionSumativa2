from django.contrib.auth import views as auth_views
from django.urls import include, path
from gestion.views import PortalLoginView

urlpatterns = [
    path('', include('gestion.urls')),
    path('cuentas/ingresar/', PortalLoginView.as_view(), name='login'),
    path('cuentas/salir/', auth_views.LogoutView.as_view(), name='logout'),
    path('cuentas/recuperar/', auth_views.PasswordResetView.as_view(
        template_name='registration/password_reset_form.html',
        email_template_name='registration/password_reset_email.html',
        subject_template_name='registration/password_reset_subject.txt',
        success_url='/cuentas/recuperar/enviado/',
    ), name='password_reset'),
    path('cuentas/recuperar/enviado/', auth_views.PasswordResetDoneView.as_view(
        template_name='registration/password_reset_done.html'), name='password_reset_done'),
    path('cuentas/recuperar/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='registration/password_reset_confirm.html',
        success_url='/cuentas/recuperar/completado/'), name='password_reset_confirm'),
    path('cuentas/recuperar/completado/', auth_views.PasswordResetCompleteView.as_view(
        template_name='registration/password_reset_complete.html'), name='password_reset_complete'),
    path('noticias/', include('noticias.urls')),
    path('cine/', include('cine.urls')),
]
