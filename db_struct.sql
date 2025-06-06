DROP TABLE IF EXISTS workshop CASCADE;

CREATE TABLE IF NOT EXISTS workshop(
workshop_ID SERIAL PRIMARY KEY,
workshop_name VARCHAR(20)
);


DROP TABLE IF EXISTS facility_types CASCADE;

CREATE TABLE IF NOT EXISTS facility_types(
type_ID SERIAL PRIMARY KEY,
type_name VARCHAR(35)
);


DROP TABLE IF EXISTS posts CASCADE;

CREATE TABLE IF NOT EXISTS posts(
post_ID SERIAL PRIMARY KEY,
post_name VARCHAR(30)
);
    

DROP TABLE IF EXISTS scada_scheme CASCADE;

CREATE TABLE IF NOT EXISTS scada_scheme(
scheme_ID SERIAL PRIMARY KEY,
scheme_name VARCHAR(30)
);


DROP TABLE IF EXISTS facility CASCADE;

CREATE TABLE IF NOT EXISTS facility(
facility_ID SERIAL PRIMARY KEY,
facility_name VARCHAR(30),
type_id INTEGER,
workshop_id INTEGER,
SCADA_scheme INTEGER,
FOREIGN KEY (workshop_ID) REFERENCES workshop (workshop_id),
FOREIGN KEY (type_ID) REFERENCES facility_types (type_id),
FOREIGN KEY (scada_scheme) REFERENCES scada_scheme (scheme_id)
);


DROP TABLE IF EXISTS employee CASCADE;

CREATE TABLE IF NOT EXISTS employee(
employee_ID SERIAL PRIMARY KEY,
surname VARCHAR(20),
name VARCHAR(20),
fathersname VARCHAR(20),
facility INTeger,
post_id INTEGER,
hire_date DATE,
employee_login VARCHAR(20),
employee_password VARCHAR(20),
FOREIGN KEY (post_id) REFERENCES posts (post_id),
FOREIGN KEY (facility) REFERENCES facility (facility_ID)
);