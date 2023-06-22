from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from datetime import datetime
from reportlab.platypus import Image
from reportlab.platypus.flowables import HRFlowable

now = datetime.now()
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
month_now = String(now.strftime("%m")) + "/" + String(now.strftime("%Y"))
amount_due = 1150.45
energy_this_month = 152
connected_load = 5000


# Sample data for the electricity bill
bill_data = {
    'customer_name': 'FISAT',
    'consumer_number': '1234567890',
    'address': 'Hormis Nagar, Mookkannoor',
    'month': month_now,
    'amount_due': amount_due,
    'energy': energy_this_month,
    'bill_generated_on': dt_string,
    'connected_load': connected_load
}

def create_bill_pdf(file_name, bill_data):
    doc = SimpleDocTemplate(file_name, pagesize=letter)
    styles = getSampleStyleSheet()

    # Create the content for the PDF
    content = []

    title_style = styles['Title']
    title_style.alignment = 1  # Center alignment
    title_style.fontSize = 24  # Increase the heading size
    title = Paragraph('<b>DISCOM NAME HERE</b>', title_style)
    content.append(title)
    content.append(Spacer(1, 50))  # Add some space

    # Add a horizontal line
    content.append(HRFlowable(width="100%", thickness=1, lineCap='round', color=colors.black, spaceBefore=6, spaceAfter=6))

    # Add the title
    title_style = styles['Title']
    title_style.alignment = 1  # Center alignment
    title_style.fontSize = 24  # Increase the heading size
    title = Paragraph('<b>ELECTRICITY BILL FOR {}</b>'.format(bill_data['month']), title_style)
    content.append(title)
    content.append(Spacer(1, 4))  # Add some space

    # Add a horizontal line
    content.append(HRFlowable(width="100%", thickness=1, lineCap='round', color=colors.black, spaceBefore=6, spaceAfter=6))
    content.append(Spacer(1, 24))  # Add some space

    # Add the customer details
    content.append(Paragraph('Bill generated on: {}'.format(bill_data['bill_generated_on']), styles['Normal']))
    content.append(Paragraph('Bill number: #12345678', styles['Normal']))
    content.append(Spacer(1, 7))  # Add some space
    content.append(Paragraph('Tariff type: dynamic pricing/3 phase', styles['Normal']))
    content.append(Paragraph('connected load: <b>{} W</b>'.format(bill_data['connected_load']), styles['Normal']))
    content.append(Spacer(1, 7))  # Add some space
    content.append(Paragraph('Customer Name: {}'.format(bill_data['customer_name']), styles['Normal']))
    content.append(Paragraph('Consumer number: {}'.format(bill_data['consumer_number']), styles['Normal']))
    content.append(Paragraph('Address: {}'.format(bill_data['address']), styles['Normal']))
    content.append(Spacer(1, 12))  # Add some space
    content.append(Paragraph('<b>Energy used this month: </b>{} units'.format(bill_data['energy']), styles['Normal']))
    content.append(Spacer(1, 30))  # Add some space
    # Add the bill details




    # Create a table for the bill data
    data = [
        ['Amount Due', f'Rs: {bill_data["amount_due"]}'],
    ]
    table = Table(data, colWidths=[200, 200])
    table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
        ('FONTSIZE', (0, 0), (-1, 0), 14),
        ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
        ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
        ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),
        ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 1), (-1, -1), 12),
        ('ALIGN', (0, -1), (-1, -1), 'CENTER'),
        ('BOTTOMPADDING', (0, -1), (-1, -1), 12),
    ]))

    content.append(table)
    doc.build(content)

# Call the function to create the PDF
create_bill_pdf('electricity_bill.pdf', bill_data)
