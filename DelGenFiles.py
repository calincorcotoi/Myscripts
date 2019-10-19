#! python3
import sys
import os
import shutil

def del_gen_file(path):
    for folderName, subfolders, filenames in os.walk(path):

        for subfolder in subfolders:

            if(subfolder=='GeneratedFiles'):
                #print('delete: ' + os.path.join(folderName,subfolder))
                shutil.rmtree(os.path.join(folderName,subfolder))

            if(subfolder=='Debug' or subfolder =='DebugStatic'):
                #print('delete: ' + os.path.join(folderName,subfolder))
                shutil.rmtree(os.path.join(folderName,subfolder))

            if(subfolder=='Release' or subfolder == 'ReleaseStatic'):
                #print('delete: ' + os.path.join(folderName,subfolder))
                for folderName1, subfolders1, filenames1 in os.walk(os.path.join(folderName,subfolder)):
                    for subfolder1 in subfolders1:
                        #print(os.path.join(folderName1,subfolder1))
                        shutil.rmtree(os.path.join(folderName1,subfolder1))
                    for filename1 in filenames1:
                     #shutil.rmtree(os.path.join(folderName,subfolder))
                        if(filename1!='Qwt_5_23.lib'):
                             #print('delete: ' + os.path.join(folderName1,filename1)+'---')
                             os.unlink(os.path.join(folderName1,filename1))

        del_empty_file(path)


def del_empty_file(path):
    AAA=1
    while(AAA):
        for folderName, subfolders, filenames in os.walk(path):
            for subfolder in subfolders:
                if len(os.listdir(os.path.join(folderName,subfolder)))==0:           
                    os.rmdir(os.path.join(folderName,subfolder))
                else:
                    AAA=0;
                

del_gen_file(sys.argv[1])