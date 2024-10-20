from django.urls import path
from . import views

urlpatterns = [
    path('', views.new_discuss_set, name='new_discuss_set'),
    path('your_label_task/', views.your_label_task, name='your_label_task'),
    path('empty_discuss/', views.empty_discuss, name='empty_discuss'),
    path('do_label/<int:ques_id>/', views.do_label, name = 'do_label'),
    path('do_label/<int:ques_id>/next/<str:pure_next>/', views.next_data, name='next_data'),
    path('do_label/<int:ques_id>/prev/<str:pure_prev>/', views.prev_data, name='prev_data'),
    path('admin_review_labels/<int:ques_id>/', views.admin_review_labels, name='admin_review_labels'),   
    path('admin_review_labels/<int:ques_id>/next/<str:pure_next>/', views.next_review_data, name='admin_review_labels_next'),   
    path('admin_review_labels/<int:ques_id>/prev/<str:pure_prev>/', views.prev_review_data, name='admin_review_labels_prev'),
    # path('do_summary/<int:ques_id>', views.do_summary),
]