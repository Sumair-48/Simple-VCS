class CommitNode:
    def __init__(self, commit_id, message, timestamp, files):
        self.id = commit_id
        self.message = message
        self.timestamp = timestamp
        self.files = files
        self.next = None

class CommitLinkedList:
    def __init__(self):
        self.head = None

    def add_commit(self, commit_id, message, timestamp, files):
        new_node = CommitNode(commit_id, message, timestamp, files)
        new_node.next = self.head
        self.head = new_node

    def display_commits(self):
        current = self.head
        while current:
            print("=" * 40)
            print(f"Commit ID: {current.id}")
            print(f"Timestamp: {current.timestamp}")
            print(f"Message: {current.message}")
            print("Files:")
            for file, file_hash in current.files.items():
                print(f"  {file} -> {file_hash}")
            current = current.next
        print("=" * 40)
