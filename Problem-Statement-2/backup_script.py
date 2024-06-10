import os
import shutil
from datetime import datetime

def backup_directory(source_dir, backup_dir):
    try:
        if not os.path.exists(backup_dir):
            os.makedirs(backup_dir)
        
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        backup_subdir = os.path.join(backup_dir, f"backup_{timestamp}")
        shutil.copytree(source_dir, backup_subdir)
        print(f"Backup successful: {backup_subdir}")
        return True
    except Exception as e:
        print(f"Backup failed: {e}")
        return False

if __name__ == "__main__":
    source_directory = '/path/to/source_directory'  # Update this path to your source directory
    backup_directory_path = '/path/to/backup_directory'  # Update this path to your backup directory
    backup_directory(source_directory, backup_directory_path)
