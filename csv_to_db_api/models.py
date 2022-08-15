from django.db import models

# Create your models here.


class Report(models.Model):
    crime_id = models.IntegerField('Идентификатор преступления', unique=True)
    original_crime = models.CharField('Название инцидента', max_length=255, blank=True, null=True)
    report_date = models.DateTimeField('Дата поступления жалобы', db_index=True, blank=True)
    call_date = models.DateTimeField('Дата звонка', blank=True)
    offense_date = models.DateTimeField('Дата правонарушения', blank=True)
    call_time = models.TimeField('Время звонка', blank=True)
    call_date_time = models.DateTimeField('Дата и время звонка', blank=True)
    disposition = models.TextField('Описание', blank=True, null=True)
    address = models.CharField('Адрес', max_length=255, blank=True, null=True)
    city = models.CharField('Город', max_length=50, blank=True, null=True)
    state = models.CharField('Штат', max_length=50, blank=True, null=True)
    agency_id = models.IntegerField('id Отдела')
    address_type = models.CharField('Тип адреса', max_length=255, blank=True, null=True)
    common_location = models.CharField('Расположение', max_length=255, null=True)

    class Meta:
        ordering = ['report_date']
        verbose_name = 'Сообщение о инциденте'
        verbose_name_plural = 'Инциденты'

    def __str__(self):
        if self.original_crime:
            return self.original_crime
        return self.crime_id


class ReportDocument(models.Model):
    file = models.FileField(upload_to='files/')

    class Meta:
        verbose_name = 'CSV файл'
        verbose_name_plural = 'Файлы'