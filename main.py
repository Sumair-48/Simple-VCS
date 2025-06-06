import sys
from Control.control import init,add,commit,show_log


def main():
    if len(sys.argv) < 2:
        print("Usage: python main.py [init|add|commit|log] <args>")
        return
    command = sys.argv[1]
    if command == "init":
        init()
    elif command == "add":
        add(sys.argv[2:])
    elif command == "commit":
        if len(sys.argv) < 3:
            print("Commit message required.")
            return
        message = ' '.join(sys.argv[2:])
        commit(message)
    elif command == "log":
        show_log()
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()