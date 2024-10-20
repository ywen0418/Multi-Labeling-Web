from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import TemplateView
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
import json, os
import datetime
from .settings import BASE_DIR
from labeling.models import Question, models, Task

class HomeView(TemplateView):
    template_name = 'home.html'

@login_required
def home_set(request):
    undone = Question.objects.filter(task__tUser=request.user.id, task__tdone=False).order_by("qQuestion_ID")[0:1].get().qQuestion_ID
    print(undone)
    return redirect(f'/labeling/do_label/{undone}/')


def process_byte_data(save_dir, data):
    with open(save_dir, 'wb')as destination:
        for chunk in data.chunks():
            destination.write(chunk)

@login_required
def upload_raw_json_data(request):
    Users_model = get_user_model() # 現有的users
    users = Users_model.objects.all()
    error = False
    error_msg = ''
    success = False
    success_msg = ''
    context = {
        'success': success,
        'success_msg': success_msg,
        'error': error,
        'error_msg': error_msg
    }
    if request.method == 'POST':
        json_file = request.FILES['jsonfile_upload']

        if json_file.name.split('.')[1] != 'json':
            context['error'] = True
            context['error_msg'] = "請上傳json格式!"
            return render(request, 'data/upload_raw_json_data.html', context)

        saved_json_file_name = 'medi_data_{}.json'.format(datetime.datetime.today().strftime("%Y-%m-%d"))
        saved_location = os.path.join(BASE_DIR, 'uploaded_data', saved_json_file_name)

        process_byte_data(saved_location, json_file)

        with open(saved_location, 'r', encoding='utf-8')as f:
            json_array = json.load(f)

        upload_data_num = len(json_array)
        new_data = 0
        old_data = 0
        for element in json_array:
            try:
                q_id = element['No']
                q_user = element['User']
                q_ques = element['Message']
                question_qs, created = Question.objects.get_or_create(qQuestion_ID=q_id)

                if created:
                    #there is no same question id in DB, will be created new data
                    try:
                        #q_event, q_topic = filter_summarized_data(element)
                        sum = Task.objects.create(tQuestion = question_qs, tUser = request.user)
                        sum.save()
                    except KeyError:
                        #IF NOT means haven't be watch before
                        q_event = 0
                        q_topic = 0
                    question_qs.qQuestion_User = q_user
                    question_qs.qOriginal_Message = q_ques
                    #question_qs.sQuestion_Topic = q_topic
                    #question_qs.sQuestion_Event = q_event
                    question_qs.save()
                    new_data += 1
                else:
                    old_data += 1

            except KeyError:
                context['error'] = True
                context['error_msg'] = 'json檔案中有keyword不符合規定格式！'
                return render(request, 'data/upload_raw_json_data.html', context)

        context['success'] = True
        context['success_msg'] = "總共有{}筆資料，其中新增{}筆，與現有的重疊有{}筆，請再去DB確認資料！".format(upload_data_num, new_data, old_data)
        
        return render(request, 'data/upload_raw_json_data.html', context)

        # print(json_array)
    

    return render(request, 'data/upload_raw_json_data.html', context)

def data_information(request):
    skip_id_information = Question.objects.filter(qSkip=True)#查詢被跳過的留言id

    context = {
        'skip_id_information':skip_id_information
    }

    return render(request, 'data/data_information.html', context)