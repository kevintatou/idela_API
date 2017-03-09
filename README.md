##Setup
1. Install Python v3.5.2
2. Install Django v1.10.4
3. git clone https://github.com/kevintatou/idela_API.git
4. pip install pymongo
5. pip install django-cors-headers
6. cd idela_API
7. Run server
  * For Windows Users: windows.bat
  * For Linux Users: bash linux.sh
8. Go to localhost:8000/

##API Docs
### Get Requests
#### Get Requests - Bare-bones
/get/`key`=`value` 
```
Gets everythings where `key`=`value`.
```
/get/`key1`=`value1`&`key2`=`value2`
```
Gets everythings where `key`=`value` and `key2`=`value2`.
```
#### Get Requests - Allowed keys
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
#### Post Requests - Bare-bones
/post
```
Post form data with a `key` and `value` 
```
#### Post Requests - Users Minimum Requirements
'firstname',
'lastname',
'email',
'tokens'
#### Post Requests - Nodes Minimum Requirements
'tags',
'name',
'public',
'owner'
#### Post Requests - Tags Minimum Requirements
'name'
#### Get Requests - Example
//ADD HTML FORM//
