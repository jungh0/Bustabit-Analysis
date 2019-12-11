import csv
import queue

filename = "data"

csvfileRead = open(filename + '.csv', 'r', encoding='utf-8')
csvReader = list(csv.reader(csvfileRead))
csvReader.reverse()

csvfileWrtie = open(filename + "_output.csv", "w", newline="")
csvWriter = csv.writer(csvfileWrtie)

line = list()
line.append('배수')
line.append('총배팅')
#line.append('총이득')

line.append('1게임배수')
line.append('2게임배수')
line.append('3게임배수')
line.append('4게임배수')
line.append('5게임배수')
line.append('6게임배수')
line.append('7게임배수')
line.append('8게임배수')
line.append('9게임배수')
line.append('10게임배수')


line.append('100게임이득')
line.append('50게임이득')
line.append('10게임이득')
line.append('5게임이득')
line.append('3게임이득')

csvWriter.writerow(line)

for idx, line2 in enumerate(csvReader):
    if (idx >= 100):
        if(float(csvReader[idx][1]) > 100):
            continue
        if(float(csvReader[idx][2]) > 100000):
            continue

        line = list()

        line.append(csvReader[idx][1])
        line.append(csvReader[idx][2])
        #line.append(csvReader[idx][3])

        flag = False
        for idx2 in range(idx - 10, idx):
            if(float(csvReader[idx2][1]) > 100):
                flag = True
                break
        if flag:
             continue

        previous = 0
        for idx2 in range(idx - 1, idx):
            #print(line[3])
            previous += float(csvReader[idx2][1])
        line.append(previous)
        
        previous = 0
        for idx2 in range(idx - 2, idx):
            #print(line[3])
            previous += float(csvReader[idx2][1])
        line.append(previous)

        previous = 0
        for idx2 in range(idx - 3, idx):
            #print(line[3])
            previous += float(csvReader[idx2][1])
        line.append(previous)

        previous = 0
        for idx2 in range(idx - 4, idx):
            #print(line[3])
            previous += float(csvReader[idx2][1])
        line.append(previous)

        previous = 0
        for idx2 in range(idx - 5, idx):
            #print(line[3])
            previous += float(csvReader[idx2][1])
        line.append(previous)

        previous = 0
        for idx2 in range(idx - 6, idx):
            #print(line[3])
            previous += float(csvReader[idx2][1])
        line.append(previous)

        previous = 0
        for idx2 in range(idx - 7, idx):
            #print(line[3])
            previous += float(csvReader[idx2][1])
        line.append(previous)

        previous = 0
        for idx2 in range(idx - 8, idx):
            #print(line[3])
            previous += float(csvReader[idx2][1])
        line.append(previous)

        previous = 0
        for idx2 in range(idx - 9, idx):
            #print(line[3])
            previous += float(csvReader[idx2][1])
        line.append(previous)

        previous = 0
        for idx2 in range(idx - 10, idx):
            #print(line[3])
            previous += float(csvReader[idx2][1])
        line.append(previous)



        previous = 0
        for idx2 in range(idx - 100, idx):
            #print(line[3])
            previous += int(csvReader[idx2][3])
        line.append(previous)
        if(previous > 1000000 or previous < -1000000):
            continue

        previous = 0
        for idx2 in range(idx - 50, idx):
            #print(line[3])
            previous += int(csvReader[idx2][3])
        line.append(previous)
        if(previous > 1000000 or previous < -1000000):
            continue

        previous = 0
        for idx2 in range(idx - 10, idx):
            #print(line[3])
            previous += int(csvReader[idx2][3])
        line.append(previous)

        previous = 0
        for idx2 in range(idx - 5, idx):
            #print(line[3])
            previous += int(csvReader[idx2][3])
        line.append(previous)

        previous = 0
        for idx2 in range(idx - 3, idx):
            #print(line[3])
            previous += int(csvReader[idx2][3])
        line.append(previous)

        #print(line)
        csvWriter.writerow(line)

csvfileRead.close()
csvfileWrtie.close()
