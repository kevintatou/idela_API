from pymongo import MongoClient



client = MongoClient('localhost', 27017)
#print(client.test.command('buildinfo'))

#Get idela database
db = client['idela']

#Defining collections in idela database
user = db.user
node = db.node
tag = db.tag
feedback = db.feedback
softdelete = db.softdelete
