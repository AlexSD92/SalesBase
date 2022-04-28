# SalesBase
##### By Alejandro Spara Dominguez

##### This project was developed for the fourth project with the Code Institute and the Full Stack Development Course. 

### [Click here to view the app.](https://salesbase-asd.herokuapp.com/)

### [Click here to view the repository.](https://github.com/AlexSD92/SalesBase)

# Table of Contents:

1. [Why](#Why)
2. [User Experience (UX)](#user-experience-UX)
    1. [Target Audience](#target-audience)
    2. [User Stories](#user-stories)
    3. [Strategy](#strategy)
    4. [Scope](#scope)
3. [Features](#features)
    1. [Current Features](#current-features)
    2. [Future Features](#future-features)
4. [Technologies](#technologies)
    1. [Languages](#languages)
    2. [Other Technologies, Frameworks and Libraries](#other-technologies-frameworks-and-libraries)
5. [Testing and Development](#testing-and-development)
    1. [Sprints](#sprints)
    2. [Code Tests](#code-tests)
    3. [User Tests](#user-tests)
    4. [Bugs and Fixes](#bugs-and-fixes)
6. [Deployment](#deployment)
    1. [GitHub Pages](#github-pages)
    2. [Cloning and Forking the GitHub Repository](#cloning-and-forking-the-github-repository)
    3. [Local Deployment](#local-deployment)
    4. [Remote Deployment](#remote-deployment)
7. [Credits](#credits)


# User Experience (UX)

## Target Audience

**Sales Professionals** are the target audience for SalesBase.
- *Sales Executives* will be able to use SalesBase while they are hunting for new business. They will be able to add on new contacts, accounts and opportunities. 
- *Account Managers* will be able to use SalesBase while they are managing existing business. They will be able to update and manage existing contacts, accounts and opportunities.
- *Sales Managers* and beyond will be able to use SalesBase to manage and oversee a sales team and all of their contacts, accounts and opportunities to drive growth and sales. 

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

17. User Story: Relate Accounts, Contacts and Opportunities
    - As a **Sales Person** I can **associate accounts, contacts and opportunities** so that **I can effectively manage my data, information and pipeline**.

18. User Story: Delete Accounts, Contacts and Opportunities
    - As an **Admin** I can **delete accounts, contacts and opportunities** so that **remove unnecessary or out of date data**.

19. User Story: Create Accounts, Contacts and Opportunities
    - As an **Admin** I can **create accounts, contacts and opportunities** so that **I can behave like a salesperson**.

20. User Story: Manage Users and Rights
    - As an **Admin** I can **fully manage users on the platform and their rights** so that **manage what my team are capable of doing with the data**.

21. User Story: Sales Overview
    - As an **Admin** I can **see every action by every user** so that **see and understand the behaviour of my team**.

22. User Story: User Profiles
    - As a **Sales Person**, I can **edit the profile that gets created when I register for an account** so that **I may update information about myself, such as my position within the organisation, my expertise, and a profile picture**.

23. User Story: Log Out
    - As a **Sales Person**, I can **log out of my account** so that **I can protect my data once I am finished working**.

24. User Story: Delete Existing Accounts
    - As an **Sales Person** I can **delete my accounts** so that **I can manage duplicate accounts**.

25. User Story: Delete Existing Contacts
    - As an **Sales Person** I can **delete my contacts** so that **I can manage duplicate contacts**.

26. User Story: Delete Existing Opportunities
    - As an **Sales Person** I can **delete my opportunities** so that **I can manage duplicate opportunities**.


## Strategy

Design a straight-forward CRM that is intuitive to use and has a small learning curve. Users will be able to access accounts, users and opportunities at any point within the CRM and be able to quickly and accurately navigate to specific instances of accounts, users and opportunities.

## Scope

- Create new accounts, users and opportunities. 
- Update existing accounts, users and opportunities. 
- Delete existing accounts, users and opportunities. 
- Manage a user profile.

# Testing and Development

## Sprints

### Plan

Dates | Focus | Use Case(s) | Total
:--- | :--- | :--- | :---:
24/04/22 - 30/04/22 <br> Week 1 | Initial Project Setup <br> and deployment | Log In <br> Log Out <br> User Profiles <br> Manage Users and Rights | 4
01/05/22 - 07/05/22 <br> Week 2 | Accounts | Accounts View <br> Access Individual Account Information <br> New Accounts <br> Edit Existing Accounts <br> Delete Existing Accounts | 5
08/05/22 - 14/05/22 <br> Week 3 | Opportunities | View Opportunities <br> View Individual Opportunities <br> Create New Opportunities <br> Edit Existing Opportunities <br> Delete Existing Opportunities | 5
15/05/22 - 21/05/22 <br> Week 4 | Contacts | View Contacts <br> View Individual Contacts <br> Create New Contacts <br> Edit Existing Contacts <br> Delete Existing Contacts | 5
22/05/22 - 28/05/22 <br> Week 5 | Database & Admin | Relate Accounts, Contacts and Opportunities <br> Delete Accounts, Contacts and Opportunities <br> Create Accounts, Contacts and Opportunities <br> Manage Users and Rights | 4
29/05/22 - 04/06/22 <br> Week 6 | Dashboard | Dashboard <br> Accounts, Contacts & Opportunity Access <br> Sales Overview | 3
05/06/22 - 11/06/22 <br> Week 7 | Manual & Automated Testing |  | 0
12/06/22 - 18/06/22 <br> Week 8 | Styling |  | 0
19/06/22 - 25/06/22 <br> Week 9 | Submission Checks |  | 0
26/06/22 - 30/06/22 <br> Submission | Submission |  | 0

### Actuals

Dates | Focus | Use Case(s) | Total
:--- | :--- | :--- | :---:
24/04/22 - 30/04/22 <br> Week 1 | Initial Project Setup <br> and deployment | Log In <br> Log Out <br> User Profiles <br> Manage Users and Rights | 4
01/05/22 - 07/05/22 <br> Week 2 | Accounts | Accounts View <br> Access Individual Account Information <br> New Accounts <br> Edit Existing Accounts <br> Delete Existing Accounts | 5
08/05/22 - 14/05/22 <br> Week 3 | Opportunities | View Opportunities <br> View Individual Opportunities <br> Create New Opportunities <br> Edit Existing Opportunities <br> Delete Existing Opportunities | 5
15/05/22 - 21/05/22 <br> Week 4 | Contacts | View Contacts <br> View Individual Contacts <br> Create New Contacts <br> Edit Existing Contacts <br> Delete Existing Contacts | 5
22/05/22 - 28/05/22 <br> Week 5 | Database & Admin | Relate Accounts, Contacts and Opportunities <br> Delete Accounts, Contacts and Opportunities <br> Create Accounts, Contacts and Opportunities <br> Manage Users and Rights | 4
29/05/22 - 04/06/22 <br> Week 6 | Dashboard | Dashboard <br> Accounts, Contacts & Opportunity Access <br> Sales Overview | 3
05/06/22 - 11/06/22 <br> Week 7 | Manual & Automated Testing |  | 0
12/06/22 - 18/06/22 <br> Week 8 | Styling |  | 0
19/06/22 - 25/06/22 <br> Week 9 | Submission Checks |  | 0
26/06/22 - 30/06/22 <br> Submission | Submission |  | 0


# Deployment

## Cloning and Forking the GitHub Repository

In order to make changes to this code without affecting the original code, you must fork the repository. This means that you will be given a copy of the code for that moment in time. In order to do this, you must:

1. Create a GitHub account (if you have one already, skip this step).
2. Navigate to the [repository](https://github.com/AlexSD92/SalesBase).
3. Near the top right, click 'Fork'.
4. A copy of the repository will be available for you to use within your own remote repositories.

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
7. The repository will be cloned in to your chosen directory.

## Local Deployment

1. Create a new folder in your preferred IDE.
    - If you would like to copy this project exactly, use VSCode. 
2. Give your folder a project name, for example '*salesbase*'.
3. Open up your terminal.
4. First and foremost, install Django by typing '*pip install Django*', and wait for the installation to finish.
5. Time to start the project, so type '*django-admin startproject [insert your project name here]*' and wait for the folders and files to be created. Our project is named *crm*.
6. In your terminal, type '*python manage.py runserver*'
7. Your project should be hosted locally.
8. You should view the following message 'The install worked succesfully! Congratulations!'.

## Remote Deployment

##### What you need to do locally

1. Create a new folder in your preferred IDE.
    - If you would like to copy this project exactly, use VSCode. 
2. Give your folder a project name, for example '*salesbase*'.
3. Open up your terminal.
4. First and foremost, install Django by typing '*pip install Django*', and wait for the installation to finish.
5. Then install psycopg2-binary, gunicorn and dj-database-url by typing '*pip install psycopg2-binary gunicorn dj-database-url*' in to your terminal and wait for the installation to finish.
6. Time to start the project, so type '*django-admin startproject [insert your project name here]*' and wait for the folders and files to be created. Our project is named *crm*.
7. In your root directory, use the following command to freeze your requiremens and create your requirements.txt file, '*pip freeze > requirements.txt*'.
8. In your root directory, you also need to create a procfile. Create the file manually to avoid either case-sensitivity issues and to ensure that it only contains UTF-8 characters. This is done by right clicking in to your root directory and clicking *New File*. Name this file '*Procfile*'. Please note, no file extension is required. 
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
13. Decide whether you want for the repo to be either public or private.
14. Don't select to initialize your repository with any starting files, you can create these later on and push them to the repo. 
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
    - Include requirements.txt as a key and copy all of the contents of your requirements.txt in to the value field. 
    - Within your project folder and in the settings.py file, you should find a 'SECRET_KEY'. Include this as a key and the secret key as the value. You can edit this to be whatever you like, just be sure to include it in your Config vars. 
    - Finally, you need to deal with any static files. The file key value pair you need to add is 'DISABLE_COLLECTSTATIC=1'.
    - An alternative would be to use WhiteNoise. The documentation for installing whitenoise to a django project can be found [here](http://whitenoise.evans.io/en/stable/). If you are using WhiteNoise, then you don't need to set DISABLE_STATIC in Heroku.
23. Click on 'Add Buildpack' and select python, then 'Save changes'.

##### The final things you need to do locally

24. At the top of your settings.py file, '*import os*' and '*import dj_database_url*'.
25. Decide whether you want to set your 'DEBUG' as True or False.
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
    - Search for the repository your created. 
    - Click 'Connect'.
30. Head down to the 'Manual deploy' section and click on 'Deploy Branch'. 
31. Wait for Heroku to build your app and then open your app.
32. You should view the following message 'The install worked succesfully! Congratulations!'. 

