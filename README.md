
📌 Fake Account Detector (Rule-Based Python Project)
🧠 Project Description

This project is a simple Fake Account Detection system built using Python and Pandas. It analyzes social media account behavior using basic features such as followers, following, posts, profile picture presence, and verification status.

The system first loads a CSV file containing dataset feature information and then allows the user to manually input account details. Based on a rule-based scoring system, it predicts whether an account is Fake or Real.

⚙️ How It Works
Loads dataset using Pandas
Displays dataset preview and column structure
Prints feature details from CSV file
Takes real-time user input:
Number of followers
Number of following accounts
Number of posts
Profile picture availability
Verification status
Calculates a fake score using simple rules
Gives final prediction: Fake or Real account
📌 Code
# =========================================
# FAKE ACCOUNT DETECTOR USING YOUR CSV FILE
# =========================================

import pandas as pd

# Load your CSV file
data = pd.read_csv("fake_account__data_dict(1).csv")

# =========================================
# SHOW DATASET
# =========================================

print("\nDataset Preview:\n")
print(data.head())

print("\nColumn Names:\n")
print(data.columns)

# =========================================
# DISPLAY FEATURES PROPERLY
# =========================================

print("\n========== FEATURE DETAILS ==========\n")

for index, row in data.iterrows():

    print(f"Feature Number : {row['No.']}")
    print(f"Feature Name   : {row['Column name']}")
    print(f"Data Type      : {row['Data Type']}")
    print(f"Description    : {row['Description']}")
    print("-" * 60)

# =========================================
# SIMPLE FAKE ACCOUNT CHECKER
# =========================================

print("\n========== FAKE ACCOUNT CHECKER ==========\n")

followers = int(input("Enter Followers: "))
following = int(input("Enter Following: "))
posts = int(input("Enter Number of Posts: "))
profile_pic = int(input("Profile Picture? (1=yes,0=no): "))
verified = int(input("Verified Account? (1=yes,0=no): "))

# =========================================
# RULE-BASED DETECTION LOGIC
# =========================================

fake_score = 0

if followers < 20:
    fake_score += 1

if following > 1000:
    fake_score += 1

if posts < 3:
    fake_score += 1

if profile_pic == 0:
    fake_score += 1

if verified == 0:
    fake_score += 1

# =========================================
# FINAL RESULT
# =========================================

print("\n========== RESULT ==========\n")

if fake_score >= 3:
    print("Prediction: FAKE ACCOUNT DETECTED ❌")
else:
    print("Prediction: REAL ACCOUNT ✅")

print(f"\nFake Score: {fake_score}/5")
🚀 Technologies Used
Python
Pandas
Rule-Based Logic
📊 Output
Displays dataset features
Takes user input
Calculates fake score
Predicts Fake or Real account
