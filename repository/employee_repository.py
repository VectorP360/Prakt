from typing import List, Optional
from datetime import date

from psycopg import Connection

from schemas.employee import EmployeeOut, EmployeeIn, FacilityOut, PostsOut, FacilityTypeOut, WorkshopOut, ScadaSchemeOut


class EmployeeRepository:
    def __init__(self, connection: Connection):
        self.__connection = connection

    def create(self, new_employee: EmployeeIn)-> EmployeeOut:
        cursor = self.__connection.cursor()

        cursor.execute(
        '''
        INSERT INTO employee (surname, name, fathersname, facility, post_id, hire_date, employee_login, employee_password) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        RETURNING employee_id, surname, name, fathersname, facility, post_id, hire_date, employee_login, employee_password
        ''', (new_employee.surname, new_employee.name, new_employee.fathersname, new_employee.facility.facility_id, new_employee.post.post_ID,
            new_employee.hire_date, new_employee.employee_login, new_employee.employee_password,)
        )
        self.__connection.commit()
        
        fetched_row = cursor.fetchone()

        return EmployeeOut(
            employee_id=fetched_row[0],
            surname=fetched_row[1],
            name = fetched_row[2],
            fathersname = fetched_row[3],
            facility = new_employee.facility,
            post = new_employee.post,
            hire_date = fetched_row[6],
            employee_login = fetched_row[7],
            employee_password = fetched_row[8]
            )
        

    def get_by_ID(self, employee_id: str) -> Optional[EmployeeOut]:
        cursor = self.__connection.cursor()

        cursor.execute('''SELECT employee_id, surname, name, fathersname, facility.facility_id, facility.facility_name, facility_types.facility_type_id, facility_types.facility_type_name, 
                        workshop.workshop_id, workshop.workshop_name, scada_scheme.scheme_id, scada_scheme.scheme_name, posts.post_id, posts.post_name, hire_date, employee_login, employee_password
                        FROM employee
                        JOIN facility ON employee.facility = facility.facility_id
                            JOIN facility_types ON facility.facility_type_id = facility_types.facility_type_id
                            JOIN workshop ON facility.workshop_id = workshop.workshop_id
                            JOIN scada_scheme ON facility.scada_scheme_id = scada_scheme.scheme_id
                        JOIN posts USING (post_id)
                        WHERE employee_id = %s''', (employee_id,))

        fetched_row = cursor.fetchone()
        
        if fetched_row:
            return EmployeeOut(
                employee_id = fetched_row[0],
                surname = fetched_row[1],
                name = fetched_row[2],
                fathersname = fetched_row[3],
                facility = FacilityOut(
                    facility_id = fetched_row[4],
                    name = fetched_row[5],
                    type = FacilityTypeOut(
                        facility_type_ID = fetched_row[6],
                        facility_type_name = fetched_row[7]
                    ),
                    workshop = WorkshopOut(
                        workshop_id = fetched_row[8],
                        name = fetched_row[9]
                    ),
                    scada_scheme = ScadaSchemeOut(
                        scheme_ID = fetched_row[10],
                        scheme_name = fetched_row[11]
                    ),
                ),
                post = PostsOut(
                    post_ID = fetched_row[12],
                    post_name = fetched_row[13]
                ),
                hire_date = fetched_row[14],
                employee_login = fetched_row[15],
                employee_password = fetched_row[16]
            )
        else:
            return None
    
    
    def get_all(self) -> List[EmployeeOut]:
        cursor = self.__connection.cursor()

        cursor.execute('''
                        SELECT employee_id, surname, name, fathersname, facility.facility_id, facility.facility_name, facility_types.facility_type_id, facility_types.facility_type_name, 
                        workshop.workshop_id, workshop.workshop_name, scada_scheme.scheme_id, scada_scheme.scheme_name, posts.post_id, posts.post_name, hire_date, employee_login, employee_password
                        FROM employee
                        JOIN facility ON employee.facility = facility.facility_id
                            JOIN facility_types ON facility.facility_type_id = facility_types.facility_type_id
                            JOIN workshop ON facility.workshop_id = workshop.workshop_id
                            JOIN scada_scheme ON facility.scada_scheme_id = scada_scheme.scheme_id
                        JOIN posts USING (post_id)
                        ORDER BY employee_ID;
                       ''')
        
        result = []        
        for record in cursor.fetchall():
            new_employee = EmployeeOut(
                employee_id = record[0],
                surname = record[1],
                name = record[2],
                fathersname = record[3],
                facility = FacilityOut(
                    facility_id = record[4],
                    name = record[5],
                    type = FacilityTypeOut(
                        facility_type_ID = record[6],
                        facility_type_name = record[7]
                    ),
                    workshop = WorkshopOut(
                        workshop_id = record[8],
                        name = record[9]
                    ),
                    scada_scheme = ScadaSchemeOut(
                        scheme_ID = record[10],
                        scheme_name = record[11]
                    ),
                ),
                post = PostsOut(
                    post_ID = record[12],
                    post_name = record[13]
                ),
                hire_date = record[14],
                employee_login = record[15],
                employee_password = record[16]
            )
            result.append(new_employee)  
        return result


    def update(self, employee_id, new_employee: EmployeeIn) -> Optional[EmployeeOut]:
        cursor = self.__connection.cursor()

        cursor.execute(
        '''
        UPDATE employee SET surname = %s, name = %s, fathersname = %s, facility = %s, post_id = %s, hire_date = %s, employee_login = %s, employee_password = %s
        WHERE employee_id = %s

        RETURNING employee_id, surname, name, fathersname, hire_date, employee_login, employee_password''', 
        (new_employee.surname, new_employee.name, new_employee.fathersname, new_employee.facility.facility_id, new_employee.post.post_ID,
        new_employee.hire_date, new_employee.employee_login, new_employee.employee_password, employee_id,)
        )
        self.__connection.commit()

        fetched_row = cursor.fetchone()

        if fetched_row:
            facility = new_employee.facility
            post = new_employee.post
            return EmployeeOut(
                employee_id=fetched_row[0],
                surname=fetched_row[1],
                name = fetched_row[2],
                fathersname = fetched_row[3],
                facility = facility,
                post = post,
                hire_date = fetched_row[4],
                employee_login = fetched_row[5],
                employee_password = fetched_row[6]
            )
        else:
            return None


    def delete(self, employee_id: int) -> bool:
        cursor = self.__connection.cursor()
        
        cursor.execute('''DELETE FROM employee WHERE employee_ID = %s''', (employee_id,))
        self.__connection.commit()

        return bool(cursor.rowcount)