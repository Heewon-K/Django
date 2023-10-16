## Progress on Django class!
### From 2023.10.05 ~ on going!

Day 1. setting env for Django! (23.10.05)
  - create virtual env
  - pip install django==4.0.3
  - create root directoty = this repository!
  - create django project at Django/mysite
  - create mysite.cmd file for easy access
  - download pycharm and set settings for current project - python interpreter, LANGUAGE_CODE, TIME_ZONE were modified
  - create apps - pybo, main, encore
  - modify config/urls.py, pybo/views.py, pybo/urls.py to manage url mapping and view

Day 2. Database, Tables and how to work with them in Django (23.10.06)
  - python manage.py migrate
  - download and set SQLite
  - create models on pybo/models.py : Question(subject, content, create_date) & Answer(question, content, create_date)
    - subject/question : CharField(max_length : 200), content : TextField, create_date : DateTimeField
  - add pybo app on config/settings.py - INSTALLED_APPS
  - create DB table(question&answer) by makemigrations --> migrate
  - use django shell to save, get, modify and delete data in question & answer tables
  - Django admin : make superuser account, modify admin.py to give permission to modify Question model
  - modify pybo/views.py and create templates to show list of questions and answers on 'localhost.../pybo/'
  - use namespaces to use url without confusion!

Day 3. (23.10.10)

Day 4. (23.10.11) - missed the class

Day 5. (23.10.12) - catching up missed class! + today's class

Day 6. AWS! setting up AWS lightsail :3
  - upload the django project files to github. (I was already uploading the files to github so I only updated .gitignore)
  - it is hard to manage a server so let's use AWS lightsail!
  - made an account for lightsail and created an instance(Linux/Unix, Ubuntu 20.04 LTS)
  - create static IP
  - add a new rule on firewall : port 8000
  - set the date to KST
  - download MobaXterm -> use SSH key and static IP to connect to the server

Day 7. Continue setting the server
  - install: pyrhon3-venv
  - mkdir : projects/venvs
  - make venv named mysite in projects/venvs
  - 
