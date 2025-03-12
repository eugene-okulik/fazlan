import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

cursor.execute("INSERT INTO `st-onl`.students (name, second_name) VALUES('Sam', 'Smith')")
student_id = cursor.lastrowid
print(student_id)

insert_query_books = "INSERT INTO `st-onl`.books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(
    insert_query_books, [
        ('Алхимик', student_id),
        ('Преступление и наказание', student_id),
        ('Последняя лекция', student_id)
    ]
)

cursor.execute("INSERT INTO `st-onl`.`groups` (title, start_date, end_date) VALUES('Testers', 'feb 2025', 'may 2025');")
group_id = cursor.lastrowid
print(group_id)
cursor.execute(f"UPDATE `st-onl`.students SET group_id = {group_id} WHERE students.group_id is NULL;")

cursor.execute("INSERT INTO `st-onl`.subjets(title) VALUES ('Изобразительное искусство');")
art_id = cursor.lastrowid
print(art_id)
cursor.execute("INSERT INTO `st-onl`.subjets(title) VALUES ('Сопротивление материалов');")
resist_id = cursor.lastrowid
print(resist_id)
cursor.execute("INSERT INTO `st-onl`.subjets(title) VALUES ('Музыка');")
music_id = cursor.lastrowid
print(music_id)

cursor.execute(f"INSERT INTO `st-onl`.lessons (title, subject_id) VALUES ('Изо', {art_id});")
lesson_1_id = cursor.lastrowid
print(lesson_1_id)
cursor.execute(f"INSERT INTO `st-onl`.lessons (title, subject_id) VALUES ('Изо 2', {art_id});")
lesson_2_id = cursor.lastrowid
print(lesson_2_id)
cursor.execute(f"INSERT INTO `st-onl`.lessons (title, subject_id) VALUES ('Сопромат', {resist_id});")
lesson_3_id = cursor.lastrowid
print(lesson_3_id)
cursor.execute(f"INSERT INTO `st-onl`.lessons (title, subject_id) VALUES ('Сопромат 2', {resist_id});")
lesson_4_id = cursor.lastrowid
print(lesson_4_id)
cursor.execute(f"INSERT INTO `st-onl`.lessons (title, subject_id) VALUES ('Музыка', {music_id});")
lesson_5_id = cursor.lastrowid
print(lesson_5_id)
cursor.execute(f"INSERT INTO `st-onl`.lessons (title, subject_id) VALUES ('Музыка 2', {music_id});")
lesson_6_id = cursor.lastrowid
print(lesson_6_id)

insert_query_marks = "INSERT INTO `st-onl`.marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
cursor.executemany(
    insert_query_marks, [
        ('5', lesson_1_id, student_id),
        ('4', lesson_2_id, student_id),
        ('3', lesson_3_id, student_id),
        ('3', lesson_4_id, student_id),
        ('5', lesson_5_id, student_id),
        ('5', lesson_6_id, student_id),

    ]
)

cursor.execute(f"SELECT value from `st-onl`.marks where student_id = {student_id}")
marks = cursor.fetchall()
for mark in marks:
    print(mark['value'])

cursor.execute(f"SELECT title FROM `st-onl`.books where taken_by_student_id = {student_id}")
books = cursor.fetchall()
for book in books:
    print(book['title'])

cursor.execute(
    f"SELECT * from `st-onl`.students s join `groups` g on s.group_id = g.id join books b on s.id = b.taken_by_student_id join marks m on s.id = m.student_id where s.id = {student_id}")
student_info = cursor.fetchall()
print(f'Вся инфа про студента: {student_info}')

db.commit()

db.close()
