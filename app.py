
from flask import *

app = Flask(__name__)

@app.route('/')
def hello_world():
	return render_template('index.html')


@app.route('/ACADEMIC.html')
def hello_world1():
	return render_template('ACADEMIC.html')
 
 
@app.route('/CO-CURRICURAL.html')
def hello_world2():
	return render_template('CO-CURRICURAL.html')


@app.route('/EDUCATION.html')
def hello_world3():
	return render_template('EDUCATION.html')    

@app.route('/INTERNSHIPS.html')
def hello_world4():
	return render_template('INTERNSHIPS.html')



@app.route('/PERSONAL.html')
def hello_world5():
	return render_template('PERSONAL.html')
 
 
 
@app.route('/POSITIONS.html')
def hello_world6():
	return render_template('POSITIONS.html') 
    
    
@app.route('/PROJECTS.html')
def hello_world7():
	return render_template('PROJECTS.html')
 
 
 
@app.route('/TECHNICAL.html')
def hello_world8():
	return render_template('TECHNICAL.html')  

    
@app.route('/index.html')
def hello_world9():
	return render_template('index.html')  
if __name__ == '__main__':
	app.run()