import os

VCS_DIR = ".svcs"
OBJECTS_DIR = os.path.join(VCS_DIR, "objects")
INDEX_FILE = os.path.join(VCS_DIR, "index")
LOG_FILE = os.path.join(VCS_DIR, "log")
HEAD_FILE = os.path.join(VCS_DIR, "HEAD")