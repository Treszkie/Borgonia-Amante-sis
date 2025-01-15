from flask import Flask, render_template, request, redirect, session, url_for
from users import Users
from students import Students

app = Flask(__name__)
app.secret_key = "gege"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check-user', methods=['POST'])
def check_user():
    username = request.form["username"]
    password = request.form["password"]

    result = Users.check_user(username, password)

    if result:
        return redirect('/student-list')
    else:
        return render_template('index.html')

@app.route('/student-list')
def student_list():
    students = Students.get_all()
    message = session.pop('message', "")
    return render_template('student_list.html', students=students, message=message)

@app.route('/add-form')
def add_student():
    return render_template('add_student.html')

@app.route('/add-form', methods=["POST"])
def add_student_post():
    student_id = request.form["student_id"]
    lname = request.form["lname"]
    fname = request.form["fname"]
    mname = request.form["mname"]
    sex = request.form["sex"]
    address = request.form["address"]
    course_id = request.form["course_id"]

    success = Students.add_student(student_id, lname, fname, mname, sex, address, course_id)

    if success:
        session["message"] = "Student successfully added"
    else:
        session["message"] = "Failed to add student"
    
    return redirect('/student-list')

@app.route('/update-student/<student_id>', methods=['GET', 'POST'])
def update_student(student_id):
    if request.method == 'POST':
        lname = request.form["lname"]
        fname = request.form["fname"]
        mname = request.form["mname"]
        sex = request.form["sex"]
        address = request.form["address"]
        course_id = request.form["course_id"]

        success = Students.update_student(student_id, lname, fname, mname, sex, address, course_id)

        if success:
            session["message"] = "Student successfully updated"
        else:
            session["message"] = "Failed to update student"
        
        return redirect('/student-list')
    else:
        student = Students.get_student(student_id)
        return render_template('update_student.html', student=student)

@app.route('/delete-student/<student_id>')
def delete_student(student_id):
    success = Students.delete_student(student_id)
    if success:
        session["message"] = "Student successfully deleted"
    else:
        session["message"] = "Failed to delete student"
    return redirect('/student-list')

if __name__ == '__main__':
    app.run(debug=True)
