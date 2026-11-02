from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from cine.models import Genero, Pelicula
from noticias.models import Categoria
from .models import Reserva


class BootstrapFormMixin:
    def add_bootstrap(self):
        for field in self.fields.values():
            field.widget.attrs.setdefault('class', 'form-control')


class CategoriaForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nombre']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs); self.add_bootstrap()


class GeneroForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Genero
        fields = ['nombre']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs); self.add_bootstrap()


class ReservaForm(BootstrapFormMixin, forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['pelicula', 'fecha', 'cantidad']
        widgets = {'fecha': forms.DateInput(attrs={'type': 'date'}), 'cantidad': forms.NumberInput(attrs={'min': 1, 'max': 6})}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs); self.add_bootstrap()
    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if not 1 <= cantidad <= 6:
            raise forms.ValidationError('Selecciona entre 1 y 6 entradas.')
        return cantidad
    def clean_fecha(self):
        from django.utils import timezone
        fecha = self.cleaned_data['fecha']
        if fecha < timezone.localdate():
            raise forms.ValidationError('La fecha de función no puede estar en el pasado.')
        return fecha
    def clean(self):
        cleaned = super().clean()
        if cleaned.get('pelicula') and cleaned.get('fecha') and self.initial.get('usuario'):
            if Reserva.objects.filter(usuario=self.initial['usuario'], pelicula=cleaned['pelicula'], fecha=cleaned['fecha']).exists():
                raise forms.ValidationError('Ya tienes una reserva para esta película en esa fecha.')
        return cleaned


class CrearUsuarioForm(BootstrapFormMixin, UserCreationForm):
    email = forms.EmailField(required=True, label='Correo electrónico')
    perfil = forms.ChoiceField(choices=[('Administrador', 'Administrador'), ('Supervisor', 'Supervisor'), ('Administrativo', 'Administrativo')], label='Perfil')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs); self.add_bootstrap()
        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['class'] = 'form-control'
    def clean_email(self):
        email = self.cleaned_data['email'].strip().lower()
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError('Ya existe una cuenta con ese correo.')
        return email
    def save(self, commit=True):
        user = super().save(commit=commit)
        if commit:
            group = Group.objects.get(name=self.cleaned_data['perfil'])
            user.groups.set([group])
        return user
