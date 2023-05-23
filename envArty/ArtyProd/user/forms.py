from datetime import date
from django import forms

from .models import Detail, Personnel, Projet, ProjetUtilisateur
from .models import Service
from .models import Equipe


from django.contrib.auth.models import User
from django.forms import CheckboxSelectMultiple, ModelForm, ModelMultipleChoiceField
from django.contrib.auth.forms import UserCreationForm


class ProjetForm(ModelForm):
    class Meta:
        model = Projet
        fields = "__all__"


class DetailForm(ModelForm):
    class Meta:
        model = Detail
        fields = "__all__"


class ProjetForm(ModelForm):
    class Meta:
        model = Projet
        fields = "__all__"


class PersonnelForm(ModelForm):
    class Meta:
        model = Personnel
        fields = "__all__"


class ServiceForm(ModelForm):
    class Meta:
        model = Service
        fields = "__all__"


class EquipeForm(ModelForm):
    personnels = ModelMultipleChoiceField(
        queryset=Personnel.objects.all(), widget=CheckboxSelectMultiple)

    class Meta:
        model = Equipe
        fields = "__all__"


class ProjetUtilisateurForm(forms.ModelForm):
    projet = forms.ModelMultipleChoiceField(queryset=Projet.objects.filter(date_debut=date.today()), widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = ProjetUtilisateur

        fields = "__all__"


class UserRegistrationForm(UserCreationForm):
    first_name = forms.CharField(label='Prénom')
    last_name = forms.CharField(label='Nom')
    number = forms.CharField(label='number')
    email = forms.EmailField(label='Adresse e-mail')

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + \
            ('first_name', 'last_name', 'number', 'email')


class DemandeProjetForm(forms.ModelForm):
    class Meta:
        model = Projet
        fields = ['libellai', 'description', 'img_projet',
                  'date_debut', 'date_fin', 'Service', 'equipe']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Peupler le champ équipe avec toutes les équipes disponibles
        self.fields['equipe'].queryset = Equipe.objects.all()

    def clean(self):
        cleaned_data = super().clean()
        date_debut = cleaned_data.get('date_debut')
        date_fin = cleaned_data.get('date_fin')

        if date_debut and date_fin and date_debut > date_fin:
            raise forms.ValidationError(
                "La date de début doit être antérieure à la date de fin.")
