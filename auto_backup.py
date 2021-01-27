from stat import ST_CTIME, ST_MTIME, ST_SIZE
import os, shutil, time
from datetime import datetime

# query on path_backupsFrom
path_backupsFrom = '/home/company/backupsFrom'

files_backupsFrom = (os.path.join(path_backupsFrom, file) for file in os.listdir(path_backupsFrom))

files_backupsFrom = ((os.stat(path), path) for path in files_backupsFrom)

files_backupsFrom = ((stat[ST_CTIME], stat[ST_SIZE], stat[ST_MTIME], path)
                     for stat, path in files_backupsFrom)

# writing log file
log = open('/home/company/backupsFrom.log', 'w', encoding='utf8')

for cdate, size, last_mod, path in sorted(files_backupsFrom):
    file_info = os.path.basename(path), str(os.path.getsize(path), ), datetime.fromtimestamp(
        cdate), datetime.fromtimestamp(last_mod)
    file_name, file_size, file_creation, file_modified = file_info

    log = open('/home/company/backupsFrom.log', 'a', encoding='utf8')
    log.write('{0} - {1}Bytes - created in:{2} - last modified:{3} \n'.format(file_name, file_size, file_creation,
                                                                              file_modified))
    log.close()

# new query on path_backupsFrom
files_backupsFrom = (os.path.join(path_backupsFrom, file) for file in os.listdir(path_backupsFrom))
files_backupsFrom = ((os.stat(path), path) for path in files_backupsFrom)

today_in_seconds = time.time()
three_days_in_seconds = 3 * 86400

for stat, path in files_backupsFrom:

    file_created = stat[ST_CTIME]
    interval_now_creation = today_in_seconds - file_created
    if interval_now_creation > three_days_in_seconds:
        os.remove(path)
    else:
        copy_backupsTo = shutil.copy(path, '/home/company/backupsTo')

# query on path_backupsTo
path_backupsTo = '/home/company/backupsTo'

files_backupTo = (os.path.join(path_backupsTo, file) for file in os.listdir(path_backupsTo))
files_backupTo = ((os.stat(path), path) for path in files_backupTo)

files_backupTo = ((stat[ST_CTIME], stat[ST_SIZE], stat[ST_MTIME], path)
                  for stat, path in files_backupTo)

# writing log file
log = open('/home/company/backupsTo.log', 'w', encoding='utf8')

for cdate, size, last_mod, path in sorted(files_backupTo):
    file_info = os.path.basename(path), str(os.path.getsize(path), ), datetime.fromtimestamp(
        cdate), datetime.fromtimestamp(last_mod)
    file_name, file_size, file_creation, file_modified = file_info

    log = open('/home/company/backupsTo.log', 'a', encoding='utf8')
    log.write(
        '{0} - {1}Bytes - criado em:{2} - última modificação:{3} \n'.format(file_name, file_size, file_creation,
                                                                            file_modified))
    log.close()
