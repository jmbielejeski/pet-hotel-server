import flask
import psycopg2
from flask import request, jsonify, make_response
from psycopg2.extras import RealDictCursor
import logging 
# import os

# # export DATABASE_USERNAME="username_goes_here"
# DATABASE_USERNAME = os.getenv('DATABASE_USERNAME')

log_level = logging.INFO


app = flask.Flask(__name__)
app.config["DEBUG"] = True
app.logger.setLevel(log_level)

# default route to show home page and history table
@app.route('/api/pets/all', methods=['GET'])
def api_all():

  # if we can get the data back and then even print it 
  # user=DATABASE_USERNAME,
    connection = psycopg2.connect(
                                  host="127.0.0.1",
                                  port="5432",
                                  database="pet_hotel")
    app.logger.info(request)
                                          
    # Avoid getting arrays of arrays!
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    postgresSQL_select_Query = "SELECT pets.*, owners.owner_name FROM pets, owners WHERE pets.owner_id = owners.id"
    
    # Executes query
    cursor.execute(postgresSQL_select_Query)
    pets = cursor.fetchall()

    return jsonify(pets)

    # route to grab all teh owners
@app.route('/api/owners/all', methods=['GET'])
def api_all_owners():

  # if we can get the data back and then even print it 
  # user=DATABASE_USERNAME,
    connection = psycopg2.connect(
                                  host="127.0.0.1",
                                  port="5432",
                                  database="pet_hotel")
    app.logger.info(request)
                                          
    # Avoid getting arrays of arrays!
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    postgresSQL_select_Query = "SELECT * FROM owners"
    
    # Executes query
    cursor.execute(postgresSQL_select_Query)
    owners = cursor.fetchall()

    return jsonify(owners)

@app.route('/api/owner/add', methods=['POST'])
def api_add_owner():
  print(request)
  owner_name = request.form['owner_name']
  try:
      connection = psycopg2.connect(
                                    host="127.0.0.1",
                                    port="5432",
                                    database="pet_hotel")
      # To avoid getting arrays of arrays RealDictCursor
      cursor = connection.cursor(cursor_factory=RealDictCursor)
      print(name)
      # Insert owner into DB
      insertQuery = "INSERT INTO owners (owner_name) VALUES (%s)"
      cursor.execute(insertQuery, (name,))
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
def api_add_pet():
  print('hello')
  print(request.json)
  owner_id = request.json['owner_id']
  pet_name = request.json['pet_name']
  breed = request.json['breed']
  color = request.json['color']
  try:
      connection = psycopg2.connect(
                                    host="127.0.0.1",
                                    port="5432",
                                    database="pet_hotel")
      cursor = connection.cursor(cursor_factory=RealDictCursor)
      print(owner_id, pet_name, breed, color)
      # Insert pet into DB
      insertQuery = "INSERT INTO pets (owner_id, pet_name, breed, color) VALUES (%s, %s, %s, %s)"
      cursor.execute(insertQuery, (owner_id, pet_name, breed, color))
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

<<<<<<< HEAD
# DELETES pet
@app.route('/api/pets/delete/<id>', methods=['DELETE'])
def api_delete_pet(id):
    print('id', id)
  # if we can get the data back and then even print it 
  # user=DATABASE_USERNAME,
    connection = psycopg2.connect(
                                  host="127.0.0.1",
                                  port="5432",
                                  database="pet_hotel")
                                          
    # Avoid getting arrays of arrays!
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    delete_Query = "DELETE FROM pets WHERE id = %s"
    # Executes query
    cursor.execute(delete_Query, (id,))
    connection.commit()

    print(cursor.rowcount, "pet deleted")


    # DELETES owner
@app.route('/api/owner/all', methods=['DELETE'])
def api_delete_owner():
  # if we can get the data back and then even print it 
    connection = psycopg2.connect(
                                  host="127.0.0.1",
                                  port="5432",
                                  database="pet_hotel")                   
    # Avoid getting arrays of arrays!
    cursor = connection.cursor(cursor_factory=RealDictCursor)
    delete_Query = "DELETE FROM owner WHERE id = %s"
    # Executes query
    cursor.execute(delete_Query)
    connection.commit()

    print(cursor.rowcount, "owner deleted")

=======
>>>>>>> e6b1bebb244366199c3b28696333f75e4f154b76
app.run()
# export default FLASK_APP=pet_hotel.py
# flask run 
# python3 pet_hotel.py
