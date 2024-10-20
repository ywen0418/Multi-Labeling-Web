from django import forms
from .models import Question, Task
from django.contrib.auth.models import User


class LabelForm(forms.ModelForm):
    # fOriginal_Question = forms.CharField()
    # fQuery = forms.CharField()
    # fQuestion_Type = forms.IntegerField()
    class Meta:
        model = Question
        fields = [
                    'qOriginal_Message'
                    ]
        labels = {
                    'qOriginal_Message': (''),
        }
        widgets = {
            'qOriginal_Message': forms.Textarea(attrs={'class': 'form-control', 'style':'height:350px;width:100%;font-size:20px;font-weight:bold;'}),
        }

class SelectForm(forms.ModelForm):
    # fOriginal_Question = forms.CharField()
    # fQuery = forms.CharField()
    # fQuestion_Type = forms.IntegerField()
    class Meta:
        model = Question
        fields = ['eRelationship_1','eRelationship_2','eRelationship_3','eRelationship_4',
                    'eWork_1','eWork_2', 'eWork_3','eWork_4','eWork_5','eWork_6',
                    'eSchool_1','eSchool_2','eSchool_3','eSchool_4','eSchool_5','eSchool_6',
                    'eMarriage_1','eMarriage_2','eMarriage_3','eMarriage_4',
                    'eFamily_1','eFamily_2','eFamily_3','eFamily_4','eFamily_5','eFamily_6',
                    'eLife_1','eLife_2','eLife_3','eLife_4','eLife_5','eLife_6','eLife_7',
                    'eMental_1','eMental_2','eMental_3','eMental_4','eMental_5','eMental_6',
                    'ePhysiology_1','ePhysiology_2','ePhysiology_3','ePhysiology_4','ePhysiology_5',
                    'eAddiction_1','eAddiction_2','eAddiction_3','eAddiction_4','eAddiction_5','eAddiction_6',
                    'eLawsandCrime_1','eLawsandCrime_2','eLawsandCrime_3','eLawsandCrime_4','eLawsandCrime_5','eLawsandCrime_6','eLawsandCrime_7',
                    'ePassedAway_1','ePassedAway_2','ePassedAway_3','ePassedAway_4','ePassedAway_5','qSkip']
        labels = {
            'eRelationship_1': ('伴侶問題'),
            'eRelationship_2': ('單戀'),
            'eRelationship_3': ('朋友問題'),
            'eRelationship_4': ('感情其他'),
                    'eWork_1': ('退休'),
                    'eWork_2': ('同事問題'),
                    'eWork_3': ('上司問題'),
                    'eWork_4': ('客戶問題'),
                    'eWork_5': ('工作不順'),
                    'eWork_6': ('職場其他'),
                    'eSchool_1': ('學業不順'),
                    'eSchool_2': ('升學'),
                    'eSchool_3': ('轉學'),
                    'eSchool_4': ('同儕問題'),
                    'eSchool_5': ('師生問題'),
                    'eSchool_6': ('校園其他'),
                    'eMarriage_1': ('離婚'),
                    'eMarriage_2': ('夫妻失和'),
                    'eMarriage_3': ('分居'),
                    'eMarriage_4': ('婚姻其他'),
                    'eFamily_1': ('父母問題'),
                    'eFamily_2': ('兒女問題'),
                    'eFamily_3': ('兄弟姊妹問題'),
                    'eFamily_4': ('親戚問題'),
                    'eFamily_5': ('公婆問題'),
                    'eFamily_6': ('家庭其他'),
                    'eLife_1': ('個人習慣改變'),
                    'eLife_2': ('生活環境'),
                    'eLife_3': ('宗教問題'),
                    'eLife_4': ('人際關係'),
                    'eLife_5': ('經濟問題'),
                    'eLife_6': ('同性戀'),
                    'eLife_7': ('生活適應其他'),
                    'eMental_1': ('壓力'),
                    'eMental_2': ('恐懼'),
                    'eMental_3': ('自我傷害'),
                    'eMental_4': ('憤怒'),
                    'eMental_5': ('焦躁憂鬱'),
                    'eMental_6': ('心理情緒其他'),
                    'ePhysiology_1': ('身體不適'),
                    'ePhysiology_2': ('受傷或生病'),
                    'ePhysiology_3': ('懷孕'),
                    'ePhysiology_4': ('失眠'),
                    'ePhysiology_5': ('生理狀態其他'),
                    'eAddiction_1': ('藥物成癮'),
                    'eAddiction_2': ('酒精成癮'),
                    'eAddiction_3': ('菸癮'),
                    'eAddiction_4': ('網路成癮'),
                    'eAddiction_5': ('賭博成癮'),
                    'eAddiction_6': ('成癮其他'),
                    'eLawsandCrime_1': ('詐騙'),
                    'eLawsandCrime_2': ('性騷擾'),
                    'eLawsandCrime_3': ('暴力'),
                    'eLawsandCrime_4': ('酒駕'),
                    'eLawsandCrime_5': ('服刑'),
                    'eLawsandCrime_6': ('威脅'),
                    'eLawsandCrime_7': ('法律犯罪其他'),
                    'ePassedAway_1': ('親人過世'),
                    'ePassedAway_2': ('朋友過世'),
                    'ePassedAway_3': ('伴侶過世'),
                    'ePassedAway_4': ('寵物過世'),
                    'ePassedAway_5': ('親友過世其他'),
                    'qSkip':('是否跳過'),

            
        }



class summaryUserDetailForm(forms.Form):
    question = forms.ModelChoiceField(queryset=Question.objects.all())
    Time_stamp = forms.DateTimeInput()
    sUser = forms.ModelChoiceField(queryset=User.objects.all())