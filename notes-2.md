## Recap

- Covered

## Django Templates

Templates have the static part of Django HTML
Special syntax to add the dynamic content

Contributors/Employee Information

[pic]
[name]
[Designation]


Components of Template
- Variables

    {{ var_name }}

- Looping and Conditional / Tags

    {% %}

    For loop: 
    <ul>

    {% for element in name_of_list %}
        <li>{{ element }}</li>
    {% endfor %}
    </ul>

- Conditionals:

    {% if IMDb_rating == "8.5"%}

    {% elif condition %}

    {% else %}

    {% endif %}

- Comments

    {# #} Single line comments
    {% comment %} {% endcomment %} Multiline comments

- Filters
    - length -> length of the variable string
    - default -> var_name | default:"Default statement"
    - title -> 
    - lower ->
    - make_list -> 


Steps followed:

    - We created templates folder inside main project directory, and then add folder containing templates for that specific application

    - In that application folder, just create an HTML file with all the context variable names


    - Tell Django, that where it can find these templates, thats why we change in settings.py. We add TEMPLATES_DIR in TEMPLATES config

    - In views.py add the response return render(request, "firstapp/main.html", context=var)

    var is a python dictionary 
    var = {
        "name": "Rahul",
        "age": "21"
    }


- Relative URLS

    Exact paths won't work <a href="main.html"> </a>
    {% url %}

   <a href=" {% url 'about' num=2 %}"> </a>

- Inheritance
    -> base.html

    ```html
    <!DOCTYPE html>
    <html lang="en">
    <head>
    <title>{% block title %} {% endblock %}</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
    </head>
    <body>

    <nav class="navbar navbar-default navbar-static-top">
    <div class=container>
        <ul class= "nav navbar-nav">
        <li><a class="navbar-brand" href="{% url 'home' %}">Home</a></li>
        <li><a class="navbar-brand" href="{% url 'about' %}">about</a></li> 
        <li><a class="navbar-brand" href="{% url 'search' %}">search</a></li>
        </ul>
    </div>
    </nav>  

    
    <div class="container">
    {% block content %}<!-- Page content   -->{% endblock %}
    </div>

    </body>
    </html>
    ```

    Search.html
    ```html
    <!DOCTYPE html>
    {% extends "firstapp/base.html" %}

    {% block title %} Search {% endblock %}

    {% block content %}

    <h3>Welcome to Search Page</h3>

    {% endblock %}


    ```




