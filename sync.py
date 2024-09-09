import sys
import logging

def main():
    teste()
    #print(getArgs()[1])
    p1T=UserInput()
    print(p1T.folderPathSource, p1T.folderPathReplica, p1T.synchronizationInterval, p1T.logFilePath)
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