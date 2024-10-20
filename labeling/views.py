import json
from django.shortcuts import render, redirect, get_object_or_404
from .models import Question, Task
from .forms import LabelForm,SelectForm
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Min, Max
from django.http import HttpResponseRedirect,Http404
from django.urls import reverse
from django.contrib.auth.decorators import user_passes_test
# Create your views here.



@login_required
def new_discuss_set(request):
    user_id = request.user.id
    current_users = get_user_model()
    total_discuss_num = Question.objects.filter(sQuestion_Filter=1,task__tUser=current_users.objects.get(pk=user_id)).count()
    if total_discuss_num != 0 :
        discuss = Question.objects.filter(task__tUser=request.user.id, sQuestion_Filter=1).order_by("qQuestion_ID")[0:1].get().qQuestion_ID
        return redirect(f'/labeling/admin_review_labels/{discuss}/')
    else :
        return redirect(f'/labeling/empty_discuss/')
        
@login_required
def empty_discuss(request):

    return render(request,"labeling/empty_discuss.html")

@login_required
def your_label_task(request):
    context = {}

    if request.user.is_authenticated:
        username = request.user.username
        user_id = request.user.id

    your_tasks = Task.objects.filter(tUser=user_id)
    
    if request.method == 'POST':
        return redirect(f'/labeling/do_label/{request.POST["label_id"]}/')
    else:
        undone = Question.objects.filter(task__tdone=False)
        done = Question.objects.filter(task__tdone=True)
        skip = Question.objects.filter(qSkip=True)
        discuss = Question.objects.filter(sQuestion_Filter=1)
        context = {
            'undone': undone,
            'done': done,
            'skip': skip,
            'discuss':discuss
        }

    return render(request, 'labeling/your_label_task.html', context)
    
@login_required #搜尋框框
def pdaq_search(request ):

        try:
            if request.method == 'POST':

                return redirect(f'/labeling/do_label/{request.POST["label_id"]}/')

        except Exception as search_error:
            print(search_error)


