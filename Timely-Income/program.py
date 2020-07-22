import csv
from datetime import date, timedelta, datetime

filename1 = 'Basic.txt'
filename2 = 'Delux.txt'
filename3 = 'Total.txt'

rows = []
basic = []
delux = []
total = []
dates = []
weekly_list = []
monthly_list = []
yearly_list = []

# Read contents from Basic.txt file and append its contents to a list
with open(filename1, 'r') as csvfile:
    csvreader1 = csv.reader(csvfile, delimiter='\n')
    for row in csvreader1:
        rows.append(row)

for row in rows[1:]:
    basic.append(int(row[0]))

rows.clear()

# Read contents from Delux.txt file and append its contents to a list
with open(filename2, 'r') as csvfile:
    csvreader2 = csv.reader(csvfile, delimiter='\n')
    for row in csvreader2:
        rows.append(row)

for row in rows[1:]:
    delux.append(int(row[0]))

rows.clear()

# Read contents from Total.txt file and append its contents to a list
with open(filename3, 'r') as csvfile:
    csvreader3 = csv.reader(csvfile, delimiter='\n')
    for row in csvreader3:
        rows.append(row)

for row in rows[1:]:
    total.append(int(row[0]))

rows.clear()

# Writing dates into dates.txt file accordingly
with open('Dates.txt', 'w') as csvfile:
    csvwriter1 = csv.writer(csvfile, delimiter='\n')
    for i in range(len(basic)):
        dates.append((date.today() - timedelta(days = i)).isoformat())

    dates.append('Dates:')
    dates.reverse()
    csvwriter1.writerow(dates)

# Type conversion string to dates
dates.pop(0)
for i in range(len(dates)):
    date_obj = datetime.strptime(dates[i], '%Y-%m-%d')
    dates[i] = date_obj


# Writing requirements into Yearly.txt file
with open('Revenue-Yearly.csv', 'w') as yearly:
    csvyearly = csv.writer(yearly)
    fields = ['Year','Number of Basic', 'Number of Delux', 'Total Income']
    csvyearly.writerow(fields)

    no_of_basic = no_of_delux = total_income = iteration = 0
    start_date = dates[0]
    end_date = dates[len(dates)-1]
    temp_list = []
    temp_lists = []
    present_year = start_date.year

    while(start_date <= end_date):
        if(start_date.year == present_year):
            no_of_basic += basic[iteration]
            no_of_delux += delux[iteration]
            total_income += total[iteration]
        else:
            temp_list.append(present_year)
            temp_list.append(no_of_basic)
            temp_list.append(no_of_delux)
            temp_list.append(total_income)

            temp_lists.append(temp_list)
            temp_list = []
            no_of_basic = no_of_delux = total_income = 0
            present_year = start_date.year

        start_date += timedelta(days=1)
        iteration +=1

    temp_list.append(present_year)
    temp_list.append(no_of_basic)
    temp_list.append(no_of_delux)
    temp_list.append(total_income)
    temp_lists.append(temp_list)

    csvyearly.writerows(temp_lists)


# Writing requirements into Monthly.txt file
with open('Revenue-Monthly.csv', 'w') as monthly:
    csvmonthly = csv.writer(monthly)
    fields = ['Month','Number of Basic', 'Number of Delux', 'Total Income']
    csvmonthly.writerow(fields)

    no_of_basic = no_of_delux = total_income = iteration = 0
    start_date = dates[0]
    end_date = dates[len(dates)-1]
    temp_list = []
    temp_lists = []
    present_month = start_date.month

    while(start_date <= end_date):
        if(start_date.month == present_month):
            no_of_basic += basic[iteration]
            no_of_delux += delux[iteration]
            total_income += total[iteration]
        else:
            temp_list.append(present_month)
            temp_list.append(no_of_basic)
            temp_list.append(no_of_delux)
            temp_list.append(total_income)
            temp_lists.append(temp_list)
            temp_list = []
            no_of_basic = no_of_delux = total_income = 0
            present_month = start_date.month

        start_date += timedelta(days=1)
        iteration +=1

    temp_list.append(present_month)
    temp_list.append(no_of_basic)
    temp_list.append(no_of_delux)
    temp_list.append(total_income)
    temp_lists.append(temp_list)
    csvmonthly.writerows(temp_lists)

# Writing requirements into Weekly.txt file
with open('Revenue-Weekly.csv', 'w') as weekly:
    csvweekly = csv.writer(weekly)
    fields = ['Week','Number of Basic', 'Number of Delux', 'Total Income']
    csvweekly.writerow(fields)

    no_of_basic = no_of_delux = total_income = week = day_count = iteration = 0

    start_date = dates[0]
    end_date = dates[len(dates)-1]
    temp_list = []
    temp_lists = []

    while(start_date <= end_date):
        day_count +=1
        no_of_basic += basic[iteration]
        no_of_delux += delux[iteration]
        total_income += total[iteration]

        if(day_count == 7):
            week += 1
            temp_list.append(week)
            temp_list.append(no_of_basic)
            temp_list.append(no_of_delux)
            temp_list.append(total_income)

            temp_lists.append(temp_list)
            temp_list = []
            no_of_basic = no_of_delux = total_income = day_count = 0

        start_date += timedelta(days=1)
        iteration +=1

    temp_list.append(week)
    temp_list.append(no_of_basic)
    temp_list.append(no_of_delux)
    temp_list.append(total_income)

    temp_lists.append(temp_list)
    csvweekly.writerows(temp_lists)


# Graphical representation of sale X-Axis : DATE/MONTH/YEAR Y-AXIS : NO OF BASIC/DELUX