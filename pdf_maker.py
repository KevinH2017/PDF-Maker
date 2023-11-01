from fpdf import FPDF
import pandas as pd

# P is portrait orientation, millimeter units, and with A4 standard paper size
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pd.read_csv("./app3/topics.csv")

for index, row in df.iterrows():
    # Sets up header
    pdf.add_page()
    # Sets font family to Times, Bold text, at font size 24
    pdf.set_font(family="Times", style="B", size=24)
    # RGB values
    pdf.set_text_color(0,0,255)        
    # Width goes to end of page, Height is 12, Left-Aligned, ln is break line
    pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)

    # Creates lines within each page
    # range(start, end, steps)
    for y in range(20, 298, 10):
        pdf.line(10, y, 200, y)

    # Sets up page 1 footer
    pdf.ln(265)           
    pdf.set_font(family="Times", style="I", size=8)
    pdf.set_text_color(255,0,0)
    pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
    
    # Creates the number of Pages of a Topic from topics.csv
    for i in range(row["Pages"]-1):
        pdf.add_page()

        for y in range(20, 298, 10):
            pdf.line(10, y, 200, y)

        # Sets up Footer      
        pdf.ln(277)        
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(255,0,0)
        pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

pdf.output("./app3/output.pdf")