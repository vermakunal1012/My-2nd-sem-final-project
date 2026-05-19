import tkinter as tk
from tkinter import messagebox
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# --------------------------
# Sample Training Data
# [followers, following, posts, bio_length, account_age]
# --------------------------
X = np.array([
    [5000, 300, 200, 50, 5],   # Real
    [50, 5000, 2, 5, 1],       # Fake
    [8000, 400, 500, 80, 6],   # Real
    [100, 7000, 1, 0, 1],      # Fake
    [6000, 500, 300, 70, 4],   # Real
    [70, 4000, 3, 2, 1]        # Fake
])

# Labels
# 0 = Real
# 1 = Fake

y = np.array([0, 1, 0, 1, 0, 1])

# --------------------------
# Train Model
# --------------------------

model = RandomForestClassifier()
model.fit(X, y)

# --------------------------
# Prediction Function
# --------------------------

def predict_account():

    try:
        followers = int(entry_followers.get())
        following = int(entry_following.get())
        posts = int(entry_posts.get())
        bio = int(entry_bio.get())
        age = int(entry_age.get())

        data = np.array([[followers, following, posts, bio, age]])

        prediction = model.predict(data)

        if prediction[0] == 1:
            result_label.config(
                text="Fake Account Detected",
                fg="red"
            )
        else:
            result_label.config(
                text="Real Account",
                fg="green"
            )

    except:
        messagebox.showerror(
            "Error",
            "Please enter valid numbers"
        )

# --------------------------
# GUI Window
# --------------------------

root = tk.Tk()
root.title("Fake Social Account Detector")
root.geometry("400x500")
root.configure(bg="white")

# Heading
heading = tk.Label(
    root,
    text="Real vs Fake Prediction",
    font=("Arial", 18, "bold"),
    bg="white"
)
heading.pack(pady=15)

# Followers
tk.Label(root, text="Followers", bg="white").pack()
entry_followers = tk.Entry(root, width=30)
entry_followers.pack(pady=5)

# Following
tk.Label(root, text="Following", bg="white").pack()
entry_following = tk.Entry(root, width=30)
entry_following.pack(pady=5)

# Posts
tk.Label(root, text="Posts", bg="white").pack()
entry_posts = tk.Entry(root, width=30)
entry_posts.pack(pady=5)

# Bio Length
tk.Label(root, text="Bio Length", bg="white").pack()
entry_bio = tk.Entry(root, width=30)
entry_bio.pack(pady=5)

# Account Age
tk.Label(root, text="Account Age", bg="white").pack()
entry_age = tk.Entry(root, width=30)
entry_age.pack(pady=5)

# Button
predict_btn = tk.Button(
    root,
    text="Predict",
    command=predict_account,
    bg="blue",
    fg="white",
    font=("Arial", 12, "bold")
)
predict_btn.pack(pady=20)

# Result
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 14, "bold"),
    bg="white"
)
result_label.pack(pady=20)

# Run App
root.mainloop()