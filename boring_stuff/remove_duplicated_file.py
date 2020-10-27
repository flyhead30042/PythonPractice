import hashlib
import os
import pandas

def remove(f):
    print("removing {}".format(f))
    os.remove(f)

def get_md5(file):
    m = hashlib.md5()
    with open (file, "rb") as f:
        while chunk:= f.read(4096):
            m.update(chunk)
    return m.hexdigest()

def remove_duplicated_file(p):
    data = list()
    for dirPath, _, fileNames in os.walk(p):
        for fileName in fileNames:
            f=  os.path.join(dirPath, fileName)
            data.append( {"name":f,  "md5":get_md5(f) } )

    df = pandas.DataFrame(data)
    duplicated_files=df[df.duplicated("md5")]["name"]
    duplicated_files.map(lambda x: remove(x))
    return duplicated_files

if __name__ == "__main__":
    p = 'D:\\Users\\Flyhead\\Downloads\\aaaaa'
    # folders = [(x[0], x[1], x[2]) for x in os.walk(p)]
    df = remove_duplicated_file(p)
    print(df.head(10))

