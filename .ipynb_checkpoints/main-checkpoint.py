import sys
import subprocess


if __name__ == "__main__":
    # Run main.py using subprocess
    print("start processing file to duckdb")
    subprocess.run(['python', 'scripts/python/file_to_duckdb.py'])
    print("finished file to duckdb")
    
    print("start processing duckdb to postgre")
    subprocess.run(['python', 'scripts/python/duckdb_to_postgre.py'])
    print("finish duckdb to postgre")