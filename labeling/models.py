from django.db import models
from django.utils import timezone
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    qQuestion_ID = models.IntegerField(primary_key=True, unique=True)
    qQuestion_User = models.CharField(max_length=100)
    qOriginal_Message = models.TextField(max_length=5000)

    tRelationship = models.BooleanField(default=False)
    tWork = models.BooleanField(default=False)
    tSchool = models.BooleanField(default=False)
    tMarriage = models.BooleanField(default=False)
    tFamily = models.BooleanField(default=False)
    tLife = models.BooleanField(default=False)
    tMental = models.BooleanField(default=False)
    tPhysiology = models.BooleanField(default=False)
    tAddiction = models.BooleanField(default=False)
    tLawsandCrime = models.BooleanField(default=False)
    tPassedAway = models.BooleanField(default=False)

    
    eRelationship_1 = models.BooleanField(default=False) #小寫t表示topic e表示event
    eRelationship_2 = models.BooleanField(default=False)
    eRelationship_3 = models.BooleanField(default=False)
    eRelationship_4 = models.BooleanField(default=False)
    eWork_1 = models.BooleanField(default=False)
    eWork_2 = models.BooleanField(default=False)
    eWork_3 = models.BooleanField(default=False)
    eWork_4 = models.BooleanField(default=False)
    eWork_5 = models.BooleanField(default=False)
    eWork_6 = models.BooleanField(default=False)
    eSchool_1 = models.BooleanField(default=False)
    eSchool_2 = models.BooleanField(default=False)
    eSchool_3 = models.BooleanField(default=False)
    eSchool_4 = models.BooleanField(default=False)
    eSchool_5 = models.BooleanField(default=False)
    eSchool_6 = models.BooleanField(default=False)
    eMarriage_1 = models.BooleanField(default=False)
    eMarriage_2 = models.BooleanField(default=False)
    eMarriage_3 = models.BooleanField(default=False)
    eMarriage_4 = models.BooleanField(default=False)
    eFamily_1 = models.BooleanField(default=False)
    eFamily_2 = models.BooleanField(default=False)
    eFamily_3 = models.BooleanField(default=False)
    eFamily_4 = models.BooleanField(default=False)
    eFamily_5 = models.BooleanField(default=False)
    eFamily_6 = models.BooleanField(default=False)
    eLife_1 = models.BooleanField(default=False)
    eLife_2 = models.BooleanField(default=False)
    eLife_3 = models.BooleanField(default=False)
    eLife_4 = models.BooleanField(default=False)
    eLife_5 = models.BooleanField(default=False)
    eLife_6 = models.BooleanField(default=False)
    eLife_7 = models.BooleanField(default=False)
    eMental_1 = models.BooleanField(default=False)
    eMental_2 = models.BooleanField(default=False)
    eMental_3 = models.BooleanField(default=False)
    eMental_4 = models.BooleanField(default=False)
    eMental_5 = models.BooleanField(default=False)
    eMental_6 = models.BooleanField(default=False)
    ePhysiology_1 = models.BooleanField(default=False)
    ePhysiology_2 = models.BooleanField(default=False)
    ePhysiology_3 = models.BooleanField(default=False)
    ePhysiology_4 = models.BooleanField(default=False)
    ePhysiology_5 = models.BooleanField(default=False)
    eAddiction_1 = models.BooleanField(default=False)
    eAddiction_2 = models.BooleanField(default=False)
    eAddiction_3 = models.BooleanField(default=False)
    eAddiction_4 = models.BooleanField(default=False)
    eAddiction_5 = models.BooleanField(default=False)
    eAddiction_6 = models.BooleanField(default=False)
    eLawsandCrime_1 = models.BooleanField(default=False)
    eLawsandCrime_2 = models.BooleanField(default=False)
    eLawsandCrime_3 = models.BooleanField(default=False)
    eLawsandCrime_4 = models.BooleanField(default=False)
    eLawsandCrime_5 = models.BooleanField(default=False)
    eLawsandCrime_6 = models.BooleanField(default=False)
    eLawsandCrime_7 = models.BooleanField(default=False)
    ePassedAway_1 = models.BooleanField(default=False)
    ePassedAway_2 = models.BooleanField(default=False)
    ePassedAway_3 = models.BooleanField(default=False)
    ePassedAway_4 = models.BooleanField(default=False)
    ePassedAway_5 = models.BooleanField(default=False)

    qSkip = models.BooleanField(default=False)
    QUES_FILTER = (
        (0, "Save"),
        (1, 'Discuss'),
        (2, 'Trash')
    )
    sQuestion_Filter = models.PositiveSmallIntegerField(null=True, choices=QUES_FILTER, default=0)




    def __str__(self):
        return 'id: {}'.format(self.qQuestion_ID)

class Task(models.Model):
    tUser = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    tQuestion = models.ForeignKey(Question, on_delete=models.CASCADE)
    tdone = models.BooleanField(default=False)

    def __str__(self):
        return "{}, {}".format(self.tUser.username, self.tQuestion)