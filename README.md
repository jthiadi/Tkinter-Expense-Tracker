# 💰 Tkinter Expense & Income Tracker

A simple **Python desktop application** for tracking your expenses and income.  
Built with **Tkinter (GUI)** and stores data locally in a `records.txt` file.

---

## ✨ Features

- ✔ Graphical user interface  
- ✔ Hierarchical category system  
- ✔ Record filtering by category / sub-category  
- ✔ File-based data storage  
- ✔ Input validation  
- ✔ Object-oriented design  
- ✔ Generator-based utilities  
- ✔ Pie-chart visualization (Income vs Expense)  
- ✔ Delete records  
- ✔ Current balance display  
- ✔ Income & Expense summary popup  

---

## 📂 Data Storage

Your data is saved in:

```
records.txt
```

### File Format

```
<initial_money>
<category> <description> <amount>
<category> <description> <amount>
...
```

### Example

```
1000
meal breakfast -50
salary part-time 1200
bus 902 -20
```

👉 If `records.txt` is missing, the app will ask for your **starting balance**.

---

## 🧭 Categories

Categories are structured **hierarchically**, for example:

```
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
```

Filtering by `food` will also match:

```
meal
snack
drink
```

---

## ▶️ How to Run

### 1️⃣ Install Python 3
Python **3.8+ recommended**

---

### 2️⃣ Install dependencies

```bash
pip install matplotlib
```

> ℹ️ Tkinter is included with most Python installations.

---

### 3️⃣ Run the program

```bash
python main.py
```

*(replace with your script filename if different)*

---

## 📊 Tools Inside the App

- View **total income**
- View **total expense**
- View **current balance**
- Pie-chart visualization
- Filter large expenses (via generators)
- Delete selected records
- Save to file manually or on exit

---

## 🛠 Technology Used

- Python  
- Tkinter — GUI  
- Matplotlib — charts  
- Object-Oriented Programming  

---

## 💾 Saving

You can click **Save** anytime —  
or choose to save when exiting the application.  
All data is stored in `records.txt`.

---

🎉 Enjoy tracking your finances!
