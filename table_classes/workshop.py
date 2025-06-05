
# Здесь workshop_id написан явно, 
# так как таким образом можно проще писать SQL запросы, 
# используя конструкцию USING. 
# Если кратко, то он использует Foreign и Primary Keys 
# для упразднения записи конструации JOIN <table> ON <condition> в JOIN <table> USING(<key_column>)
# Почитай про использование USING в SQL. 

# Поэтому явно указывать workshop_name не надо

class Workshop:
    def __init__(self, workshop_id: int, name: str):
        self.workshop_id = workshop_id
        self.name = name
