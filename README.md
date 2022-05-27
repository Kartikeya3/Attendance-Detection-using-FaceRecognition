# Submission for Microsoft Engage Program 2022

This project is a part of my participation in Microsoft Engage Mentorship Program 2022. I've implemented Face Recognition Application. You can check out the project using https://acehacker.com/microsoft/engage2022/ .

# Project Link : https://enagaefacerecognition.azurewebsites.net/

# Presentation Link : https://shorturl.at/gjAG1

# Video Demo : 

# Technologies Used 

- Python
- DJANGO
- HTML
- CSS
- JavaScript
- WebRTC

# Installation

Note : Make sure you have Python version 3.8+

### Environment Setup 🚀

```$ git clone https://github.com/Kartikeya3/Attendance-Detection-using-FaceRecognition.git```

### Open Visual Studio 

```$ pip install virtualenv```

Create a virtual environment

```$ virtualenv venv```

Activate the environment everytime you open the project

```$ source venv/Scripts/activate``` (or) ```pipenv shell```

```$ pip install django``` 

### Install requirements 🛠

```$ pip install -r requirements.txt```

### Run migrations for Database

```$ python manage.py makemigrations```

```$ python manage.py migrate```

### Create superuser for Admin Login 🔐

```$ python manage.py createsuperuser```

Enter your desired username, email and password. Make sure you remember them as you'll need them in future.

eg.

```Username: admin```

```Email: admin@admin.com```

```Password: HighlyConfidentialPassword```

All Set! 🤩

Now you can run the server to see your application up & running 🚀

```$ python manage.py runserver```

### To exit the environment ❎

```$ deactivate```

# Features For The Project:
- Authentication using Facial recognition
- Attendance using Facial verification
- They can add Profiles and Biometric Photo
- They can edit the Details of user and Delete the UserDetails. 
- They can Download the attendance Sheet

# Point to note :
- To run in local First they have to go into Azure Database for PostgreSQL flexible servers and then Select recognition under settings click Networking tab in the       firewall add your Firewall rule name and IP Address of start and end. 
- Hostname/address  : recognition.postgres.database.azure.com 
  -port : 5432
 -Maintenance Database : postgres
 -username : postgres
 -password : password   click save
- Allow permissions for camera
- In case any user is not broadcasted it is probably due to server overload, REFRESH the window to solve this.
