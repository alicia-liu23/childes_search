from django.db import models

# Create your models here.
class Transcript(models.Model):
    name = models.CharField(max_length=200)
    SES_CHOICES = [
        ('PRO', 'Professional Class'),
        ('MID', 'Middle Class'),
        ('WORK', 'Working Class'),
        ('WEL', 'Welfare Class'),
    ]
    ses = models.CharField(choices=SES_CHOICES, max_length = 4)
    child_age = models.CharField(max_length = 10)
    GENDER_CHOICES = [
        ('male', 'male'), 
        ('female', 'female'),
        ('na', 'na'),
    ]
    child_gender = models.CharField(choices=GENDER_CHOICES, max_length=6, default='MALE')
    corpus = models.CharField(max_length=200)
    RACE_CHOICES = [
        ('White', 'White'), 
        ('Black', 'Black'), 
        ('na', 'na'),
        ('Other', 'Other')
    ]
    race = models.CharField(choices=RACE_CHOICES, max_length = 5) 
    url = models.URLField(max_length = 200, default = 'example.html')
    tot_utts = models.IntegerField(default = 0) 
    mlu_utts = models.IntegerField(default = 0) 
    mlu_words = models.DecimalField(max_digits = 7, decimal_places = 3, default=0.0)
    mlu_morphs = models.DecimalField(max_digits = 7, decimal_places = 3, default=0.0) 
    freq_ttr = models.DecimalField(max_digits = 7, decimal_places = 3, default=0.0) 
    percent_nouns = models.DecimalField(max_digits = 7, decimal_places = 3, default=0.0) 
    percent_verbs = models.DecimalField(max_digits = 7, decimal_places = 3, default=0.0) 
    percent_adjs = models.DecimalField(max_digits = 7, decimal_places = 3, default=0.0) 
    percent_adv = models.DecimalField(max_digits = 7, decimal_places = 3, default=0.0) 
    percent_prep = models.DecimalField(max_digits = 7, decimal_places = 3, default=0.0)

    def __str__(self):
        return self.name


class Mother(models.Model):
    name = models.CharField(max_length=200)
    corpus = models.CharField(max_length=200)
    tot_utts = models.IntegerField(default = 0) 
    mlu_utts = models.IntegerField(default = 0) 
    mlu_words = models.DecimalField(max_digits = 7, decimal_places = 3, default=0.0)
    mlu_morphs = models.DecimalField(max_digits = 7, decimal_places = 3, default=0.0) 
    freq_ttr = models.DecimalField(max_digits = 7, decimal_places = 3, default=0.0) 
    percent_nouns = models.DecimalField(max_digits = 7, decimal_places = 3, default=0.0) 
    percent_verbs = models.DecimalField(max_digits = 7, decimal_places = 3, default=0.0) 
    percent_adjs = models.DecimalField(max_digits = 7, decimal_places = 3, default=0.0) 
    percent_adv = models.DecimalField(max_digits = 7, decimal_places = 3, default=0.0) 
    percent_prep = models.DecimalField(max_digits = 7, decimal_places = 3, default=0.0)

    def __str__(self):
        return self.name
