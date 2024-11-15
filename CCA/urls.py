from django.contrib import admin
from django.urls import path
from app.views import *
from django.contrib.auth import views as auth_views
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('form/',addData,name='sform'),
    path('placed/',placed,name='placed'),
    path('not_placed/',not_placed,name='not_placed'),
    path('backlog/',backlog,name='backlog'),
    path('update/<int:student_id>/',addData, name='update_student'),
    path('delete_student/<int:student_id>/',delete_student, name='delete_student')
]

urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)