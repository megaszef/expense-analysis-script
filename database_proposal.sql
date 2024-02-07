CREATE TABLE Department (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL
);

CREATE TABLE Expense (
    id SERIAL PRIMARY KEY,
    department_id INTEGER REFERENCES Department(id),
    year INTEGER NOT NULL,
    month INTEGER NOT NULL,
    amount DECIMAL(12, 2) NOT NULL
);
