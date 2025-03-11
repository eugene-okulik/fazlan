INSERT INTO `st-onl`.students (name, second_name) VALUES('John', 'Lock');

INSERT INTO `st-onl`.books (title, taken_by_student_id) VALUES('Алхимик', 4859)
INSERT INTO `st-onl`.books (title, taken_by_student_id) VALUES('Преступление и наказание', 4859);
INSERT INTO `st-onl`.books (title, taken_by_student_id) VALUES('Последняя лекция', 4859);

INSERT INTO `st-onl`.`groups` (title, start_date, end_date) VALUES('Testers', 'feb 2025', 'may 2025');
UPDATE `st-onl`.students SET group_id = (select `groups`.id from `groups` where title = 'Testers') WHERE students.group_id is NULL;

INSERT INTO `st-onl`.subjets(title) VALUES ('Изобразительное искусство'), ('Сопротивление материалов'), ('Музыка');

INSERT INTO `st-onl`.lessons (title, subject_id) VALUES ('Изо', 5086);
INSERT INTO `st-onl`.lessons (title, subject_id) VALUES ('Изо 2', 5086);
INSERT INTO `st-onl`.lessons (title, subject_id) VALUES ('Сопромат', 5087);
INSERT INTO `st-onl`.lessons (title, subject_id) VALUES ('Сопромат 2', 5087);
INSERT INTO `st-onl`.lessons (title, subject_id) VALUES ('Музыка', 5088);
INSERT INTO `st-onl`.lessons (title, subject_id) VALUES ('Музыка 2', 5088);

INSERT INTO `st-onl`.marks (value, lesson_id, student_id) VALUES('5', 9191, 4859);
INSERT INTO `st-onl`.marks (value, lesson_id, student_id) VALUES('4', 9192, 4859);
INSERT INTO `st-onl`.marks (value, lesson_id, student_id) VALUES('3', 9192, 4859);
INSERT INTO `st-onl`.marks (value, lesson_id, student_id) VALUES('3', 9192, 4859);
INSERT INTO `st-onl`.marks (value, lesson_id, student_id) VALUES('5', 9192, 4859);
INSERT INTO `st-onl`.marks (value, lesson_id, student_id) VALUES('5', 9192, 4859);

SELECT value from `st-onl`.marks where student_id = 4859;

SELECT title FROM `st-onl`.books where taken_by_student_id = 4859;

SELECT * from `st-onl`.students s join `groups` g on s.group_id = g.id join books b on s.id = b.taken_by_student_id join marks m on s.id = m.student_id;
