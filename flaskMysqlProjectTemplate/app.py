import sqlparse
from flask import Flask, render_template, request, redirect, url_for
from flask_mysqldb import MySQL
from MySQLConfig import MySQLConfig

app = Flask(__name__)

# Configure MySQL using the imported config
app.config['MYSQL_HOST'] = MySQLConfig.HOST
app.config['MYSQL_USER'] = MySQLConfig.USER
app.config['MYSQL_PASSWORD'] = MySQLConfig.PASSWORD
app.config['MYSQL_DB'] = MySQLConfig.DATABASE

# Create a MySQL connection
mysql = MySQL(app)

def execute_initial_sql(mysql):
    try:
        cursor = mysql.connection.cursor()
        # Read and execute the initial.sql file
        with open('static/sql/init.sql') as sql_file:
            statements = sqlparse.split(sql_file.read())
            for query in statements:
                print(query)
                cursor.execute(query)
                mysql.connection.commit()

        cursor.close()
    except Exception as e:
        print(f"Error executing initial SQL script: {str(e)}")

# you can comment out the following two lines if using docker compose
with app.app_context():
    execute_initial_sql(mysql)


# @app.before_first_request
# def before_first_request():
#     # run this line if database initialization is needed
#     execute_initial_sql()
#     pass


@app.route('/')
def index():

    # Display a list of records from the database
    cursor = mysql.connection.cursor()
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
        cursor = mysql.connection.cursor()
        # Option 1
        # cursor.execute("INSERT INTO student (sname, age, email) VALUES (%s, %s, %s)",(name, age, email))
        # Option 2
        cursor.execute("INSERT INTO student (sname, age, email) VALUES ('{}', '{}', '{}')".format(name, age, email))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('index'))



# Route for deleting students
@app.route('/delete/<int:id>')
def delete(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM student WHERE id = %s", (id,))
    mysql.connection.commit()
    cursor.close()
    return redirect(url_for('index'))


@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        name = request.form['name']
        age = request.form['age']
        email = request.form['email']
        cursor = mysql.connection.cursor()
        cursor.execute("UPDATE student SET sname = %s, age=%s, email = %s WHERE id = %s", (name, age, email, id))
        mysql.connection.commit()
        cursor.close()
        return redirect(url_for('index'))
    else:
        print(id)
        cursor = mysql.connection.cursor()
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
    app.run(debug=True, host="localhost", port=9999)

