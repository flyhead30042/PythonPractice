import os
from  boring_stuff.zhtools.langconv import Converter



def t2s_convert(path):
    flist = os.listdir(os.path.abspath(path))

    for f in flist:
        f= os.path.join(path, f)
        if os.path.isdir(f):
            print("==============")
            print("dir {:s}".format(path))
            os.mkdir(f.replace("T2S_Source", "T2S_Conv"))
            t2s_convert(f)
        if os.path.isfile(f):
            st = os.stat(f)
            print("{0:s}, size {1:d}".format(f, st.st_size))
            with open(f, "r", encoding = 'utf8' ) as file_src:
                with open(f.replace("T2S_Source", "T2S_Conv"), "w+", encoding = 'utf8') as file_conv:

                    lines_src = file_src.readlines()
                    print("Converting", end=" ", flush=True)
                    for line_src in lines_src:
                        line_conv = Converter('zh-hant').convert(line_src)
                        file_conv.write(line_conv)
                        print(".", end=" ", flush=True)
                    print("Done")


if __name__ == "__main__":
    t2s_convert("D:\workspace\citest\PythonPractice\data\T2S_Source")




