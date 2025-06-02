import psycopg

con = psycopg.connect(
    dbname="Zavod",
    user="postgres",
    password="mysecretpassword",
    host="localhost",
    port="5432"
)

cur = con.cursor()

executer = cur.execute('''
  INSERT INTO ceh (ceh_ID) VALUES (1);
  INSERT INTO ceh (ceh_ID) VALUES (2);
                       
  INSERT INTO Ust_types (Type) VALUES ('Шлифовальный');
  INSERT INTO Ust_types (Type) VALUES ('Токарный');
  INSERT INTO Ust_types (Type) VALUES ('Сверлильный');
  INSERT INTO Ust_types (Type) VALUES ('Резьбаобрабатывающий');
                       
  INSERT INTO posts (post_name) VALUES ('Шлифовщик');
  INSERT INTO posts (post_name) VALUES ('Токарь');
  INSERT INTO posts (post_name) VALUES ('Сверлильщик');
  INSERT INTO posts (post_name) VALUES ('Эксперт по обработке резьбы');
                       
  INSERT INTO SCADA_schema (schema_ID) VALUES (1);
  INSERT INTO SCADA_schema (schema_ID) VALUES (2);
  INSERT INTO SCADA_schema (schema_ID) VALUES (3);
  INSERT INTO SCADA_schema (schema_ID) VALUES (4);
                       
  INSERT INTO ustanovka (ust_ID, Type, ceh_ID, SCADA_schema) VALUES (1, 'Шлифовальный', 1, 1);
  INSERT INTO ustanovka (ust_ID, Type, ceh_ID, SCADA_schema) VALUES (2, 'Токарный', 1, 2);
  INSERT INTO ustanovka (ust_ID, Type, ceh_ID, SCADA_schema) VALUES (3, 'Сверлильный', 2, 3);
  INSERT INTO ustanovka (ust_ID, Type, ceh_ID, SCADA_schema) VALUES (4, 'Резьбаобрабатывающий', 2, 4);
                     
  INSERT INTO employee (employee_ID, FIO, Ustanovka, post, hire_date, login, password) VALUES (1, 'Морозов С.С', 1, 'Шлифовщик', '2022-03-21','MoroVoro','Vorobei');
  INSERT INTO employee (employee_ID, FIO, Ustanovka, post, hire_date, login, password) VALUES (2, 'Шпаков С.В', 3, 'Сверлильщик', '2023-04-15','Shpak','VotTak');
  INSERT INTO employee (employee_ID, FIO, Ustanovka, post, hire_date, login, password) VALUES (3, 'Круглов В.И', 2, 'Токарь', '2023-04-13','Krug00','Shansonye');
  INSERT INTO employee (employee_ID, FIO, Ustanovka, post, hire_date, login, password) VALUES (4, 'Жуков Д.В', 4, 'Эксперт по обработке резьбы', '2023-05-05','ZhuDmi568','SDGgr32');
  ''')
con.commit()