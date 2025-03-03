from django.contrib.auth import get_user_model
from django.db.models import Count

User = get_user_model()

def check_for_duplicates():
    # Check for duplicate emails
    duplicate_emails = User.objects.values('email').annotate(email_count=Count('email')).filter(email_count__gt=1)
    print("Duplicate Emails: ", list(duplicate_emails))

    # Check for duplicate usernames
    duplicate_usernames = User.objects.values('username').annotate(username_count=Count('username')).filter(username_count__gt=1)
    print("Duplicate Usernames: ", list(duplicate_usernames))

def merge_duplicate_users():
    duplicates = User.objects.values('email').annotate(email_count=Count('email')).filter(email_count__gt=1)
    
    for duplicate in duplicates:
        email = duplicate['email']
        users = User.objects.filter(email=email)
        
        # Keep the first user and delete the rest
        primary_user = users.first()
        for user in users[1:]:
            # Merge data if necessary
            # Example: primary_user.profile.update(user.profile)
            user.delete()

if __name__ == "__main__":
    check_for_duplicates()
    merge_duplicate_users()