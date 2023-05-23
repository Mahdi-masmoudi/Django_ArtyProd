from django.urls import path
from . import views
from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
urlpatterns = [
     path('projets/', views.projet_utilisateur_list, name='projet_utilisateurlist'),
    path('projetsajouter/', views.ajouter_projet_utilisateur, name='ajouterprojetutilisateur'),



    path('contact/', views.contact_form, name='contact_form'),
    path('Equipe/', views.EquipeList, name='equipe'),
    path('AjouterProjet/', views.AjouterProjet, name='AddProjet'),
    path('deleteProjet/<int:id>/', views.deleteProjet, name='deleteProjet'),
    path('viewProjet/<int:id>/view', views.Projet_det, name='projet_det'),
    path('Projet_det', views.Projet_det, name='Projet_det'),
    path('updateProjet/<int:id>/edit/', views.edit_Projet, name='edit_Projet'),

    path('', views.projets_acheves, name='portf'),
    path('projets-non-acheves/', views.projets_non_acheves,
         name='Projets_non_acheves'),


    path('details/', views.detail_list, name='detail_list'),
    path('ajouterdetails/', views.ajouter_details, name='ajouter_details'),


    path('ajouterequipe/', views.ajouter_equipe, name='ajouter_equipe'),
    path('listService/', views.listService, name='listser'),
    path('AjouterService/', views.AjouterService, name='AddService'),
    path('deleteService/<int:id>/', views.deleteService, name='deleteService'),
    path('viewService/<int:id>/view', views.Service_det, name='service_det'),
    path('Service_det', views.Service_det, name='service_det'),
    path('updateService/<int:id>/edit/',
         views.edit_Service, name='edit_Service'),

    path('listequipe/', views.EquipeList, name='listequipe'),
    path('equipe_create/', views.equipe_create, name='equipe_create'),

    path('edit_team/', views.edit_team, name='edit_team'),
    path('delete_team/', views.delete_team, name='delete_team'),

    path('listq/<int:team_id>/edit', views.edit_team, name='edit_team'),
    path('listq/<int:team_id>/Delete', views.delete_team, name='delete_team'),

    path('register/', views.register, name='register'),

    path('contact/', views.contact, name='cont'),
    path('register/', views.register, name='register'),
    path('success/', views.success, name='success'),

    path('listPerson/', views.listPerson, name='listPerson'),
    path('personnel_create/', views.personnel_create, name='personnel_create'),

    path('personnel_edit/', views.personnel_edit, name='personnel_edit'),
    path('listpe/edit_personnel/<int:id>/',
         views.personnel_edit, name='personnel_edit'),

    path('personnel_delete/<int:id>',
         views.personnel_delete, name='personnel_delete'),

    path('editpersonne/', views.edit_personne, name='view_personne'),
    path('listpe/<int:id>/view_personnel',
         views.edit_personne, name='view_personne'),
    path('updatePersonne/<int:id>', views.editPersonnel, name='Updateper'),
    path('password-reset/', PasswordResetView.as_view(
        template_name='user/password/password_reset.html'), name='password-reset'),
    path('password-reset/done/', PasswordResetDoneView.as_view(
        template_name='user/password/password_reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', PasswordResetConfirmView.as_view(
        template_name='user/password/password_reset_confirm.html'), name='password_reset_confirm'),
    path('password-reset-complete/', PasswordResetCompleteView.as_view(
        template_name='user/password/password_reset_complete.html'), name='password_reset_complete'),

]
