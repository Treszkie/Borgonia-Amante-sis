from connector import Connector

class Students:

    @staticmethod
    def get_all():
        query = "SELECT student_id, last_name, first_name, middle_name, sex, address, course_id FROM students"

        Connector.cursor.execute(query)
        result = Connector.cursor.fetchall()
        
        return result
    
    @staticmethod
    def add_student(student_id, lname, fname, mname, sex, address, course_id):
        query = "INSERT INTO students (student_id, last_name, first_name, middle_name, sex, address, course_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"

        try: 
            Connector.cursor.execute(query, (student_id, lname, fname, mname, sex, address, course_id))
            Connector.db.commit()
            return True
        except:
            Connector.db.rollback()
            return False
    
    @staticmethod
    def get_student(student_id):
        query = "SELECT student_id, last_name, first_name, middle_name, sex, address, course_id FROM students WHERE student_id = %s"
        
        Connector.cursor.execute(query, (student_id,))
        result = Connector.cursor.fetchone()
        
        return result

    @staticmethod
    def update_student(student_id, lname, fname, mname, sex, address, course_id):
        query = "UPDATE students SET last_name = %s, first_name = %s, middle_name = %s, sex = %s, address = %s, course_id = %s WHERE student_id = %s"

        try:
            Connector.cursor.execute(query, (lname, fname, mname, sex, address, course_id, student_id))
            Connector.db.commit()
            return True
        except:
            Connector.db.rollback()
            return False

    @staticmethod
    def delete_student(student_id):
        query = "DELETE FROM students WHERE student_id = %s"

        try:
            Connector.cursor.execute(query, (student_id,))
            Connector.db.commit()
            return True
        except:
            Connector.db.rollback()
            return False
