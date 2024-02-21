from flask import Flask, render_template, request, redirect, url_for
from myconfig import myconfig
import psycopg2
import sqlparse

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(host=myconfig.HOST,
                            database=myconfig.DATABASE,
                            user=myconfig.USER,
                            password=myconfig.PASSWORD)
    return conn


def execute_initial_sql():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        # Read and execute the initial.sql file
        with open('static/sql/init.sql') as sql_file:
            statements = sqlparse.split(sql_file.read())
            for query in statements:
                print(query)
                cursor.execute(query)
                conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Error executing initial SQL script: {str(e)}")


with app.app_context():
    execute_initial_sql()

@app.route('/')
def index():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student")
    data = cursor.fetchall()
    cursor.close()
    return render_template('index.html', data=data)


# Route for adding students
@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        email = request.form['email']
        conn = get_db_connection()
        cursor = conn.cursor()
        # Option 1
        # cursor.execute("INSERT INTO student (sname, age, email) VALUES (%s, %s, %s)",(name, age, email))
        # Option 2
        cursor.execute("INSERT INTO student (sname, age, email) VALUES ('{}', '{}', '{}')".format(name, age, email))
        conn.commit()
        cursor.close()
        conn.close()
        return redirect(url_for('index'))



# Route for deleting students
@app.route('/delete/<int:id>')
def delete(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM student WHERE id = %s", (id,))
    conn.commit()
    cursor.close()
    return redirect(url_for('index'))


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        email = request.form['email']
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("UPDATE student SET sname = %s, age=%s, email = %s WHERE id = %s", (name, age, email, id))
        conn.commit()
        cursor.close()
        return redirect(url_for('index'))
    else:
        print(id)
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM student WHERE id = %s", (id,))
        result = cursor.fetchone()
        print(result)
        for row in result:
            print(row)
            # data = [row['id'], row['sname'], row['email']]
        data = result
        cursor.close()
        return render_template('update.html', data=data)

if __name__ == '__main__':
    app.run()
