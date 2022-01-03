from django.db import models

#model for storing information about user and his/her referral link
class botUser(models.Model):
    referral_id = models.CharField(max_length=8)
    user_name = models.CharField(max_length=50)

    class Meta:
        db_table = "bot_user"

#model for storing information about frequency of using incorrect referral link by user
class incorrectLink(models.Model):
    referral_id = models.CharField(max_length=8)
    chat_id = models.IntegerField(default=-1)
    frequency = models.IntegerField()

    class Meta:
        db_table = "incorrect_link"

