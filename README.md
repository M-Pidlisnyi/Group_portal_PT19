Application "account_app"


The "account_app" is a system for authorization and authentication. You can register, log in, or view your profile information.
Registration
The registration template is available at the URL: /register. It creates a user with standard permissions. To register, you need to follow these rules:
    A login is required, with a maximum length of 150 characters. It can only contain letters, digits, and the symbols @, ., +, -, _.
    An email is optional.
    The password must:
        Not be too similar to your other personal information.
        Be at least 8 characters long.
        Not be a commonly used password.
        Not consist entirely of numbers.
    You must confirm the password after entering it.

Login
The login template is available at the URL: /login. It allows you to access the system and use its features. To log in, you need to:
    Enter your login.
    Enter your password.

Profile
The profile template is available at the URL: /profile and is accessible immediately after logging in. If you are not authorized, you will be redirected to the login page.
Additionally, if you are already authorized and attempt to access the registration or login URLs, you will be redirected to your profile.



Application "announcement_app"


The "announcement_app" is an application for managing announcements (how unexpected!). Essentially, it is just a model with a title, content, and a creation timestamp.
Additionally:
    The latest announcement is always displayed on all templates.
    You can close it or simply ignore it (who even looks at announcements anyway?).



Application "main_page_app"
The "main_page_app" is an application for the main page template. It is simply a template with navigation and a short description of this project.

Application "Portfolio":
#urls.py:

    path('', views.portfolio_list, name='portfolio_list'), #Displays a list of all user portfolios.
    path('create/', views.create_portfolio, name='create_portfolio'), #Provides a form to create a new portfolio.
    path('edit/<int:pk>/', views.edit_portfolio, name='edit_portfolio'), #Allows editing an existing portfolio, identified by its primary key (`pk`).
    path('add_item/<int:portfolio_pk>/', views.add_portfolio_item, name='add_portfolio_item'), #Adds an item (e.g., a project) to a specific portfolio, identified by its primary key (`portfolio_pk`).
    path('view/<int:pk>/', views.portfolio_detail, name='portfolio_detail'), #Displays detailed information about a specific portfolio, identified by its primary key (`pk`).

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)#When `DEBUG` mode is enabled, the `urlpatterns` includes static file handling for media files using the `settings.MEDIA_URL` and `settings.MEDIA_ROOT`.

#views.py

def portfolio_list(request): #Displays a list of portfolios owned by the current user.


def create_portfolio(request): #Allows users to create a new portfolio. 

def edit_portfolio(request, pk): #Allows editing an existing portfolio.

def add_portfolio_item(request, portfolio_pk): #Adds a new item to a portfolio.

def portfolio_detail(request, pk): #Displays detailed information about a specific portfolio.


Application "Gallery"
galleryapp 
If we go to galleryapp/, the main page opens to us, where we have seen the videos or photos added by gallery-
app/add/ on this page we can see that you can add a name, description, choose the type of photo or video and below we can download this photo or video
