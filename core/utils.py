from crum import get_current_user


# to save currently logged in user by model itself
def auto_save_current_user(obj):
    user = get_current_user()
    if user and not user.pk:
        user = None
    if not obj.pk:
        obj.added_by = user