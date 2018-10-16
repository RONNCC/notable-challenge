

# How to Run

Run the following in terminal to install dependencies and then run it (if preferred I can also just send a docker container since that's a much nicer experience

virtualenv env
source env/bin/activate
pip install -r requirements.txt
FLASK_APP=main.py flask run
