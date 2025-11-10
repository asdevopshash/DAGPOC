-- 3️⃣ Create a Readable View
CREATE VIEW student_summary AS
SELECT
    student_id,
    CONCAT(first_name, ' ', last_name) AS full_name,
    age,
    grade,
    enrolled_on
FROM students;