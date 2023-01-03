import psycopg2
from psycopg2.extras import RealDictCursor
import json
import twstock
from twstock import Stock

host = "database-1.c4alhaecwxce.us-east-1.rds.amazonaws.com"
username = "postgres"
password = "postgres"
database = "dbhw1"

conn = psycopg2.connect(
    host = host,
    database = database,
    user = username,
    password = password
)
cur = conn.cursor(cursor_factory = RealDictCursor)
stock_list = twstock.twse


cur.execute("insert into list values(\'股票\', 1110, \'台泥\', \'TW0001101004\', \'1962/02/09\', \'上市\', \'水泥工業\', \'ESVUFR\')")



# Iterate over the first 3 elements in the dictionary
for i, (key, value) in enumerate(stock_list.items()):
    # print(key, value)
    command = ' insert into list values(\'' + stock_list[key].type + '\', \'' + stock_list[key].code + '\', \'' + stock_list[key].name + '\', \'' + stock_list[key].ISIN + '\', \'' + stock_list[key].start + '\', \'' + stock_list[key].market + '\', \'' + stock_list[key].group + '\', \'' + stock_list[key].CFI + '\');' 
    
    cur.execute(command)
    conn.commit()
    # results = cur.fetchall()

    
    if i == 20:
        break

cur.execute('select * from list limit 10')
results = cur.fetchall()
print(results)




# for i in len(twstock.twsw):
#     cur = conn.cursor(cursor_factory = RealDictCursor)
#     cur.execute("insert into list values")
#     results = cur.fetchall()
#     json_result = json.dumps(results)
#     print(json_result)