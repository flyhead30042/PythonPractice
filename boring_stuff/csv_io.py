import csv

with open('example.csv', 'w', newline='') as f2:
    csv_out = csv.writer(f2, delimiter='-')

    csv_out.writerow(['a', '', 'aaa'])
    csv_out.writerow(['b', 'bb', 3])

with open('example.csv', 'r') as f1:
    csv_in = csv.reader(f1, delimiter='-')
    l = list(csv_in)

    for idx, item in enumerate(l):
        print('Row[%d]=' % (idx))
        for i in item:
            print (i)
