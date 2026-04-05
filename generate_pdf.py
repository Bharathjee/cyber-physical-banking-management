from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def create_project_pdf():
    c = canvas.Canvas("cyber_physical_banking.pdf", pagesize=letter)
    width, height = letter
    
    # Title
    c.setFont("Helvetica-Bold", 24)
    c.drawString(100, height - 100, "Cyber Physical Banking System")
    
    # Subtitle
    c.setFont("Helvetica", 14)
    c.drawString(100, height - 130, "Full-Stack Flask + Docker Banking Demo")
    
    # Features
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, height - 200, "Features:")
    c.setFont("Helvetica", 12)
    features = [
        "• Admin creates customer accounts (ID + Password)",
        "• Customer portal: balance, deposit, withdraw", 
        "• Role-based dashboards & authentication",
        "• Dockerized (production-ready)",
        "• Responsive cyberpunk UI"
    ]
    y = height - 230
    for feature in features:
        c.drawString(120, y, feature)
        y -= 20
    
    # Demo
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, y - 20, "Demo Flow:")
    c.setFont("Helvetica", 12)
    demo = [
        "1. Admin: admin / admin123",
        "2. Create customer: cust001 / pass123",
        "3. Customer login → Manage account"
    ]
    y -= 50
    for step in demo:
        c.drawString(120, y, step)
        y -= 20
    
    # Links
    c.setFont("Helvetica", 12)
    c.drawString(100, y - 30, "Live: http://localhost:5000")
    c.drawString(100, y - 50, "Repo: github.com/Bharathjee/cyber-physical-banking-management")
    
    c.save()
    print("PDF created: cyber_physical_banking.pdf - generate_pdf.py:52")

if __name__ == "__main__":
    create_project_pdf()
