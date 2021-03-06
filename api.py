from flask import Flask, jsonify, request
app = Flask(__name__)

students = [
    {'id': 0,
     'Surname': 'Khen',
     'Name': 'Sophya',
     'Course': '4',
     'Speciality': 'VTiPO'},
     {'id': 1,
     'Surname': 'Erkinbekova',
     'Name': 'Zhanel',
     'Course': '4',
     'Speciality': 'VTiPO'},
     {'id': 2,
     'Surname': 'Li',
     'Name': 'Angelina',
     'Course': '1',
     'Speciality': 'VTiPO'},
    {'id': 3,
     'Surname': 'Shin',
     'Name': 'Michail',
     'Course': '1',
     'Speciality': 'AiU'},
    {'id': 4,
     'Surname': 'Kuknariev',
     'Name': 'Dmitriy',
     'Course': '4',
     'Speciality': 'IIP'},
    {'id': 5,
     'Surname': 'Kuknariev',
     'Name': 'Dmitriy',
     'Course': '4',
     'Speciality': 'IIP'}
]
@app.route('/', methods = ['GET'])
def test():
    return jsonify({'message': 'Hi from Alexandra!'})
@app.route('/studs',methods = ['GET'])
def returnAll(): 
    return jsonify({'students': students})
@app.route('/studs/<string:Surname>',methods = ['GET'])
def returnOne(Surname):
    studs = [student for student in students if student['Surname'] == Surname]
    return jsonify({'student':studs[0]})

@app.route('/studs', methods = ['POST'])
def addOne():
    student = {'id':request.json['id'],'Surname' : request.json['Surname'], 'Name': request.json['Name'],'Course': request.json['Course'], 'Speciality': request.json['Speciality']}
    students.append(student)
    return jsonify({'students':students})
@app.route('/studs/<int:id>', methods =['PUT'])
def editOne(id):
    studs = [student for student in students if student['id'] == id]
    studs[0]['Course'] = request.json['Course']
    return jsonify({'student': studs[0]})
@app.route('/studs/<int:id>', methods = ['DELETE'])
def removeOne(id):
    stud = [student for student in students if student['id'] == id]
    students.remove(stud[0])
    return jsonify({'students':students})
if __name__ == '__main__':
    app.run(debug=True,port=8000)