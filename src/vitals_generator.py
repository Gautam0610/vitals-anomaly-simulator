import random
from faker import Faker

fake = Faker()

def generate_vitals():
    age = random.randint(18, 85)
    name = fake.name()
    temperature = round(random.uniform(36.5, 37.5), 1)
    heart_rate = random.randint(60, 100)
    breaths_per_minute = random.randint(12, 20)
    blood_pressure_systolic = random.randint(110, 140)
    blood_pressure_diastolic = random.randint(70, 90)
    oxygen_saturation = random.randint(95, 99)

    # Introduce anomalies in heart rate and breaths per minute
    if random.random() < 0.1:
        heart_rate = random.randint(150, 220)  # Unrealistic heart rate
    if random.random() < 0.1:
        breaths_per_minute = random.randint(30, 50) # Unrealistic breaths per minute

    vitals = {
        "name": name,
        "age": age,
        "temperature": temperature,
        "heart_rate": heart_rate,
        "breaths_per_minute": breaths_per_minute,
        "blood_pressure_systolic": blood_pressure_systolic,
        "blood_pressure_diastolic": blood_pressure_diastolic,
        "oxygen_saturation": oxygen_saturation
    }
    return vitals