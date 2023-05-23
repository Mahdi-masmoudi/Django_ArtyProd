
from django.http import HttpResponse
from .models import Personnel, Projet, ProjetUtilisateur
from .models import Service
from .models import Equipe
from django.contrib.auth.models import User

from django.shortcuts import get_object_or_404, render, redirect
from .forms import DemandeProjetForm, PersonnelForm, ProjetForm, ProjetUtilisateurForm
from .forms import ServiceForm
from .forms import EquipeForm
from django.contrib.auth.decorators import login_required

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.core.mail import send_mail
from django.http import HttpResponseRedirect

from .models import Detail
from .forms import DetailForm

from django.shortcuts import render, redirect
from .forms import DetailForm


def projets_acheves(request):
    projets = Projet.objects.filter(acheve='o')
    return render(request, 'user/Portfolio.html', {'projets': projets})


@login_required
def projets_non_acheves(request):
    projets = Projet.objects.filter(acheve='n')
    return render(request, 'user/Portfolio_non_acheves.html', {'projets': projets})


def ajouter_details(request):
    form = DetailForm()
    if request.method == 'POST':
        form = DetailForm(request.POST)
        if form.is_valid():
            form.save()
    context = {'form': form}
    return render(request, 'ajouter_details.html', context)


def detail_list(request):
    details = Detail.objects.all()
    return render(request, 'detail_list.html', {'details': details})


@login_required
def EquipeList(request):
    Equipes = Equipe.objects.all()
    return render(request, 'user/EquipeList.html', {'Equipes': Equipes})


def ajouter_equipe(request):
    if request.method == 'POST':
        form = EquipeForm(request.POST)
        if form.is_valid():
            Equipe = form.save()
            return redirect('AddProjet')
            # Effectuez ici toute autre opération souhaitée après l'ajout de l'équipe
    else:
        form = EquipeForm()
    return render(request, 'user/ajouter_equipe.html', {'form': form})


def portfolio(request):
    projets = Projet.objects.all()
    context = {'projets': projets}
    return render(request, 'user/Portfolio.html', context)


def AjouterProjet(request):
    if request.method == "POST":
        form = ProjetForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('portf')
    else:
        form = ProjetForm()
    service = Projet.objects.all()
    return render(request, 'user/AjouterProjet.html', {'Projet': Projet, 'form': form})


def Projet_det(request, id):
    f = get_object_or_404(Projet, id=id)
    return render(request, 'user/viewProjet.html', {'Projet': f})


def edit_Projet(request, id):
    p = Projet.objects.get(id=id)
    form = ProjetForm(instance=p)

    if request.method == 'POST':
        form = ProjetForm(request.POST, instance=p)
        if form.is_valid():
            form.save()
            return redirect('portf')

    return render(request, 'user/updateProjet.html', {'form': form, 'Projet': p})


def deleteProjet(request, id):
    post = get_object_or_404(Projet, pk=id)
    context = {'post': post}

    if request.method == 'GET':
        return render(request, 'user/deleteProjet.html', context)
    elif request.method == 'POST':
        post.delete()
        messages.success(request,  'The post has been deleted successfully.')
        return redirect('portf')

#
#


@login_required
def listService(request):
    Services = Service.objects.all()
    context = {'Services': Services}
    return render(request, 'user/service.html', context)


def AjouterService(request):
    if request.method == "POST":
        form = ServiceForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listser')
    else:
        form = ServiceForm()
    service = Service.objects.all()
    return render(request, 'user/AjouterSer.html', {'service': service, 'form': form})


def Service_det(request, id):
    f = get_object_or_404(Service, id=id)
    return render(request, 'user/viewService.html', {'service': f})


def edit_Service(request, id):
    p = Service.objects.get(id=id)
    form = ServiceForm(instance=p)

    if request.method == 'POST':
        form = ServiceForm(request.POST, instance=p)
        if form.is_valid():
            form.save()
            return redirect('listser')

    return render(request, 'user/updateService.html', {'form': form, 'Service': p})


