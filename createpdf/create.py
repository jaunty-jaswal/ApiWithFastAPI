from fpdf import FPDF
async def createPDF():
    ob = FPDF()
    ob.add_page()
    ob.set_font("Arial", size = 10)
    text = "This is a text we are generating randomly to store into pdf. You can enter your text here."
    ob.cell(0, 0, txt = text, ln = 1, align = 'L')
    ob.output("ourpdf.pdf")