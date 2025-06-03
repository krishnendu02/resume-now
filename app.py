from flask import Flask, render_template, request, redirect, jsonify, send_file
from flask_mail import Mail, Message
from pymongo import MongoClient
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import Paragraph, Frame, SimpleDocTemplate
from reportlab.lib.colors import red, blue, green, HexColor
import io

# python flask_app\\app.py  --> to start the app
# python app.py
# http://127.0.0.1:5000/landing


app = Flask(__name__)

client = MongoClient('mongodb://localhost:27017/resume_now')

contact_us_db = client['contact_us_form']
contacts_collection = contact_us_db['queries/feedbacks']



#http://127.0.0.1:5000/landing
@app.route('/') 
def Landing():
     return render_template("Landing.html")
 

 
@app.route('/submit', methods=['POST'])

def submit():
    data = request.get_json()  # Get JSON data from JS fetch()
    
    name = data.get('user')
    email = data.get('user_email')
    message = data.get('Queries/Feedback')
    
    
    # Save to MongoDB
    contact_data = {
        'name': name,
        'email': email,
        'message': message
    }
    contacts_collection.insert_one(contact_data)
    # Return JSON response
    return jsonify({'message': 'Thank you for contacting us!'})


@app.route('/pdf') 
def pdf_template():
     return render_template("pdf_template.html")
 


# image_path1 = "static\images\pdf\pint1.jpg"
# image_path2 = "static\images\pdf\pint2.jpg"
# image_path3 = "static\images\pdf\pint3.jpg"
# image_path4 = "static\images\pdf\pint4.jpg"
# image_path5 = "static\images\pdf\pint5.jpg"
# image_path6 = "static\images\pdf\pint6.jpg"
# image_path7 = "static\images\pdf\pint7.jpg"


@app.route('/main') 
def main():
     return render_template("main.html") 


# Defining Paragraph
styles = getSampleStyleSheet()    
custom_style = ParagraphStyle('CustomStyle',
    parent=styles['BodyText'],  # Inherit basic styles
    fontName="Helvetica",
    fontSize=14,  # ✅ Change font size here
    leading=24,  # Adjust line spacing (leading)
    alignment=0,  # 0=Left, 1=Center, 2=Right, 4=Justified
    textColor="black"
    )

custom_style_link = ParagraphStyle('CustomStyle',
    parent=styles['BodyText'],  # Inherit basic styles
    fontName="Helvetica",
    fontSize=13,  # ✅ Change font size here
    leading=24,  # Adjust line spacing (leading)
    alignment=0,  # 0=Left, 1=Center, 2=Right, 4=Justified
    textColor="#3498db"
    
    )


        


