# SalesBase
##### By Alejandro Spara Dominguez

##### This project was developed for the fourth project with the Code Institute and the Full Stack Development Course. 

### [Click here to view the app.](https://salesbase-asd.herokuapp.com/)
##### To access the admin view you must be logged in as an admin user and enter https://salesbase-asd.herokuapp.com/admin/ in your browser

### [Click here to view the repository.](https://github.com/AlexSD92/SalesBase)

# Table of Contents:

1. [Why](#Why)
2. [User Experience (UX)](#user-experience-UX)
    1. [Target Audience](#target-audience)
    2. [User Stories](#user-stories)
    3. [Strategy](#strategy)
    4. [Scope](#scope)
    5. [Skeleton](#skeleton)
3. [Features](#features)
    1. [Current Features](#current-features)
    2. [Future Features](#future-features)
4. [Technologies](#technologies)
    1. [Languages](#languages)
    2. [Other Technologies, Frameworks and Libraries](#other-technologies-frameworks-and-libraries)
5. [Testing and Development](#testing-and-development)
    1. [Sprints](#sprints)
    2. [Manual Testing](#manual-testing)
    3. [Automated Testing](#automated-testing)
6. [Deployment](#deployment)
    1. [Cloning and Forking the GitHub Repository](#cloning-and-forking-the-github-repository)
    2. [Local Deployment](#local-deployment)
    3. [Remote Deployment](#remote-deployment)
7. [Credits](#credits)


# User Experience (UX)

## Target Audience

**Sales Professionals** are the target audience for SalesBase.
- Hunting for new business - create new contacts, accounts and opportunities.
- Manage existing business - update and manage existing contacts, accounts and opportunities. 
- Administrators - manage and oversee a sales team and all their contacts, accounts and opportunities. 

## User Stories

1. User Story: Log In
    - As a **Sales Person** I can **log in** so that **I can view my sales dashboard**.

2. User Story: Dashboard
    - As a **Sales Person** I can **view my dashboard** so that **I can see an overview of my recent accounts, contacts and opportunities**.

3. User Story: Accounts, Contacts & Opportunity Access
    - As a **Sales Person** I can **access my accounts, opportunities and opportunities at any point within the crm** so that **I can quickly accomplish tasks and get the information I need**.

4. User Story: Manage Users and Rights
    - As an **Sales Person** I can **see visual representations of my sales data** so that **more quickly digest my data and understand how I am performing against target**.

5. User Story: Accounts View
    - As a **Sales Person** I can **access an account view** so that **I may view the accounts I am responsible for**.

6. User Story: Access Individual Account Information
    - As a **Sales Person** I can **click on individual accounts from my list view** so that **view more detailed information**.

7. User Story: Create New Accounts
    - As a **Sales Person** I can **create new accounts** so that **I may add new customers to my accounts view**.

8. User Story: Edit Existing Accounts
    - As a **Sales Person** I can **edit existing account information and add notes** so that **I can update the account when required.**.

9. User Story: View Opportunities
    - As a **Sales Person** I can **see my opportunities in a list view** so that **I can manage my current opportunities**.

10. User Story: View Individual Opportunities
    - As a **Sales Person** I can **view individual opportunities** so that **I may view more detailed information, such as notes**.

11. User Story: Create New Opportunities
    - As a **Sales Person** I can **create new opportunities** so that **I can manage new sales and update my pipeline**.

12. User Story: Edit Existing Opportunities
    - As a **Sales Person** I can **edit existing opportunities** so that **I can update opportunity status, notes, value, etc.**.

13. User Story: View Contacts
    - As a **Sales Person** I can **view contacts in a list view** so that **may view and manage all of my contacts**.

14. User Story: View Individual Contacts
    - As a **Sales Person** I can **view specific contacts** so that **I may view more detailed information**.

15. User Story: Create New Contacts
    - As a **Sales Person** I can **create new contacts** so that **I can add to my database of contacts and update my contact list**.

16. User Story: Edit Existing Contacts
    - As a **Sales Person** I can **edit my existing contacts** so that **I can keep my contacts up to date and manage my contacts**.

17. User Story: Manage Users and Rights
    - As an **Admin** I can **fully manage users on the platform and their rights** so that **manage what my team are capable of doing with the data**.

18. User Story: Sales Overview
    - As an **Admin** I can **see every action by every user** so that **see and understand the behaviour of my team**.

19. User Story: User Profiles
    - As a **Sales Person**, I can **edit the profile that gets created when I register for an account** so that **I may update information about myself, such as my position within the organisation, my expertise, and a profile picture**.

20. User Story: Log Out
    - As a **Sales Person**, I can **log out of my account** so that **I can protect my data once I am finished working**.

21. User Story: Delete Existing Accounts
    - As an **Sales Person** I can **delete my accounts** so that **I can manage duplicate accounts**.

22. User Story: Delete Existing Contacts
    - As an **Sales Person** I can **delete my contacts** so that **I can manage duplicate contacts**.

23. User Story: Delete Existing Opportunities
    - As an **Sales Person** I can **delete my opportunities** so that **I can manage duplicate opportunities**.

24. User Story: Register For Account
    - As a **User** I can **register for an account**, so that **I may use the platform**.


## Strategy

Design a straight-forward CRM that is intuitive to use and has a small learning curve. Users will be able to access accounts, users and opportunities at any point within the CRM and be able to quickly and accurately navigate to specific instances of accounts, users and opportunities.

## Scope

- Create new accounts, users and opportunities. 
- Update existing accounts, users and opportunities. 
- Delete existing accounts, users and opportunities. 
- Manage a user profile.

## Skeleton

Mobile and desktop wireframes can be found [here](assets\wireframes).

# Features

## Current Features

- User registration system
- User activation system
- Log in method
- Log out method
- C.R.U.D. accounts, opportunities and contacts
- Access a profile and update profile details, including image

## Future Features

- Reset password
- Additional authentication, such as email authentication, 2FA, etc.
- Relate accounts, users and opportunities
    - For example, when you view an account detail view, you would be able to see associated opportunities and contacts
- View pipeline totals, such as total potential revenue, total opportunities
- Account, users and opportunity statuses
- Messaging and commenting feature
- Filtering objects by status
- Clear rights, such as manager vs user

# Technologies

## Languages

- [Python](https://www.python.org/)
- [HTML](https://www.w3schools.com/html/)
- [CSS](https://www.w3schools.com/css/)
- [SQL](https://www.w3schools.com/sql/)

## Other Technologies, Frameworks and Libraries

- [Django](https://www.djangoproject.com/)
- [Heroku](https://id.heroku.com/)
- [Heroku Postgres](https://www.heroku.com/postgres)
- [Bootstrap 4](https://getbootstrap.com/docs/4.0/getting-started/introduction/)
- [Cloudinary](https://cloudinary.com/)
- [Django Money](https://pypi.org/project/django-money/)
- [Flask](https://flask.palletsprojects.com/en/2.1.x/)
- [Gunicorn](https://gunicorn.org/)
- [Jinja2](https://palletsprojects.com/p/jinja/)
- [Pillow](https://pypi.org/project/Pillow/2.2.1/)
- [Psycopg2-Binary](https://pypi.org/project/psycopg2-binary/)
- [Whitenoise](http://whitenoise.evans.io/en/stable/)

# Testing and Development

## Sprints

Scheduled Dates | Focus | Use Case(s) | Total | Dates Completed
:--- | :--- | :--- | :---: | ---:
24/04/22 - 30/04/22 <br> Week 1 | Initial Project Setup <br> and deployment | Log In <br> Log Out <br> User Profiles <br> Manage Users and Rights | 4 | 24/04/22 - 10/05/22 | 
01/05/22 - 07/05/22 <br> Week 2 | Accounts | Accounts View <br> Access Individual Account Information <br> New Accounts <br> Edit Existing Accounts <br> Delete Existing Accounts | 5 | 24/05/22 - 29/05/22
08/05/22 - 14/05/22 <br> Week 3 | Opportunities | View Opportunities <br> View Individual Opportunities <br> Create New Opportunities <br> Edit Existing Opportunities <br> Delete Existing Opportunities | 5 | 24/05/22 - 29/05/22
15/05/22 - 21/05/22 <br> Week 4 | Contacts | View Contacts <br> View Individual Contacts <br> Create New Contacts <br> Edit Existing Contacts <br> Delete Existing Contacts | 5 | 24/05/22 - 29/05/22
22/05/22 - 28/05/22 <br> Week 5 | Database & Admin | Manage Users and Rights | 4 | 24/05/22 - 29/05/22
29/05/22 - 04/06/22 <br> Week 6 | Dashboard | Dashboard <br> Accounts, Contacts & Opportunity Access <br> Sales Overview | 3 | 24/05/22 - 20/06/22
05/06/22 - 11/06/22 <br> Week 7 | Manual & Automated Testing |  | 0 | 21/06/22 - 26/06/22
12/06/22 - 18/06/22 <br> Week 8 | Styling |  | 0 | 10/06/22 - 20/06/22
19/06/22 - 25/06/22 <br> Week 9 | Submission Checks |  | 0 | 21/06/22 - 28/06/22
26/06/22 - 30/06/22 <br> Submission | Submission |  | 0 | 30/06/22

## Manual Testing

Test | Desired Functionality | Working As Intended (Y / N)
--- | --- | :---:
Log In | Incorrect input results in an error message. Correct input logs the user in | Yes
Register | Accounts cannot be created with existing usernames. Successful registration results in message telling user to contact administrator | Yes
Account Approval | Administrator needs to activate new user accounts | Yes
Log Out | When a user clicks log out, they are redirected to the log out page and must log in again | Yes
URLs | All URLs work as intended and redirect users to correct pages | Yes
CRUD | Create, update and delete functionality in place across accounts, contacts and opportunities | Yes
Profile | Profile is accessible and users can update their profile picture and username | Yes
Admin | Only accessible by super user | Yes
Cloudinary | CSS and images stored on cloudinary, including new uploads | Yes
Responsiveness | All components collapse into mobile view | Yes
Authentication | Users must be logged in to access certain pages | Yes
Pagination | Paginates at 5 and links working correctly | Yes

## Automated Testing

[Coverage](https://pypi.org/project/coverage/) was used to determine the test coverage for this project. 

Original report can be found [here](assets\coverage\coverage.jpg), demonstrating 95% coverage.

# Deployment

## Cloning and Forking the GitHub Repository

In order to make changes to this code without affecting the original code, you must fork the repository. This means that you will be given a copy of the code for that moment in time. In order to do this, you must:

1. Create a GitHub account (if you have one already, skip this step).
2. Navigate to the [repository](https://github.com/AlexSD92/SalesBase).
3. Near the top right, click 'Fork'.
4. A copy of the repository will be available for you to use within your own remote repository.

In order to clone the repository, you must:

1. Create a GitHub account (if you have one already, skip this step).
2. Navigate to the [repository](https://github.com/AlexSD92/SalesBase) you would like to clone.
3. Near the top, select 'Code' in the dropdown.
4. Copy the HTTPS address.
5. Navigate to the directory where you would like to create a new directory using the terminal.
    - Use the pwd command to know where you currently are.
    - Use cd followed by the directory name to change directories.
    - use mkdir followed by a new directory name to create a new directory.
6. Enter 'git clone https://github.com/AlexSD92/SalesBase.git'.
7. The repository will be cloned into your chosen directory.

## Local Deployment

1. Create a new folder in your preferred IDE.
    - If you would like to copy this project exactly, use VSCode. 
2. Give your folder a project name, for example '*salesbase*'.
3. Open up your terminal.
4. First and foremost, install Django by typing '*pip install Django*', and wait for the installation to finish.
5. Time to start the project, so type '*django-admin startproject [insert your project name here]*' and wait for the folders and files to be created. Our project is named *crm*.
6. In your terminal, type '*python manage.py runserver*'
7. Your project should be hosted locally.
8. You should view the following message 'The install worked successfully! Congratulations!'.

## Remote Deployment

##### What you need to do locally

1. Create a new folder in your preferred IDE.
    - If you would like to copy this project exactly, use VSCode. 
2. Give your folder a project name, for example '*salesbase*'.
3. Open up your terminal.
4. First and foremost, install Django by typing '*pip install Django*', and wait for the installation to finish.
5. Then install psycopg2-binary, gunicorn and dj-database-url by typing '*pip install psycopg2-binary gunicorn dj-database-url*' into your terminal and wait for the installation to finish.
6. Time to start the project, so type '*django-admin startproject [insert your project name here]*' and wait for the folders and files to be created. Our project is named *crm*.
7. In your root directory, use the following command to freeze your requirements and create your requirements.txt file, '*pip freeze > requirements.txt*'.
8. In your root directory, you also need to create a procfile. Create the file manually to avoid case-sensitivity issues and to ensure that it only contains UTF-8 characters. This is done by right clicking in to your root directory and clicking *New File*. Name this file '*Procfile*'. Please note, no file extension is required. 
9. Within the procfile, type the following: '*web: gunicorn [insert your project name here].wsgi*'. For example, for this project, you would type *web: gunicorn crm.wsgi*.
10. Create your *.gitignore* and include:
    - *.log
    - *.pot
    - *.pyc
    - __pycache__/
    - local_settings.py
    - *.sqlite3
    - media
    - .env 
    - .venv 
    - env/ 
    - venv/ 
    - ENV/ 
    - env.bak/ 
    - venv.bak/

##### What you need to do with Git and GitHub

11. Create a GitHub account if you don't already have one.
12. Create a new repository by clicking the green button labelled as *New*, and name your repo the same as you named your project locally for consistency.
13. Decide whether you want the repo to be either public or private.
14. Don't select to initialise your repository with any starting files, you can create these later on and push them to the repo. 
15. Click the green *Create repository* button.
16. On your command line, execute the following:
    1. *git init*
    2. *git add .*
    3. *git commit -m "Initial commit"*
    4. *git branch -M main*
    5. *git remote add origin [insert your SSH link]*
        - Your SSH link should look something like https://github.com/AlexSD92/SalesBase.git
    6. *git push -u origin main*
17. Your local files are now linked to your github repository and from here on out, you only need to use the add, commit and push commands to update your repo.

##### What you need to do with Heroku

18. Create an account if you don't already have one. 
19. Click on create new app.
20. Give your app a name, choose your region and click create.
21. Click on the 'Resources' tab first. 
    - Under Add-ons, search and select 'Heroku Postgres'.
    - Select your plan name, most likely 'Hobby Dev - Free'.
    - Then click 'Submit Order Form'
22. Next head to your settings and click on 'Reveal Config Vars'.
    - Notice that Heroku has created a 'DATABASE_URL' for use later.
    - Include requirements.txt as a key and copy all of the contents of your requirements.txt into the value field. 
    - Within your project folder and in the settings.py file, you should find a 'SECRET_KEY'. Include this as a key and the secret key as the value. You can edit this to be whatever you like, just be sure to include it in your Config vars. 
    - Finally, for development, you will need to disable the collection of static files. The file key value pair you need to add is 'DISABLE_COLLECTSTATIC=1'.
23. Click on 'Add Buildpack' and select python, then 'Save changes'.

##### The final things you need to do locally

24. At the top of your settings.py file, '*import os*' and '*import dj_database_url*'.
25. Ensure DEBUG is set to True for development purposes or True for production.
26. Set your 'ALLOWED_HOST' to ['[*your heroku project name*].herokuapp.com']. For example, 'ALLOWED_HOSTS = ['salesbase.herokuapp.com']
27. Comment out the existing database and include a new DATABASE setting. 
    - Go back to your Heroku config vars and grab the DATABASE_URL key value. 
    - Include it as your new DATABASE setting. For example: 
    DATABASE = {
        'default': dj_database_url.parse('insert DATABASE_URL KEY VALUE'),
    }
28. In your terminal, type '*python manage.py migrate*'.
    - You should see all migrations with a green OK status.
28. Head back to Heroku and click on the 'Deploy' tab.
29. Select your 'Deployment method' as 'GitHub'. 
    - Follow the prompts to link your GitHub account.
    - Search for the repository you created. 
    - Click 'Connect'.
30. Head down to the 'Manual deploy' section and click on 'Deploy Branch'. 
31. Wait for Heroku to build your app and then open your app.
32. You should view the following message 'The install worked successfully! Congratulations!'. 

# Credits

1. [The Django Documentation](https://docs.djangoproject.com/en/4.0/)
    - For the details of how django works.

2. [W3Schools](https://www.w3schools.com/django/)
    - For their Django tutorial.

3. [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django)
    - For their Django tutorial.

4. [Corey Schafer](https://coreyms.com/development/python/python-django-tutorials-full-series)
    - For excellent Python and Django explanations and tutorials.

5. [Stack Overflow](https://stackoverflow.com/)
    - Amazing forums with great and detailed discussions demonstrating how to write code and why it should be written that way.

6. [Code Institute](https://codeinstitute.net/)
    - For their learning platform and support. 

7. [Django for Beginners: Build Websites with Python and Django](https://djangoforbeginners.com/)
    - A great, project-base resource for any beginner learning Django.

8. Chris Quinn, Mentor
    - Excellent resource and a wealth of knowledge and insight.

---

[RETURN TO THE TOP](#SalesBase)
