import psycopg

con = psycopg.connect(
    dbname="Zavod",
    user="postgres",
    password="mysecretpassword",
    host="localhost",
    port="5432"
)

cur = con.cursor()

executer = cur.execute(
    '''CREATE TABLE IF NOT EXISTS ceh(
    ceh_ID INTeger PRIMARY KEY);

    CREATE TABLE IF NOT EXISTS ustanovka(
    ust_ID INTeger PRIMARY KEY,
    Type VARCHAR(35),
    ceh_ID INTeger,
    SCADA_schema INTeger);

    CREATE TABLE IF NOT EXISTS Ust_types(
    Type VARCHAR(35) PRIMARY KEY);

    CREATE TABLE IF NOT EXISTS employee(
    employee_ID INTEGER PRIMARY KEY,
    FIO VARCHAR(50),
    Ustanovka INTeger,
    post VARCHAR(30),
    hire_date DATE,
    login VARCHAR(20),
    password VARCHAR(20));

    CREATE TABLE IF NOT EXISTS posts(
    post_name VARCHAR(30) PRIMARY KEY);
    
    CREATE TABLE IF NOT EXISTS SCADA_schema(
    schema_ID INTEGER PRIMARY KEY);''')

con.commit()

executer = cur.execute('''
    ALTER TABLE ustanovka ADD FOREIGN KEY (ceh_ID) REFERENCES ceh (ceh_ID);
    ALTER TABLE ustanovka ADD FOREIGN KEY (Type) REFERENCES Ust_types (Type);
    ALTER TABLE ustanovka ADD FOREIGN KEY (SCADA_schema) REFERENCES SCADA_schema (schema_ID);
    
    ALTER TABLE employee ADD FOREIGN KEY (post) REFERENCES posts (post_name);
    ALTER TABLE employee ADD FOREIGN KEY (Ustanovka) REFERENCES ustanovka (ust_ID);''')

con.commit()