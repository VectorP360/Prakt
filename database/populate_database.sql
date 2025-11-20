INSERT INTO public.workshop (workshop_id,name) VALUES (1,'Цех №1');
INSERT INTO public.workshop (workshop_id,name) VALUES (2,'Цех №2');
                       
INSERT INTO public.facility_type (facility_type_id,name) VALUES (1,'Шлифовальный');
INSERT INTO public.facility_type (facility_type_id,name) VALUES (2,'Токарный');
INSERT INTO public.facility_type (facility_type_id,name) VALUES (3,'Сверлильный');
INSERT INTO public.facility_type (facility_type_id,name) VALUES (4,'Резьбаобрабатывающий');
                       
INSERT INTO public.post (post_id, name) VALUES (1,'Генеральный директор');
INSERT INTO public.post (post_id, name) VALUES (2,'Главный специалист');
INSERT INTO public.post (post_id, name) VALUES (3,'Старший специалист');
INSERT INTO public.post (post_id, name) VALUES (4,'Специалист 1 категории');
                       
INSERT INTO public.facility (facility_id, name, type_id, workshop_id) VALUES (1,'Установка 1', 1, 1);
INSERT INTO public.facility (facility_id, name, type_id, workshop_id) VALUES (2,'Установка 2', 2, 1);
INSERT INTO public.facility (facility_id, name, type_id, workshop_id) VALUES (3,'Установка 3', 3, 2);
INSERT INTO public.facility (facility_id, name, type_id, workshop_id) VALUES (4,'Установка 4', 4, 2);
                       
INSERT INTO public.scada_scheme (scada_scheme_id, name, content, facility_id) VALUES (1,'Схема №1','Код Схемы',1);
INSERT INTO public.scada_scheme (scada_scheme_id, name, content, facility_id) VALUES (2,'Схема №2','Код Схемы',2);
INSERT INTO public.scada_scheme (scada_scheme_id, name, content, facility_id) VALUES (3,'Схема №3','Код Схемы',3);
INSERT INTO public.scada_scheme (scada_scheme_id, name, content, facility_id) VALUES (4,'Схема №4','Код Схемы',4);
                     
INSERT INTO public.user (surname, name, fathersname, facility_id, post_id, hire_date, login, password) VALUES ('Морозов','Сергей','Сергеевич', 1, 1, '2022-03-21','MoroVoro','Vorobei');
INSERT INTO public.user (surname, name, fathersname, facility_id, post_id, hire_date, login, password) VALUES ('Шпаков','Сергей','Викторович', 3, 3, '2023-04-15','Shpak','VotTak');
INSERT INTO public.user (surname, name, fathersname, facility_id, post_id, hire_date, login, password) VALUES ('Круглов','Владимир','Иванович', 2, 2, '2023-04-13','Krug00','Shansonye');
INSERT INTO public.user (surname, name, fathersname, facility_id, post_id, hire_date, login, password) VALUES ('Жуков','Дмитрий','Владимирович', 4, 4, '2023-05-05','ZhuDmi568','SDGgr32');

INSERT INTO public.element_type (element_type_id ,name) VALUES (1, 'Микроконтроллер');
INSERT INTO public.element_type (element_type_id ,name) VALUES (2, 'Шаговый двигатель');
INSERT INTO public.element_type (element_type_id ,name) VALUES (3, 'Датчик');
INSERT INTO public.element_type (element_type_id ,name) VALUES (4, 'Панель');

INSERT INTO public.element (name, material, element_type_id, facility_id) VALUES ('stm32', 'Кремний', 1, 1);
INSERT INTO public.element (name, material, element_type_id, facility_id) VALUES ('NEMA 17', 'Железо', 2, 2);
INSERT INTO public.element (name, material, element_type_id, facility_id) VALUES ('Термостат', 'Алюминий', 3, 3);
INSERT INTO public.element (name, material, element_type_id, facility_id) VALUES ('Панель управления', 'Пластик', 4, 4);

INSERT INTO public.condition (temperature, loading, pressure, facility_id) VALUES (65, 70, 43, 1);
INSERT INTO public.condition (temperature, loading, pressure, facility_id) VALUES (50, 62, 32, 2);
INSERT INTO public.condition (temperature, loading, pressure, facility_id) VALUES (74, 81, 48, 3);
INSERT INTO public.condition (temperature, loading, pressure, facility_id) VALUES (59, 67, 36, 4);
