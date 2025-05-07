import tkinter as tk
import random  
import tkinter.font as tkFont

vocab = [
    {"word": "いぬ",  "meaning": "dog", "options": ["dog","cat","bird"]},
    {"word": "みず", "meaning": "water", "options": ["fire", "water", "tree"]},
    {"word": "ほん", "meaning": "book", "options": ["pen", "book", "desk"]},
    {"word": "せんせい", "meaning": "teacher", "options": ["student", "teacher", "parent"]},
    {"word": "あか", "meaning": "red", "options": ["blue", "green", "red"]},
]

# print(item["options"][0])  # → 'dog'


# Choose a random vocab item 
item = random.choice(vocab)

# Shuffling options
options = item["options"]  # saving the options list in the dictionary into a variable called options - options = ["dog", "cat", "bird"]
random.shuffle(options)  # shuffles the order of the options in list - options → ["bird", "dog", "cat"]

# GUI setup
root = tk.Tk()
root.title("Japanesse Vocab Quiz")
root.geometry("300x250")
root['background']= "#9ff553"

heading_label = tk.Label(root, text="Let's Practice!", fg="#F4C2C2", font=("Arial", 14, "bold",))  # come back to this later!

question_label = tk.Label(root, text=f"What does '{item['word']}' mean?", font=("Arial", 14))
question_label.pack(pady=20)

feedback_label = tk.Label(root, text="", font=("Arial", 12))
feedback_label.pack(pady=10)

#Checking answer
def check_answer(selected_option):
    if selected_option == item["meaning"]:
        feedback_label.config(text="✅ Yay correct!", fg="green")
    else:
        feedback_label.config(text=f"❌ Oops! It's '{item['meaning']}'", fg="red")

# Buttons for options
for option in item["options"]:
    button = tk.Button(root, text=option, width=20, command=lambda opt=option: check_answer(opt))
    button.pack(pady=5)

def button_click():
    print("Button Clicked!")

button = tk.Button(
    root,
    text="Next",
    command=button_click,
    font=("Arial", 12),
    fg="#F4C2C2",
    bg="#9ff553",
    padx=15,
    pady=8,
    relief=tk.RAISED,
)
button.pack()

root.mainloop()


# Displaying the questions

#print(f"\nWhat does '{item['word']}' mean?")   # Using f-string (formatted string literal) to insert the item variable into the string
#for i, option in enumerate(options):  
#   print(f"{i + 1}. {option}")  # so option can start from 1 not 0 

# enumerate() a function used working with lists. Loops overs lists and gets the index & value.

#before
#for option in options:
#    print(option)

#after
#for i, option in enumerate(options):
#   print(i, option)

#output
#0 dog
#1 cat
#2 bird

# User input
# answer = input("Choose the correct number (1-3): ")

# Check if answer is correct
# selected_option = options[int(answer) -1]
# if selected_option == item["meaning"]:
#     print("✅ Yay correct!")
# else:
#     print(f"❌ Oops! The correct answer was '{item['meaning']}'.")