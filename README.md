# TATA AGI Programming Assignment

Hi as the per the requirement listed in the document, API provides user with functionality of:
1.  Get the list of policy owned by a user 
2.  Get the policy details for the given policy no

To get these functionality to working Lets begin by setting-up the required environment:
1.  Install Python from "https://www.python.org/downloads/" by clicking the download button 
2.  Open download location and install python
3.  After installation has completed, Goto terminal and Type "Python" to check the installation is sucessfull
4.  Now download the source code file as zip from github; open terminal navigate to the source code folder and use command "pip install requirement.txt" to set all the dependencies required.
5.  In termial type "python manage.py createsuperuser" and type out the necessary details
6.  Once super user is created run the project using "python manage.py runserver"
7.  Open the web-browser and type "localhost" to check if the system is running. Now type "localhost/admin" to get to admin panel to add policy in the database. As there are policy sample present in the system so this may not be required.
8.  To check for the api call install postman from "https://www.postman.com/downloads/" 
9.  Type "localhost/policy_list_user/*user name* " to get all the policy in the system for the user.
10. Type "localhost/policy_details/*policy no* " to get detials of the policy in currently in the system.
11. Making the above api call will fetch you data in json format for processing further.  
  
