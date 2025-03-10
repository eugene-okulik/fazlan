INSERT INTO `st-onl`.students (name, second_name) VALUES('John', 'Lock');

INSERT INTO `st-onl`.books (title, taken_by_student_id) SELECT 'Алхимик', s.id  FROM students s order by id desc limit 1;
INSERT INTO `st-onl`.books (title, taken_by_student_id) SELECT 'Преступление и наказание', s.id  FROM students s order by id desc limit 1;
INSERT INTO `st-onl`.books (title, taken_by_student_id) SELECT 'Последняя лекция', s.id  FROM students s order by id desc limit 1;

INSERT INTO `st-onl`.`groups` (title, start_date, end_date) VALUES('Testers', 'feb 2025', 'may 2025');
UPDATE `st-onl`.students SET group_id = (select `groups`.id from `groups` where title = 'Testers') WHERE students.group_id is NULL;

INSERT INTO `st-onl`.subjets(title) VALUES ('Изобразительное искусство'), ('Сопротивление материалов'), ('Музыка');

INSERT INTO `st-onl`.lessons (title, subject_id) select 'Изо', s.id  FROM subjets s order by id desc limit 2, 1;
INSERT INTO `st-onl`.lessons (title, subject_id) select 'Изо 2', s.id  FROM subjets s order by id desc limit 2, 1;
INSERT INTO `st-onl`.lessons (title, subject_id) select 'Сопромат', s.id  FROM subjets s order by id desc limit 1, 1;
INSERT INTO `st-onl`.lessons (title, subject_id) select 'Сопромат 2', s.id  FROM subjets s order by id desc limit 1, 1;
INSERT INTO `st-onl`.lessons (title, subject_id) select 'Музыка', s.id  FROM subjets s order by id desc limit 1;
INSERT INTO `st-onl`.lessons (title, subject_id) select 'Музыка 2', s.id  FROM subjets s order by id desc limit 1;

INSERT INTO `st-onl`.marks (value, lesson_id, student_id) VALUES('5', 9191, 4859);
INSERT INTO `st-onl`.marks (value, lesson_id, student_id) VALUES('4', 9192, 4859);
INSERT INTO `st-onl`.marks (value, lesson_id, student_id) VALUES('3', 9192, 4859);
INSERT INTO `st-onl`.marks (value, lesson_id, student_id) VALUES('3', 9192, 4859);
INSERT INTO `st-onl`.marks (value, lesson_id, student_id) VALUES('5', 9192, 4859);
INSERT INTO `st-onl`.marks (value, lesson_id, student_id) VALUES('5', 9192, 4859);

SELECT value from `st-onl`.marks where student_id = (select id from students s ORDER by id desc limit 1);

SELECT title FROM `st-onl`.books where taken_by_student_id = (select id from students s ORDER by id desc limit 1);

SELECT * from `st-onl`.students s join `groups` g on s.group_id = g.id join books b on s.id = b.taken_by_student_id join marks m on s.id = m.student_id;
