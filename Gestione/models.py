from django.db import models
from django.contrib.auth.models import User


# Classe che definisce un produttore di una macchina
# Un esempio di produttore può essere NuovaSima, TecnoFerrari, Sacmi
class ProduttoreMacchine(models.Model):
    prod_nome = models.CharField(max_length=100)


class Reparto(models.Model):
    rep_nome = models.CharField(max_length=200)
    rep_stab = models.IntegerField(blank=True, null=True)


# Classe che definisce una tipologia di macchina
class TipoDiMacchina(models.Model):
    tipo_m_descrizione = models.CharField(max_length=300)
    tipo_m_versione = models.CharField(max_length=20)
    tipo_m_produttore = models.ForeignKey(ProduttoreMacchine, on_delete=models.CASCADE)

    class Meta:
        unique_together = ['tipo_m_descrizione', 'tipo_m_versione', 'tipo_m_produttore']


class Macchina(models.Model):
    macc_descrizione = models.CharField(max_length=300, blank=True, null=True)
    data_montaggio = models.DateField
    macc_reparto = models.ForeignKey(Reparto, on_delete=models.CASCADE)
    macc_tipo_macchina = models.ForeignKey(TipoDiMacchina, on_delete=models.CASCADE)


class Problema(models.Model):
    prob_descrizione = models.CharField(max_length=400)
    prob_data = models.DateField(auto_now=True)
    prob_turno = models.CharField(max_length=15)


class CategoriaProblema(models.Model):
    cat_prob_tag = models.CharField(max_length=100)


class DettaglioProblemaCategoria(models.Model):
    det_problema = models.ForeignKey(Problema, on_delete=models.CASCADE)
    det_categoria = models.ForeignKey(CategoriaProblema, on_delete=models.CASCADE)


class Soluzione(models.Model):
    sol_descrizione = models.CharField(max_length=500)
    sol_is_risolto = models.BooleanField(default=True)
    sol_user = models.ForeignKey(User, on_delete=models.CASCADE)
    sol_problema = models.ForeignKey(Problema, on_delete=models.CASCADE)

