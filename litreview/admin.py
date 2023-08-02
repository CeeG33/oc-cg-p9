from django.contrib import admin
from litreview.models import User, Ticket, Review, UserFollows

models = [User, Ticket, Review, UserFollows]

admin.site.register(models)
