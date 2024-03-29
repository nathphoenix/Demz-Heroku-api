import sqlite3
from flask_restful import Resource, reqparse
from models.user import UserModel


 
class UserRegister(Resource): #we use resource as we are interracting with the api
      parser = reqparse.RequestParser()
      parser.add_argument("username", type=str, required=True, help="This field cannot be empty")
      parser.add_argument("password", type=str, required=True, help="This field cannot be empty")
      
      def post(self):

          data = UserRegister.parser.parse_args()

          if UserModel.find_by_username(data["username"]):
              return {"message": "Auser with this email already exist"}, 400

        #   user = UserModel(data["username"], data["password"])
                        #OR....THIS ONE BELOW
          user = UserModel(**data)
          user.save_to_db()
        #   connection = sqlite3.connect("data.db")
        #   cursor = connection.cursor()

        #   query = "INSERT INTO users VALUES (NULL, ?, ?)"
        #   cursor.execute(query, (data["username"], data["password"]))

        #   connection.commit()
        #   connection.close()

          return {"message": "User created successfully"}, 201
