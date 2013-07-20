import sqlite3 

@app.before_request 
def before_request():  	  	  	  
	db = sqlite3.connect(…) 

@app.after_request 
def after_request(response):
	db.close()  	  	  	  
	return  response