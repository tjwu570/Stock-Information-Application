import psycopg2

try:
    connection = psycopg2.connect(user="postgres",
                                  password="postgres",
                                  host="database-1.c4alhaecwxce.us-east-1.rds.amazonaws.com",
                                  port="5432",
                                  database="dbhw1")
    cursor = connection.cursor()

    postgres_insert_query = """ INSERT INTO list VALUES (%s,%s,%s,%s,%s,%s,%s,%s) """
    record_to_insert = ('股票', '1101', '台泥', 'TW0001101004', '1962/02/09', '上市', '水泥工業', 'ESVUFR')
    cursor.execute(postgres_insert_query, record_to_insert)


    connection.commit()
    count = cursor.rowcount
    print(count, "Record inserted successfully into mobile table")

except (Exception, psycopg2.Error) as error:
    print("Failed to insert record into mobile table", error)

finally:
    # closing database connection.
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")