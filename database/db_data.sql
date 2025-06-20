INSERT INTO workshop (workshop_id,name) VALUES (1,'Цех №1');
INSERT INTO workshop (workshop_id,name) VALUES (2,'Цех №2');
                       
INSERT INTO facility_type (facility_type_id,type_name) VALUES (1,'Шлифовальный');
INSERT INTO facility_type (facility_type_id,type_name) VALUES (2,'Токарный');
INSERT INTO facility_type (facility_type_id,type_name) VALUES (3,'Сверлильный');
INSERT INTO facility_type (facility_type_id,type_name) VALUES (4,'Резьбаобрабатывающий');
                       
INSERT INTO posts (post_id, name) VALUES (1,'Генеральный директор');
INSERT INTO posts (post_id, name) VALUES (2,'Главный специалист');
INSERT INTO posts (post_id, name) VALUES (3,'Старший специалист');
INSERT INTO posts (post_id, name) VALUES (4,'Специалист 1 категории');
                       
INSERT INTO facility (facility_id, name, type_ID, workshop_ID) VALUES (1,'Установка 1', 1, 1);
INSERT INTO facility (facility_id, name, type_ID, workshop_ID) VALUES (2,'Установка 2', 2, 1);
INSERT INTO facility (facility_id, name, type_ID, workshop_ID) VALUES (3,'Установка 3', 3, 2);
INSERT INTO facility (facility_id, name, type_ID, workshop_ID) VALUES (4,'Установка 4', 4, 2);
                       
INSERT INTO scada_scheme (scada_scheme_id, name, content, facility_id) VALUES (1,'Схема №1','Код Схемы',1);
INSERT INTO scada_scheme (scada_scheme_id, name, content, facility_id) VALUES (2,'Схема №2','Код Схемы',2);
INSERT INTO scada_scheme (scada_scheme_id, name, content, facility_id) VALUES (3,'Схема №3','Код Схемы',3);
INSERT INTO scada_scheme (scada_scheme_id, name, content, facility_id) VALUES (4,'Схема №4','Код Схемы',4);
                     
INSERT INTO users (surname, name, fathersname, facility_id, post_ID, hire_date, login, password) VALUES ('Морозов','Сергей','Сергеевич', 1, 1, '2022-03-21','MoroVoro','Vorobei');
INSERT INTO users (surname, name, fathersname, facility_id, post_ID, hire_date, login, password) VALUES ('Шпаков','Сергей','Викторович', 3, 3, '2023-04-15','Shpak','VotTak');
INSERT INTO users (surname, name, fathersname, facility_id, post_ID, hire_date, login, password) VALUES ('Круглов','Владимир','Иванович', 2, 2, '2023-04-13','Krug00','Shansonye');
INSERT INTO users (surname, name, fathersname, facility_id, post_ID, hire_date, login, password) VALUES ('Жуков','Дмитрий','Владимирович', 4, 4, '2023-05-05','ZhuDmi568','SDGgr32');
