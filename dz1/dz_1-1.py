def celoe(a, b):
    result = a // b
    return result

def ostatok(a, b):
    result = a % b
    return result

second = int(input("Введите  количество секунд: "))

#переменные сколько секунд в минуте, часе, дне, итд
min_sec = 60
hour_sec = 60 * min_sec
day_sec = 24 * hour_sec
month_sec = 30 * day_sec # сильно не привязывался к разному количеству дней в месяца и весокосному году.
year_sec = 365 * day_sec

#переменные остатков от целых
year_ost = ostatok(second, year_sec)
month_ost = ostatok(year_ost, month_sec)
day_ost = ostatok(month_ost, day_sec)
hour_ost = ostatok(day_ost, hour_sec)
min_ost = ostatok(hour_ost, min_sec)

result = f'{second} second(s) = {celoe(second, year_sec)} year(s) {celoe(year_ost, month_sec)} month(s)' \
         f' {celoe(month_ost, day_sec)} day(s) {celoe(day_ost, hour_sec)} hour(s) {celoe(hour_ost, min_sec)}' \
         f' min {min_ost} sec'

print(result)
