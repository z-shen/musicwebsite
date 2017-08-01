from common.database import Database

database = Database('localhost:27017','user')
database.insert('users',{"account":"luke","password":"4321"})
#user = database.find_one("student",{"e-mail" : "luke@hotmail"})
print (user)