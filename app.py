Python 3.11.9 (tags/v3.11.9:de54cf5, Apr  2 2024, 10:12:12) [MSC v.1938 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> from flask import Flask, jsonify, request
... app = Flask(__name__)
... students = [
... {"id": 1, "name": "Ravi", "course": "BSc CS"},
... {"id": 2, "name": "Ayesha", "course": "BSc CS"}
... ]
... @app.route("/")
... def home():
... return "Student Microservice is Running"
... 
... @app.route("/students", methods=["GET"])
... def get_students():
... return jsonify(students)
... 
... @app.route("/students/<int:id>", methods=["GET"])
... def get_student(id):
... for student in students:
... if student["id"] == id:
... return jsonify(student)
... return jsonify({"message": "Student not found"}), 404
... 
... APIs & Microservices — Lab Guide
... 
... 6
... @app.route("/students", methods=["POST"])
... def add_student():
... data = request.get_json()
... student = {
... "id": len(students) + 1,
... "name": data["name"],
... "course": data["course"]
... }
... students.append(student)
... return jsonify(student), 201
... 
... if __name__ == "__main__":
