
from flask import *
from flask_pymongo import PyMongo
from flask_bootstrap import Bootstrap
from bson import ObjectId
import pymongo
import os
from dotenv import load_dotenv


# loading environment from .env file

app_path = os.path.join(os.path.dirname(__file__), '.')
dotenv_path = os.path.join(app_path, '.env')
load_dotenv(dotenv_path)


app = Flask(__name__)
app.config['MONGO_URI'] = os.environ.get("MONGO_URI")
Bootstrap(app)
mongo = PyMongo(app)


@app.route('/', methods = ['GET', 'POST'])
def home():
    if request.method == "GET":
        allPhones = mongo.db.addressbook.find()
        return render_template('home.html', contacts = allPhones)
    elif request.method == "POST":
        name = request.form['name']
        phone = request.form['phone']
        mongo.db.addressbook.insert_one({'name' : name, 'phone' : phone})
        return redirect('/')

@app.route('/delete/<id>')
def delete(id):
    mongo.db.addressbook.delete_one({'_id' : ObjectId(id)})
    return redirect('/')

if __name__ == '__main__':
    app.run(debug = True)

