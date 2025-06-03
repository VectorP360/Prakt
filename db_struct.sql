CREATE TABLE IF NOT EXISTS workshop(
workshop_ID INTeger PRIMARY KEY,
workshop_name VARCHAR(20));

CREATE TABLE IF NOT EXISTS facility(
facility_ID INTeger PRIMARY KEY,
type_ID INTeger,
workshop_ID INTeger,
SCADA_scheme INTeger);

CREATE TABLE IF NOT EXISTS facility_types(
type_ID INTeger PRIMARY KEY,
type_name VARCHAR(35));

CREATE TABLE IF NOT EXISTS employee(
employee_ID INTEGER PRIMARY KEY,
surname VARCHAR(20),
name VARCHAR(20),
fathersname VARCHAR(20),
facility INTeger,
post_ID INTeger,
hire_date DATE,
employee_login VARCHAR(20),
employee_password VARCHAR(20));

CREATE TABLE IF NOT EXISTS posts(
post_ID INTeger PRIMARY KEY,
post_name VARCHAR(30));
    
CREATE TABLE IF NOT EXISTS scada_scheme(
scheme_ID INTEGER PRIMARY KEY,
scheme_name VARCHAR(30));

ALTER TABLE facility ADD FOREIGN KEY (workshop_ID) REFERENCES workshop (workshop_ID);
ALTER TABLE facility ADD FOREIGN KEY (type_ID) REFERENCES Ust_types (type_ID);
ALTER TABLE facility ADD FOREIGN KEY (scada_scheme) REFERENCES scada_scheme (scheme_ID);
    
ALTER TABLE employee ADD FOREIGN KEY (post_ID) REFERENCES posts (post_ID);
ALTER TABLE employee ADD FOREIGN KEY (facility) REFERENCES facility (ust_ID);