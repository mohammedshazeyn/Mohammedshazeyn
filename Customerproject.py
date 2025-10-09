# By Mohammed Shazeyn

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

name = input("Enter customer's full name: ")
age = input("Enter customer's age: ")
email = input("Enter customer's email: ")
phone = input("Enter customer's phone number: ")
city = input("Enter customer's city: ")
product = input("Enter interested product/service: ")

file_name = name.replace(" ", "_").lower() + "_profile.pdf"
pdf = canvas.Canvas(file_name, pagesize=A4)

pdf.setTitle("Customer Profile Page")
pdf.setFont("Helvetica-Bold", 20)
pdf.drawCentredString(300, 800, "CUSTOMER PROFILE PAGE")

pdf.setFont("Helvetica", 14)
pdf.drawString(100, 750, f"Name: {name}")
pdf.drawString(100, 720, f"Age: {age}")
pdf.drawString(100, 690, f"Email: {email}")
pdf.drawString(100, 660, f"Phone: {phone}")
pdf.drawString(100, 630, f"City: {city}")
pdf.drawString(100, 600, f"Interested Product: {product}")

pdf.line(80, 580, 520, 580)
pdf.setFont("Helvetica-Oblique", 12)
pdf.drawString(100, 560, "Profile created successfully by Mohammed Shazeyn")

pdf.save()

print(f"\nProfile saved successfully as '{file_name}'")
