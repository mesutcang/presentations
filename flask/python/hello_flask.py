from flask import Flask 
#import flask 

app = Flask(__name__) 

@app.route('/') 
def index():
	asda  	  	  	  
	return 'Hello World!!!' 


if __name__ == '__main__':  	  	  
	app.run(debug=True) 
