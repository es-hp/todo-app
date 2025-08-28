# === UI Formating Tools ===

def divider(lines=1, char="-", length=40):
  print("\n" + (char * length + "\n") * lines)
  
def line_breaks(num=1):
  print("\n" * num, end="")
  
def h1(heading):
  print(f"=== {heading} ===\n")
  
def h2(heading):
  print(f"--- {heading} ---\n")
  
def h3(heading):
  print(f"--{heading}--")
  
def h4(heading):
  print(f"\n[{heading}]")
  
def invalid_msg(message="Invalid input. Please try again."):
  print(f"\n❌ {message}\n")
  
def success_msg(message="Success!"):
  print(f"\n✅ {message}\n")