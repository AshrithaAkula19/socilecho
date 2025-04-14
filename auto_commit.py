import os
import datetime
import time

# File to update
FILENAME = "commit_log.txt"

# Number of commits you want to do
NUM_COMMITS = 500

for i in range(NUM_COMMITS):
    with open(FILENAME, "a") as f:
        f.write(f"Commit number {i + 1} at {datetime.datetime.now()}\n")
    
    os.system("git add .")
    os.system(f'git commit -m "Auto commit {i + 1}"')
    time.sleep(1)  # optional delay

# Push to GitHub
os.system("git push origin main")
