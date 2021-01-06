from django.urls import path, re_path, include
from . import views

urlpatterns = [
    path('', views.technique_view, name='technique_view'),  # '' (show techniques)
    path('<slug:tech_slug>/', views.instance_view, name='instance_view'),
    path('<slug:tech_slug>/<str:inst_id>/', views.topic_view, name='topic_view'),
    path('<slug:tech_slug>/<str:inst_id>/<int:topic_id>', views.summary_view, name='summary_view'),
    # path('<slug:tech_slug>/<int:inst_id>/', views.topic_view, name='topic_view')
    # re_path(r'^?P<technique_name_slug>[\w\-]+/$', views.instance_view, name='show_instances'),
    # path('<slug:slug>/', views.instance_view),   # technique/ (show instances)
    # path('<slug:slug>/<slug:slug>/', view.topic_view)  # technique/instance/ (show topics)
    # path('<slug:slug>/<slug:slug>/', view.summary_view)  # technique/instance/topic_name (show summary)
]