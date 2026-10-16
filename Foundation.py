document = """
Line 1: My name is Anuj.
Line 2: I use Sublime Text 4.
Line 3: My operating system is Windows 11.
Line 4: My favorite coding language is Python.
"""

ser = input("Ask the question? ")

for line in document.split("\n"):
    # Convert both target elements to lowercase to bypass capitalization blocks!
    if ser.lower() in line.lower():
        if ":" in line:
            clean_answer = line.split(":", 1)[1].strip()
            print("[FOUND ANSWER]:", clean_answer)
