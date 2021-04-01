import flask
import psycopg2
from flask import request, jsonify, make_response
from psycopg2.extras import RealDictCursor
# import os

# # export DATABASE_USERNAME="username_goes_here"
# DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')

app = flask.Flask(__name__)
app.config["DEBUG"] = True

# default route to show home page and history table
@app.route('/api/pets/all', methods=['GET'])
def api_all():

  # if we can get the data back and then even print it 
  # user=DATABASE_USERNAME,
    connection = psycopg2.connect(
                                  host="127.0.0.1",
                                  port="5432",
                                  database="pet_hotel")
                                          
    # Avoid getting arrays of arrays!
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    postgresSQL_select_Query = "SELECT pets.*, owners.owner_name FROM pets, owners WHERE pets.owner_id = owners.id"
    
    # Executes query
    cursor.execute(postgresSQL_select_Query)
    pets = cursor.fetchall()

    return jsonify(pets)

app.run()

@app.route('/api/owner/add', methods=['POST'])
def api_add():
  print(request)
  name = request.form['name']
  try:
      connection = psycopg2.connect(
                                    host="127.0.0.1",
                                    port="5432",
                                    database="python_flask")
      # To avoid getting arrays of arrays RealDictCursor
      cursor = connection.cursor(cursor_factory=RealDictCursor)
      print(name)
      # Insert owner into DB
      insertQuery = "INSERT INTO owners (name) VALUES (%s)"
      cursor.execute(insetQuery, (name,))
      # commit the query
      connection.commit()
      count = cursor.rowcount
      print(count, "Owner added")

      result = {'status': 'CREATED'}
      return make_response(jsonify(result), 201)
  except (Exception, psycopg2.Error) as error:
    # there was a problem
    if(connection):
        print("Failed to insert book", error)
        # respond with error
        result = {'status': 'ERROR'}
        return make_response(jsonify(result), 500)
  finally:
    # closing database connection.
    if(connection):
        # clean up our connections
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")



@app.route('/api/pets/add', methods=['POST'])
def api_add():
  print(request)
  name = request.form['name']
  breed = request.form['breed']
  color = request.form['color']
  try:
      connection = psycopg2.connect(
                                    host="127.0.0.1",
                                    port="5432",
                                    database="python_flask")
      cursor = connection.cursor(cursor_factory=RealDictCursor)
      print(owner_id, name, breed, color)
      # Insert pet into DB
      insertQuery = "INSERT INTO pets (owner_id, name, breed, color) VALUES (%s, %s, %s, %s)"
      cursor.execute(insetQuery, (owner_id, name, breed, color))
      # commit the query
      connection.commit()
      count = cursor.rowcount
      print(count, "pet added")

      result = {'status': 'CREATED'}
      return make_response(jsonify(result), 201)
  except (Exception, psycopg2.Error) as error:
    # there was a problem
    if(connection):
        print("Failed to insert book", error)
        # respond with error
        result = {'status': 'ERROR'}
        return make_response(jsonify(result), 500)
  finally:
    # closing database connection.
    if(connection):
        # clean up our connections
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")




# export default FLASK_APP=pet_hotel.py
# flask run 
# python3 pet_hotel.py
