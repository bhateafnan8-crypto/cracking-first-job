... venv = virtual environment
... cd django
... always activate venv ---  venv\Scripts\activate" 
... mysite = projectname
... invoices = application name
... venv venv -> last venv is folder name


venv\Scripts\activate " whenever open file in vscode '


--- steps for django installation ---

step 1 --- virtual environment installing
command -> python -m venv venv
what happens --> inside folder venv folder create and installing venv and all files etc inside venv folder

step 2 --- go inside that virtual environment (activation of venv)
command -> venv\Scripts\activate 
what happens --> same like this " (venv) " at left will show

step 3 --- install django
command -> pip3 install django
what happens --> django istalling inside your folder

step 4 --- verfication of django installing (django version check)
command -> python -m django --version or python -m  django --v
what happens --> it check is djangi installed or not if installed then show version otherwise not installed show

step 5 --- start of project
command -> django-admin startproject mysite .
what happens --> creation of new project building using helper manager " django-admin " and " . " is for telling where to start means exact location for starting new project or current location for starting project " . " is says that .

step 6 --- running manage.py file 
command -> python manage.py runserver
what happens --> it will run the project and server  and show this (Watching for file changes with StatReloader , Performing system checks... , System check identified no issues (0 silenced). ,  You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions. , Run 'python manage.py migrate' to apply them. , September 13, 2026 - 17:00:08 , Django version 6.1.1, using settings 'mysite.settings' , Starting WSGI development server at http://127.0.0.1:8000/ , Quit the server with CTRL-BREAK. , WARNING: This is a development server. Do not use it in a production setting. Use a production WSGI or ASGI server instead.For more information on production servers see: https://docs.djangoproject.com/en/6.1/howto/deployment/ , [13/Sep/2026 17:10:01] "GET / HTTP/1.1" 200 12149 , Not Found: /favicon.ico , [13/Sep/2026 17:10:01] "GET /favicon.ico HTTP/1.1" 404 2280 )  ... main link " http://127.0.0.1:8000/ "

step 7 --- django application starting
command -> python manage.py startapp invoices
what happens --> here starting an application (invoices = projectname/application name) inside our project we have to start an application or creation of new application so it will control using manage.py in python so use " python manage.py " and for starting new app that's why " startapp " use and then application name " invoices " and here invoices folder creates and inside this files and folders creates

step 8 --- tell django about our application is exist
command -> no command we have to write application name in "INSTALLED_APPS" lists like this [appname,]
what happens --> it will show that our application is exist if we dont do django dont know existance of application so we have to do this everytime whenever we create a new application

step 9 --- migration creation, compare model-db and write instruction
command -> python manage.py makemigrations
what happens --> migration will create automatically, it will check model and in db check what currently exist then compare both and write instruction for what need to change, django will read model.py chack modelclass and call " 0001__initial__.py " file

step 10 --- migrate
command -> python manage.py migrate