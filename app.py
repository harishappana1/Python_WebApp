# app.py
def greet(name):
    print(f"Hello, {name}! Welcome to our program.")

if __name__ == "__main__":
    names = ["Alice", "Bob", "Charlie"]
    for name in names:
        greet(name)
