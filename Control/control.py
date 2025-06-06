import os
import json
from datetime import datetime
import hashlib
from src_file import VCS_DIR, OBJECTS_DIR, INDEX_FILE, LOG_FILE, HEAD_FILE
from ..Model.ll_class import CommitLinkedList

commit_list = CommitLinkedList()

def init():
    if os.path.exists(VCS_DIR):
        print("Repository already initialized.")
        return
    os.makedirs(OBJECTS_DIR)
    with open(INDEX_FILE, 'w') as f:
        json.dump({}, f)
    with open(LOG_FILE, 'w') as f:
        json.dump([], f)
    with open(HEAD_FILE, 'w') as f:
        f.write('')
    print("Initialized empty Simple VCS repository.")

def hash_file(filepath):
    hasher = hashlib.sha1()
    with open(filepath, 'rb') as f:
        hasher.update(f.read())
    return hasher.hexdigest()

def add(files):
    if not os.path.exists(VCS_DIR):
        print("Repository not initialized.")
        return
    with open(INDEX_FILE, 'r') as f:
        index = json.load(f)
    for file in files:
        if not os.path.isfile(file):
            print(f"File not found: {file}")
            continue
        file_hash = hash_file(file)
        index[file] = file_hash
    with open(INDEX_FILE, 'w') as f:
        json.dump(index, f)
    print("Files added to staging area.")

def commit(message):
    if not os.path.exists(VCS_DIR):
        print("Repository not initialized.")
        return
    with open(INDEX_FILE, 'r') as f:
        index = json.load(f)
    if not index:
        print("No files staged for commit.")
        return

    commit_id = hashlib.sha1((message + datetime.now().isoformat()).encode()).hexdigest()
    timestamp = datetime.now().isoformat()

    for file, file_hash in index.items():
        if not os.path.isfile(file):
            print(f"Missing file: {file}")
            continue
        with open(file, 'rb') as f:
            content = f.read()
        with open(os.path.join(OBJECTS_DIR, file_hash), 'wb') as f:
            f.write(content)

    # Update commit log
    with open(LOG_FILE, 'r') as f:
        log = json.load(f)
    log.append({
        'id': commit_id,
        'timestamp': timestamp,
        'message': message,
        'files': index
    })
    with open(LOG_FILE, 'w') as f:
        json.dump(log, f, indent=2)

    # Update memory and HEAD
    commit_list.add_commit(commit_id, message, timestamp, index)
    with open(HEAD_FILE, 'w') as f:
        f.write(commit_id)
    with open(INDEX_FILE, 'w') as f:
        json.dump({}, f)
    print(f"Committed: {commit_id}")

def show_log():
    if not os.path.exists(LOG_FILE):
        print("No commits yet.")
        return
    with open(LOG_FILE, 'r') as f:
        log = json.load(f)
    for entry in reversed(log):
        commit_list.add_commit(entry['id'], entry['message'], entry['timestamp'], entry['files'])
    commit_list.display_commits()
