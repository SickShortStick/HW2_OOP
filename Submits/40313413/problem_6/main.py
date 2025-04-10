import random


class Person:

    def __init__(self, person_details: dict):
        self.first_name = person_details['first_name']
        self.last_name = person_details['last_name']
        self.age = int(person_details['age'])
        self.gender = person_details['gender']

class Patient(Person):


    unique_id = 1

    def __init__(self, person_details, disease, assigned_doctor):
        super().__init__(person_details)
        self.disease = disease
        self.assigned_doctor = assigned_doctor
        self.id = f'P{Patient.unique_id: 03d}'
        Patient.unique_id += 1
    
    def get_patient_details(self):
        print(f'''Name: {self.first_name} {self.last_name}
ID: {self.id}
Age: {self.age}
Gender: {self.gender}
Disease: {self.disease}
Assigned Doctor: {self.assigned_doctor}''')

class Doctor(Person):


    unique_id = 1

    def __init__(self, person_details, specialization):
        super().__init__(person_details)
        self.specialization = specialization
        self.patients = []
        self.id = f'D{Doctor.unique_id: 03d}'
        Doctor.unique_id += 1

    def add_patient(self, patient: Patient):
        self.patients.append(patient)
    
    def get_doctor_details(self):
        patients_str = ''
        for patient in self.patients:
            patients_str += f'- {patient.first_name} {patient.last_name}\n    '
        print(f'''Name: {self.first_name} {self.last_name}
ID: {self.id}
Age: {self.age}
Gender: {self.gender}
Specialization: {self.specialization}
Patients:
{patients_str}''')

class Nurse(Person):


    unique_id = 1

    def __init__(self, person_details, department):
        super().__init__(person_details)
        self.department = department
        self.assisted_patient = 'None'
        self.id = f'N{Nurse.unique_id: 03d}'
        Nurse.unique_id += 1
    
    def assist_patient(self, patient: Patient):
        self.assisted_patient += f'{patient.first_name} {patient.last_name}\n'
        print(f'Nurse: {self.first_name} {self.last_name} assisted {patient.first_name} {patient.last_name}')

    def get_nurse_details(self):
        print(f'''Name: {self.first_name} {self.last_name}
ID: {self.id}
Age: {self.age}
Gender: {self.gender}
Department: {self.department}
Assisted patient: {self.assisted_patient}''')

class Appointment:

    patient: Patient
    doctor: Doctor
    appointment_time: str
    status: str

    def __init__(self, doctor: Doctor, patient: Patient):
        self.doctor = doctor
        self.patient = patient
        self.status = 'In queue'
        self.appointment_time = "None"

    def schedule_appointment(self, appointment_time):
        self.appointment_time = appointment_time
        self.status = 'Scheduled'

    def cancel_appointment(self):
        self.status = 'Canceled'

    def get_appointment_details(self):
        print(f'''Patient: {self.patient.first_name} {self.patient.last_name}
Doctor: {self.doctor.first_name} {self.doctor.last_name}
Date and Time: {self.appointment_time}
Status: {self.status}''')

class Hospital:

    patients = dict()
    doctors = dict()
    nurses = dict()
    appointments = list()

    def add_patient(self, patient: Patient):
        self.patients[f'{patient.first_name} {patient.last_name}'] = patient
        print('Patient added successfully:')
        patient.get_patient_details()

    def add_doctor(self, doctor: Doctor):
        self.doctors[f'{doctor.first_name} {doctor.last_name}'] = doctor
        print('Doctor added successfully:')
        doctor.get_doctor_details()
    
    def add_nurse(self, nurse: Nurse):
        self.nurses[f'{nurse.first_name} {nurse.last_name}'] = nurse
        print('Nurse added successfully:')
        nurse.get_nurse_details()
    
    def schedule_appointment(self, doctor, patient, appointment_time):
        appointment = Appointment(doctor, patient)
        appointment.schedule_appointment(appointment_time)
        self.appointments.append(appointment)
        patient.assigned_doctor = f'{doctor.first_name} {doctor.last_name}'
        doctor.add_patient(patient)

    def get_all_appointments(self):
        patients_str = 'All Appointments\n'
        for patient in self.patients:
            patients_str += f'Patient: {patient.first_name} {patient.last_name}, \
                             Doctor: Dr. {patient.assigned_doctor.first_name} {patient.assigned_doctor.last_name}, \
                                Date: {patient.appointment_time}'
            patients_str += '\n'
        print(patients_str)

    def get_all_patients(self):
        patients_str = 'All Patients:\n'
        for patient in self.patients.values():
            patients_str += f'Name: {patient.first_name} {patient.last_name}, \
                ID: {patient.id}, \
                Age: {patient.age}, \
                Gender: {patient.gender}, \
                Disease: {patient.disease}, \
                Assigned Doctor: {patient.assigned_doctor}\n'
        print(patients_str)
                
    def get_all_doctors(self):
        doctors_str = 'All Doctors:\n'
        for doctor in self.doctors:
            doctors_str += f'Dr. {doctor.first_name} {doctor.last_name}, \
                ID: {doctor.id}, \
                    Specialization: {doctor.specialization}\n'
        print(doctors_str)

    def get_all_nurses(self):
        nurses_str = 'All Nurses:\n'
        for nurse in self.nurses.values():
            nurses_str += f'Name: {nurse.first_name} {nurse.last_name}, \
                ID: {nurse.id}, \
                Age: {nurse.age}, \
                Gender: {nurse.gender}, \
                Department: {nurse.department}\n'
        print(nurses_str)

    def get_doctor_patients(self, doctor: Doctor):
        for patient in doctor.patients:
            print(f'Patient: {patient.first_name} {patient.last_name}')
