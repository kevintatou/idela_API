##Setup
1. Install Python v3.5.2
3. Install Django v1.10.4
4. git clone https://github.com/kevintatou/idela_API.git
5. pip install pymongo
6. pip install django-cors-headers
7. cd idela_API
8. py manage.py runserver
9. Go to localhost:8000/

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
Gets all documents from 'collection' named 'node' in the database.
```
/get/`col`=`node`&`name`=`LiamNode`
```
Gets all documents from 'collection' named 'node' in the database 
where field name is 'name' and has the value of 'liam'.
```
***Note: Unlimited amount of filters allowed, but do NOT duplicate terms***
### Post Requests
/post
```
Hard coded data 
```
