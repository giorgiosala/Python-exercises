import pandas as pd
import numpy as np
import random
from faker import Faker

# Initialize Faker
fake = Faker()

# Define constants
num_records = 1000

# Define possible values for columns
genders = ['Male', 'Female']
blood_types = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
departments = ['Cardiology', 'Oncology', 'Neurology', 'Pediatrics', 'Orthopedics']
diagnoses = {
    'Cardiology': ['Hypertension', 'Heart Disease', 'Arrhythmia'],
    'Oncology': ['Cancer', 'Leukemia', 'Lymphoma'],
    'Neurology': ['Migraine', 'Epilepsy', 'Parkinson\'s'],
    'Pediatrics': ['Asthma', 'Chickenpox', 'Cystic Fibrosis'],
    'Orthopedics': ['Fracture', 'Arthritis', 'Osteoporosis']
}
treatments = ['Medication', 'Surgery', 'Therapy', 'Chemotherapy']
treatment_outcomes = ['Improved', 'Stable', 'Deteriorated']
patient_conditions = ['Good', 'Fair', 'Serious', 'Critical']
doctors = [f'D{str(i).zfill(3)}' for i in range(1, 21)]  # 20 doctors
follow_ups = ['Yes', 'No']
medication_levels = ['Low', 'Medium', 'High']
appointment_durations = list(range(15, 121, 15))  # 15, 30, 45, ..., 120 minutes

# Generate unique patient IDs
patient_ids = list(range(1, num_records + 1))

# Generate random data
data = []
for _ in range(num_records):
    patient_id = patient_ids.pop()
    age = random.choices(range(0, 100), weights=[2]*5 + [5]*5 + [10]*10 + [20]*10 + [15]*10 + [10]*10 + [10]*10 + [8]*10 + [5]*10 + [3]*10 + [2]*10, k=1)[0]
    gender = random.choice(genders)
    blood_type = random.choice(blood_types)
    department = random.choice(departments)
    diagnosis = random.choice(diagnoses[department])
    treatment = random.choice(treatments)
    visit_cost = round(random.uniform(100, 1000), 2)
    follow_up_required = random.choice(follow_ups)
    patient_condition = random.choice(patient_conditions)
    medication_level = random.choice(medication_levels)
    appointment_duration = random.choice(appointment_durations)
    treatment_outcome = random.choice(treatment_outcomes)
    doctor_notes = fake.sentence(nb_words=10)
    
    # Generate realistic health metrics and improvement
    health_metric = round(random.uniform(80, 200), 2)
    improvement_factor = random.uniform(0.01, 0.3)
    health_improvement = round(health_metric * improvement_factor, 2)
    
    visit_date = fake.date_between(start_date='-1y', end_date='today')
    treatment_start_date = fake.date_between(start_date='-2y', end_date=visit_date)
    doctor_id = random.choice(doctors)
    
    data.append([
        patient_id, age, gender, visit_date, diagnosis, treatment, doctor_id, department, visit_cost, 
        follow_up_required, blood_type, patient_condition, medication_level, appointment_duration, 
        treatment_outcome, doctor_notes, health_metric, treatment_start_date, health_improvement
    ])

# Create DataFrame
columns = [
    'PatientID', 'Age', 'Gender', 'VisitDate', 'Diagnosis', 'Treatment', 'DoctorID', 'Department', 
    'VisitCost', 'FollowUpRequired', 'BloodType', 'PatientCondition', 'MedicationLevels', 
    'AppointmentDuration', 'TreatmentOutcome', 'DoctorNotes', 'HealthMetric', 'TreatmentStartDate', 
    'HealthImprovement'
]
df = pd.DataFrame(data, columns=columns)

# Save to CSV
df.to_csv('healthcare_data_expanded.csv', index=False)

df.head()
import pandas as pd
import numpy as np
import random
from faker import Faker

# Initialize Faker
fake = Faker()

# Define constants
num_records = 1000

# Define possible values for columns
genders = ['Male', 'Female']
blood_types = ['A+', 'A-', 'B+', 'B-', 'AB+', 'AB-', 'O+', 'O-']
departments = ['Cardiology', 'Oncology', 'Neurology', 'Pediatrics', 'Orthopedics']
diagnoses = {
    'Cardiology': ['Hypertension', 'Heart Disease', 'Arrhythmia'],
    'Oncology': ['Cancer', 'Leukemia', 'Lymphoma'],
    'Neurology': ['Migraine', 'Epilepsy', 'Parkinson\'s'],
    'Pediatrics': ['Asthma', 'Chickenpox', 'Cystic Fibrosis'],
    'Orthopedics': ['Fracture', 'Arthritis', 'Osteoporosis']
}
treatments = ['Medication', 'Surgery', 'Therapy', 'Chemotherapy']
treatment_outcomes = ['Improved', 'Stable', 'Deteriorated']
patient_conditions = ['Good', 'Fair', 'Serious', 'Critical']
doctors = [f'D{str(i).zfill(3)}' for i in range(1, 21)]  # 20 doctors
follow_ups = ['Yes', 'No']
medication_levels = ['Low', 'Medium', 'High']
appointment_durations = list(range(15, 121, 15))  # 15, 30, 45, ..., 120 minutes

# Generate unique patient IDs
patient_ids = list(range(1, num_records + 1))

# Generate random data
data = []
for _ in range(num_records):
    patient_id = patient_ids.pop()
    age = random.choices(range(0, 100), weights=[2]*5 + [5]*5 + [10]*10 + [20]*10 + [15]*10 + [10]*10 + [10]*10 + [8]*10 + [5]*10 + [3]*10 + [2]*10, k=1)[0]
    gender = random.choice(genders)
    blood_type = random.choice(blood_types)
    department = random.choice(departments)
    diagnosis = random.choice(diagnoses[department])
    treatment = random.choice(treatments)
    visit_cost = round(random.uniform(100, 1000), 2)
    follow_up_required = random.choice(follow_ups)
    patient_condition = random.choice(patient_conditions)
    medication_level = random.choice(medication_levels)
    appointment_duration = random.choice(appointment_durations)
    treatment_outcome = random.choice(treatment_outcomes)
    doctor_notes = fake.sentence(nb_words=10)
    
    # Generate realistic health metrics and improvement
    health_metric = round(random.uniform(80, 200), 2)
    improvement_factor = random.uniform(0.01, 0.3)
    health_improvement = round(health_metric * improvement_factor, 2)
    
    visit_date = fake.date_between(start_date='-1y', end_date='today')
    treatment_start_date = fake.date_between(start_date='-2y', end_date=visit_date)
    doctor_id = random.choice(doctors)
    
    data.append([
        patient_id, age, gender, visit_date, diagnosis, treatment, doctor_id, department, visit_cost, 
        follow_up_required, blood_type, patient_condition, medication_level, appointment_duration, 
        treatment_outcome, doctor_notes, health_metric, treatment_start_date, health_improvement
    ])

# Create DataFrame
columns = [
    'PatientID', 'Age', 'Gender', 'VisitDate', 'Diagnosis', 'Treatment', 'DoctorID', 'Department', 
    'VisitCost', 'FollowUpRequired', 'BloodType', 'PatientCondition', 'MedicationLevels', 
    'AppointmentDuration', 'TreatmentOutcome', 'DoctorNotes', 'HealthMetric', 'TreatmentStartDate', 
    'HealthImprovement'
]
df = pd.DataFrame(data, columns=columns)

# Save to CSV
df.to_csv('healthcare_data.csv', index=False)

df.head()
