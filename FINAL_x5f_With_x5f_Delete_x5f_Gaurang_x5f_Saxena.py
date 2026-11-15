# SMART STUDENT RECORD MANAGEMENT SYSTEM
# With File Handling & AI Smart Search
# Name: Gaurang Saxena
# Roll No: 2501090100023
# College: Aligarh College of Engineering and Technology, Aligarh
# Affiliated to Dr. A.P.J. Abdul Kalam Technical University, Lucknow
# Department: Computer Science & Engineering, 2nd Year
# Guided By: Akash Kumar Jain
# Session: 2026-27
# Secret Watermark: GS_ACET_2025_CSE2_GAURANG_ORIGINAL

import os
from difflib import get_close_matches

FILE_NAME = "Gaurang_ACET_Students_2025.txt"

def add_student():
    print("\n--- ADD STUDENT ---")
    name = input("Enter Name: ")
    roll = input("Enter Roll No: ")
    course = input("Enter Course (B.Tech CSE): ")
    year = input("Enter Year (2nd Year): ")
    # File Handling - 'a' = Append Mode - Data Permanent Save Hoga
    with open(FILE_NAME, "a") as file:
        file.write(f"{name},{roll},{course},{year}\n")
    print("SUCCESS: Student Added Successfully!")

def view_all():
    print("\n--- ALL STUDENTS ---")
    if not os.path.exists(FILE_NAME):
        print("No Record Found! Pehle Student Add Karo.")
        return
    with open(FILE_NAME, "r") as file:
        data = file.readlines()
    if len(data) == 0:
        print("No Record Found!")
    else:
        for line in data:
            print(line.strip())
    print(f"Total Students: {len(data)}")

def normal_search():
    print("\n--- NORMAL SEARCH (By Roll No) ---")
    roll = input("Enter Roll No to Search: ")
    found = False
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                if roll in line:
                    print("Found:", line.strip())
                    found = True
    if not found:
        print("Not Found!")

def ai_smart_search():
    print("\n--- AI SMART SEARCH ---")
    print("Galat spelling likhoge tab bhi sahi naam mil jayega!")
    search_name = input("Enter Name to Search (ex: Gorang): ")
    if not os.path.exists(FILE_NAME):
        print("No Record Found!")
        return
    all_names = []
    all_lines = []
    with open(FILE_NAME, "r") as file:
        for line in file:
            all_lines.append(line.strip())
            # Pehla part = Name
            all_names.append(line.split(",")[0].strip())
    # AI - Fuzzy Search using difflib
    matches = get_close_matches(search_name, all_names, n=3, cutoff=0.5)
    if matches:
        print("AI Suggest Karta Hai - Kya Aapka Matlab Ye Hai?")
        for m in matches:
            for line in all_lines:
                if m in line:
                    print("->", line)
    else:
        print("Koi Milta-Julta Naam Nahi Mila!")

def delete_student():
    print("\n--- DELETE STUDENT ---")
    print("Agar koi student mid-sem me college chhod de to yahan se delete karo.")
    roll = input("Enter Roll No to Delete: ")
    if not os.path.exists(FILE_NAME):
        print("No Record Found!")
        return
    with open(FILE_NAME, "r") as file:
        lines = file.readlines()
    found = False
    # 'w' mode se file dobara likhenge, delete wali line chhod ke
    with open(FILE_NAME, "w") as file:
        for line in lines:
            if roll not in line:
                file.write(line)
            else:
                found = True
    if found:
        print("DELETED: Student Deleted Successfully!")
    else:
        print("Roll No Not Found!")

def show_stats():
    print("\n--- STATS ---")
    if not os.path.exists(FILE_NAME):
        print("Total Students: 0")
        return
    with open(FILE_NAME, "r") as file:
        data = file.readlines()
    print(f"Total Students: {len(data)}")
    print(f"Data File: {FILE_NAME}")
    print("College: ACET Aligarh")

# Main Menu
while True:
    print("\n===== SMART STUDENT RECORD MANAGEMENT SYSTEM =====")
    print("1. Add Student (Mid-Sem Joining)")
    print("2. View All Students")
    print("3. Normal Search (By Roll No)")
    print("4. AI Smart Search (By Name - Galat Spelling Par Bhi)")
    print("5. Delete Student (Mid-Sem Leaving)")
    print("6. Stats")
    print("7. Exit")
    choice = input("Enter Your Choice (1-7): ")

    if choice == "1":
        add_student()
    elif choice == "2":
        view_all()
    elif choice == "3":
        normal_search()
    elif choice == "4":
        ai_smart_search()
    elif choice == "5":
        delete_student()
    elif choice == "6":
        show_stats()
    elif choice == "7":
        print("Thank You! - Gaurang Saxena, ACET Aligarh")
        break
    else:
        print("Galat Choice! 1 se 7 ke beech me dabao.")
