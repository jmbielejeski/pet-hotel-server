import flask
import psycopg2
from flask import request, jsonify, make_response
from psycopg2.extras import RealDictCursor

import os



app = flask.Flask(__name__)
app.config["DEBUG"] = True

# default route to show home page and history table
@app.route('/api/pets/all', methods=['GET'])
def api_all():
  # if we can get the data back and then even print it 
    connection = psycopg2.connect(user=DATABASE_USERNAME,
                                  host="127.0.0.1",
                                  port="5432",
                                  database="pet_hotel")
    cursor = connection.cursor()
    postgresSQL_select_Query = "SELECT pets.*, owners.name FROM pets, owners WHERE pets.owner_id = owners.id"
    
    # Executes query
    cursor.execute(postgresSQL_select_Query)
    pets = cursor.fetchall()

    return jsonify(pets)

app.run()

# @app.route('/api/pets/add', methods=['POST'])
# def api_add():
#   print(request)
#   name = request.form['name']

#   try:
        # connection = psycopg2.connect(user=DATABASE_USERNAME,
        #                               host="127.0.0.1",
        #                               port="5432",
        #                               database="python_flask")
        # cursor = connection.cursor(cursor_factory=RealDictCursor)
        # print(name,    ,    ,    )
        # insertQuery = "INSET INTO pets (name,     ,     ,    )


# export default FLASK_APP=pet_hotel.py
# flask run 
# python3 pet_hotel.py
