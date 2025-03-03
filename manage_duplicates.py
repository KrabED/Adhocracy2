from django.contrib.auth import get_user_model
>>> from django.db.models import Count
>>> 
>>> User = get_user_model()
>>> duplicates = User.objects.values('email').annotate(email_count=Count('email')).filter(email_count__gt=1)
>>> 
>>> 
>>> for duplicate in duplicates:
...     email = duplicate['email']
...     users = User.objects.filter(email=email)
...     
...     # Keep the first user and delete the rest
...     primary_user = users.first()
...     for user in users[1:]:
...         print(f"Deleting duplicate user: {user.username} with email: {user.email}")
...         user.delete()
