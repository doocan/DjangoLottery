from django.db.utils import InterfaceError
from django.db.models.signals import post_save
from django.dispatch import receiver

from push.tasks import dlt_status_push
from dlt.models import DLT, ActDlt


@receiver(post_save, sender=ActDlt, dispatch_uid='dlt_status_handler')
def dlt_status_handler(sender, **kwargs):
    instance = kwargs.get('instance')

    num = instance.num
    dlts = DLT.objects.filter(num=num)

    if len(dlts):
        for dlt in dlts:
            dlt.status = _dlt_handler(instance, dlt)
            dlt.save()

        dlt_status_push.delay(num)


# @receiver(post_save, sender=DLT, dispatch_uid='dlt_status_handler_push')
# def dlt_status_push_handler(sender, **kwargs):
#     if not kwargs.get('created'):
#         print('=' * 40)
#         print(kwargs.get('update_fields'))
#         print(kwargs.get('created'))
#         print('=' * 40)


def _dlt_handler(instance, dlt):
    if not isinstance(dlt, DLT):
        raise InterfaceError('Argument dlt must be a instance of <DLT>.')

    front = set([dlt.a, dlt.b, dlt.c, dlt.d, dlt.e])
    back = set([dlt.f, dlt.g])
    front_act = set([instance.a, instance.b, instance.c, instance.d, instance.e])
    back_act = set([instance.f, instance.g])

    r1 = len(front & front_act)
    r2 = len(back & back_act)


    # if r1 == 5:
    #     if r2 == 2:
    #         return '1'
    #     elif r2 == 1:
    #         return '2'
    #     return '3'
    # elif r1 == 4:
    #     if r2 == 2:
    #         return '3'
    #     elif r2 == 1:
    #         return '4'
    #     return '5'
    # elif r1 == 3:
    #     if r2 == 2:
    #         return '4'
    #     elif r2 == 1:
    #         return '5'
    #     return '6'
    # elif r1 == 2:
    #     if r2 == 2:
    #         return '5'
    #     elif r2 == 1:
    #         return '6'
    # return 0


    if r1==5 and r2==2:
        return '1'
    if r1==5 and r2==1:
        return '2'
    if r1==5:
        return '3'
    if r1==4 and r2==2:
        return '3'
    if r1==4 and r2==1:
        return '4'
    if r1==3 and r2==2:
        return '4'
    if r1==4:
        return '5'
    if r1==3 and r1==1:
        return '5'
    if r1==2 and r2==2:
        return '5'
    if r1==3:
        return '6'
    if r1==2 and r2==1:
        return '6'
    if r1==1 and r2==2:
        return '6'
    if r2==2:
        return '6'

    return '0'
