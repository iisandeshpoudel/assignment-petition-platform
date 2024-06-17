As I got interviewed as a Python Developer. I decided to do this assignment in a Pythonic way.
Hence, I used [venv](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/#create-and-use-virtual-environments) package to manage the virtual environment and Django as the backend framework.
And HTML, CSS and JS for the front end.

### Features with their details
Since this is a demo project, I decide to keep Sign up only with username and password intentionally for the sake of simplicity
| Feature                         | Aspect/Trigger                                                 |
|---------------------------------|----------------------------------------------------------------|
| Contact Form in the Homepage    | User can send contact with message directly from the homepage, and the data gets stored in the datbase  |
| Sign Up              | User can Sign Up and if they are already authenticate they will be redirected to petition list feed
| Login              | User can login and if they are already logged in they will be redirected to petition list feed  
| Petition Creation               | Form submission for creating a new petition
| Petition Update| Form submission for updating a  petition
| Petition Delete| Form submission for deleting a  petition
| Search Function|User can search for petition and user name from petition list feed
| Voting (Sign and Unsign)| User can vote/sign petition, and can undo their action
| My Profile| User can view thier profile where they can update and delete thier petition, search their petition. And also change their password

## Snippets
https://github.com/iisandeshpoudel/assignment-petition-platform/blob/main/Documentation/Snippets/create.png

# Code Structure
```
📦 
├─ .env
├─ .gitignore
├─ Documentation
│  ├─ How to run locally.md
│  └─ My Thought Process.md
├─ Pipfile
├─ Readme.md
├─ backend
│  ├─ api
│  │  ├─ __init__.py
│  │  ├─ __pycache__
│  │  │  ├─ __init__.cpython-312.pyc
│  │  │  ├─ admin.cpython-312.pyc
│  │  │  ├─ apps.cpython-312.pyc
│  │  │  ├─ models.cpython-312.pyc
│  │  │  ├─ urls.cpython-312.pyc
│  │  │  └─ views.cpython-312.pyc
│  │  ├─ admin.py
│  │  ├─ apps.py
│  │  ├─ migrations
│  │  │  ├─ 0001_initial.py
│  │  │  ├─ 0002_petition_likes.py
│  │  │  ├─ 0003_remove_petition_likes_petition_signed_users.py
│  │  │  ├─ 0004_contactus.py
│  │  │  ├─ 0005_alter_contactus_options.py
│  │  │  ├─ __init__.py
│  │  │  └─ __pycache__
│  │  │     ├─ 0001_initial.cpython-312.pyc
│  │  │     ├─ 0002_petition_likes.cpython-312.pyc
│  │  │     ├─ 0003_remove_petition_likes_petition_signed_users.cpython-312.pyc
│  │  │     ├─ 0004_contactus.cpython-312.pyc
│  │  │     ├─ 0005_alter_contactus_options.cpython-312.pyc
│  │  │     └─ __init__.cpython-312.pyc
│  │  ├─ models.py
│  │  ├─ serializer.py
│  │  ├─ templates
│  │  │  └─ api
│  │  │     ├─ change-password.html
│  │  │     ├─ create-petition.html
│  │  │     ├─ css
│  │  │     │  ├─ change-password.css
│  │  │     │  ├─ create-petition.css
│  │  │     │  ├─ delete-petition.css
│  │  │     │  ├─ index.css
│  │  │     │  ├─ login.css
│  │  │     │  ├─ petition-details.css
│  │  │     │  ├─ petitions.css
│  │  │     │  ├─ profile.css
│  │  │     │  └─ register.css
│  │  │     ├─ index.html
│  │  │     ├─ login.html
│  │  │     ├─ logout.html
│  │  │     ├─ main.html
│  │  │     ├─ myprofile.html
│  │  │     ├─ petition_confirm_delete.html
│  │  │     ├─ petitiondetails.html
│  │  │     ├─ petitionlist.html
│  │  │     ├─ register.html
│  │  │     ├─ thankyou.html
│  │  │     └─ update-petition.html
│  │  ├─ tests.py
│  │  ├─ urls.py
│  │  └─ views.py
│  ├─ backend
│  │  ├─ __init__.py
│  │  ├─ __pycache__
│  │  │  ├─ __init__.cpython-312.pyc
│  │  │  ├─ settings.cpython-312.pyc
│  │  │  ├─ urls.cpython-312.pyc
│  │  │  └─ wsgi.cpython-312.pyc
│  │  ├─ asgi.py
│  │  ├─ settings.py
│  │  ├─ urls.py
│  │  └─ wsgi.py
│  ├─ db.sqlite3
│  ├─ logs
│  │  └─ debug.log
│  ├─ manage.py
│  └─ requirements.txt
└─ db.sqlite3
```
### Key Files and Their Roles

-   **`settings.py`**: Contains all the settings and configurations for the Django project, such as database settings, installed apps, middleware, etc.
-   **`urls.py`**: The URL configuration file, routing URLs to appropriate views.
-   **`models.py`**: Defines the data models for the petitions, outlining the structure of the database tables.
-   **`views.py`**: Contains the logic for handling requests and returning responses.
-   **`templates/`**: HTML files that define the structure and layout of the web pages.

## Libraries or Tools Used

-   **Django**: The main framework used to build the application. It provides a robust structure for developing web applications.
-   **SQLite**: The default database used for development purposes. Django supports various databases, and SQLite is lightweight and easy to set up.
-   **Bootstrap**: Used for the front-end design to make the application responsive and visually appealing.

## Justifications for Design Decisions

1.  **Use of Django**:
    
    -   Django was chosen due to its high-level, scalable nature and built-in admin interface which speeds up development.
    -   The framework follows the DRY (Don't Repeat Yourself) principle and has robust documentation and community support.
2.  **SQLite as Database**:
    
    -   SQLite is easy to set up and suitable for development and testing environments. It requires no additional configuration and is included with Python.

3.  **Bootstrap for Frontend**:

    -   Bootstrap was used to create a responsive and modern user interface quickly. It offers pre-designed components and is highly customizable.

# Additional Steps or Configurations

### Creating a Superuser

To access the Django admin interface, you need to create a superuser:

```sh
python manage.py createsuperuser` 
```
Follow the prompts to set up your superuser account.

### Running Tests

To run tests and ensure everything is working correctly, use:

```sh
python manage.py test
```

### Static Files

During development, Django serves static files automatically. However, for production, you need to collect static files into a single directory:

```sh
python manage.py collectstatic
```
