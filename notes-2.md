# Github Repo https://github.com/rahulgrover99/django-todo-app

1. Login
2. Register
3. Logout functionality
4. Dashboard -> We can see only the todays of the logged in user
5. Ensure that other people cant see the todos of other people


6. That we dont want user to open dashboard as anonymous


1. Login
    - username
    - password
    - submit button

    If you are not user? Register button

    If a user is already logged in simply redirect to dashboard

    -> If combination is correct
        - redirect to dashboard
    -> If incorrect
        - display a message 
        - keep the user on the same login page


2. Register
    - username
    - password
    - password confirmation
    - email 
    - Register button

    - if already a user -> login button

3. Logout functionality 
    - Logout button on dashboard
    - if user is logged in then on home page as well
    - Redirect to home


4. Dashboard
    - Welcome {username}
    - Task lists of that user
    - Add task list button here
    - All tasks of that user
    - Add task button here
    - logout button

5. Home
    - Welcome to todo app
    - Register
    - Login/Logout 


To ensure the last requirement

Some way to associate users with Task Lists and Tasks

Task List -> id | name | created_at | user_id


Task -> id | content | created_at | deadline | status | task_list_id