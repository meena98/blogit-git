from django.conf.urls import include, url

from rest_framework.routers import DefaultRouter

from .views import ArticleViewSet,ArticlesFavouriteAPIView,ArticlesFeedAPIView,CommentsListCreateAPIView,CommentsDestroyAPIView,TagListAPIView

router = DefaultRouter(trailing_slash=False)
router.register(r'articles', ArticleViewSet)

urlpatterns = [
    url(r'^articles/feed/?$', ArticlesFeedAPIView.as_view()),
    url(r'^articles/(?P<article_slug>[-\w]+)/favorite/?$',ArticlesFavouriteAPIView.as_view()),
    url(r'^articles/(?P<article_slug>[-\w]+)/comments/?$',CommentsListCreateAPIView.as_view()),
    url(r'^articles/(?P<article_slug>[-\w]+)/comments/(?P<comment_pk>[\d]+)/?$',CommentsDestroyAPIView.as_view()),
    url(r'^tags/?$', TagListAPIView.as_view()),
    url(r'^', include(router.urls)),
]

# url(r'^articles/feed/?$', ArticlesFeedAPIView.as_view()),
# url(r'^', include(router.urls)),
# url(r'^articles/(?P<article_slug>[-\w]+)/favorite/?$', ArticlesFavouriteAPIView.as_view()),
# url(r'^articles/(?P<article_slug>[-\w]+)/comments/?$', CommentsListCreateAPIView.as_view()),
# url(r'^articles/(?P<article_slug>[-\w]+)/comments/(?P<comment_pk>[\d]+)/?$', CommentsDestroyAPIView.as_view()),
# url(r'^tags/?$ListAPIView.as_view()),', Tag