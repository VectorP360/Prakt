INSERT INTO workshop (workshop_ID, workshop_name) VALUES (1,'Цех №1');
INSERT INTO workshop (workshop_ID, workshop_name) VALUES (2,'Цех №2');
                       
INSERT INTO facility_types (type_ID, type_name) VALUES (1,'Шлифовальный');
INSERT INTO facility_types (type_ID, type_name) VALUES (2,'Токарный');
INSERT INTO facility_types (type_ID, type_name) VALUES (3,'Сверлильный');
INSERT INTO facility_types (type_ID, type_name) VALUES (4,'Резьбаобрабатывающий');
                       
INSERT INTO posts (post_ID, post_name) VALUES (1,'Шлифовщик');
INSERT INTO posts (post_ID, post_name) VALUES (2,'Токарь');
INSERT INTO posts (post_ID, post_name) VALUES (3,'Сверлильщик');
INSERT INTO posts (post_ID, post_name) VALUES (4,'Эксперт по обработке резьбы');
                       
INSERT INTO scada_schema (schema_ID, scheme_name) VALUES (1,'Схема №1');
INSERT INTO scada_schema (schema_ID, scheme_name) VALUES (2,'Схема №2');
INSERT INTO scada_schema (schema_ID, scheme_name) VALUES (3,'Схема №3');
INSERT INTO scada_schema (schema_ID, scheme_name) VALUES (4,'Схема №4');
                       
INSERT INTO facility (facility_ID, type_ID, workshop_ID, scada_schema) VALUES (1, 1, 1, 1);
INSERT INTO facility (facility_ID, type_ID, workshop_ID, scada_schema) VALUES (2, 2, 1, 2);
INSERT INTO facility (facility_ID, type_ID, workshop_ID, scada_schema) VALUES (3, 3, 2, 3);
INSERT INTO facility (facility_ID, type_ID, workshop_ID, scada_schema) VALUES (4, 4, 2, 4);
                     
INSERT INTO employee (employee_ID, surname, name, fathersname, facility, post_ID, hire_date, employee_login, employee_password) VALUES (1, 'Морозов','Сергей','Сергеевич', 1, 1, '2022-03-21','MoroVoro','Vorobei');
INSERT INTO employee (employee_ID, surname, name, fathersname, facility, post_ID, hire_date, employee_login, employee_password) VALUES (2, 'Шпаков','Сергей','Викторович', 3, 3, '2023-04-15','Shpak','VotTak');
INSERT INTO employee (employee_ID, surname, name, fathersname, facility, post_ID, hire_date, employee_login, employee_password) VALUES (3, 'Круглов','Владимир','Иванович', 2, 2, '2023-04-13','Krug00','Shansonye');
INSERT INTO employee (employee_ID, surname, name, fathersname, facility, post_ID, hire_date, employee_login, employee_password) VALUES (4, 'Жуков','Дмитрий','Владимирович', 4, 4, '2023-05-05','ZhuDmi568','SDGgr32');
