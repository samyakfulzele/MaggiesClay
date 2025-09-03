from flask import *
import mysql.connector

class user():
    _db = mysql.connector.connect(host="localhost",user="root",password="",database="maggiesclay")
    _curr = _db.cursor()
    def register(self,first_name,last_name,gender,email,password):
        query = "INSERT INTO users(first_name,last_name,gender,email,password) VALUES('"+first_name+"','"+last_name+"','"+gender+"','"+email+"','"+password+"')"
        self._curr.execute(query)
        if self._db.commit() == False:
            return(0)
        else:
            return(1)
        
    def login(self,username,password):
        query = "SELECT id,first_name,email,password FROM users WHERE email = '"+username+"' and password = '"+password+"';"
        self._curr.execute(query)
        data = self._curr.fetchone()
        print(data)
        if data:
            session['u_loggedIn'] = True          
            session['u_id'] = data[0]            
            return(1)
        else:
            return(0)