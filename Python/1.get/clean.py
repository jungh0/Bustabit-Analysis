import csv
import queue

filename = "data"

csvfileRead = open(filename + '.csv', 'r', encoding='utf-8')
csvReader = list(csv.reader(csvfileRead))
csvReader.reverse()

csvfileWrtie = open(filename + "_output.csv", "w", newline="")
csvWriter = csv.writer(csvfileWrtie)

for idx, line in enumerate(csvReader):
    if (idx >= 100):
        previous = 0
        for idx2 in range(idx - 5, idx):
            #print(line[3])
            previous += float(csvReader[idx2][1])
        line.append(previous)

        previous = 0
        for idx2 in range(idx - 3, idx):
            #print(line[3])
            previous += float(csvReader[idx2][1])
        line.append(previous)

        previous = 0
        for idx2 in range(idx - 100, idx):
            #print(line[3])
            previous += int(csvReader[idx2][3])
        line.append(previous)

        previous = 0
        for idx2 in range(idx - 50, idx):
            #print(line[3])
            previous += int(csvReader[idx2][3])
        line.append(previous)

        previous = 0
        for idx2 in range(idx - 30, idx):
            #print(line[3])
            previous += int(csvReader[idx2][3])
        line.append(previous)

        previous = 0
        for idx2 in range(idx - 20, idx):
            #print(line[3])
            previous += int(csvReader[idx2][3])
        line.append(previous)

        previous = 0
        for idx2 in range(idx - 10, idx):
            #print(line[3])
            previous += int(csvReader[idx2][3])
        line.append(previous)

        #print(line)
        csvWriter.writerow(line)

csvfileRead.close()
csvfileWrtie.close()
