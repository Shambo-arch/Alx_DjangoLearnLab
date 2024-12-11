Social Meia API

1) Created a project named soial_media_api by typing: django-admin startproject social_media_api in the directory named also: social_media_api
2) Created an app named accounts in the project
3) Defined a rest_framework and acoounts app in settings.py specifically in INSTALLED APP List
4) Defined Custom User Model for fields: bio, profile_picture and followers
5) Updated settings.py to use the custom user model
6) Runned in bash : python3 manage.py makemigrations accounts and python3 manage.py migrate
7) Created Serializers in accounts/serializers.py
8) Created Views: RegisterView, LoginView, ProfileView in accounts/views.py
9) Configured URL patterns in accounts/urls.py to include routes for registration (/register), login (/login), and user profile management (/profile).
10)Ensured that registration and login endpoints return a token upon successful operations.
