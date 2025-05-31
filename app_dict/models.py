from django.db import models


class Catagory(models.Model):
    catagory_name=models.CharField(max_length=45,unique=True)
    description=models.TextField()

    def __str__(self):
        return self.catagory_name
    
    class Meta:
        db_table = 'catagory'
        managed = True
        verbose_name = 'catagory'
        verbose_name_plural = 'catagories'


class Dictionary(models.Model):
    word_ru=models.CharField(max_length=36,unique=True)
    word_uz_k=models.CharField(max_length=36,unique=True)
    word_uz_l=models.CharField(max_length=36,unique=True)
    word_en=models.CharField(max_length=36,unique=True)
    word_tr=models.CharField(max_length=36,unique=True)
    catagory=models.ForeignKey(Catagory,on_delete=models.CASCADE)

    def __str__(self):
        return self.word_uz_l
    
    class Meta:
        db_table = 'dictionary'
        managed = True
        verbose_name = 'Dictionary'
        verbose_name_plural = 'Dictionaries'