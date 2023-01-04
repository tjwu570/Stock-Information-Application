import csv
import psycopg2
from psycopg2.extras import RealDictCursor
import json
import twstock
from twstock import Stock
import numpy 

stock_id = '2330'

stock = twstock.Stock(stock_id)

# stock_open = numpy.asarray(stock.open)
stock_close = numpy.asarray(stock.close)
stock_high = numpy.asarray(stock.high)
stock_low = numpy.asarray(stock.low)
stock_date = numpy.asarray(stock.date)

print(stock_close)