import os
import pandas


def remove(d):
    print("removing {}".format(d))
    os.removedirs(d)


def remove_empty_dir(p):
    data = [{"dirPath": x[0], "dirLen": len(x[1]), "fileLen": len(x[2])} for x in os.walk(p)]
    df = pandas.DataFrame(data)
    empty_folders = df.loc[(df["dirLen"] == 0) & (df["fileLen"] == 0)]["dirPath"]
    empty_folders.map(lambda x: remove(x))
    return empty_folders

if __name__ == "__main__":
    p = 'D:\\Users\\Flyhead\\Downloads\\aaaaa'
    df = remove_empty_dir(p)
    print(df.head())
