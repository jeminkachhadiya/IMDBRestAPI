# Imdbrestapi


1.first create virtualenvironment then activate it.

Windows:
 -  python -m venv env
 -  env\scripts\activate

2.pip install -r requirements.txt

3.python server.py

4.login page 
username:admin 
password:password

* Login page

![page1](https://user-images.githubusercontent.com/26074662/71502561-e75c1b00-2896-11ea-8b8d-4260ebcc98ce.png)

* Main page

![page2](https://user-images.githubusercontent.com/26074662/71502585-00fd6280-2897-11ea-9baa-6db9f82811a1.png)

* Activity page

![page3](https://user-images.githubusercontent.com/26074662/71502604-1d010400-2897-11ea-8e47-a27dcea7c919.png)

* Another activity page

![page4](https://user-images.githubusercontent.com/26074662/71502617-30ac6a80-2897-11ea-9f33-6371e70e5922.png)




# If you want to do from scratch

Delete logindata.db and imdb.db

* step 1.first create virtualenvironment then activate it.

Windows:
1. python -m venv env
2. env\scripts\activate


* step 2.pip install -r requirements.txt


* step 3.make imdb.db

1. sqlite3 imdb.db 
2. CREATE TABLE MOVIES(ID INTEGER PRIMARY KEY,TITLE TEXT,RATING NUMBER,RELEASEDATE TEXT,DURATION TEXT,DESCRIPTION TEXT);


* step 4.python task.py

it will take time to scrap data from https://www.imdb.com/chart/top?ref_=nv_mv_250 

nearly 5 minutes to scrap and store data in imdb.db


* step 5.python tablelogin.py

1. sqlite3 logindata.db \n
2. CREATE TABLE users(id INTEGER PRIMARY KEY,username TEXT,password TEXT); 
3. INSERT INTO users(username,password) VALUES('admin','password'); 

* step 6.python server.py

