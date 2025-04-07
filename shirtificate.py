from fpdf import FPDF

# Instantiate the pdf class to inherit all the features of FPDF
class Pdf(FPDF):
    ...


def main():
    # Prompt user for their name
    name = input("Name: ").title()


    # The orientation of the PDF should be Portrait, the format of the PDF should be A4, which is 210mm wide by 297mm tall.
    pdf = Pdf(orientation="P", unit="mm", format=(210, 297))
    pdf.add_page()
    pdf.set_font("helvetica", style="B", size=35)

    # Create new line in pdf
    pdf.ln(20)

    # The top of the PDF should say “CS50 Shirtificate” as text, centered horizontally.
    pdf.cell(0, 10, "CS50 Shirtificate", align="C")

    # The shirt’s image should be centered horizontally.
    pdf.image("shirtificate.png", w=189, h=188, x=10.5, y=60)

    # The user’s name should be on top of the shirt, in white text.
    pdf.set_text_color(255, 255, 255)
    pdf.set_font_size(25)
    pdf.cell(-190 , 198, f"{name} took CS50", align="C")
    pdf.output("shirtificate.pdf")


if __name__ == "__main__":
    main()
