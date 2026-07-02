# 🏥 Hospital Management System (Python OOP)

A simple **Hospital Management System** developed using **Python Object-Oriented Programming (OOP)** concepts. This project demonstrates how classes and objects can be used to model a real-world hospital management system.

The application allows hospitals to manage doctors, patients, appointments, and billing efficiently while showcasing important OOP principles such as **Inheritance, Encapsulation, Composition, and Polymorphism**.

---

## 📌 Features

### 👨‍⚕️ Doctor Management
- Add new doctors
- Store doctor details
- View all registered doctors
- Doctor specialization management

### 🧑‍🤝‍🧑 Patient Management
- Add new patients
- Store patient details
- View patient information
- Maintain disease records

### 📅 Appointment Management
- Book appointments
- Assign doctors to patients
- Store appointment dates
- View all appointments

### 💳 Billing System
- Generate patient bills
- Consultation fee management
- Medicine fee management
- Automatic total bill calculation

---

## 🏗️ OOP Concepts Used

### ✅ Classes and Objects
- Person
- Doctor
- Patient
- Appointment
- Bill
- Hospital

### ✅ Inheritance
- `Doctor` inherits from `Person`
- `Patient` inherits from `Person`

### ✅ Method Overriding
- `display()` method is overridden in both `Doctor` and `Patient` classes.

### ✅ Encapsulation
- Each class stores its own attributes and methods.

### ✅ Composition
- A `Hospital` contains multiple doctors, patients, and appointments.
- An `Appointment` is composed of both a doctor and a patient.
- A `Bill` is generated for a patient.

---

# 📂 Project Structure

```
Hospital Management System
│
├── Person
├── Doctor
├── Patient
├── Appointment
├── Bill
├── Hospital
└── main.py
```

---

# 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/Hospital-Management-System.git
```

### 2. Navigate to the project folder

```bash
cd Hospital-Management-System
```

### 3. Run the program

```bash
python main.py
```

---

# 📋 Sample Output

```
Doctor Ramesh added successfully.
Doctor Priya added successfully.

Patient Rahul added successfully.
Patient Anjali added successfully.

Appointment booked successfully.

========== DOCTORS ==========

Doctor ID      : 101
Name           : Ramesh
Age            : 45
Gender         : Male
Specialization : Cardiologist

...

Total Bill : ₹850
```

---

# 💻 Technologies Used

- Python 3
- Object-Oriented Programming (OOP)

---

# 🎯 Learning Objectives

This project was developed to practice and understand:

- Object-Oriented Programming
- Class Design
- Inheritance
- Method Overriding
- Composition
- Encapsulation
- Object Interaction
- Real-world System Design

---

# 🔮 Future Enhancements

- User Login System
- File Handling for Data Storage
- Database Integration (MySQL/SQLite)
- Doctor Availability Management
- Appointment Cancellation
- Search Patient by ID
- Search Doctor by Specialization
- Billing History
- GUI using Tkinter or PyQt
- Web Version using Django or Flask

---

# 👩‍💻 Author

**Supraja Challa**

B.Tech – Computer Science and Engineering

Python | Object-Oriented Programming | Full Stack Development

---

## ⭐ If you found this project useful, consider giving it a Star on GitHub!