def deleteService(request, id):
    post = get_object_or_404(Service, pk=id)
    context = {'post': post}

    if request.method == 'GET':
        return render(request, 'user/deleteService.html', context)
    elif request.method == 'POST':
        post.delete()
        messages.success(request,  'The post has been deleted successfully.')
        return redirect('listser')


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(
                request, f'Coucou {username}, Votre compte a été créé avec succès !')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


@login_required
def contact_form(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')

        # Envoyer l'e-mail
        send_mail(subject, f"Nom : {name}\nE-mail : {email}\n{message}", email,  # L'adresse e-mail de l'expéditeur
                  # L'adresse e-mail du destinataire
                  ['mahdi.masmoudi92@gmail.com'],
                  fail_silently=False,
                  )

        # Redirection après l'envoi de l'e-mail
        # Remplacez '/success/' par l'URL souhaitée après l'envoi du formulaire
        return HttpResponseRedirect('/success/')

    return render(request, 'user/contact_form.html')


@login_required
def contact(request):
    return render(request, 'user/contact_form.html')


@login_required
def success(request):
    return render(request, 'user/success.html')


def equipe_create(request):
    if request.method == 'POST':
        form = EquipeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listequipe')
    else:
        form = EquipeForm()
    equipe = Equipe.objects.all()
    return render(request, 'user/ajouter_equipe.html', {'equipe': equipe, 'form': form})


def edit_team(request, team_id):
    team = get_object_or_404(Equipe, id=team_id)
    if request.method == 'POST':
        form = EquipeForm(request.POST, instance=team)
        if form.is_valid():
            form.save()
            return redirect('listequipe')
    else:
        form = EquipeForm(instance=team)
    return render(request, 'user/updateEquipe.html', {'form': form})


def delete_team(request, team_id):
    team = get_object_or_404(Equipe, id=team_id)
    if request.method == 'POST':
        team.delete()
        return redirect('listequipe')
    return render(request, 'equipe/delete_equipe.html', {'team': team})


def listPerson(request):
    listp = Personnel.objects.all()
    return render(request, 'user/personnel.html', {'listp': listp})


def personnel_create(request):
    if request.method == 'POST':
        form = PersonnelForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('listPerson')
    else:
        form = PersonnelForm()
    personne = Personnel.objects.all()
    return render(request, 'user/ajouterPersonne.html', {'personne': personne, 'form': form})


def personnel_edit(request, id):
    post = get_object_or_404(Personnel, id=id)
    if request.method == 'GET':
        context = {'form': PersonnelForm(instance=post), 'id': id}
        return render(request, 'user/editPersonnel.html', context)
    elif request.method == 'POST':
        form = PersonnelForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            return redirect('listPerson')
        else:
            return render(request, 'user/editPersonnel.html', {'form': form})


def personnel_delete(request, id):
    personnel = get_object_or_404(Personnel, pk=id)
    context = {'personnel': personnel}
    if request.method == 'GET':
        return render(request, 'user/deletePersonnel.html', context)
    elif request.method == 'POST':
        personnel.delete()
        return redirect('listPerson')


def edit_personne(request, id):
    personnel = get_object_or_404(Personnel, id=id)
    return render(request, 'user/personnel_detail.html', {'personnel': personnel})


def editPersonnel(request, id):
    p = Personnel.objects.get(id=id)
    form = PersonnelForm(instance=p)

    if request.method == 'POST':
        form = PersonnelForm(request.POST, instance=p)
        if form.is_valid():
            form.save()
            return redirect('listPerson')

    return render(request, 'user/updatepersonnel.html', {'form': form, 'Personnel': p})


###############################################


def projet_utilisateur_list(request):
    projetutilisateurs = ProjetUtilisateur.objects.filter(utilisateur=request.user)
    context = {'projetutilisateurs': projetutilisateurs}
    return render(request, 'user/projet_utilisateur_list.html', context)
def ajouter_projet_utilisateur(request):
    if request.method == 'POST':
        form = ProjetUtilisateurForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('projet_utilisateurlist')
    else:
        form = ProjetUtilisateurForm()
    return render(request, 'user/ajouter_projet_utilisateur.html', {'form': form})
