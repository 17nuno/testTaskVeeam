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
        replicaConcat=replica+'/'+i

        if(os.path.isfile(iConcat)):
            shutil.copy2(iConcat, replicaConcat)
            logging.info("File %s has been added to replica folder", iConcat)
        elif os.path.isdir(iConcat):
            if not os.path.exists(replicaConcat):
                shutil.copytree(iConcat, replicaConcat)
            else:
                updateReplica(iConcat, replicaConcat)

    for i in dcmp.diff_files:
        iConcat = os.path.join(source, i)
        replicaConcat = os.path.join(replica, i)
        # Copy different files from source to replica
        shutil.copy2(iConcat, replicaConcat)
        logging.info("File %s has been updated in replica", iConcat)


#Remove files and folders if only in Replica Folder or have the same name but differents
def removeReplicaFiles(dcmp):
    for i in dcmp.right_only + dcmp.diff_files:
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

main()