Drop table if exists student;

-- Create the student table if it doesn't exist

CREATE TABLE IF NOT EXISTS student (
    id SERIAL PRIMARY KEY,
    sname VARCHAR(255) NOT NULL,
    age INT,
    email VARCHAR(255) NOT NULL
);

DELETE from student;

-- Insert 5 fake student records
INSERT INTO student (sname, age, email) VALUES ('John Doe', 19, 'john@example.com');
INSERT INTO student (sname, age, email) VALUES ('Jane Smith', 21, 'jane@example.com');
INSERT INTO student (sname, age, email) VALUES ('Alice Johnson',22, 'alice@example.com');
INSERT INTO student (sname, age, email) VALUES ('Bob Brown', 20, 'bob@example.com');
INSERT INTO student (sname, age, email) VALUES ('Eve Davis', 18, 'eve@example.com');