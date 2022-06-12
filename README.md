## Awwards

## Description
This is a Django web application where users get to rate projects that have been uploaded based on their design,content and usability.The application also allows users to post their projects and have it reviewed by their peers.

## Author
Nazarena Wambura.</br>
[Github Account](https://github.com/nazarena254)

<!-- ### Homepage
![nazinstagram](./insta/static/images/myhomepg.png)
### Admin panel
![nazinstagram](./insta/static/images/myadmin.png)
### Wireframe sample
![nazinstagram](wireframe.png) -->

## User Story
1. View posted projects and their details.
2. Post a project to be rated/reviewed.
3. Rate/ review other users' project
4. Search for projects 
5. View projects overall score
6. View my profile page

## Behaviour Driven Development (BDD)
1. Sign up to the application

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| Click on sign up  | username,password,email | user account and profile is created  | 

2. log into the application 

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| Enter details in the log in form   | username, password| Landing page is loaded is login is successful else an error message is shown  | 


3. See profiles 

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| For user profile, click on the profile icon on navbar,or click on other users username | Username| User is redirected to the profile pages  |  

4. Post project

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| Click on button submit project on the navbar | Enter required details| Project is posted and displayed on the index page under nominees | 


5. Rate a project

|Behaviour 	           |    Input 	                 |       Output          |
|----------------------------------------------|:-----------------------------------:|-----------------------------:|       
| Click on button vote on the project  | Enter rate for design content and usability | The rates are updated and displayed  |

## Setup/Installation Requirements
1. Create a folder and cd to it.
2. Clone the repository below with the command `git clone <https option url> .`  <br>
    https://github.com/nazarena254/Awwards  
3. Install dependencies in the requirements.txt file `pip install -r requirements.txt` .
4.  Type code . or atom . based on the text editor you have and work on it.   

## Database
1. Set up Database(postgresql),and put your username and password in the code
2. Make migrations
    python3 manage.py makemigrations
3. Migrate
   python3 manage.py migrate 
       
## Running the Application
1. Run main aplication<br>    
   * python3.9 manage.py runserver<br>
    Note: python version will vary in future

## Creating Admins
1. Creating Admin Locally<br>
     python manage.py createsuperuser. Then set username, email & password

2. Creating Django Admin   
     heroku run python manage.py createsuperuser. Then set username, email & password

## Technologies Used
* Python3.9.2 - as backend language
* Django4.0.5 - as a Framework
* Bootstrap4 - for responsiveness & styling 
* PostgreSQL - as database
* Cloudinary - as cloud-based image storage server
* Heroku - for deploying app

## Support & Contact Information
For any further inquiries, bugs, contributions or comments, reach me at:<br>
Email:<nancyngunjiri1@gmail.com>

## License
[MIT License](https://github.com/nazarena254/Awwards/blob/master/LICENSE)<br>
Copyright (c) 2021 **Nazarena Wambura**