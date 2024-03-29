## Setup
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

***Note: Proper SSH key is required.***

## API Docs
### Get Requests
#### Get Requests - Bare-bones
/get/`key`=`value` 
```
Gets everythings where `key`=`value`.
```
/get/`key1`=`value1`&`key2`=`value2,value3`
```
Gets everythings where `key`=`value` and `key2`=`value2` and `value3`.
```
#### Get Requests - Allowed keys
"col": str,
"desc": str,
"fname": str,
"lname": str, 
"id": str, 
"public": int, 
"tags": str, 
"views": int, 
"trend": int, 
"media": int, 
"date": int, 
"alias": str, 
"weekly": int, 
"nodes": str,
"email": str,
"owners": str,
"members": str,
"comment" : str,
"type": str,
"token_type": str,
"token_value": str
#### Get Requests - Example
/get/`col`=`node`
```
Gets all documents from "collection" named "node" in the database.
```
/get/`col`=`node`&`owners`=`liam`
```
Gets all documents from "collection" named "node" in the database 
where key is "owners" and has the value "liam".
```
/get/`col`=`node`&`members`=`liam,kevin`
```
Gets all documents from "collection" named "node" in the database 
where key is "owners" and has the value "liam" and "kevin".
```

### Post Requests
#### Post Requests - Bare-bones
/post 
```
[
    {
        "key": "value",
        "key2": "value2",
        "key3": "value3,value4"
    }
]
```
Posts a json object to /post with keys including values
#### Post Requests - Minimum Requirements
##### User
```
"col": "user"
"fname": ",
"lname": "",
"email": "",
"token_type": "",
"token_value": ""
```
##### Nodes
```
"col": "node",
"tags": "",
"name": "",
"type": "",
"public": "",
"owners": ""
```
##### Tags
```
"col": "tags",
"name": ""
```
#### Post Requests - Allowed keys
##### User
```
"col": "user",
"alias": "",
"firstname": "",
"lastname": "",
"email": "",
"desc": "",
"tokens" "",
"nodes": "",
"image": "",
"views": 0,
"weekly": 0,
"trending": 0,
"level": 0,
"comment": ""
```
##### Nodes
```
"col": "node",
"weekly": 0,
"tags": "",
"desc": "",
"comment": "",
"rating": "",
"name": "",
"public": 0,
"token": "",
"image": "",
"media": "",
"views": 0,
"owners": "",
"members": "",
"trending": 0,
"quality_score": 0,
"opinion_score": 0,
"relevance_score": 0,
"opinion_votes": 0,
"quality_votes": 0,
"relevance_votes": 0
```
##### Tags
```
"col": "tags"
"name": "",
"desc": "",
"nodes": ""
```
#### Get Requests - Example
/post
```
[
    {
        "col": "node",
        "tags": "github,code",
        "name": "Bob the Coder",
        "public": 1,
        "owners": "0560940564",
        "members": "095609507 04793912"
    }
]
```
Requests a json object to post. Request want to be put in node collection `"col": "node"` in DB with keys containing a value `"name": "Bob the Coder"`ect. The tags key `"tags": "github,code"` gets split by comma into a array of strings `["github","code"]`, meaning the node gets two tags not a single tag. The same goes with members key. Note that `owners` and `members` values are MongoDB ObjectID(s).

When posting a node tags related to that node get automaticly updated and new tags get created if they dont exist in the database.
