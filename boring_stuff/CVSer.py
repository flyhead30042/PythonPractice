import csv

class CSVer:

    def __init__(self, a_filname, a_delimiter, a_quotechar=None):
        if  a_quotechar is not None:
                    csv.register_dialect('mycsv', delimiter=a_delimiter, quotechar=a_quotechar, quoting=csv.QUOTE_ALL)
        else:
            csv.register_dialect('mycsv', delimiter=a_delimiter, quotechar=a_quotechar)
        self.filename = a_filname

    def write_rows(self, a_list):
        with open(self.filename, 'w', newline='', encoding='utf-8') as f:
            csv_out = csv.writer(f, 'mycsv')
            for row in a_list:
                csv_out.writerow(row)

    def add_rows(self, a_list):
        with open(self.filename, 'a', newline='', encoding='utf-8') as f:
            csv_out = csv.writer(f, 'mycsv')
            for row in a_list:
                csv_out.writerow(row)

    def add_one_row(self, a_row):
        with open(self.filename, 'a', newline='', encoding='utf-8') as f:
            csv_out = csv.writer(f, 'mycsv')
            csv_out.writerow(a_row)
        return self

    def __add__ (self, a_row):
        return self.add_one_row(a_row)


    def read_rows(self):
        with open(self.filename, newline='', encoding='utf-8') as f:
            csv_in = csv.reader(f, 'mycsv')
            l = list(csv_in)

        return l


def main():
    csvio = CSVer('./example.csv', ',', '*')

    l = [[1,'中文','bb'], [2,'aa','bb'], [3,'aa','bb']]
    csvio.write_rows(l)

    csvio = csvio + [4,'aa','bb']

    rs = csvio.read_rows()
    for idx, r in  enumerate(rs):
        print('[%d] = %s' % (idx , r))

if __name__ == "__main__": main()

