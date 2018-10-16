

# How to Run

Run the following in terminal to install dependencies and then run it (if preferred I can also just send a docker container since that's a much nicer experience

```
virtualenv env #create a python virtualenv (scopes packages to the directory to assist in preventing installs from running amok)
source env/bin/activate #(uses the environment)
pip install -r requirements.txt # pip installs dependencies - really only flask since I use native python2.7 libs mostly
FLASK_APP=main.py flask run # runs the flask framework - defaults to  127.0.0.1:5000

```
