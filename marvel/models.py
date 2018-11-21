# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AA(models.Model):
    fk_parafer1 = models.ForeignKey('Parafer', models.DO_NOTHING, db_column='fk_parafer1', primary_key=True)
    fk_parafer2 = models.ForeignKey('Parafer', models.DO_NOTHING, db_column='fk_parafer2')

    class Meta:
        managed = False
        db_table = 'a_a'
        unique_together = (('fk_parafer1', 'fk_parafer2'),)


class Afili(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=2, decimal_places=0)
    nombre = models.CharField(max_length=30)
    ind_poder_aum = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    fk_lugar = models.ForeignKey('Lugar', models.DO_NOTHING, db_column='fk_lugar')

    class Meta:
        managed = False
        db_table = 'afili'


class CP(models.Model):
    fk_person = models.ForeignKey('Person', models.DO_NOTHING, db_column='fk_person', primary_key=True)
    fk_catego = models.ForeignKey('Catego', models.DO_NOTHING, db_column='fk_catego')

    class Meta:
        managed = False
        db_table = 'c_p'
        unique_together = (('fk_person', 'fk_catego'),)


class Catego(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=2, decimal_places=0)
    nombre = models.CharField(max_length=30)
    descrip = models.CharField(max_length=300, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'catego'


class Combat(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=2, decimal_places=0)
    fech = models.DateField()
    etp = models.DecimalField(max_digits=1, decimal_places=0)
    ganador = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    dura_min = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    fk_inscri1 = models.ForeignKey('Inscri', models.DO_NOTHING, db_column='fk_inscri1', blank=True, null=True)
    fk_inscri2 = models.ForeignKey('Inscri', models.DO_NOTHING, db_column='fk_inscri2', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'combat'


class Destr(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=2, decimal_places=0)
    nombre = models.CharField(max_length=30)
    descrip = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'destr'


class Even(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=2, decimal_places=0)
    fech_in = models.DateField()
    fech_fin = models.DateField()
    dura = models.DecimalField(max_digits=2, decimal_places=0)
    fk_lugar = models.ForeignKey('Lugar', models.DO_NOTHING, db_column='fk_lugar')

    class Meta:
        managed = False
        db_table = 'even'


class Habili(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=2, decimal_places=0)
    nombre = models.CharField(max_length=4)
    valor = models.DecimalField(max_digits=1, decimal_places=0)
    fk_person = models.ForeignKey('Person', models.DO_NOTHING, db_column='fk_person')

    class Meta:
        managed = False
        db_table = 'habili'
        unique_together = (('id', 'fk_person'),)


class Inscri(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=2, decimal_places=0)
    n_grupo = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    punto_etp1 = models.DecimalField(max_digits=2, decimal_places=0, blank=True, null=True)
    campeon = models.BooleanField(blank=True, null=True)
    descrip = models.CharField(max_length=300, blank=True, null=True)
    fk_person = models.ForeignKey('Person', models.DO_NOTHING, db_column='fk_person')
    fk_even = models.ForeignKey(Even, models.DO_NOTHING, db_column='fk_even')

    class Meta:
        managed = False
        db_table = 'inscri'


class Lugar(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=2, decimal_places=0)
    nombre = models.CharField(max_length=30)
    tipo_uni = models.CharField(max_length=1)
    tipo_geo = models.CharField(max_length=1, blank=True, null=True)
    fk_lugar = models.ForeignKey('self', models.DO_NOTHING, db_column='fk_lugar', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'lugar'


class PA(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=2, decimal_places=0)
    status = models.CharField(max_length=8)
    fk_afili = models.ForeignKey(Afili, models.DO_NOTHING, db_column='fk_afili')
    fk_person = models.ForeignKey('Person', models.DO_NOTHING, db_column='fk_person', blank=True, null=True)
    fk_personnocombat = models.ForeignKey('PersonNoCombat', models.DO_NOTHING, db_column='fk_personnocombat', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_a'


class PD(models.Model):
    fk_person = models.ForeignKey('Person', models.DO_NOTHING, db_column='fk_person', primary_key=True)
    fk_destr = models.ForeignKey(Destr, models.DO_NOTHING, db_column='fk_destr')

    class Meta:
        managed = False
        db_table = 'p_d'
        unique_together = (('fk_person', 'fk_destr'),)


class PPar(models.Model):
    fk_person = models.ForeignKey('Person', models.DO_NOTHING, db_column='fk_person', primary_key=True)
    fk_parafer = models.ForeignKey('Parafer', models.DO_NOTHING, db_column='fk_parafer')
    altur_armor = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)
    peso_armor = models.DecimalField(max_digits=3, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'p_par'
        unique_together = (('fk_person', 'fk_parafer'),)


class PPod(models.Model):
    fk_person = models.ForeignKey('Person', models.DO_NOTHING, db_column='fk_person', primary_key=True)
    fk_poder = models.ForeignKey('Poder', models.DO_NOTHING, db_column='fk_poder')

    class Meta:
        managed = False
        db_table = 'p_pod'
        unique_together = (('fk_person', 'fk_poder'),)


class Parafer(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=2, decimal_places=0)
    nombre = models.CharField(max_length=30)
    descrip = models.CharField(max_length=300)
    tipo = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'parafer'


class PerNoper(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=2, decimal_places=0)
    tipo_rel = models.CharField(max_length=30)
    tipo_paren = models.CharField(max_length=30, blank=True, null=True)
    fk_person = models.ForeignKey('Person', models.DO_NOTHING, db_column='fk_person')
    fk_person_rel = models.ForeignKey('Person', models.DO_NOTHING, db_column='fk_person_rel', blank=True, null=True)
    fk_noperson = models.ForeignKey('PersonNoCombat', models.DO_NOTHING, db_column='fk_noperson', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'per_noper'
        unique_together = (('id', 'fk_person'),)


class Person(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=2, decimal_places=0)
    nombre = models.CharField(max_length=30)
    tipo = models.CharField(max_length=2)
    tipo_iden = models.CharField(max_length=1)
    genero = models.CharField(max_length=1)
    altura = models.DecimalField(max_digits=3, decimal_places=0)
    color_ojo = models.CharField(max_length=30)
    biografia = models.CharField(max_length=300)
    nombre_real = models.CharField(max_length=30, blank=True, null=True)
    apellido_real = models.CharField(max_length=30, blank=True, null=True)
    edo_civil = models.CharField(max_length=1, blank=True, null=True)
    color_pelo = models.CharField(max_length=30, blank=True, null=True)
    fk_lugar = models.ForeignKey(Lugar, models.DO_NOTHING, db_column='fk_lugar')
    fk_univer = models.ForeignKey('Univer', models.DO_NOTHING, db_column='fk_univer')

    class Meta:
        managed = False
        db_table = 'person'


class PersonNoCombat(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=2, decimal_places=0)
    nombre = models.CharField(max_length=30)
    genero = models.CharField(max_length=1)
    fallece = models.BooleanField()
    nombre_real = models.CharField(max_length=30, blank=True, null=True)
    apellido_real = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'person_no_combat'


class Poder(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=2, decimal_places=0)
    nombre = models.CharField(max_length=30)
    descrip = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'poder'


class Univer(models.Model):
    id = models.DecimalField(primary_key=True, max_digits=2, decimal_places=0)
    nombre = models.CharField(max_length=30)
    descrip = models.CharField(max_length=300)

    class Meta:
        managed = False
        db_table = 'univer'
