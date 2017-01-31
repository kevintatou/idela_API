##Setup
1. Install Python v3.5.2
2. Install Django v1.10.4
3. git clone https://github.com/kevintatou/idela_API.git
4. cd idela_API
5. py manage.py runserver
6. Go to localhost:8000/

##API Docs
### Get Requests
#### Get Requests - Bare-bones
/get/`term`=`value` 
```
Gets everythings where `term`=`value`.
```
/get/`term1`=`value1`&`term2`=`value2`
```
Gets everythings where `term`=`value` and `term2`=`value2`.
```
#### Get Requests - Allowed Terms
'alias',
'col',
'date',
'email'
'id',
'media',
'name',
'nodes',
'public',
'tags',
'trending',
'views',
'weekly',
#### Get Requests - Example
/get/`col`=`node`
```
Gets all objects from 'collection' named 'node' in the database .
```
/get/`col`=`node`&`name`=`liam`
```
Gets all objects from 'collection' named 'node' in the database 
where field name is 'name' and has the value of 'liam'.
```
/get/`col`=`node`&`name`=`liam`&`tags`=`LiamTag`
```
Gets all objects from 'collection' named 'node' in the database 
where field name is 'name' and has the value of 'liam' and also
where field name is 'tags' and has the value of 'liamtag'. 
```
***Unlimited amount of filters allowed***
### Post Requests
/post
```
Hard coded data 
```
