import filecmp
import shutil
import sys
import logging
import os
import time

def main():
    #print(getArgs()[1])
    UsIn=UserInput()
    #print(UsIn.folderPathSource, UsIn.folderPathReplica, UsIn.synchronizationInterval, UsIn.logFilePath)
    createLogFile(UsIn.logFilePath)
    createReplica(UsIn.folderPathSource, UsIn.folderPathReplica)
    print("UsIn.synchronizationInterval",type(UsIn.synchronizationInterval))
    while True:
        logging.info("Start synchronization")
        
        updateReplica(UsIn.folderPathSource, UsIn.folderPathReplica)
        time.sleep(int(UsIn.synchronizationInterval))
        #break




#Create Replica Folder if not exists
def createReplica(source, replica):
    print("createReplica")
    print(source, replica)
    if not (os.path.isdir(replica)):
        logging.info("Create Replica Folder")
        os.makedirs(replica)
        

#Create Log File
def createLogFile(LogFilename):
    logging.basicConfig(filename=LogFilename, level=logging.INFO)


#Update Replica Folder
def updateReplica(source, replica):
    #print("hello world test")
    #print(source, replica)

    dcmp=filecmp.dircmp(source, replica)
    removeReplicaFiles(dcmp)
    #print_diff_files(dcmp)

    
    print("depois entra aqui para atualizar a replica")
    for i in dcmp.left_only:
        iConcat=source+"/"+i
        print("uyuyuyuyuuya",i, iConcat)
        if(os.path.isfile(iConcat)):
            print(1)
            shutil.copy(iConcat, replica)
            logging.info("File %s has been added to replica folder", iConcat)
        else:
            print(iConcat, replica)
            shutil.copytree(iConcat, replica+"/"+i)
            logging.info("Folder %s has been added to replica", iConcat)
            




#We dont need that
#def print_diff_files(dcmp):
    #print("befor for")
#    for name in dcmp.diff_files:
#        print(dcmp.diff_files)
#        print("diff_file %s found in %s and %s" % (name, dcmp.left,
#              dcmp.right))
#    for sub_dcmp in dcmp.subdirs.values():
#        print_diff_files(sub_dcmp)



#Remove files and folders if only in Replica Folder OR have the same name but differents
def removeReplicaFiles(dcmp):
    for i in dcmp.right_only or dcmp.diff_files:
        print("tem fich duferetes fdd!!")
        iConc=dcmp.right+"/"+i
        if(os.path.isfile(iConc)):
            print ("é file", i)
            os.remove(iConc)
            logging.info("File %s has been removed", iConc)
        else:
            print ("nao é file", iConc)
            #ver esta função
            #os.rmdir(iConc)
            shutil.rmtree(iConc)
            logging.info("Folder %s has been removed", iConc)



#Class used to store all the user input
    #1)folderPathSource
    #2)folderPathReplica
    #3)synchronizationInterval
    #4)logFilePath
class UserInput:
    def __init__(self):
        self.folderPathSource = sys.argv[1]
        self.folderPathReplica = sys.argv[2]
        self.synchronizationInterval=sys.argv[3]
        self.logFilePath=sys.argv[4]

#def getArgs():
    #return folderPathSource, folderPathSource, synchronizationInterval, logFilePath


main()