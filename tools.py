import os
def clear_screen(numlines=100):
  if os.name == "posix":
    # Unix, Linux, macOS, BSD, etc.
    os.system('clear')
  elif os.name in ("nt", "dos", "ce"):
    # DOS/Windows
    os.system('CLS')
  else:
    # Fallback for other operating systems.
    print('\n' * numlines)