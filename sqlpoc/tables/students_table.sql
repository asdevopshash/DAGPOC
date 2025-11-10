-- ============================================
-- PostgreSQL Script: Students Table and View
-- Author: Abhishek S Singh
-- Date: 2025-11-10
-- Description: Creates a table and view for students
-- ============================================

-- Drop existing objects (optional, for reruns)
DROP VIEW IF EXISTS student_summary;
DROP TABLE IF EXISTS students;

-- 1️⃣ Create Students Table
CREATE TABLE students (
    student_id SERIAL PRIMARY KEY,
    first_name VARCHAR(50) NOT NULL,
    last_name  VARCHAR(50) NOT NULL,
    age        INT CHECK (age > 0),
    grade      VARCHAR(5),
    enrolled_on DATE DEFAULT CURRENT_DATE
);

-- 2️⃣ Insert Sample Data
INSERT INTO students (first_name, last_name, age, grade)
VALUES
('Alice', 'Johnson', 15, 'A'),
('Bob', 'Smith', 16, 'B'),
('Charlie', 'Davis', 14, 'A'),
('Diana', 'Brown', 17, 'C');


-- 4️⃣ Verify Results
SELECT * FROM student_summary;