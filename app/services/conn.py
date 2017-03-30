from pymongo import MongoClient

client = MongoClient('localhost', 4321)

#print(client.test.command('buildinfo'))

#Get idela database
db = client['idela']

#Defining collections in idela database
#user = db.user
#node = db.node
#tag = db.tag
#feedback = db.feedback
#softdelete = db.softdelete

user = db.user_test
node = db.node_test
tag = db.tag_test
feedback = db.feedback_test
softdelete = db.softdelete_test

#Jespers Kandidat
placeholder = db.placeholder