# project description
Our project’s aim is to create a client-server project that acts as a community hub; in other words, a volunteer network. With the use of the Google API we display community fridges. When local organizations are in need of volunteers, sanitary products, etc., they can create a posting in order to gain traction in the community. Users (organizations and individuals) can post their events and projects for others to find these community events near them. There already exists websites where volunteer services are provided, however, our aim is to be a medium through which organizations can get in contact with locals and vice versa. We also offer filter options and a thread of posts wil be displayed based on the input. Our goal is to create a platform that can continuously be improved upon in order to give nonprofits and communities an efficient space to manage and promote their efforts. 

**Actions** 
We want to enable Login capabilities for users. For extra functionality, we would like all users to be able to interat with one another in a public commenting section. Additionally, users should be able to make posts, like posts (so that they can refer back to them later on). Organizations and users with a following on other websites (Facebook, Twitter, etc...) should be able to link these pages on this site.

**Setup**
Currently, `make prod` commits and pushes to GitHub, and `make dev_env` executes the announcement "Installing developer requirements". Later on, what it will do is download everything you need to run the environment.


**Actionable Requirements**
* Each user can:
  * Register in the system
      * Upon registering, they will need to provide their name and email.
      * If a username already exists, the community member will be notified to change it.
  * Modify an account:
    * change basic account information (i.e. profile picture, username, display name, password, etc.)
  * Create a post
    * 	A post is an informational graphic or description of issues that may be occurring within a specific community. It can also be an ad promoting a certain cause or event. Within a post you can incorporate text, images, gifs, etc. 
  * Modify a post 
    * 	Allows user to make edits to all parts of a post. They can modify the text or remove/change attachments to their post. 
  * Delete a post 
    * 	Removes a post from the user’s account and from the community feed.  
  * Comment on a post
    * Users can react to a post created by another user. This is where users can leave any questions in regards to the post or questions they would like the the author of the post to answer.
  * Like a post
    * A 'like' of a post represents that the user is interested on what has been uploaded by the organization when scrolling through the main feed.
    * A user can also unlike a post that they have liked
 
  **How to get set up**
  * To get your django project set up, you must first make sure to have the latest version of Django installed on your device. From the command line, cd into a directory where you want to store code that establishes your Django project, and run this command: $ django-admin startproject mysite
  This creates a mysite directory in your current directory. Startproject sohuld create:
  - The outer mysite/ directory.
  - manage.py
  - The inner mysite/ directory
  - mysite/__init__.py
  - mysite/settings.py
  - mysite/urls.py
  - mysite/asgi.py
  - mysite/wsgi.py

Now you have a working environment (project). To create an app, you need to be in the same directory as manage.py, and you can run: $ python3 manage.py startapp appname
             
  **How to run tests**
   * Run make tests
  
  **How to run the app**
  * To check that the Django project works, run the following command in your outer mysite directory: python3 manage.py runserver
  
  


