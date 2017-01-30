##Setup
1. Install Python v3.5.2
2. Install Django v1.10.4
3. git clone https://github.com/kevintatou/idela_API.git
4. cd idela_API
5. py manage.py runserver
6. Go to localhost:8000/

##API Docs
### Get Requests
/get/`collection`/
```
Gets all objects from collection
```
/get/`collection`/`id`
```
Gets a single object by ObjectId from collection
```
/get/`collection`/`id`/`field`/`relation_collection`/
```
Gets object by ObjectId from collection and selects field then 
uses values in field to get objects in related_collection by ObjectId
```
### Post Requests
/post
```
Hard coded data 
```
