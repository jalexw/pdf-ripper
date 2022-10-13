import sys
from gui.eventloop import run

if __name__ == "__main__":
  if len(sys.argv) > 1 and sys.argv[1] == "--dev":
    run(dev=True)
  else:
    # Run the program not in dev mode
    run()
else:
  raise Exception("Please run this file as a script; PDF-Ripper.py is not meant to be imported.")