@app.route('/generate-pdf', methods=['POST'])
def generate_pdf():
    
    # Fetching the information from HTML
    
    #from main.html
    
    # Personal Details
    First_name = request.form.get("First_name", "N/A")
    Middle_name = request.form.get("Middle_name", "N/A")
    Last_name = request.form.get("Last_name", "N/A")
    
    email = request.form.get("email", "N/A")
    mobile_number = request.form.get("mobile_number", "N/A")
    LinkedIn = request.form.get("LinkedIn", "N/A")
    GitHub = request.form.get("GitHub", "N/A")
    
    birthday = request.form.get("birthday", "N/A")
    
    Country = request.form.get("Country", "N/A")
    State = request.form.get("State", "N/A")
    City_District = request.form.get("City_District", "N/A")
    Town_Village = request.form.get("Town_Village", "N/A")
    Pin_Code = request.form.get("Pin_Code", "N/A")
    
    # Highest Education
    Degree = request.form.get("Degree", "N/A")
    Course = request.form.get("Course", "N/A")
    Stream = request.form.get("Stream", "N/A")
    School_College = request.form.get("School_College", "N/A")
    Board_University = request.form.get("Board_University", "N/A")
    marks_type = request.form.get("marks_type", "N/A")
    marks_val = request.form.get("marks_val", "N/A")
    from_date = request.form.get("from_date", "N/A")
    to_date = request.form.get("to_date", "N/A")
    
    # Skill Details
    core_skill = request.form.get("core_skill", "N/A")
    soft_skill = request.form.get("soft_skill", "N/A")
    
    # Projects Details
    project_details = request.form.get("project_details", "N/A")
    
    language1 = request.form.get("language1", "N/A")
    language1_level = request.form.get("language1_level", "N/A")
    
    language2 = request.form.get("language2", "N/A")
    language2_level = request.form.get("language2_level", "N/A")
    
    language3 = request.form.get("language3", "N/A")
    language3_level = request.form.get("language3_level", "N/A")
    about_me = request.form.get("about_me", "N/A")

    #                   #
    #                   #
    #                   #
    # Creating The PDF  #
    #                   #
    #                   #
    #                   #


    pdf_buffer = io.BytesIO()
    pdf = canvas.Canvas(pdf_buffer)
    
    page_width, page_height = A4  # A4 size: (595 x 842 points)
    #pdf.setFont("Helvetica-Bold", 16)
    
    
    image_path = "static\images\pdf\pint2.jpg"
    pdf.drawImage(image_path, 0, 0, width=page_width, height=page_height)
    
    # Calculate centered X position
    text = First_name
    text_width = pdf.stringWidth(text)
    x_position = (page_width - text_width) / 2  # Centered horizontally
    
    # Set border thickness (optional)
    border_thickness = 5
    
    # Draw border (x, y, width, height) 
    pdf.setStrokeColorRGB(0, 0, 0)  # Set border color (black) 
    pdf.setLineWidth(border_thickness)  # Set border thickness
    #pdf.rect(20, 20, page_width - 40, page_height - 40)  # Draw rectangle with padding
    pdf.roundRect(20, 20, page_width - 40, page_height - 40, 10)  # Rounded corners
    
    # Adding data in the PDF
    
    # main.html pdf
    
    pdf.setFont("Helvetica-Bold", 25)
    pdf.drawString(50, page_height - 60, f"{First_name + ' '+Middle_name}")
    pdf.drawString(50, page_height - 90, f"{Last_name}")
    
    # Link
    
    # Create the paragraph object
    text_link = LinkedIn+'<br/>'+GitHub
    paragraph_link = Paragraph(text_link, custom_style_link)
    frame = Frame(45, page_height - 300, 270, 200)  # (x, y, width, height)
    frame.addFromList([paragraph_link], pdf)
    
    
    # Core skill
    pdf.setFont("Times-BoldItalic", 15)
    pdf.drawString(50, page_height - 200, f"Core Skill")
    
    # Create the paragraph object
    text_core_skill = core_skill
    paragraph_core_skill = Paragraph(text_core_skill, custom_style)
    frame = Frame(45, page_height - 410, 200, 200)  # (x, y, width, height)
    frame.addFromList([paragraph_core_skill], pdf)
    
    
    # Soft Skill
    pdf.setFont("Times-BoldItalic", 15)
    pdf.drawString(50, page_height - 370, f"Soft Skill")
    
    # Create the paragraph object
    text_soft_skill = soft_skill
    paragraph_soft_skill = Paragraph(text_soft_skill, custom_style)
    frame = Frame(45, page_height - 580, 200, 200)  # (x, y, width, height)
    frame.addFromList([paragraph_soft_skill], pdf)
    
    
    # Spoken Language
    pdf.setFont("Times-BoldItalic", 15)
    pdf.drawString(50, page_height - 530, 'Spoken Language')
    
    def lev_name(x):
        if x == '0':
            return ('Only Speak')
        elif x == '1':
            return ('Read & Write')
        elif x == '2':
            return ('Mother Tongue')
    
    pdf.setFont("Helvetica", 15)
    lev1_name = lev_name(language1_level)
    pdf.drawString(50, page_height - 560, f"{language1+' '+' --> '+' '+lev1_name}")
    lev2_name = lev_name(language2_level)
    pdf.drawString(50, page_height - 580, f"{language2+' '+' --> '+' '+lev2_name}")
    lev3_name = lev_name(language3_level)
    pdf.drawString(50, page_height - 600, f"{language3+' '+' --> '+' '+lev3_name}")
    
    # About Me
    
    pdf.setFont("Times-BoldItalic", 20)
    pdf.drawString(50, page_height - 660, 'About Me')
    
    text_about_me = about_me

    # Create the paragraph object
    paragraph_about_me = Paragraph(text_about_me, custom_style)
    frame = Frame(45, page_height - 870, 500, 200)  # (x, y, width, height)
    frame.addFromList([paragraph_about_me], pdf)
    
    
    
    # Contact
    pdf.setFont("Times-BoldItalic", 15)
    pdf.drawString(330, page_height - 60, 'Contact')
    pdf.setFont("Helvetica", 15)
    pdf.drawString(330, page_height - 90, f"{mobile_number}")
    pdf.setFillColor(HexColor("#3498db"))
    pdf.drawString(330, page_height - 110, f"{email}")
    
    
    # Address
    pdf.setFillColor(HexColor("#000000"))
    pdf.setFont("Times-BoldItalic", 15)
    pdf.drawString(350, page_height - 170, 'Address')
    pdf.setFont("Helvetica", 15)
    pdf.drawString(350, page_height - 200, f"{Country+','+' '+State}")
    pdf.drawString(350, page_height - 220, f"{Town_Village+','+' '+City_District}")
    pdf.drawString(350, page_height - 240, f"{'Pin/Zip Code - '+Pin_Code}")
    
    # Birthday
    pdf.drawString(350, page_height - 280, f"Birthday: {birthday}")
    
    # Highest Education
    pdf.setFont("Times-BoldItalic", 15)
    pdf.drawString(350, page_height - 320, f"Education")
    
    # Create the paragraph object
    
    text_Education = Course+' '+'in'+' '+Stream+','+' '+Degree+'<br/>'+School_College+'<br/>'+Board_University+'<br/>'+marks_type+' '+marks_val+'<br/>'+from_date+' '+'to'+' '+to_date
    
    paragraph_Education = Paragraph(text_Education, custom_style)
    frame = Frame(345, page_height - 530, 200, 200)  # (x, y, width, height)
    frame.addFromList([paragraph_Education], pdf)
    
    # project_details
    pdf.setFont("Times-BoldItalic", 15)
    pdf.drawString(350, page_height - 530, f"Project Details")
    
    # Create the paragraph object
    
    text_project = project_details
    
    paragraph_project = Paragraph(text_project, custom_style)
    frame = Frame(345, page_height - 730, 200, 200)
    frame.addFromList([paragraph_project], pdf)
      

    
    pdf.save()

    pdf_buffer.seek(0)

    return send_file(
        pdf_buffer,
        mimetype="application/pdf",
        as_attachment=False,  # Open in browser
        download_name="Resume.pdf"
    )

if __name__ == '__main__':
    app.run(debug=True)
