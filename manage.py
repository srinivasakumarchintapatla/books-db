#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import sqlite3
import subprocess
import time

def fix_malformed_sqlite_db(db_path):
    try:
        print(f"Attempting to repair database: {db_path}")
        
        # Try to salvage data with iterdump, skipping integrity check
        dump_file = db_path + '.dump.sql'
        try:
            conn = sqlite3.connect(db_path)
            with open(dump_file, 'w', encoding='utf-8') as f:
                for line in conn.iterdump():
                    f.write(f'{line}\n')
            conn.close()
            print(f"Successfully dumped database content to {dump_file}")
            
            # Create new database and import dump
            new_db_path = db_path + '.fixed'
            if os.path.exists(new_db_path):
                os.remove(new_db_path)
                
            new_conn = sqlite3.connect(new_db_path)
            with open(dump_file, 'r', encoding='utf-8') as f:
                sql_script = f.read()
            new_conn.executescript(sql_script)
            new_conn.close()
            
            print(f'Successfully created repaired database at {new_db_path}')
            
            # Replace the original database with the fixed one
            backup_path = db_path + '.corrupted_backup'
            os.rename(db_path, backup_path)
            os.rename(new_db_path, db_path)
            os.remove(dump_file)  # Clean up the dump file
            
            print(f'Database repaired successfully. Corrupted database backed up to {backup_path}')
            return True
            
        except Exception as dump_error:
            print(f'Failed to dump database content: {dump_error}')
            # If dumping fails, the database is too corrupted, remove it
            print('Database is severely corrupted and cannot be repaired.')
            corrupted_path = db_path + '.corrupted_' + str(int(time.time()))
            os.rename(db_path, corrupted_path)
            print(f'Corrupted database moved to: {corrupted_path}')
            print('A new database will be created when you run migrations.')
            return False
            
    except Exception as e:
        print(f'Error during database repair: {e}')
        return False


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Book_store.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Database repair function disabled - database was too corrupted
    # If you need to re-enable repair functionality, uncomment the following:
    # db_path = 'db.sqlite3'
    # if os.path.exists(db_path):
    #     repair_success = fix_malformed_sqlite_db(db_path)

    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
