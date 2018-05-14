from django.db import models
from django.db.utils import InterfaceError


class DLT(models.Model):
    STATUS = (
        ('1', '一等奖'),
        ('2', '二等奖'),
        ('3', '三等奖'),
        ('4', '四等奖'),
        ('5', '五等奖'),
        ('6', '六等奖'),
        ('un', '待开奖'),
        ('0', '未中奖'),
    )
    a = models.IntegerField()
    b = models.IntegerField()
    c = models.IntegerField()
    d = models.IntegerField()
    e = models.IntegerField()
    f = models.IntegerField()
    g = models.IntegerField()
    num = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=2, choices=STATUS, default='un')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '大乐透'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'<DLT: {self.num}>'


class ActDlt(models.Model):
    a = models.IntegerField()
    b = models.IntegerField()
    c = models.IntegerField()
    d = models.IntegerField()
    e = models.IntegerField()
    f = models.IntegerField()
    g = models.IntegerField()
    num = models.IntegerField()
    published = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = '大乐透开奖'
        verbose_name_plural = verbose_name

    def __str__(self):
        return f'<ActDlt: {self.num} on {self.published}>'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        self.dlt_handle()

    def dlt_handle(self):
        dlt_list = DLT.objects.filter(num=self.num)

        if len(dlt_list):
            for dlt in dlt_list:
                dlt.status = self._dlt_handle(dlt)
                dlt.save()
                
    def _dlt_handle(self, dlt):
        if not isinstance(dlt, DLT):
            raise InterfaceError('Argument dlt must be a instance of <DLT>.')

        front = set([dlt['a'], dlt['b'], dlt['c'], dlt['d'], dlt['e']])
        back = set(dlt['f'], dlt['g'])
        front_act = set([self['a'], self['b'], self['c'], self['d'], self['e']])
        back_act = set([self['f'], self['g']])

        r1 = len(front & front_act)
        r2 = len(back & back_act)

        if r1==5 and r2==2:
            return '1'
        elif r1==5 and r2==1:
            return '2'
        elif r1==5:
            return '3'
        elif r1==4 and r2==2:
            return '3'
        elif r1==4 and r2==1:
            return '4'
        elif r1==3 and r2==2:
            return '4'
        elif r1==4:
            return '5'
        elif r1==3 and r1==1:
            return '5'
        elif r1==2 and r2==2:
            return '5'
        elif r1==3:
            return '6'
        elif r1==2 and r2==1:
            return '6'
        elif r1==1 and r2==2:
            return '6'
        elif r2==2:
            return '6'
        else:
            return '0'
