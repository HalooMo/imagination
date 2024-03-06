from mysql.connector import connect
from logging import info


def data_b_add(value):
    with connect(
        host="localhost",
        user="root",
        password="Sazim16pk#",
        database="image_data"
    ) as connection:
        try:
            query_form = """
            INSERT INTO image_tabel(img_path, oder, saves)
            VALUES(%s, %s, %s)
            """
            query_data = []
            query_data.append(value)
            info(query_data)
            with connection.cursor() as cursor:
                cursor.executemany(query_form, query_data)
                connection.commit()
                query_data.clear()
        except Exception as e:
            print(e)

def data_b_recieve():
    with connect(
        host="localhost",
        user="root",
        password="Sazim16pk#",
        database="image_data"
    ) as connection:
        try:
            query = "SELECT * FROM image_tabel"
            data = []
            with connection.cursor() as cursor:
                cursor.execute(query)
                for i in cursor.fetchall():
                    data.append((i[1], i[2], i[3]))
                return data
                
                         
        except Exception as e:
            print(e)
