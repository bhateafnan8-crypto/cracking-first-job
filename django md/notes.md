------------ Django Project Struture ------------

file " manage.py " will control overall django project , (it's a remote control like tv remote (where remote control overall tv functions (on/off , channel change , volume handling etc))) , everytime whenever we need to serverstart , db setup , new application creation we have to come inside this file , """ do not edit or change to this file or inside this file """

file " settings.py " will says all features of project , (like for school features or rule book (time,subjects,how much students in single class , language etc),for laptop(ram,rom,harddisk,storage,battery life , performance etc)) , its a rule book of django project (which language is used now , which db should be use , in which timezone project running , which project running) , we can add application in INSTALLED_APP List inside settings.py file , 

file " urls.py " is address book of project (use for pagination) , if user search for any page in site or project django will come in urls.py to find that pagee url ex about page url seaarching.. if found or exist in urls.py then django redirect to that url from urls.py and show that page to user 

files " asgi.py and wssgi.py " will use or will be in use when we live our website or project on internet

file " __init__.py " will always empty it will says that the file or folder is python file or folder 



# ------------  Django Application ------------

using command " python manage.py startapp invoices " we have to create a new application 

file " views.py " its like ui showing of wesbpage like home page ui (like a menu card and visuals in restaurant) , if user search for any page that will show that ui (urls.py find that url and redirect to that page and views.py show the content isnide that url)

file " models.py " will handle that which type data will collect from user and whats the shape and types of data and a structure of data collecting and showing

file " admin.py " handle all records from entering to leaving datas 

folder " migrations " will create and maitain a diary of ''' crud ''' operations (which [data , column , db ]creates , updates , delete in project ).. maintain all records in that diary

file " tests.py " we will write test cases for our project and code to check is it work well or not

tell django about our application is exist
command -> no command we have to write application name in "INSTALLED_APPS" lists like this [appname,]
what happens --> it will show that our application is exist if we dont do django dont know existance of application so we have to do this everytime whenever we create a new application



# ------------  urls and views ------------

These (urls and views) are the heart of django 

url routing checking what user typing and clicking and match with right page and redirect to that page to user (search food for order and get exactly that page where they want to go after click)

view will handle after search and click operation (backend part) and return that infromation to user (oredre succesfuly submit withing 20 mins order will be placed to you)

All pages works with these (urls and views) , if user type about page urls search and match then redirect to that page and views will show the content of that url to user 

--- Urls 

" url routing " read the web address check what user type,search,click then decide to what page to redirect or return

url = web address

routing = read address and redirect to page after deciding destination

url routing = address reading + destination deciding + return to page or redirect to page(url)

in file " urls.py " - in (urlpatterns) list path() function syntax for set/add url of page --> path('address/',view_func(),name='pageNickName') ex -> path('home/',views.HomePageView.as_view(),name='home'), here this "HomePageView" will be the exact same as the function name defined in views.py file  

--- Views

function based views (fbv) and class based views (cbv)

fbv -> always take request input and send repsonse output .. responseObject will collect and store all informations and datas ... function name should be always Request (we can set other always but request is best practices) we have import HttpResponse from django.http (from django.http import HttpResponse) 

ex -> for show invoice -> def show_invoice(request): return HttpsResponse("Your Invoice page") 

In urls.py:

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

In urls.py:

python
from .views import BookListView

urlpatterns = [
    path('books/', book_list, name='book-list'),]

django will automatiaclly set the request in the function parameter

here this "show_invoice" will be add to the urls.py - > urlpatterns list " path('address/',view_func(),name='pageNickName') " at the view_func() place 

get -> means user only wants to view .. search and click to view that page

post -> data sends by user (forms filling , submit button click ,any information, data (login form , searchbar , crud )) ex -> user check the menu and order something (check menu = get , order=post)

flow ---> user Search for anything (about page)-> get Request -> find in urls.py -> check content in views.py to show -> redirect to page and show the ui content to user


cbv + (request) -> A Class-Based View is a way to write Django views using Python classes instead of functions. Django provides built-in generic classes (like ListView, DetailView, CreateView) that handle common patterns, so you write less code. 

ex -> from django.views.generic import ListView
from .models import Book

In urls.py:
class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'

In urls.py:

python
from .views import BookListView

urlpatterns = [
    path('books/', BookListView.as_view(), name='book-list'),]


Why use CBVs?
Less code for common tasks (list, detail, create, update, delete)
Reusable — inherit and override methods instead of rewriting logic
Organized — different HTTP methods (GET, POST) become class methods (get(), post())



# ------------  Template and Static Files ------------

Templates : - variables,tags,filters: - Template is a html file where we create blank spaces(variables) that is django template language , django find blank spaces and filled with real data 

Variables: It means in a django template language how you show data inside your html 
syntax: {{variable_name}}
ex: - inside html: - <p> customer name  {{ cust_name }}</p>
inside views.py: data = {"cust_name":"adfar"}

in both file variable_name should be same 

now django will find cust_name and fill with tha value means adfar will be placed at variable_name , 


Tags: It means in a django template language how you add logics
syntax: - " {% tag %} " [inside "" is a syntax "" is not include in syntax,  only {% tag %} include ] 
types: for,if most used , for looping and condition based uses for ending loop or tag at the endline or last line where we want to stop use always " {% endfor %} , {% endif %}" " {% if cond %} html code {% else %} html code {% endif %} " , " {% for loop %} html code {% endfor %} " 


filters: means changing the variables appearance without changing actual data 
syntax: {{ variable_name | filter_name }}
ex: {{ variable_name | upper  }} - afdar -> ADFAR


Template Inheritance: Its a system where we create master html file(base.html) , inside this file a common structure will be added which will be shared with all pages with each other "all pages will use this base.html file for extend them for comon content" , whenever we want to change contnet we have to change in only base.html file in all files automatically changed, {like css link, navbar,footer etc}

syntax: -  Inside base.html: - common content {% block content %} {% endblock %} common content, 
Inside anontherPage where we want to add or use base.html: - {% entends base.html file path %} {% block content %} current page content {% endblock %} , 
base.html inside template and template inside invoice {invoices\template\base.html} all html files inside template folder

{% block content %} {% endblock %} this is blank space where is page content will be added this is dynamically change by django or fill by django using that current page 

ex: - Inside the aboutpage: {% extends templates\base.html %} {% block content %} about page content {% endblock %},
Inside base.html: common content like navbar {% block content %} {% endblock %} common content like footer 


Static files: Its handle the look of website , not change the file or workflow onlyn for ui (css)

syntax: - Inside base.html file: at the top most line of or first line add this {% load static %} and after title tag in head tag add linkcss tage and at href: "{% static "cssfilepath" %}" , create the css file inside the static folder and this static folder we have to create inside invoices folder




# ------------  Models and ORM (DataBase)------------

model's fields: models is nothing but a table in database and their data in that filled in blank space is field in that model.. django will read that data and fill the blank space in db, " always inherit models.Model in your class ", this models.Model says that class is model class not common class so that django will create db and create tabel for that content or data, their are so many fields use (like DecimalFields(max_digit,decimal_point), CharFields(max_length),etc) 


Migrations: it will create a real table in db of data wrote in python scripts in file " model.py " ,  model.py is a blueprint and migration is worker who will create a table in db for that blueprint, in model.py a class with inherit models.Model in that the blueprint or content written migration will create for these written content in db from model.py, 2 workers will work here 1 for read the data and 1 for telling how will the actual db create with table, migrations is a file that automatically created by django in that file the instructions included for how to change db so that ,this match with exact model

migrations commands: - " python manage.py makemigrations " : - is use for djnago check model.py file and db content and compare and write instruction for what need to change read files modelclass and call 0001__init__.py

" python manage.py migrate " : - for migrate, it will tell django for all those migrations done currently carry all and check whats not apply till now, then apply them to db

!important : " whenever you change the model.py file always run above 2 commands "

ORM : it's a way to communicate with db using normal python Scripts  , its a middle person between python and db , it will translate the python Scripts to sql and communicate with db then return the result to python

{ORM = Object Relational Mapper} - after calling python function/model orm translate it to sql and return the result.

ORM methods: -

# creating new data/record (invoice) - invoice=example
create : it will create a new record, and save in db immidiatly in one step, you have to only provide value for every fields it will create and save record in db and return the saved object 

syntax: -  Inside view.py : from .models import Invoice ... def func(request): Invoice.Object.Create(Data) return render(request,'filepath',{}) - Invoice = Model, Object = Manager , Create = Method for create a new record , {} = it means no extra data pass to template "{Model.Object.Create(Data)}"

ex: def func(request): Invoice.Object.Create(Cust_Name="Adfar",Sal=15000.00,is_paid=False,Invoice_num="INV-001") return render(request,'/invoices/template/invoice_list.html',{})

# for fetch data/record invoice - invoice=example
get: it will return only a single record which is based on condition after user input or selection it match record with condition and return in python object , it can be crash sometime like not match

syntax: - Inside view.py: def func(request):invoice = Invoice.Object.get(cond) data = {'invoice':invoice} return render(request,'filepath',{}), cond (like invoice_num = "INV-001") , Model = Invoice , Object = Manager , get = Method for fetch single record based on cond or user input, pass unique value to get single record (like id , unvoice_num , emp_num, emp_id etc)

ex: def show_invoice(request): invoice = Invoice.Object.get(invoice='INV-001') data = {'invoice':invoice} return render
(request,'invoice/template/invoice_detail.html',{}) 

# filtering multiple data/records based on condition  , invoice - invoice=example
filter: it will return mulitple record python object after matching coniditon with record after filtering the db or all records in db, collection of record return, it will not crash because of returing empty collection if not match

syntax: - In view.py : def func(request): variable_name = Model.Object.filter(cond) data = {"Obj_value_variable_name",variable_name} return render(request,'filepath',data)

ex: def show_unpaid_invoices(request):unpaid_invoice= Invoice.Object.filter(is_paid=False) data = {'unpaid_invoices':unpaid_invoices} return render (request,'invoice/template/invoice_list.html',data) 

# for update record/data invoice - invoice=example 

update: it will change the record of field after matching the condition (like is_paid = False to True),we can update multiple reecord at a time by seprateing using comma (,)

syntax: - In view.py: def func(request): variable_name = Model.Object.filter(cond).update(value wants tp update) data = {"Obj_value_variable_name",variable_name} return render(request,'filepath',data})

ex: def mark_as_paid_invoices(request): Invoice.Object.filter(invoice_num="INV-001").update(is_paid=True) all_invoices = Invoice.Object.filter(is_paid=False) data = {'all_invoices':all_invoices} return render (request,'invoice/template/invoice_list.html',data) 