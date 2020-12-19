# PyQuotes

PyQuotes is a Django-based web application and REST API. That will allow you to launch an online quotes service.

![](https://img.shields.io/github/stars/mavenium/PyQuotes) ![](https://img.shields.io/github/forks/mavenium/PyQuotes) ![](https://img.shields.io/github/issues/mavenium/PyQuotes) ![](https://img.shields.io/twitter/url?url=https%3A%2F%2Fgithub.com%2Fmavenium%2FPyQuotes)

------------
### Features

- Has a person management section to create and edit a person (Full Name, Bio, Avatar)
- Has a category section to create and edit category (Title)
- Has a quote section to create and edit quote (Content, Person, Category)
- Has a REST-API to show content in other client user interface
- Add a category from front-end
- Add a person from front-end
- Add a quote from front-end
- Displays the list of quotes as paged in Index
- Contains random quotes display page
- Displays the list of people as paged
- Show list of persons as widgets
- Show list of categories as widgets
- Show quotes by person
- Show quotes by category
- Used by "Django Admin" to manage quotes and categories and persons
- Used by "Bootstrap v4.x" to create front-end web application
- Used by "Sqlite" to create DB

------------
### Special Thanks

| Python | Django | Pycharm |
| ------------- | ------------- | ------------- |
| [![](https://s17.picofile.com/file/8418101118/python.png)](https://www.python.org "Python")  | [![](https://s17.picofile.com/file/8418100976/django.png)](https://www.djangoproject.com "Django")  | [![](https://s17.picofile.com/file/8418101034/pycharm.png)](https://www.jetbrains.com/pycharm/ "Pycharm")  |

------------
### Screenshots

![](https://raw.githubusercontent.com/mavenium/PyQuotes/master/Screenshots/Home.png)
> Index Page

![](https://raw.githubusercontent.com/mavenium/PyQuotes/master/Screenshots/Persons.png)
> Persons Page

![](https://raw.githubusercontent.com/mavenium/PyQuotes/master/Screenshots/Random.png)
> Random Quotes Page

![](https://raw.githubusercontent.com/mavenium/PyQuotes/master/Screenshots/Quotes%20By%20Person.png)
> Show Quotes By Person

![](https://raw.githubusercontent.com/mavenium/PyQuotes/master/Screenshots/Quotes%20By%20Category.png)
> Show Quotes By Category
>
![](https://raw.githubusercontent.com/mavenium/PyQuotes/master/Screenshots/Create_Category.png)
> Add Category From Front-End
>
![](https://raw.githubusercontent.com/mavenium/PyQuotes/master/Screenshots/Create_Person.png)
> Add Person From Front-End
>
![](https://raw.githubusercontent.com/mavenium/PyQuotes/master/Screenshots/Create_Quote.png)
> Add Quote From Front-End

------------
### How to install and run (GNU/Linux and Mac)
                
1. Install `git`,`python3`, `pip3`, `virtualenv` in your operating system
2. Create a development environment ready by using these commands
```
git clone https://github.com/mavenium/PyQuotes		# clone the project
cd PyQuotes		# go to the project DIR
virtualenv -p python3 .venv		# Create virtualenv named .venv
source .venv/bin/activate		# Active virtualenv named .venv
pip install -r requirements.txt		# Install project requirements in .venv
python manage.py makemigrations		# Create migrations files
python manage.py migrate		# Create database tables
python manage.py collectstatic		# Create statics files
python manage.py runserver		# Run the project
```
3. Go to  `http://127.0.0.1:8000/` to use project
                

------------
### REST API

```
http://127.0.0.1:8000/api/persons/		# JSON objects of persons
http://127.0.0.1:8000/api/categories/		# JSON objects of categories
http://127.0.0.1:8000/api/quotes/		# JSON objects of quotes
http://127.0.0.1:8000/api/quotes_random/	# JSON objects of quotes by random
http://127.0.0.1:8000/api/qbp/pk/		# JSON objects of quotes by person pk
http://127.0.0.1:8000/api/qbc/pk/		# JSON objects of quotes by category pk
```

------------
### TODO list

- [ ] Create useful tests
- [x] Create user profile & Login/Logout forms in front-end
- [ ] Create update form for person/category/quote objects models in front-end
- [ ] Create delete action for person/category/quote objects models in front-end
