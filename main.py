import psycopg

con = psycopg.connect(
    dbname="Zavod",
    user="postgres",
    password="mysecretpassword",
    host="localhost",
    port="5432"
)

class Data_reader:
    def __init__(self, table: str):
        self.__table = table,
        self.__cursor = con.cursor()

    @property
    def data(self):
        return self.__table
    
    @data.setter
    def data(self, new_table):
        self.__table = new_table

    def Lookup(self):
        self.__cursor.execute(f'''SELECT * FROM {self.__table};''')
        one_data = self.__cursor.fetchone()
        print(one_data)

data_reader = Data_reader("employee")
print(data_reader.data)
#data_reader.Lookup()