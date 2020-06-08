from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from . import views

r = SimpleRouter(trailing_slash=False)

r.register(r"users", views.UserViewSet)
r.register(r"scopes", views.ScopeViewSet)
r.register(r"roles", views.RoleViewSet)
r.register(r"permissions", views.PermissionViewSet)
r.register(r"acls", views.ACLViewSet)

urlpatterns = [
    url(r"^me", views.MeViewSet.as_view({"get": "retrieve"}), name="me-detail"),
    url(
        r"^myacls/(?P<pk>[^/.]+)$",
        views.MyACLViewSet.as_view({"get": "retrieve"}),
        name="myacls-detail",
    ),
    url(r"^myacls", views.MyACLViewSet.as_view({"get": "list"}), name="myacls-list"),
]

urlpatterns.extend(r.urls)