@login_required #標記頁面
def do_label(request, ques_id):
    user_id = request.user.id
    current_users = get_user_model()
    seen_questions_num = Task.objects.filter(tdone=True,tUser=current_users.objects.get(pk=user_id)).count() #當前使用者已看過進度
    total_questions_num = Task.objects.filter(tUser=current_users.objects.get(pk=user_id)).count() #當前使用者擁有的總資料筆數(須完成的資料))
    total_discuss_num = Question.objects.filter(sQuestion_Filter=1,task__tUser=current_users.objects.get(pk=user_id)).count()
    print(total_discuss_num)
    done_or_not = Task.objects.get(tQuestion=ques_id)

    message_list = Question.objects.get(qQuestion_ID= ques_id, task__tUser=request.user.id)
    message_form = LabelForm(instance=message_list, 
                                        initial={'qOriginal_Message': message_list.qOriginal_Message,
                                                })
    select_form=SelectForm(instance=message_list)

    # task_list = Task.objects.get(tQuestion= ques_id, tUser=request.user.id)
    # print(task_list)
    # skip_from=SkipForm(instance=task_list)

    context = {
                'message_form' : message_form,
                'select_form':select_form,
                # 'skip_from':skip_from,
                # 'task_list':task_list,
                'message_list': message_list,
                'done_or_not': done_or_not,
                'seen_questions_num':seen_questions_num,
                'total_questions_num':total_questions_num,
                'total_discuss_num':total_discuss_num
                }        
    ques_filter_format = {'save': 0,'discuss': 1, 'trash': 2}

    if request.method == "POST": 
        message_form = LabelForm(request.POST, instance=message_list) #建立forms物件
        select_form = SelectForm(request.POST, instance=message_list) #將表單內容傳回資料庫
        
        if message_form.is_valid():
            message_form.save()
            select_form.save()
            
            Question_Filter = ques_filter_format[request.POST['ques_filter']]
                

            message_list.sQuestion_Filter = Question_Filter

            #當有event選項被選擇，對應的topic會自動變成True
            if message_list.eRelationship_1 == True or message_list.eRelationship_2 == True or message_list.eRelationship_3 == True or message_list.eRelationship_2 == True:
                message_list.tRelationship = True
            else:
                message_list.tRelationship = False
            
            if message_list.eWork_1 == True or message_list.eWork_2 == True or message_list.eWork_3 == True or message_list.eWork_4 == True or message_list.eWork_5 == True or message_list.eWork_6 == True:
                message_list.tWork = True
            else:
                message_list.tWork = False
            
            if message_list.eSchool_1 == True or message_list.eSchool_2 == True or message_list.eSchool_3 == True or message_list.eSchool_4 == True or message_list.eSchool_5 == True or message_list.eSchool_6 == True:
                message_list.tSchool = True
            else:
                message_list.tSchool = False
            
            if message_list.eMarriage_1 == True or message_list.eMarriage_2 == True or message_list.eMarriage_3 == True or message_list.eMarriage_4 == True:
                message_list.tMarriage = True
            else:
                message_list.tMarriage = False

            if message_list.eFamily_1 == True or message_list.eFamily_2 == True or message_list.eFamily_3 == True or message_list.eFamily_4 == True or message_list.eFamily_5 == True or message_list.eFamily_6 == True:
                message_list.tFamily = True
            else:
                message_list.tFamily = False

            if message_list.eLife_1 == True or message_list.eLife_2 == True or message_list.eLife_3 == True or message_list.eLife_4 == True or message_list.eLife_5 == True or message_list.eLife_6 == True or message_list.eLife_7 == True:
                message_list.tLife = True
            else:
                message_list.tLife = False

            if message_list.eMental_1 == True or message_list.eMental_2 == True or message_list.eMental_3 == True or message_list.eMental_4 == True or message_list.eMental_5 == True or message_list.eMental_6 == True:
                message_list.tMental = True
            else:
                message_list.tMental = False

            if message_list.ePhysiology_1 == True or message_list.ePhysiology_2 == True or message_list.ePhysiology_3 == True or message_list.ePhysiology_4 == True or message_list.ePhysiology_5 == True :
                message_list.tPhysiology = True
            else:
                message_list.tPhysiology = False

            if message_list.eAddiction_1 == True or message_list.eAddiction_2 == True or message_list.eAddiction_3 == True or message_list.eAddiction_4 == True or message_list.eAddiction_5 == True or message_list.eAddiction_6 == True:
                message_list.tAddiction = True
            else:
                message_list.tAddiction = False

            if message_list.eLawsandCrime_1 == True or message_list.eLawsandCrime_2 == True or message_list.eLawsandCrime_3 == True or message_list.eLawsandCrime_4 == True or message_list.eLawsandCrime_5 == True or message_list.eLawsandCrime_6 == True or message_list.eLawsandCrime_7 == True:
                message_list.tLawsandCrime = True
            else:
                message_list.tLawsandCrime = False

            if message_list.ePassedAway_1 == True or message_list.ePassedAway_2 == True or message_list.ePassedAway_3 == True or message_list.ePassedAway_4 == True or message_list.ePassedAway_5 == True :
                message_list.tPassedAway = True
            else:
                message_list.tPassedAway = False
            message_list.save()
            print(message_list)
            print(current_users.objects.get(pk=user_id))
            sum = Task.objects.get_or_create(tQuestion=message_list, tUser= current_users.objects.get(pk=user_id))
            print(sum)
            done_or_not.tdone = True
            print(done_or_not)
            done_or_not.save()

        return redirect(f'/labeling/do_label/{ques_id}/next/False')

    return render(request, 'labeling/do_label.html', context)

@login_required #下一筆資料
def next_data(request, ques_id, pure_next):
    try:
        if pure_next == 'True':
            ret = Question.objects.filter(qQuestion_ID__gt=ques_id, task__tUser=request.user.id).order_by("qQuestion_ID")[0:1].get().qQuestion_ID
            print(Question.objects.filter(qQuestion_ID__gt=ques_id, task__tUser=request.user.id).order_by("qQuestion_ID"))
        else:
            ret = Question.objects.filter(qQuestion_ID__gt=ques_id, task__tUser=request.user.id, task__tdone=False).order_by("qQuestion_ID")[0:1].get().qQuestion_ID
    except:
        if pure_next == 'True':
            ret = Question.objects.filter(task__tUser=request.user.id).aggregate(Min("qQuestion_ID"))['qQuestion_ID__min']
        else:
            if Question.objects.filter(task__tUser=request.user.id, task__tdone=False).count()==0:
                return redirect('/labeling/')
            else:
                ret = Question.objects.filter(task__tUser=request.user.id).aggregate(Min("qQuestion_ID"))['qQuestion_ID__min']
    return redirect(f'/labeling/do_label/{ret}/')

