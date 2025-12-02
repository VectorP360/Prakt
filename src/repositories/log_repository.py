from typing import Optional

from psycopg import Connection

from schemas.operation import OperationOut
from schemas.post import PostOut
from schemas.workshop import WorkshopOut
from schemas.facility_type import FacilityTypeOut
from schemas.facility import FacilityOut
from schemas.user import UserOut
from schemas.log import LogIn, LogOut

class LogRepository:
    def __init__(self, connection: Connection):
        self.__connection = connection

    def create(self, log_in: LogIn) -> Optional[LogOut]:
        cursor = self.__connection.cursor()

        cursor.execute(
            """
            INSERT INTO log (operation_date, user_id, operation_id) VALUES (%s, %s, %s)
            RETURNING log_id, operation_date, user_id, operation_id
            """,
            (log_in.operation_date, log_in.user.user_id, log_in.operation.operation_id,),
        )

        self.__connection.commit()

        fetched_row = cursor.fetchone()

        if fetched_row:
            return LogOut(
                log_id=fetched_row[0],
                operation_date=fetched_row[1],
                user=log_in.user,
                operation=log_in.operation
            )
        return None
    
    def get_by_id(self, log_id: int) -> Optional[LogOut]:
        cursor = self.__connection.cursor()

        cursor.execute(
            """
            SELECT public.log.log_id, public.log.operation_date, public.user.user_id, public.user.surname, public.user.name, public.user.fathersname, 
                public.facility.facility_id, public.facility.name, public.facility_type.facility_type_id, public.facility_type.name,
                public.workshop.workshop_id, public.workshop.name, public.post.post_id, public.post.name, public.user.hire_date, public.user.login,
                public.user.password, public.operation.operation_id, public.operation.name
            FROM public.log
                JOIN public.user ON public.log.user_id = public.user.user_id
                JOIN public.facility ON public.user.facility_id = public.facility.facility_id
                JOIN public.facility_type ON public.facility.type_id = public.facility_type.facility_type_id
                JOIN public.workshop ON public.facility.workshop_id = public.workshop.workshop_id
            WHERE public.log.log_id = %s
            """
        )

        fetched_row = cursor.fetchone()

        if fetched_row:
            return LogOut(
                log_id=fetched_row[0],
                operation_date=fetched_row[1],
                user=UserOut(
                    user_id=fetched_row[2],
                    surname=fetched_row[3],
                    name=fetched_row[4],
                    fathersname=fetched_row[5],
                    facility=FacilityOut(
                        facility_id=fetched_row[6],
                        name=fetched_row[7],
                        type=FacilityTypeOut(
                            facility_type_id=fetched_row[8],
                            name=fetched_row[9]
                        ),
                        workshop=WorkshopOut(
                            workshop_id=fetched_row[10],
                            name=fetched_row[11]
                        )
                    ),
                    post=PostOut(
                        post_ID=fetched_row[12],
                        name=fetched_row[13]
                    ),
                    hire_date=fetched_row[14],
                    login=fetched_row[15],
                    password=fetched_row[16]
                ),
                operation=OperationOut(
                    operation_id=fetched_row[17],
                    name=fetched_row[18]
                )
            )
        return None
    
    def get_all(self, log_id: int) -> Optional[list]:
        cursor = self.__connection.cursor()

        cursor.execute(
            """
            SELECT public.log.log_id, public.log.operation_date, public.user.user_id, public.user.surname, public.user.name, public.user.fathersname, 
                public.facility.facility_id, public.facility.name, public.facility_type.facility_type_id, public.facility_type.name,
                public.workshop.workshop_id, public.workshop.name, public.post.post_id, public.post.name, public.user.hire_date, public.user.login,
                public.user.password, public.operation.operation_id, public.operation.name
            FROM public.log
                JOIN public.user ON public.log.user_id = public.user.user_id
                JOIN public.facility ON public.user.facility_id = public.facility.facility_id
                JOIN public.facility_type ON public.facility.type_id = public.facility_type.facility_type_id
                JOIN public.workshop ON public.facility.workshop_id = public.workshop.workshop_id
            ORDER BY public.log.log_id DESC
            """
        )

        result = []
        fetched_rows = cursor.fetchall()

        if fetched_rows:
            for record in fetched_rows:
                founded_log = LogOut(
                    log_id=record[0],
                    operation_date=record[1],
                    user=UserOut(
                        user_id=record[2],
                        surname=record[3],
                        name=record[4],
                        fathersname=record[5],
                        facility=FacilityOut(
                            facility_id=record[6],
                            name=record[7],
                            type=FacilityTypeOut(
                                facility_type_id=record[8],
                                name=record[9]
                            ),
                            workshop=WorkshopOut(
                                workshop_id=record[10],
                                name=record[11]
                            )
                        ),
                        post=PostOut(
                            post_ID=record[12],
                            name=record[13]
                        ),
                        hire_date=record[14],
                        login=record[15],
                        password=record[16]
                    ),
                    operation=OperationOut(
                        operation_id=record[17],
                        name=record[18]
                    )
                )
                result.append(founded_log)
                
            return result
        
        return None
    
    def update(self, new_log: LogIn) -> Optional[LogOut]:
        cursor = self.__connection.cursor()

        cursor.execute(
            """
            UPDATE log SET operation_date = %s, user_id = %s, operation_id = %s
            WHERE log_id = %s
            RETURNING log_id, operation_date
            """,
            (new_log.operation_date, new_log.user.user_id, new_log.operation.operation_id,),
        )

        self.__connection.commit()

        fetched_row = cursor.fetchone()

        if fetched_row:
            return LogOut(
                log_id=fetched_row[0],
                operation_date=fetched_row[1],
                user=new_log.user,
                operation=new_log.operation
            )
        
        return None
    
    def delete(self, log_id: int) -> bool:
        cursor = self.__connection.cursor()

        cursor.execute("""DELETE FROM log WHERE log_id = %s""", (log_id,))
        self.__connection.commit()

        return bool(cursor.rowcount)