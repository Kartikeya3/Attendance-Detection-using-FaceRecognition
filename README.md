# Submission for Microsoft Engage Program 2022

This project is a part of my participation in Microsoft Engage Mentorship Program 2022. I've implemented Face Recognition Application. You can check out the project using https://acehacker.com/microsoft/engage2022/ .

# Project Link : https://enagaefacerecognition.azurewebsites.net/

# Presentation Link : shorturl.at/gjAG1

# Video Demo : 

# Technologies Used 

1) Python
2) DJANGO
3) HTML
4) CSS
5) JavaScript
6) WebRTC

# Installation

Note : Make sure you have Python version 3.8+

Environment Setup 🚀

$ git clone https://github.com/Kartikeya3/Attendance-Detection-using-FaceRecognition.git

$ cd Attendence/psychoweb

$ pip install virtualenv

Create a virtual environment

$ virtualenv venv

Activate the environment everytime you open the project

$ source venv/Scripts/activate

install requirements 🛠

$ pip install -r requirements.txt

Run migrations for Database

$ python manage.py makemigrations

$ python manage.py migrate

Create superuser for Admin Login 🔐

$ python manage.py createsuperuser

Enter your desired username, email and password. Make sure you remember them as you'll need them in future.

eg.

Username: admin

Email: admin@admin.com

Password: HighlyConfidentialPassword

All Set! 🤩

Now you can run the server to see your application up & running 🚀

$ python manage.py runserver

To exit the environment ❎

$ deactivate

# Features For The Project:
1) Authentication using Facial recognition
2) Attendance using Facial verification
3) They can add Profiles and Biometric Photo
4) They can edit the Details of user and Delete the UserDetails. 
5) They can Download the attendance Sheet

# Point to note :
1)To run in local First they have to go into Azure Database for PostgreSQL flexible servers and then Select recognition under settings click Networking tab in the firewall add your Firewall rule name and IP Address of start and end. 
2)Allow permissions for camera
3)In case any user is not broadcasted it is probably due to server overload, REFRESH the window to solve this.
