#!/usr/bin/env python3

import pyperclip

print("Use ⌘ V to or Ctrl-V (windows) to enter/paste. Ctrl-D to save it. Ctrl-C to exit")

while True:
  contents = []
  while True:
      try:
          line = input()
      except EOFError:
          break
      contents.append(line)

  joined = " ".join(contents)
  stripped = joined.strip()

  pyperclip.copy(stripped)

  print("")
  print("Now formatted properly and already copied to your clipboard:")
  print("")
  print(stripped)
  print("")
