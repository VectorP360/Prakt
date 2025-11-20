from typing import List, Optional

from psycopg import Connection

from schemas.user import UserOut, UserIn
from schemas.facility import FacilityOut
from schemas.post import PostOut
from schemas.facility_type import FacilityTypeOut
from schemas.workshop import WorkshopOut


class UserRepository:
    def __init__(self, connection: Connection):
        self.__connection = connection

    def create(self, new_user: UserIn) -> Optional[UserOut]:
        cursor = self.__connection.cursor()

        cursor.execute(
            """
        INSERT INTO user (surname, name, fathersname, facility_id, post_id, hire_date, login, password) VALUES (%s,%s,%s,%s,%s,%s,%s,%s)
        RETURNING user_id, surname, name, fathersname, facility_id, post_id, hire_date, login, password
        """,
            (
                new_user.surname,
                new_user.name,
                new_user.fathersname,
                new_user.facility.facility_id,
                new_user.post.post_ID,
                new_user.hire_date,
                new_user.login,
                new_user.password,
            ),
        )
        self.__connection.commit()

        fetched_row = cursor.fetchone()

        if fetched_row:
            return UserOut(
                user_id=fetched_row[0],
                surname=fetched_row[1],
                name=fetched_row[2],
                fathersname=fetched_row[3],
                facility=new_user.facility,
                post=new_user.post,
                hire_date=fetched_row[6],
                login=fetched_row[7],
                password=fetched_row[8],
            )
        return None

    def get_by_ID(self, user_id: str) -> Optional[UserOut]:
        cursor = self.__connection.cursor()

        cursor.execute(
            """SELECT user_id, surname, user.name, fathersname, facility.facility_id, facility.name, facility_type.facility_type_id, facility_type.name,
                        workshop.workshop_id, workshop.name, post.post_id, post.name, hire_date, login, password
                        FROM user
                        JOIN facility ON user.facility_id = facility.facility_id
                            JOIN facility_type ON facility.type_id = facility_type.facility_type_id
                            JOIN workshop ON facility.workshop_id = workshop.workshop_id
                        JOIN post USING (post_id)
                        WHERE user_id = %s""",
            (user_id,),
        )

        fetched_row = cursor.fetchone()

        if fetched_row:
            return UserOut(
                user_id=fetched_row[0],
                surname=fetched_row[1],
                name=fetched_row[2],
                fathersname=fetched_row[3],
                facility=FacilityOut(
                    facility_id=fetched_row[4],
                    name=fetched_row[5],
                    type=FacilityTypeOut(
                        facility_type_id=fetched_row[6], name=fetched_row[7]
                    ),
                    workshop=WorkshopOut(
                        workshop_id=fetched_row[8], name=fetched_row[9]
                    ),
                ),
                post=PostOut(post_ID=fetched_row[10], name=fetched_row[11]),
                hire_date=fetched_row[12],
                login=fetched_row[13],
                password=fetched_row[14],
            )
        else:
            return None

    def get_by_login(self, login: str, password: str) -> Optional[UserOut]:
        cursor = self.__connection.cursor()

        cursor.execute(
            """SELECT user_id, surname, user.name, fathersname, facility.facility_id, facility.name, facility_type.facility_type_id, facility_type.name,
                        workshop.workshop_id, workshop.name, post.post_id, post.name, hire_date, login, password
                        FROM user
                        JOIN facility ON user.facility_id = facility.facility_id
                            JOIN facility_type ON facility.type_id = facility_type.facility_type_id
                            JOIN workshop ON facility.workshop_id = workshop.workshop_id
                        JOIN post USING (post_id)
                        WHERE user.login = %s AND user.password = %s""",
            (login, password),
        )

        fetched_row = cursor.fetchone()

        if fetched_row:
            return UserOut(
                user_id=fetched_row[0],
                surname=fetched_row[1],
                name=fetched_row[2],
                fathersname=fetched_row[3],
                facility=FacilityOut(
                    facility_id=fetched_row[4],
                    name=fetched_row[5],
                    type=FacilityTypeOut(
                        facility_type_id=fetched_row[6], name=fetched_row[7]
                    ),
                    workshop=WorkshopOut(
                        workshop_id=fetched_row[8], name=fetched_row[9]
                    ),
                ),
                post=PostOut(post_ID=fetched_row[10], name=fetched_row[11]),
                hire_date=fetched_row[12],
                login=fetched_row[13],
                password=fetched_row[14],
            )
        else:
            return None

    def get_by_FIO(
        self,
        surname: str,
        name: str,
        fathersname: str,
        facility_name: str,
        post_name: str,
    ) -> Optional[UserOut]:
        cursor = self.__connection.cursor()

        cursor.execute(
            """SELECT user_id, surname, user.name, fathersname, facility.facility_id, facility.name, facility_type.facility_type_id, facility_type.name,
                        workshop.workshop_id, workshop.name, post.post_id, post.name, hire_date, login, password
                        FROM user
                        JOIN facility ON user.facility_id = facility.facility_id
                            JOIN facility_type ON facility.type_id = facility_type.facility_type_id
                            JOIN workshop ON facility.workshop_id = workshop.workshop_id
                        JOIN post USING (post_id)
                        WHERE surname = %s AND user.name = %s AND fathersname = %s AND facility.name = %s AND post.name = %s""",
            (surname, name, fathersname, facility_name, post_name),
        )

        fetched_row = cursor.fetchone()

        if fetched_row:
            return UserOut(
                user_id=fetched_row[0],
                surname=fetched_row[1],
                name=fetched_row[2],
                fathersname=fetched_row[3],
                facility=FacilityOut(
                    facility_id=fetched_row[4],
                    name=fetched_row[5],
                    type=FacilityTypeOut(
                        facility_type_id=fetched_row[6], name=fetched_row[7]
                    ),
                    workshop=WorkshopOut(
                        workshop_id=fetched_row[8], name=fetched_row[9]
                    ),
                ),
                post=PostOut(post_ID=fetched_row[10], name=fetched_row[11]),
                hire_date=fetched_row[12],
                login=fetched_row[13],
                password=fetched_row[14],
            )
        else:
            return None

    def get_all(self) -> List[UserOut]:
        cursor = self.__connection.cursor()

        cursor.execute("""
                        SELECT user_id, surname, user.name, fathersname, facility.facility_id, facility.name, facility_type.facility_type_id, facility_type.name,
                        workshop.workshop_id, workshop.name, post.post_id, post.name, hire_date, login, password
                        FROM user
                        JOIN facility ON user.facility_id = facility.facility_id
                            JOIN facility_type ON facility.type_id = facility_type.facility_type_id
                            JOIN workshop ON facility.workshop_id = workshop.workshop_id
                        JOIN post USING (post_id)
                        ORDER BY user_ID;
                       """)

        result = []
        for record in cursor.fetchall():
            new_user = UserOut(
                user_id=record[0],
                surname=record[1],
                name=record[2],
                fathersname=record[3],
                facility=FacilityOut(
                    facility_id=record[4],
                    name=record[5],
                    type=FacilityTypeOut(facility_type_id=record[6], name=record[7]),
                    workshop=WorkshopOut(workshop_id=record[8], name=record[9]),
                ),
                post=PostOut(post_ID=record[10], name=record[11]),
                hire_date=record[12],
                login=record[13],
                password=record[14],
            )
            result.append(new_user)
        return result

    def get_by_scada(self, scada_scheme_id: str):
        cursor = self.__connection.cursor()

        cursor.execute(
            """
                        SELECT user_id, surname, user.name, fathersname, facility.facility_id, facility.name, facility_type.facility_type_id, facility_type.name,
                        workshop.workshop_id, workshop.name, post.post_id, post.name, hire_date, login, password, scada_scheme_id, scada_scheme.name, scada_scheme.content
                        FROM user
                        JOIN facility ON user.facility_id = facility.facility_id
                            JOIN scada_scheme on facility.facility_id = scada_scheme.facility_id
                            JOIN facility_type ON facility.type_id = facility_type.facility_type_id
                            JOIN workshop ON facility.workshop_id = workshop.workshop_id
                        JOIN post USING (post_id)
                        WHERE scada_scheme.scada_scheme_id = %s
                       """,
            (scada_scheme_id,),
        )

        fetched_row = cursor.fetchone()

        if fetched_row:
            return UserOut(
                user_id=fetched_row[0],
                surname=fetched_row[1],
                name=fetched_row[2],
                fathersname=fetched_row[3],
                facility=FacilityOut(
                    facility_id=fetched_row[4],
                    name=fetched_row[5],
                    type=FacilityTypeOut(
                        facility_type_id=fetched_row[6], name=fetched_row[7]
                    ),
                    workshop=WorkshopOut(
                        workshop_id=fetched_row[8], name=fetched_row[9]
                    ),
                ),
                post=PostOut(post_ID=fetched_row[10], name=fetched_row[11]),
                hire_date=fetched_row[12],
                login=fetched_row[13],
                password=fetched_row[14],
            )
        else:
            return None

    def update(self, user_id, new_user: UserIn) -> Optional[UserOut]:
        cursor = self.__connection.cursor()

        cursor.execute(
            """
        UPDATE user SET surname = %s, name = %s, fathersname = %s, facility_id = %s, post_id = %s, hire_date = %s, login = %s, password = %s
        WHERE user_id = %s

        RETURNING user_id, surname, name, fathersname, hire_date, login, password""",
            (
                new_user.surname,
                new_user.name,
                new_user.fathersname,
                new_user.facility.facility_id,
                new_user.post.post_ID,
                new_user.hire_date,
                new_user.login,
                new_user.password,
                user_id,
            ),
        )
        self.__connection.commit()

        fetched_row = cursor.fetchone()

        if fetched_row:
            facility = new_user.facility
            post = new_user.post
            return UserOut(
                user_id=fetched_row[0],
                surname=fetched_row[1],
                name=fetched_row[2],
                fathersname=fetched_row[3],
                facility=facility,
                post=post,
                hire_date=fetched_row[4],
                login=fetched_row[5],
                password=fetched_row[6],
            )
        else:
            return None

    def delete(self, user_id: int) -> bool:
        cursor = self.__connection.cursor()

        cursor.execute("""DELETE FROM user WHERE user_ID = %s""", (user_id,))
        self.__connection.commit()

        return bool(cursor.rowcount)
