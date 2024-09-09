import sys
import logging

def main():
    teste()
    print(getArgs()[1])
    createLogFile()
    createReplica()
    while True:
        logging.info("Start synchronization")    


def createReplica():
    print("createReplica")


def createLogFile():
    logging.basicConfig(filename='sync.log', level=logging.INFO)

def teste():
    print("hello world test")

def getArgs():
    folderPathSource=sys.argv[1]
    folderPathReplica=sys.argv[2]
    synchronizationInterval=sys.argv[3]
    logFilePath=sys.argv[4]
    #print("folderPathSource", folderPathSource)
    #print("folderPathReplica", folderPathReplica)
    #print("synchronizationInterval", synchronizationInterval)
    #print("logFilePath", logFilePath)
    return folderPathSource, folderPathSource, synchronizationInterval, logFilePath


main()