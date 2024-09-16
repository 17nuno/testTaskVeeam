# testTaskVeeam
Program that synchronizes two folders: source and replica. The program maintain a full, identical copy of source folder at replica folder.

Run:
python ./sync.py URL/to/source URL/to/replica 1 URL/to/sync.log

-----------------------------------||---------------------------------||----------------------------------------------||--------------------
Run:
python ./sync.py URL/to/source URL/to/replica 1 URL/to/sync.log

Example
python ./sync.py C:/Projects/testTaskVeeam/source C:/Projects/testTaskVeeam/replica 1 C:/Projects/testTaskVeeam/sync.log

python .\sync.py C:\Projects\testTaskVeeam\source C:\Projects\testTaskVeeam\replica 1000 C:\Projects\testTaskVeeam\sync.log
python ./sync.py C:/Projects/testTaskVeeam/source C:/Projects/testTaskVeeam/replica 1000 C:/Projects/testTaskVeeam/sync.log



#Class used to store all the user input
#1)folderPathSource
#2)folderPathReplica
#3)synchronizationInterval
#4)logFilePath


C:\Projects\testTaskVeeam
C:\Projects\testTaskVeeam
10
C:\Projects\testTaskVeeam



-----------------------------------||---------------------------------||----------------------------------------------||--------------------

source; replica
1)Exists in both and there is no differences: do nothing (test1)
2)Exists and are differents: copy source to replica(test2)
3)exists only on source: copy source to replica
4) Exists only in replica: deletes from replica