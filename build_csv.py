import csv


with open('example2.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')

    dates = []
    colors = []    
    for row in readCSV:
        print(row)
        color = row[2]
        date = row[0]
        dates.append(date)
        colors.append(color)

    print(dates)
    print(colors)
    whatColor = input('What color do you wish to know the date of?')
    coldex = colors.index(whatColor)
    theDate = dates[coldex]

    print('The date of',whatColor,'is the date:',theDate)
