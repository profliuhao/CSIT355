import sqlparse
from flask import Flask, request, render_template, redirect, url_for
from sqlalchemy import create_engine


app = Flask(__name__)

# MySQL configuration
app.config['MYSQL_HOST'] = 'your_mysql_host'
app.config['MYSQL_USER'] = 'your_mysql_user'
app.config['MYSQL_PASSWORD'] = 'your_mysql_password'
app.config['MYSQL_DB'] = 'your_database_name'


# mysql+<drivername>://<username>:<password>@<server>:<port>/dbname

connection_string = "mysql+mysqlconnector://{}:{}@{}:{}/{}".format(
app.config['MYSQL_USER'],
app.config['MYSQL_PASSWORD'],
app.config['MYSQL_HOST'],
3306,
app.config['MYSQL_DB']
)
engine = create_engine(connection_string, echo=True)


# connection = mysql.connect(
#             host=app.config['MYSQL_HOST'],
#             user=app.config['MYSQL_USER'],
#             password=app.config['MYSQL_PASSWORD'],
#             database=app.config['MYSQL_DB'],
#             buffered=True
#         )



# Function to execute initial.sql on startup
def execute_initial_sql():
    try:
        cur = engine.connect()
        # Read and execute the initial.sql file
        with open('static/init.sql') as sql_file:
            statements = sqlparse.split(sql_file.read())
            for query in statements:
                print(query)
                cur.execute(query)
        cur.close()
    except Exception as e:
        print(f"Error executing initial SQL script: {str(e)}")

execute_initial_sql()


@app.route('/')
def index():
    # Display a list of records from the database
    cur = engine.connect()
    data = cur.execute("SELECT * FROM student")
    cur.close()
    return render_template('index.html', data=data)

@app.route('/add', methods=['POST'])
def add():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        cur = engine.connect()
        cur.execute("INSERT INTO student (sname, email) VALUES (%s, %s)", (name, email))
        cur.close()
        return redirect(url_for('index'))

@app.route('/delete/<int:id>')
def delete(id):
    cur = engine.connect()
    cur.execute("DELETE FROM student WHERE id = %s", (id,))
    cur.close()
    return redirect(url_for('index'))

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        cur = engine.connect()
        cur.execute("UPDATE student SET sname = %s, email = %s WHERE id = %s", (name, email, id))
        cur.close()
        return redirect(url_for('index'))
    else:
        print(id)
        cur = engine.connect()
        result = cur.execute("SELECT * FROM student WHERE id = %s", (id,))
        for row in result.mappings():
            print(row)
            data = [row['id'], row['sname'], row['email']]
        cur.close()
        return render_template('update.html', data=data)


if __name__ == '__main__':
    # Run the initial SQL script on startup
    app.run(debug=True)
