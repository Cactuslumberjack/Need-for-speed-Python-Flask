First, this was pulled off my project on Python Anywhere. If you wish to run locally. Clone the repo and then create a Main.py file with the following code:

#Main.py

from Carblog import app

if __name__ == '__main__':
    app.run(debug=True)
----------------
This File will be outside the Carblog folder which contains all the code. 

Make sure you create a virtual enviroment and manually download the dependencies found in the imports section. Keep the dependencies in your virtual environment 


before deployment make sure to 

set this in your terminal 
$env:FLASK_APP = "Main.py"
$env:FLASK_DEBUG = "1" 

flask db init
flask db migrate -m "initial migration" 
flask db upgrade

If you have issues running the local deployement try running python Main.py should start the development server:
