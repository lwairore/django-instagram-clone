## MyGallery
MyGallery provides high quality and completely free stock photos. All photos are nicely tagged, and searchable.

#### Photos
I have sixty nine free photos and every week high resolution photos will be added. 

Photos are divided into eighty(8) categories:
1. Abstract photos
2. Aerial photos
3. Architectural photos
4. Landscape photos
5. Potrait photos
6. Sports photos
7. Wedding photos
8. Wildlife photos

#### Preview 
##### [Homepage]()
![Screenshot](media/images/Screenshot_from_2019-03-19_10-23-15.png)
##### [Search-results]()
![Screenshot](media/images/Screenshot_from_2019-03-19_10-23-15.png)


## BEHAVIOUR DRIVEN DEVELOPMENT (BDD)
Behaviour                                   | Input                                                                          | Output                                        |
--------------------------------------------|--------------------------------------------------------------------------------|----------------------------------------------|
Search for different categories of photos   | Click the search form, enter a category you would like to get, eg `Landscape`. |  Hit the `ENTER` keyboard button               | Search results: all images that have are in category `Landscape`               |
Copy a link to the photo onto the clipboard | Cick on the `Copy image link` button                                           | The image link is copied to the clipboard.         |

## Installation
#### Clone gallery repository
Create a folder, gallery-clone, by running
```
$ mkdir gallery-clone
```
Navigate to gallery-clone folder(this is where gallery cloned version will be stored)
```
$ cd gallery-clone
```
Next, we download gallery repository by running:
```
$ git clone https://github.com/lwairore/gallery.git
```




#### Creating a Virtual Environment
 Python3.6 and up comes with a tool called ```venv``` that allows the creation of a virtual environment.
```
$ python3.6 -m venv --without-pip virtual
```
Above we used ```venv``` tool to create a virtual environment and called it `virtual`. 
#### Activating the virtual environment
To activate the virtual environment we run the following command: 
```
$ source virtual/bin/activate
``` 
#### Download the latest version of pip
```
(virtual)$ curl https://bootstrap.pypa.io/get-pip.py | python
```
MyGallery heavily relies on pip to install Django and any other packages that we will need.
#### Install Django
Next we need to install the latst django release of version 1.11
```
(virtual)$ pip install django==1.11
```
To avoid issues, I recommend you install to you the exact version used above.
#### Install database dependency
Django projects come preconfigured to work with sqlite databases which are small dynamic SQL databases. But these prove difficult to scale when our content grows. Django also supports other kinds of databases. We will use our Postgresql Database to store data in our application.
#### Postgresql Installation
First deactivate virtual environment
```
(virtual)$ deactivate
```
1. Ubuntu
To Install Postgres on Ubuntu we need to run the following commands in our terminal.
```
$ sudo apt-get update
```
To install Postgres
```
$ sudo apt-get install postgresql postgresql-contrib libpq-dev
```
Enter `y` when prompted “Do you want to continue? [Y/n]” and wait as the installation completes. 
Postgres uses "roles" to aid in authentication and authorization. By default, Postgres creates a Postgres user and is the only user who can connect to the server.

We want to create our own superuser role to connect to the server. 

For those running on elementary or parrot, run the following command first; 
```
$ sudo service postgresql start
```
```
$ sudo -u postgres createuser --superuser $USER
```
Enter your desired password when prompted.

