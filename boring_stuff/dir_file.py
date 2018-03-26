import os

full_path= os.path.realpath(__file__)
print ('fullpath=' + full_path)
print('curdir=' + os.getcwd())

fname_list= os.listdir('.')
for fname in fname_list:
    print ("fname=" + fname)