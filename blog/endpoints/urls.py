from django.urls import path, include

from rest_framework.urlpatterns import format_suffix_patterns

from .views import ListPostsView, PostView, UpdateCountViews, ContribotorViews,  FeaturesViews, SkillViews, CharacterViews


urlpatterns = [
    path('posts/', ListPostsView.as_view()),
    path('posts/<int:pk>/', PostView.as_view()),
    path("posts/<int:id>/update-views/", UpdateCountViews.as_view()),
    path("contributors/", ContribotorViews.as_view()),
    path("features/", FeaturesViews.as_view()),
    path("skills/", SkillViews.as_view()),
    path("characters/", CharacterViews.as_view())

]

urlpatterns = format_suffix_patterns(urlpatterns=urlpatterns)