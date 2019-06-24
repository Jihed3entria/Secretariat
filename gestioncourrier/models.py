from django.contrib.auth.models import AbstractUser
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.db import models
import computed_property

# Create your models here.
L = ((('l1', 'L1')), (('l2', 'L2')), (('l3', 'L3')))
M = (('m1', 'M1'), ('m2', 'M2'))
D = (('d1', 'D1'), ('d2', 'D2'), ('d3', 'D3'), ('d4', 'D4'), ('d5', 'D5'))
T = (('tous', 'Tous'),)
Parcours = L + M + D + T
objS = (('EDT', 'EDT'),
        ('demande derogation', 'Derogation'),
        ('demande equivalence', 'Demande Equivalence'),
        ('liste etudiants ', 'Liste Etudiants'),
        ('theme pfe ', 'Theme Pfe '),
        ('copie examen', 'Copies examens '),
        ('feuille de presence', 'Feuille Presence'),
        ('recours Csd', 'Recours CSD'),
        ('liste des exclus', 'Liste des exclus'),
        ('planning pedagogique', 'Planning pedagogique'),
        ('planning examens', 'Planning examen'),
        ('releve de note', 'Releve de note'),
        ('dossier inscription', 'Dossier inscription'),
        ('pv deliberation', 'PV deliberation'),
        ('fiche de voeux', 'Fiche de voeux'),
        ('attestation reinscription', 'Attestation reinscription'),
        ('conge academique', 'Conge academique'),
        ('pv correctif', 'PV correctif'),
        ('fiche de suivi', 'Fiche de Suivi'),
        ('attestation de reuissite', 'Attestation de reuissite'),
        ('pv csd', 'PV CSD'),
        ('pv cpc', 'PV CPC'),
        )
exp = (('etudiant', 'Etudiant'),
       ('enseignant', 'Enseignant'),
       ('responsable filiere', 'Responsable Filiere'),
       ('chef departement ', 'Chef Departement '),
       ('adjoint pedagogie ', 'Adjoint Pedagogie'),
       ('adjoint post-graduation ', 'Adjoint Post-graduation'),
       ('responsable domaine ', 'Responsable Domaine'),
       )
des = exp + (('responsable reprographie', 'Responsable Reprographie'),)


class Courrier(models.Model):
    objet = models.CharField(max_length=1502, default='choisir ', choices=objS)
    dateArrive = models.DateField(default=timezone.now)
    expediteur = models.CharField(max_length=100, choices=exp)
    nom = models.CharField(max_length=100, default='', blank=True)
    surnom = models.CharField(max_length=100, blank=True)
    parcours = models.CharField(max_length=10, choices=Parcours, default='l1')
    destinataire = models.CharField(max_length=100, choices=des)
    piece_jointe = models.FileField(blank=True)
    affichable = models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.objet + '-' + self.expediteur


parc = (('D1', 'd1'), ('D2', 'd2'))
parc += L + M


class justificatif(models.Model):
    dateAbsence = models.DateField(default=timezone.now)
    dateJustification = models.DateField(default=timezone.now)
    dateArrive = models.DateField(default=timezone.now)
    valide = computed_property.ComputedCharField(compute_from='fun', max_length=10)

    def fun(self):
        s = self.dateArrive.day - self.dateAbsence.day
        if self.dateAbsence == self.dateJustification:
            if self.dateAbsence.strftime("%A") == 'Thursday' or self.dateAbsence.strftime("%A") == 'Wednesday':
                s = s-2
            if s <= 2:
                 return 'Valide'

        return  'Non-Valide'

    nom = models.CharField(max_length=100, default='', blank=True)
    surnom = models.CharField(max_length=100, blank=True)
    parcours = models.CharField(max_length=10, choices=parc, default='l1')


objR = (('Tirage TD ','tirage td '),
        ('Tirage Examen','tirage examen'),
        ('Archivage Examen','archivage examen '),
        ('Emprunter Datashow','emprunter datashow'),
        ('Recuperer datashow','recuperer datashow '),
        ('Impression','impression'),
        )


class CourrierR(models.Model):
    objet = models.CharField(max_length=1502, default='choisir', choices=objR)
    dateArrive = models.DateField(default=timezone.now)
    expediteur = models.CharField(max_length=100, choices=exp)
    nom = models.CharField(max_length=100, default='', blank=True)
    surnom = models.CharField(max_length=100, blank=True)
    parcours = models.CharField(max_length=10, choices=Parcours, default='l1')
    Nbr = models.IntegerField(default=0)
