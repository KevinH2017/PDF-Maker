from fpdf import FPDF
import pandas as pd

# P is portrait orientation, millimeter units, and with A4 standard paper size
pdf = FPDF(orientation="P", unit="mm", format="A4")

df = pd.read_csv("./app3/topics.csv")

for index, row in df.iterrows():
        pdf.add_page()
        # Sets font family to Times, Bold text, at font size 24
        pdf.set_font(family="Times", style="B", size=24)
        # RGB values
        pdf.set_text_color(0,0,255)
                        
        # Width goes to end of page, Height is 12, Left-Aligned, ln is break line
        pdf.cell(w=0, h=12, txt=row["Topic"], align="L", ln=1)
        # x1, y1 to x2, y2 in the specified unit in FPDF()
        pdf.line(10,21, 200,21)

        # Creates the number of pages of a Topic in topic.csv
        for i in range(row["Pages"]-1):
            pdf.add_page()

pdf.output("./app3/output.pdf")