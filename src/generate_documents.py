import os
import random
import string
from faker import Faker
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

fake = Faker()

BASE_DATA_DIR = "data/synthetic"
PAN_DIR = os.path.join(BASE_DATA_DIR, "pan")
AADHAAR_DIR = os.path.join(BASE_DATA_DIR, "aadhaar")

os.makedirs(PAN_DIR, exist_ok=True)
os.makedirs(AADHAAR_DIR, exist_ok=True)


def generate_pan_number():
    """Generate valid PAN-like number"""
    return (
        ''.join(random.choices(string.ascii_uppercase, k=5)) +
        ''.join(random.choices(string.digits, k=4)) +
        random.choice(string.ascii_uppercase)
    )


def generate_aadhaar_number():
    """Generate Aadhaar-like number"""
    return ' '.join(
        ''.join(random.choices(string.digits, k=4)) for _ in range(3)
    )


def create_pan_pdf(idx):
    file_path = os.path.join(PAN_DIR, f"pan_{idx}.pdf")
    c = canvas.Canvas(file_path, pagesize=A4)

    name = fake.name().upper()
    dob = fake.date_of_birth(minimum_age=18, maximum_age=65).strftime("%d/%m/%Y")
    pan = generate_pan_number()

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, 800, "INCOME TAX DEPARTMENT")
    c.drawString(50, 780, "GOVERNMENT OF INDIA")

    c.setFont("Helvetica", 12)
    c.drawString(50, 740, f"Name: {name}")
    c.drawString(50, 710, f"DOB: {dob}")
    c.drawString(50, 680, f"PAN: {pan}")

    c.rect(45, 650, 400, 170)
    c.showPage()
    c.save()


def create_aadhaar_pdf(idx):
    file_path = os.path.join(AADHAAR_DIR, f"aadhaar_{idx}.pdf")
    c = canvas.Canvas(file_path, pagesize=A4)

    name = fake.name().upper()
    gender = random.choice(["MALE", "FEMALE"])
    aadhaar = generate_aadhaar_number()
    address = fake.address().replace("\n", ", ")

    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, 800, "UNIQUE IDENTIFICATION AUTHORITY OF INDIA")

    c.setFont("Helvetica", 12)
    c.drawString(50, 760, f"Name: {name}")
    c.drawString(50, 730, f"Gender: {gender}")
    c.drawString(50, 700, f"Aadhaar No: {aadhaar}")
    c.drawString(50, 670, f"Address: {address}")

    c.rect(45, 640, 450, 200)
    c.showPage()
    c.save()


def main(num_samples=50):
    for i in range(num_samples):
        create_pan_pdf(i)
        create_aadhaar_pdf(i)

    print(f"Generated {num_samples} PAN and Aadhaar documents.")


if __name__ == "__main__":
    main()
