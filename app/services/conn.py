from pymongo import MongoClient

password = '175ACBBED517AB950D6FFA7FD4CF1436547CDC7AECA1A12D1332457A2131ED807A0292A5152EF90C5FE160545701793E1A64DC5B542C332442CD1CD0BEB254AB'



client = MongoClient('88.131.100.92')
#client.the_database.authenticate('super', password, mechanism='MONGODB-CR', source='admin')

#Get idela database
db = client['idela']

#Defining collections in idela database
user = db.user
node = db.node
tag = db.tag
feedback = db.feedback
softdelete = db.softdelete