@login_required #上一筆資料
def prev_data(request, ques_id, pure_prev):
    try:
        if pure_prev == 'True':
            ret = Question.objects.filter(qQuestion_ID__lt=ques_id,task__tUser=request.user.id).order_by("-qQuestion_ID")[0:1].get().qQuestion_ID
        else:
            ret = Question.objects.filter(qQuestion_ID__lt=ques_id,task__tUser=request.user.id, task__tdone=False).order_by("-qQuestion_ID")[0:1].get().qQuestion_ID
    except:
        if pure_prev == "True":
            ret = Question.objects.filter(task__tUser=request.user.id).aggregate(Max("qQuestion_ID"))['qQuestion_ID__max']
        else:
            if Question.objects.filter(task__tUser=request.user.id, task__tdone=False).count()==0:
                return redirect('/labeling/')
            else:
                ret = Question.objects.filter(task__tUser=request.user.id, task__tdone=False).aggregate(Max("qQuestion_ID"))['qQuestion_ID__max']
    return redirect(f'/labeling/do_label/{ret}/')


@login_required
def admin_review_labels(request, ques_id):
    user_id = request.user.id
    current_users = get_user_model()
    total_discuss_num = Question.objects.filter(sQuestion_Filter=1).count()
    print(total_discuss_num)
    done_or_not = Task.objects.get(tQuestion=ques_id)

    message_list = Question.objects.get(qQuestion_ID= ques_id)
    message_form = LabelForm(instance=message_list, 
                                        initial={'qOriginal_Message': message_list.qOriginal_Message,
                                                })
    review_form=SelectForm(instance=message_list)

    # task_list = Task.objects.get(tQuestion= ques_id, tUser=request.user.id)
    # print(task_list)
    # skip_from=SkipForm(instance=task_list)

    context = {
                'message_form' : message_form,
                'select_form':review_form,
                'message_list': message_list,
                'done_or_not': done_or_not,
                'total_discuss_num':total_discuss_num
                }        
    ques_filter_format = {'save': 0,'discuss': 1, 'trash': 2}

    if request.method == "POST": 
        message_form = LabelForm(request.POST, instance=message_list) #建立forms物件
        review_form = SelectForm(request.POST, instance=message_list) #將表單內容傳回資料庫
        
        if message_form.is_valid():
            message_form.save()
            review_form.save()
            
            Question_Filter = ques_filter_format[request.POST['ques_filter']]
                

            message_list.sQuestion_Filter = Question_Filter

            #當有event選項被選擇，對應的topic會自動變成True
            if message_list.eRelationship_1 == True or message_list.eRelationship_2 == True or message_list.eRelationship_3 == True or message_list.eRelationship_2 == True:
                message_list.tRelationship = True
            else:
                message_list.tRelationship = False
            
            if message_list.eWork_1 == True or message_list.eWork_2 == True or message_list.eWork_3 == True or message_list.eWork_4 == True or message_list.eWork_5 == True or message_list.eWork_6 == True:
                message_list.tWork = True
            else:
                message_list.tWork = False
            
            if message_list.eSchool_1 == True or message_list.eSchool_2 == True or message_list.eSchool_3 == True or message_list.eSchool_4 == True or message_list.eSchool_5 == True or message_list.eSchool_6 == True:
                message_list.tSchool = True
            else:
                message_list.tSchool = False
            
            if message_list.eMarriage_1 == True or message_list.eMarriage_2 == True or message_list.eMarriage_3 == True or message_list.eMarriage_4 == True:
                message_list.tMarriage = True
            else:
                message_list.tMarriage = False

            if message_list.eFamily_1 == True or message_list.eFamily_2 == True or message_list.eFamily_3 == True or message_list.eFamily_4 == True or message_list.eFamily_5 == True or message_list.eFamily_6 == True:
                message_list.tFamily = True
            else:
                message_list.tFamily = False

            if message_list.eLife_1 == True or message_list.eLife_2 == True or message_list.eLife_3 == True or message_list.eLife_4 == True or message_list.eLife_5 == True or message_list.eLife_6 == True or message_list.eLife_7 == True:
                message_list.tLife = True
            else:
                message_list.tLife = False

            if message_list.eMental_1 == True or message_list.eMental_2 == True or message_list.eMental_3 == True or message_list.eMental_4 == True or message_list.eMental_5 == True or message_list.eMental_6 == True:
                message_list.tMental = True
            else:
                message_list.tMental = False

            if message_list.ePhysiology_1 == True or message_list.ePhysiology_2 == True or message_list.ePhysiology_3 == True or message_list.ePhysiology_4 == True or message_list.ePhysiology_5 == True :
                message_list.tPhysiology = True
            else:
                message_list.tPhysiology = False

            if message_list.eAddiction_1 == True or message_list.eAddiction_2 == True or message_list.eAddiction_3 == True or message_list.eAddiction_4 == True or message_list.eAddiction_5 == True or message_list.eAddiction_6 == True:
                message_list.tAddiction = True
            else:
                message_list.tAddiction = False

            if message_list.eLawsandCrime_1 == True or message_list.eLawsandCrime_2 == True or message_list.eLawsandCrime_3 == True or message_list.eLawsandCrime_4 == True or message_list.eLawsandCrime_5 == True or message_list.eLawsandCrime_6 == True or message_list.eLawsandCrime_7 == True:
                message_list.tLawsandCrime = True
            else:
                message_list.tLawsandCrime = False

            if message_list.ePassedAway_1 == True or message_list.ePassedAway_2 == True or message_list.ePassedAway_3 == True or message_list.ePassedAway_4 == True or message_list.ePassedAway_5 == True :
                message_list.tPassedAway = True
            else:
                message_list.tPassedAway = False
            message_list.save()
            # sum = Task.objects.get_or_create(tQuestion=message_list, tUser= current_users.objects.get(pk=user_id))
            done_or_not.tdone = True
            print(done_or_not)
            done_or_not.save()

        return redirect(f'/labeling/admin_review_labels/{ques_id}/next/False')

    return render(request, 'labeling/admin_review_labels.html', context)