We then have to create a database with that `$USER` login name, this is what Postgres expects as default.
```
$ sudo -u postgres createdb $USER
```
Navigate to your home directory and enter the following command to create the .psql_history in order to save your history:
```
$ touch .psql_history
```
You can now connect to the postgres server by typing :
```
$ psql
```
2. Mac
Homebrew makes it really easy to install Postgres. Just run:
```
 $ brew install postgres
```
After it finishes installing, you'll need to configure your computer a bit. First, you need to tell Postgres where to find the database cluster where your databases will be stored:
```
$ echo "export PGDATA=/usr/local/var/postgres" >> ~/.bash_profile
```
This command will help some programs find Postgres more easily:
```
$ echo "export PGHOST=/tmp" >> ~/.bash_profile
```
To load these configuration changes, run:
```
$ source ~/.bash_profile
```
To start the Postgres server, simply run:
```
$ postgres
```
You'll have to leave that window open while you need the server. To stop the server, press Ctrl + C (_not_ Cmd + C). If you want Postgres to boot at startup and run in the background, run:
```
 $ ln -sfv /usr/local/opt/postgresql/*.plist ~/Library/LaunchAgents
```
And to start it now (since it won't boot automatically until you restart your computer), run:
```
$ pg_ctl start
```
#### Setting up database
First, we need to create a new database for gallery.
Type in `psql` to connect to the postgres server.
```
$ psql
```
We then use an SQL command to create a database `gallery`.Note that all SQL commands end with a semicolon.
```
james=#  CREATE DATABASE gallery;
```

Finally, activate virtual environment.
```
$ source virtual/bin/activate
```
To connect Postgres to our project we need to install ```psycopg2```. This  is a Postgres dependency to connect and communicate with Django.
```
(virtual)$ pip install psycopg2
```
Navigate to the `.env` file and add configure `DB_NAME`, `DB_USER`, `DB_PASSWORD`and `DEBUG`
```
DEBUG=True
DB_NAME=<name of database>
DB_USER=<postgres username>
DB_PASSWORD=<postgres password>
```
#### Install Pillow
Django provides an `ImageField` model field that manages Image uploads. The Images are stored in the file system and not in the database.

The `ImageField` requires a Python image Library called `pillow` for it to run.
```
(virtual) $ pip install pillow
```
The `ImageField` stores a reference to where the Image is stored in the file system.
### Start Django Server
Last but not least we need to start the Django server. Django comes loaded with a fully functional development server that contains everything from debug settings and also automatic reload when we change something in our code.
```
(virtual)$ python3.6 manage.py runserver
Performing system checks...

System check identified no issues (0 silenced).
October 04, 2017 - 01:10:12
Django version 1.11.5, using settings 'heyapp.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.
```
Django checks if there are any errors in your program then start a development server at localhost port `8000`. If everything works you should see the MyGallery homepage.
![Screenshot](media/images/Screenshot_from_2019-03-19_10-23-15.png)

## Browsers supported 
1. [Google Chrome](https://en.wikipedia.org/wiki/Google_Chrome)
2. [Mozilla Firefox](https://en.wikipedia.org/wiki/Mozilla_Firefox)
3. [Internet Exploer](https://en.wikipedia.org/wiki/Internet_Explorer)
4. [Safari](https://en.wikipedia.org/wiki/Safari_(web_browser))
5. [Microsoft Edge](https://en.wikipedia.org/wiki/Microsoft_Edge)
6. [Opera](https://en.wikipedia.org/wiki/Opera_(web_browser))
7. [UC Browser](https://en.wikipedia.org/wiki/UC_Browser)
8. [Yandex Browser](https://en.wikipedia.org/wiki/Yandex_Browser)
9. [Chromium](https://en.wikipedia.org/wiki/Chromium_(web_browser))
10. [Sogou Explorer](https://en.wikipedia.org/wiki/Sogou)
11. [QQ Browser](https://en.wikipedia.org/w/index.php?title=QQ_Browser&action=edit&redlink=1)

## Technologies used
1. [Django v1.11](https://www.djangoproject.com/) - To handle routing and navigation.
2. [MDB v.4.8.2](https://mdbootstrap.com) - To create an intuitive and simple responsive UI elements.

## FEEDBACK
Your opinion matters. 
Have some ideas how to improve my product?
Ping me at https://github.com/lwairore/feedback

## Contact Information
Email - (https://kwairore@gmail.com)

Github username - [lwairore](https://www.github.com/lwairore)

## Team
MyGallery is run by Karangu Lucas Wairore, fullstack developer.

MIT License

Copyright (c) 2019 Karangu Lucas Wairore




