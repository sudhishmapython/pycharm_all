from django.urls import path
from Futura_App import views,admin_views,trainer_views,student_views

urlpatterns = [
    path('', views.index, name='index'),
    path('student_reg', views.student_reg, name='student_reg'),
    path('trainer_reg', views.trainer_reg, name='trainer_reg'),
    path('login_view/', views.login_view, name='login_view'),
    path('logout_view', views.logout_view, name='logout_view'),



    path('admin_page', admin_views.admin_page, name='admin_page'),
    path('student_view', admin_views.student_view, name='student_view'),
    path('student_update/<int:id>', admin_views.student_update, name='student_update'),
    path('student_delete/<int:id>', admin_views.student_delete, name='student_delete'),
    path('trainer_view', admin_views.trainer_view, name='trainer_view'),
    path('trainer_update/<int:id>', admin_views.trainer_update, name='trainer_update'),
    path('trainer_delete/<int:id>', admin_views.trainer_delete, name='trainer_delete'),
    path('add_staff/<int:id>', admin_views.add_staff, name='add_staff'),
    path('admin_evaluation/', admin_views.admin_evaluation, name='admin_evaluation'),
    path('admin_evaluation_update/<int:id>', admin_views.admin_evaluation_update, name='admin_evaluation_update'),
    path('admin_evaluation_delete/<int:id>', admin_views.admin_evaluation_delete, name='admin_evaluation_delete'),
    path('add_slot/', admin_views.add_slot, name='add_slot'),
    path('slot_view', admin_views.slot_view, name='slot_view'),
    path('slot_update/<int:id>', admin_views.slot_update, name='slot_update'),
    path('slot_delete/<int:id>', admin_views.slot_delete, name='slot_delete'),
    path('add_technology/', admin_views.add_technology, name='add_technology'),
    path('technology_view', admin_views.technology_view, name='technology_view'),
    path('technology_update/<int:id>', admin_views.technology_update, name='technology_update'),
    path('technology_delete/<int:id>', admin_views.technology_delete, name='technology_delete'),
    path('add_sections/', admin_views.add_sections, name='add_sections'),
    path('sections_view', admin_views.sections_view, name='sections_view'),
    path('sections_update/<int:id>', admin_views.sections_update, name='sections_update'),
    path('sections_delete/<int:id>', admin_views.sections_delete, name='sections_delete'),
    path('get_filtered_students/', admin_views.get_filtered_students, name='get_filtered_students'),
    path('get_filtered_trainers/', admin_views.get_filtered_trainers, name='get_filtered_trainers'),
    path('add_schedule/', admin_views.add_schedule, name='add_schedule'),
    path('schedule_view', admin_views.schedule_view, name='schedule_view'),
    path('schedule_update/<int:id>', admin_views.schedule_update, name='schedule_update'),
    path('schedule_delete/<int:id>', admin_views.schedule_delete, name='schedule_delete'),
    path('upload/', admin_views.simple_upload, name='simple_upload'),
    path('active_student_view', admin_views.active_student, name='active_student'),
    path('active_update/<int:id>', admin_views.active_update, name='active_update'),
    path('active_delete/<int:id>', admin_views.active_delete, name='active_delete'),
    path('evaluation_report_admin/', admin_views.evaluation_report_admin, name='evaluation_report_admin'),





    path('student_page', student_views.student_page, name='student_page'),
    path('user_profile/', student_views.user_profile, name='user_profile'),
    path('user_evaluation/', student_views.user_evaluation, name='user_evaluation'),
    path('student_schedule_view', student_views.schedule_view, name='student_schedule_view'),
    path('chart', student_views.chart, name='chart'),




    path('trainer_page', trainer_views.trainer_page, name='trainer_page'),
    path('trainer_profile/', trainer_views.trainer_profile, name='trainer_profile'),
    path('active1_student', trainer_views.active1_student, name='active1_student'),
    path('add_evaluation/<int:id>', trainer_views.add_evaluation, name='add_evaluation'),
    path('view_evaluation/', trainer_views.view_evaluation, name='view_evaluation'),
    path('evaluation_update/<int:id>', trainer_views.evaluation_update, name='evaluation_update'),
    path('evaluation_delete/<int:id>', trainer_views.evaluation_delete, name='evaluation_delete'),
    path('trainer_schedule_view', trainer_views.schedule_view, name='trainer_schedule_view'),
    path('attendance/<int:id>', trainer_views.attendance, name='attendance'),
    path('evaluation_report/', trainer_views.evaluation_report, name='evaluation_report'),



]