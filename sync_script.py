import os 
import hashlib
import time
import sys

folder = ''
backup = ''
log_file = ''
time_interval = 0

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print ("Please launch this script with 4 args. First arg is first folder path. Second arg is backup folder path. Third arg is log_file path. The last arg is sync time interval.")
    else:
        print("First folder path is" + " " + str(sys.argv[1]))
        print("Second folder path is" + " " + str(sys.argv[2]))
        print("Log file path is" + " " + str(sys.argv[3]))
        print("Time interval is" + " " + str(sys.argv[4]))
    
    folder = sys.argv[1]
    backup = sys.argv[2]
    log_file = sys.argv[3]
    time_interval = sys.argv[4]
    
    
def log(message):
    # write log
    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    with open(log_file, 'a') as f:
        f.write('['+now+']'+message+'\n')
   

def comparefiles(file1, file2):
    with open(file1, 'rb',) as f1:
        with open(file2, 'rb',) as f2:
            if hashlib.md5(f1.read()).hexdigest() == hashlib.md5(f2.read()).hexdigest():
                return True
            else:
                return False

def compareFolderHash(folder, backup):
    files = os.listdir(folder)
    files_backup = os.listdir(backup)
    if len(files) != len(files_backup):
        return False
    
    for file in files:
        if file in files_backup:
            if not comparefiles(folder+'/'+file, backup+'/'+file):
                return False
            else:
                return False
        else: 
            return True

while True:
    # check if folder is same with backup
    if compareFolderHash(folder, backup):
        now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        print(f'[{now}] file is up to date')
        log('file is up to date')
        time.sleep(int(time_interval))
        continue    

    # check folder
    if os.path.isdir(folder):
        print('folder: OK')
        log('folder: OK')
    else:
        print('folder is not exist')
        log('folder is not exist')
        print('please check your config file')
        break

    # check backup
    if os.path.isdir(backup):
        print('backup: OK')
        log('backup: OK')
    else:
        print('backup is not exist')
        log('backup is not exist')
        print('please check your config file')
        break

    # check file hash in folder and compare with backup
    countSync = 0
    updateFile = 0
    deleteFile = 0

    # get all file in folder
    files = os.listdir(folder)
    # get all file in backup
    files_backup = os.listdir(backup)
    # compare 2 list
    for file in files_backup:
        if file in files:
            if comparefiles(folder+'/'+file, backup+'/'+file):
                log(f'{file} is up to date')
                countSync += 1
            else:
                # copy file from folder to backup
                updateFile += 1
                os.remove(backup+'/'+file)
                os.system('cp '+folder+'/'+file+' '+backup)
                log(f'{file} is updated')
        if file not in files:
            # delete file in backup
            log(f'{file} is deleted')
            deleteFile += 1
            os.remove(backup+'/'+file)

    for file in files:
        if file not in files_backup:
            # copy file from folder to backup
            updateFile += 1
            log(f'{file} is copied')
            os.system('cp '+folder+'/'+file+' '+backup)



    now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
    print(f'[{now}] sync: {countSync}; update: {updateFile}; delete: {deleteFile};')

    time.sleep(int(time_interval))