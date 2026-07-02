class Person:

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def display(self):
        print(f"Name   : {self.name}")
        print(f"Age    : {self.age}")
        print(f"Gender : {self.gender}")


# -----------------------------------------

class Doctor(Person):

    def __init__(self, doctor_id, name, age, gender, specialization):
        super().__init__(name, age, gender)
        self.doctor_id = doctor_id
        self.specialization = specialization

    def display(self):
        print("\n----- Doctor Details -----")
        print(f"Doctor ID      : {self.doctor_id}")
        super().display()
        print(f"Specialization : {self.specialization}")


# -----------------------------------------

class Patient(Person):

    def __init__(self, patient_id, name, age, gender, disease):
        super().__init__(name, age, gender)
        self.patient_id = patient_id
        self.disease = disease

    def display(self):
        print("\n----- Patient Details -----")
        print(f"Patient ID : {self.patient_id}")
        super().display()
        print(f"Disease    : {self.disease}")


# -----------------------------------------

class Appointment:

    def __init__(self, patient, doctor, date):
        self.patient = patient
        self.doctor = doctor
        self.date = date

    def display(self):
        print("\n----- Appointment -----")
        print(f"Patient : {self.patient.name}")
        print(f"Doctor  : {self.doctor.name}")
        print(f"Date    : {self.date}")


# -----------------------------------------

class Bill:

    def __init__(self, patient, consultation_fee, medicine_fee):
        self.patient = patient
        self.consultation_fee = consultation_fee
        self.medicine_fee = medicine_fee

    def calculate_total(self):
        return self.consultation_fee + self.medicine_fee

    def display(self):
        print("\n----- Bill -----")
        print(f"Patient           : {self.patient.name}")
        print(f"Consultation Fee  : ₹{self.consultation_fee}")
        print(f"Medicine Fee      : ₹{self.medicine_fee}")
        print(f"Total Bill        : ₹{self.calculate_total()}")


# -----------------------------------------

class Hospital:

    def __init__(self, name):
        self.name = name
        self.doctors = []
        self.patients = []
        self.appointments = []

    def add_doctor(self, doctor):
        self.doctors.append(doctor)
        print(f"\nDoctor {doctor.name} added successfully.")

    def add_patient(self, patient):
        self.patients.append(patient)
        print(f"\nPatient {patient.name} added successfully.")

    def book_appointment(self, appointment):
        self.appointments.append(appointment)
        print("\nAppointment booked successfully.")

    def show_doctors(self):

        print("\n========== DOCTORS ==========")

        for doctor in self.doctors:
            doctor.display()

    def show_patients(self):

        print("\n========== PATIENTS ==========")

        for patient in self.patients:
            patient.display()

    def show_appointments(self):

        print("\n======= APPOINTMENTS =======")

        for appointment in self.appointments:
            appointment.display()


# -----------------------------------------
# Main Program
# -----------------------------------------

hospital = Hospital("City Hospital")

doctor1 = Doctor(
    101,
    "Ramesh",
    45,
    "Male",
    "Cardiologist"
)

doctor2 = Doctor(
    102,
    "Priya",
    39,
    "Female",
    "Neurologist"
)

patient1 = Patient(
    201,
    "Rahul",
    24,
    "Male",
    "Fever"
)

patient2 = Patient(
    202,
    "Anjali",
    30,
    "Female",
    "Migraine"
)

hospital.add_doctor(doctor1)
hospital.add_doctor(doctor2)

hospital.add_patient(patient1)
hospital.add_patient(patient2)

appointment1 = Appointment(
    patient1,
    doctor1,
    "25-07-2026"
)

appointment2 = Appointment(
    patient2,
    doctor2,
    "26-07-2026"
)

hospital.book_appointment(appointment1)
hospital.book_appointment(appointment2)

hospital.show_doctors()

hospital.show_patients()

hospital.show_appointments()

bill = Bill(
    patient1,
    500,
    350
)

bill.display()