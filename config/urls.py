from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth.views import LogoutView
from django.urls import path
import litreview.views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", litreview.views.login_page, name="login"),
    path("login/", litreview.views.login_page, name="login"),
    path("logout/",
         LogoutView.as_view(template_name="litreview/logout.html"),
         name="logout"),
    path("home/", litreview.views.home, name="home"),
    path("signup/", litreview.views.signup_page, name="signup"),
    path("follow-users/", litreview.views.follow_users, name="follow_users"),
    path("unfollow-user/<int:id>",
         litreview.views.unfollow_user,
         name="unfollow_user"),
    path("create-ticket/",
         litreview.views.create_ticket,
         name="create_ticket"),
    path("edit-ticket/<int:id>",
         litreview.views.edit_ticket,
         name="edit_ticket"),
    path("delete-ticket/<int:id>",
         litreview.views.delete_ticket,
         name="delete_ticket"),
    path("create-review/",
         litreview.views.create_review,
         name="create_review"),
    path(
        "create-review-to-ticket/<int:id>",
        litreview.views.create_review_to_ticket,
        name="create_review_to_ticket",
    ),
    path("edit-review/<int:id>",
         litreview.views.edit_review,
         name="edit_review"),
    path("delete-review/<int:id>",
         litreview.views.delete_review,
         name="delete_review"),
    path("posts/", litreview.views.posts, name="posts"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
