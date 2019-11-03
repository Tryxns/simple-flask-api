from flask_restful import Resource


class Hello(Resource):
    def get(self):
        return {"message": "GET Hello!"}
    
    def post(self):
        return {"message": "POST Hello!"}

    def put(self):
        return {"message": "PUT Hello!"}

    def delete(self):
        return {"message": "DELETE Hello!"}