@login_required
def next_review_data(request, ques_id, pure_next):
    try:
        if pure_next == "True":
            ret = Question.objects.filter(qQuestion_ID__gt=ques_id, task__tdone=True, sQuestion_Filter=1).order_by("qQuestion_ID")[0:1].get().qQuestion_ID
        else:
            ret = Question.objects.filter(qQuestion_ID__gt=ques_id, task__tdone=True, sQuestion_Filter=1).order_by("qQuestion_ID")[0:1].get().qQuestion_ID
    except:
        if pure_next == "True":
            ret = Question.objects.filter(qQuestion_ID__gt=ques_id, task__tdone=True, sQuestion_Filter=1).aggregate(Min("qQuestion_ID"))['qQuestion_ID__min']
        else:
            if Question.objects.filter(task__tdone=True, sQuestion_Filter=1).count()==0:
                return redirect('/labeling/empty_discuss/')
            else:
                ret = Question.objects.filter(qQuestion_ID__gt=ques_id, task__tdone=True, sQuestion_Filter=1).aggregate(Min("qQuestion_ID"))['qQuestion_ID__min']
    return redirect(f'/labeling/admin_review_labels/{ret}/')

@login_required
def prev_review_data(request, ques_id, pure_prev):
    try:
        if pure_prev == 'True':
            ret = Question.objects.filter(qQuestion_ID__lt=ques_id, task__tdone=True, sQuestion_Filter=1).order_by("-qQuestion_ID")[0:1].get().qQuestion_ID
            print(Question.objects.filter(qQuestion_ID__lt=ques_id, task__tdone=True, sQuestion_Filter=1))
        else:
            ret = Question.objects.filter(qQuestion_ID__lt=ques_id, task__tdone=True, sQuestion_Filter=1).order_by("-qQuestion_ID")[0:1].get().qQuestion_ID
            print(Question.objects.filter(qQuestion_ID__lt=ques_id, task__tdone=True, sQuestion_Filter=1).order_by("-qQuestion_ID")[0:1])

    except:
        if pure_prev == 'True':
            ret = Question.objects.filter(qQuestion_ID__lt=ques_id, task__tdone=True, sQuestion_Filter=1).aggregate(Max("qQuestion_ID"))['qQuestion_ID__max']
            print(Question.objects.filter(qQuestion_ID__lt=ques_id, task__tdone=True, sQuestion_Filter=1).aggregate(Max("qQuestion_ID")))
        else:
            if Question.objects.filter(task__tdone=True, sQuestion_Filter=1).count()==0:
                return redirect('/labeling/empty_discuss/')
            else:
                ret = Question.objects.filter(qQuestion_ID__lt=ques_id, task__tdone=True, sQuestion_Filter=1).aggregate(Max("qQuestion_ID"))['qQuestion_ID__max']
                print(Question.objects.filter(qQuestion_ID__lt=ques_id, task__tdone=True, sQuestion_Filter=1).aggregate(Max("qQuestion_ID"))['qQuestion_ID__max'])
    return redirect(f'/labeling/admin_review_labels/{ret}/')