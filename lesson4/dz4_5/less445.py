from less43 import conv_val
import sys
import datetime

get_float = (conv_val(valute=sys.argv[1].upper()))
print(float(get_float[1].replace(',', '.')))
date = get_float[0].split(".")
print(datetime.date(int(date[2]), int(date[1]), int(date[0])))