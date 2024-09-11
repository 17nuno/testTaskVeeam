# testTaskVeeam
Program that synchronizes two folders: source and replica. The program maintain a full, identical copy of source folder at replica folder.

-----------------------------------||---------------------------------||----------------------------------------------||--------------------

python .\sync.py C:\Projects\testTaskVeeam\source C:\Projects\testTaskVeeam\replica 1000 C:\Projects\testTaskVeeam\sync.log
python ./sync.py C:/Projects/testTaskVeeam/source C:/Projects/testTaskVeeam/replica 1000 C:/Projects/testTaskVeeam/sync.log
python .\sync.py a nuno c d


#Class used to store all the user input
#1)folderPathSource
#2)folderPathReplica
#3)synchronizationInterval
#4)logFilePath


C:\Projects\testTaskVeeam
C:\Projects\testTaskVeeam
1000
C:\Projects\testTaskVeeam



-----------------------------------||---------------------------------||----------------------------------------------||--------------------

source; replica
1)Exists in both and there is no differences: do nothing (test1)
2)Exists and are differents: copy source to replica(test2)
3)exists only on source: copy source to replica
4) Exists only in replica: deletes from replica


-----------------------------------||---------------------------------||----------------------------------------------||--------------------

Problems:
When change a file, maybe is better tu update it 
We are delete the different file on replica folder and the we add the file again, but, we dont know why,
the file in one iteration deletes and when we run again writes, should do everything in the same iteration


