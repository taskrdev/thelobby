# The Lobby
GetBellhops sample work: Internal reddit for polls

Kind of like reddit but with polls.  We want to use TheLobby as a tool for internal discussions.  Such as deciding where the next offsite should be.

1. Polls with multiple choices associated with the polls 
2. Threaded comments.  People can 'like' comments in discussions, to give them upvotes

Below is a very quick and dirty sketch of the kind of functionality we're looking for

![](https://recruitwell.mybalsamiq.com/mockups/3231033.png?key=7b4b9fe77bce2f460da453a5d6047a9c73c6f958)

How To Checkout and Run the Code
============================ 
    git clone https://ygreif@bitbucket.org/ygreif/thelobby.git
    cd thelobby
    python manage.py migrate
    python manage.py runserver

System Requirements
==================
Python 2.7.6

Django 1.8.2

To upgrade django run 

    sudo pip django --upgrade

View the Website
=============
Navigate to http://127.0.0.1:8000/watercooler/
