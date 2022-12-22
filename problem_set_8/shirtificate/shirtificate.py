from fpdf import FPDF


name = input("Name: ")
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.add_page()
pdf.set_font("Times", "", 50)
pdf.cell(0, 25, "CS50 Shirtificate", align="C")
pdf.image("shirtificate.png", x=2, y=75)
pdf.set_font_size(24)
pdf.set_text_color(255, 255, 255)
pdf.text(x=45, y=155, txt=f"{name} took CS50")
pdf.output("shirtificate.pdf")
