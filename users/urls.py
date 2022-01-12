from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static
urlpatterns = [
    path('', views.signIn),
    path('postsignIn/', views.postsignIn),
    path('signUp/', views.signUp, name="signup"),
    path('logout/', views.logout, name="log"),
    path('postsignUp/', views.postsignUp),
    path('reset/', views.reset),
    path('postReset/', views.postReset),
    path('profile_create/',views.profile_create,name="profile_create"),
    path('post_create/',views.post_create,name="post_create"),
]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)