from fpdf import FPDF
async def createPDF():
    ob = FPDF()
    ob.add_page()
    ob.set_font("Arial", size = 10)
    text = "this is a text we are generating randomly"
    ob.cell(0, 0, txt = text, ln = 1, align = 'L')
    ob.output("ourpdf.pdf")