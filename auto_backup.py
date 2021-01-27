from stat import ST_CTIME, ST_MTIME, ST_SIZE
import os, shutil
from datetime import datetime

# path to the directory (relative or absolute)
path_backupsFrom = '/home/company/backupsFrom'

# get all entries in the directory w/ stats

files_backupsFrom = (os.path.join(path_backupsFrom, file) for file in os.listdir(path_backupsFrom))

files_backupsFrom = ((os.stat(path), path) for path in files_backupsFrom)

# insert creation date, size and last modified
files_backupsFrom = ((stat[ST_CTIME], stat[ST_SIZE], stat[ST_MTIME], path)
           for stat, path in files_backupsFrom)

for cdate, size, last_mod, path in sorted(files_backupsFrom):

    file_info = os.path.basename(path), str(os.path.getsize(path), ), datetime.fromtimestamp(
        cdate), datetime.fromtimestamp(last_mod)
    file_name, file_size, file_creation, file_modified = file_info

    log = open('/home/company/backupsFrom.log', 'a', encoding='utf8')
    log.write('{0} - {1}Bytes - criado em:{2} - última modificação:{3} \n'.format(file_name, file_size, file_creation,
                                                                                  file_modified))
    log.close()

# remove files created over three days

files = (os.path.join(path_backupsFrom, file) for file in os.listdir(path_backupsFrom))
files = ((os.stat(path), path) for path in files)

now = datetime.now()
day_today = now.day

for stat, path in files:
    file_created = datetime.fromtimestamp(stat[ST_CTIME])
    days = file_created.day

    if day_today - days > 3:
        os.remove(path)
    else:
        copy_backupsTo = shutil.copy(path, '/home/company/backupsTo')

# log BackupsTo
path_backupsTo = '/home/company/backupsTo'

files_backupTo = (os.path.join(path_backupsTo, file) for file in os.listdir(path_backupsTo))
files_backupTo = ((os.stat(path), path) for path in files_backupTo)

files_backupTo = ((stat[ST_CTIME], stat[ST_SIZE], stat[ST_MTIME], path)
                  for stat, path in files_backupTo)


for cdate, size, last_mod, path in sorted(files_backupTo):
    file_info = os.path.basename(path), str(os.path.getsize(path), ), datetime.fromtimestamp(
        cdate), datetime.fromtimestamp(last_mod)
    file_name, file_size, file_creation, file_modified = file_info

    log = open('/home/company/backupsTo.log', 'a', encoding='utf8')
    log.write('{0} - {1}Bytes - criado em:{2} - última modificação:{3} \n'.format(file_name, file_size, file_creation,
                                                                                  file_modified))
    log.close()
