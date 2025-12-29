# 💰 Tkinter Expense & Income Tracker

A simple **Python desktop application** for tracking your expenses and income.  
Built with **Tkinter (GUI)** and stores data locally in a `records.txt` file.

---

## ✨ Features

✔ Graphical user interface  
✔ Hierarchical category system  
✔ Record filtering  
✔ File-based persistence  
✔ Input validation  
✔ Object-oriented design  
✔ Generator-based utilities  
✔ Pie-chart visualization (Income vs Expense)  
✔ Delete records  
✔ Current balance display  
✔ Summary of total income & expense  

---

## 📂 Data Storage

Your data is saved in:

records.txt

markdown
Copy code

### **File format**

<initial_money>
<category> <description> <amount>
<category> <description> <amount>
...

markdown
Copy code

### **Example**

1000
meal breakfast -50
salary part-time 1200
bus 902 -20

yaml
Copy code

If `records.txt` is missing, the app will ask for your **starting balance**.

---

## 🧭 Categories

Categories are structured **hierarchically**, for example:

expense
food
meal
snack
drink
transportation
bus
railway
income
salary
bonus

csharp
Copy code

Filtering by `food` will also match:

meal
snack
drink

yaml
Copy code

---

## ▶️ How to Run

### 1️⃣ Install Python 3
Python **3.8+ recommended**

### 2️⃣ Install dependencies

```bash
pip install matplotlib
ℹ️ Tkinter is included with most Python installations

3️⃣ Run the program
bash
Copy code
python main.py
(or replace with your script filename)

📊 Tools & Utilities Inside the App
Summary popup

Total income

Total expense

Current balance

Pie-chart visualization

Big-expense filtering (via generators)

Delete selected records

Save to file anytime

🛠 Technology Used
Python

Tkinter — GUI

Matplotlib — charts

Object-Oriented Programming

💾 Saving
Click Save anytime — or choose to save when exiting.
Your data will be stored in records.txt.

