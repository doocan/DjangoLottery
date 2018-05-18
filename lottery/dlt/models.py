from django.db import models


class Tag(models.Model):
    num = models.IntegerField()

    def __str__(self):
        return f"<Tag: {self.num}>"


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
        ordering = ['-created']
        # verbose_name = '大乐透'
        # verbose_name_plural = verbose_name

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
        pass
        # verbose_name = '大乐透开奖'
        # verbose_name_plural = verbose_name

    def __str__(self):
        return f'<ActDlt: {self.num} on {self.published}>' 
