from django.core.exceptions import ObjectDoesNotExist
from . import models
from django.http import JsonResponse, HttpResponseNotFound, HttpResponse

#view for getting user's identifier and name by his/her str:referral_link
def getByLink(request, referral_id):
    try:
        object = models.botUser.objects.filter(referral_id=referral_id)
        if object.exists():
            return JsonResponse({'id': object[0].pk, 'name': object[0].user_name})
    except ObjectDoesNotExist:
        pass
    return  JsonResponse({'id': -1, 'name': ''})

#view for getting frequency of using str:referral_id by user(int:chat_id)
def frequencyByUser(request, chat_id, referral_id):
    try:
        object = models.incorrectLink.objects.filter(chat_id=chat_id, referral_id=referral_id)
        if object.exists():
            return JsonResponse({'amount': object[0].frequency})
    except ObjectDoesNotExist:
        pass
    return JsonResponse({'amount': 0})

#view for increasing amount of using str:referral_id by user(int:chat_id) in db
def frequencyByUserIncrease(request, chat_id, referral_id):
    try:
        obj = models.incorrectLink.objects.filter(chat_id=chat_id, referral_id=referral_id)
        if obj.exists():
            obj = obj[0]
            obj.frequency += 1
        else:
            obj = models.incorrectLink(chat_id=chat_id, referral_id=referral_id, frequency=0)
        obj.save()
    except ObjectDoesNotExist:
        return HttpResponseNotFound()
    return HttpResponse('')
