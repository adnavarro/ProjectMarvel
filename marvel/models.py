# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Afiliacion(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    nombre = models.CharField(max_length=30)
    id_lugar = models.ForeignKey('Lugar', models.DO_NOTHING, db_column='id_lugar')

    class Meta:
        managed = False
        db_table = 'afiliacion'


class Alias(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    nombre = models.CharField(max_length=30)
    id_personaje = models.ForeignKey('Personaje', models.DO_NOTHING, db_column='id_personaje')

    class Meta:
        managed = False
        db_table = 'alias'
        unique_together = (('id', 'id_personaje'),)


class Altura(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    centimetros = models.DecimalField(max_digits=65535, decimal_places=65535)
    id_personaje = models.ForeignKey('Personaje', models.DO_NOTHING, db_column='id_personaje', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'altura'


class Combate(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    duracion = models.DecimalField(max_digits=65535, decimal_places=65535)
    etapa = models.DecimalField(max_digits=65535, decimal_places=65535)
    id_personaje = models.ForeignKey('Personaje', models.DO_NOTHING, db_column='id_personaje')
    id_grupocombate = models.ForeignKey('GrupoCombate', models.DO_NOTHING, db_column='id_grupocombate')

    class Meta:
        managed = False
        db_table = 'combate'
        unique_together = (('id', 'id_personaje', 'id_grupocombate'),)


class Evento(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    fecha_in = models.DateField()
    fecha_fin = models.DateField()
    id_lugar = models.ForeignKey('Lugar', models.DO_NOTHING, db_column='id_lugar')

    class Meta:
        managed = False
        db_table = 'evento'


class FichaHabilidades(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    inteli = models.DecimalField(max_digits=65535, decimal_places=65535)
    fuerza = models.DecimalField(max_digits=65535, decimal_places=65535)
    veloc = models.DecimalField(max_digits=65535, decimal_places=65535)
    resiste = models.DecimalField(max_digits=65535, decimal_places=65535)
    proy_ener = models.DecimalField(max_digits=65535, decimal_places=65535)
    hab_combat = models.DecimalField(max_digits=65535, decimal_places=65535)
    id_personaje = models.ForeignKey('Personaje', models.DO_NOTHING, db_column='id_personaje')

    class Meta:
        managed = False
        db_table = 'ficha_habilidades'


class GrupoCombate(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    descripcion = models.CharField(max_length=100, blank=True, null=True)
    id_evento = models.ForeignKey(Evento, models.DO_NOTHING, db_column='id_evento')

    class Meta:
        managed = False
        db_table = 'grupo_combate'


class Lugar(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=1)
    id_lugar = models.ForeignKey('self', models.DO_NOTHING, db_column='id_lugar', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lugar'


class PA(models.Model):
    id_personaje = models.ForeignKey('Personaje', models.DO_NOTHING, db_column='id_personaje', primary_key=True)
    id_afiliacion = models.ForeignKey(Afiliacion, models.DO_NOTHING, db_column='id_afiliacion')

    class Meta:
        managed = False
        db_table = 'p_a'
        unique_together = (('id_personaje', 'id_afiliacion'),)


class PP(models.Model):
    id_personaje = models.ForeignKey('Personaje', models.DO_NOTHING, db_column='id_personaje', primary_key=True)
    id_profesion = models.ForeignKey('Profesion', models.DO_NOTHING, db_column='id_profesion')

    class Meta:
        managed = False
        db_table = 'p_p'
        unique_together = (('id_personaje', 'id_profesion'),)


class PerAl(models.Model):
    id_personaje1 = models.ForeignKey('Personaje', models.DO_NOTHING, db_column='id_personaje1', primary_key=True)
    id_personaje2 = models.ForeignKey('Personaje', models.DO_NOTHING, db_column='id_personaje2')

    class Meta:
        managed = False
        db_table = 'per_al'
        unique_together = (('id_personaje1', 'id_personaje2'),)


class PerEn(models.Model):
    id_personaje1 = models.ForeignKey('Personaje', models.DO_NOTHING, db_column='id_personaje1', primary_key=True)
    id_personaje2 = models.ForeignKey('Personaje', models.DO_NOTHING, db_column='id_personaje2')

    class Meta:
        managed = False
        db_table = 'per_en'
        unique_together = (('id_personaje1', 'id_personaje2'),)


class PerFam(models.Model):
    id_personaje1 = models.ForeignKey('Personaje', models.DO_NOTHING, db_column='id_personaje1', primary_key=True)
    id_personaje2 = models.ForeignKey('Personaje', models.DO_NOTHING, db_column='id_personaje2')

    class Meta:
        managed = False
        db_table = 'per_fam'
        unique_together = (('id_personaje1', 'id_personaje2'),)


class Personaje(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    nombre1 = models.CharField(max_length=50)
    nombre2 = models.CharField(max_length=50, blank=True, null=True)
    apellido = models.CharField(max_length=50)
    tipo = models.CharField(max_length=2)
    edo_civil = models.CharField(max_length=1)
    ojos = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'personaje'


class Peso(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    gramos = models.DecimalField(max_digits=65535, decimal_places=65535)
    id_personaje = models.ForeignKey(Personaje, models.DO_NOTHING, db_column='id_personaje', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'peso'


class Profesion(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    nombre = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'profesion'


class UP(models.Model):
    id_personaje = models.ForeignKey(Personaje, models.DO_NOTHING, db_column='id_personaje', primary_key=True)
    id_universo = models.ForeignKey('Universo', models.DO_NOTHING, db_column='id_universo')

    class Meta:
        managed = False
        db_table = 'u_p'
        unique_together = (('id_personaje', 'id_universo'),)


class Universo(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=65535, decimal_places=65535)
    nombre = models.CharField(max_length=30)
    descripcion = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'universo'
