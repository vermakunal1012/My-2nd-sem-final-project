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
# SIMPLE RULE-BASED DETECTION
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
# RESULT
# =========================================

print("\n========== RESULT ==========\n")

if fake_score >= 3:
    print("Fake Account Detected")
else:
    print("Real Account")

print(f"\nFake Score: {fake_score}/5")
