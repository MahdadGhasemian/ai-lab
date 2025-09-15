Creating Environment and Installation

```bash
python3 -m venv env
source env/bin/activate
pip3 install django
```

Creating Project

```bash
django-admin
django-admin startproject devsearch
```

Go to the devsearch folder and create virtual environment again!
```bash
deactivate
cd devsearch
python3 -m venv env
source env/bin/activate
pip3 install django

```

Run devsearch

```bash
cd devsearch/
source env/bin/activate
python3 manage.py runserver
```

Create new app
```bash
# Creating projects app
python3 manage.py startapp projects
# Config
# Add 'projects.apps.ProjectsConfig' into python/1/devsearch/devsearch/settings.py -> INSTALLED_APPS
```