hospital = Hospital()

def get_general_details():
    person_details_dict = dict()
    person_details_dict['first_name'] = input('First name: ')
    person_details_dict['last_name'] = input('Last name: ')
    person_details_dict['age'] = input('Age: ')
    person_details_dict['gender'] = input('Gender: ')
    return person_details_dict

def hospital_menu():
    print('1. Add patient')
    print('2. Add doctor')
    print('3. Add nurse')
    print('4. Schedule appointment between a doctor and a patient')
    print('5. Get all appointments')
    print('6. Get all patients')
    print('7. Get all doctors')
    print('8. Get doctor patients')
    print('9. Get all nurses')
    print('10. Assist patient')
    print('11. Exit')
    choice = input('Enter your choice: ')
    while not(1 <= int(choice) <= 10):
        choice = input('Enter a valid number: ')
    match choice:
        case '1':
            patient_details = get_general_details()
            disease = input('Disease: ')
            assigned_doctor = 'None'
            patient = Patient(patient_details, disease, assigned_doctor)
            hospital.add_patient(patient)
        case '2':
            doctor_details = get_general_details()
            specialization = input('Specialization: ')
            doctor = Doctor(doctor_details, specialization)
            hospital.add_doctor(doctor)
        case '3':
            nurse_details = get_general_details()
            department = input('Department: ')
            nurse = Nurse(nurse_details, department)
            hospital.add_nurse(nurse)
        case '4':
            doctor_first_name = input("Enter doctor's first name: ")
            doctor_last_name = input("Enter doctor's last name: ")
            doctor = hospital.doctors.get(f'{doctor_first_name} {doctor_last_name}')
            if doctor == None:
                print('A doctor with this name doesnt exist.')
                return
            patient_first_name = input("Enter patient's first name: ")
            patient_last_name = input("Enter patient's last name: ")
            patient = hospital.patients.get(f'{patient_first_name} {patient_last_name}')
            if patient == None:
                print('A patient with this name doesnt exist.')
                return
            appointment_time = input("Enter appointment time(e.g. 2025-03-10 10:00): ")
            hospital.schedule_appointment(doctor, patient, appointment_time)

        case '5':
            hospital.get_all_appointments()
        case '6':
            hospital.get_all_patients()
        case '7':
            hospital.get_all_doctors()
        case '8':
            doctor_first_name = input("Enter doctor's first name: ")
            doctor_last_name = input("Enter doctor's last name: ")
            doctor = hospital.doctors.get(f'{doctor_first_name} {doctor_last_name}')
            if doctor == None:
                print('A doctor with this name doesnt exist.')
                return
            hospital.get_doctor_patients(doctor)
        case '9':
            hospital.get_all_nurses()
        case '10':
            nurse : Nurse = random.choice(list(hospital.nurses.keys()))
            patient_first_name = input("Enter patient's first name: ")
            patient_last_name = input("Enter patient's last name: ")
            patient = hospital.patients.get(f'{patient_first_name} {patient_last_name}')
            if patient == None:
                print('A patient with this name doesnt exist.')
                return
            nurse.assist_patient(patient)
        case '11':
            exit()

while True:
    hospital_menu()