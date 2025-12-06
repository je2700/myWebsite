#!/usr/bin/env python3
"""
Generiere professionellen Lebenslauf als PDF
Basierend auf den Daten aus der Resume.vue Komponente
"""

from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle, PageBreak
from reportlab.platypus import KeepTogether
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT

def create_resume():
    """Erstelle den Lebenslauf als PDF"""
    
    # PDF Setup
    output_file = "/workspaces/myWebsite/vuetify-devsite/public/lebenslauf.pdf"
    doc = SimpleDocTemplate(output_file, pagesize=A4,
                          rightMargin=2*cm, leftMargin=2*cm,
                          topMargin=2*cm, bottomMargin=2*cm)
    
    # Story (Inhalt)
    story = []
    
    # Styles
    styles = getSampleStyleSheet()
    
    # Custom Styles
    title_style = ParagraphStyle(
        'CustomTitle',
        parent=styles['Heading1'],
        fontSize=24,
        textColor=colors.HexColor('#667eea'),
        spaceAfter=6,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    )
    
    subtitle_style = ParagraphStyle(
        'CustomSubtitle',
        parent=styles['Normal'],
        fontSize=14,
        textColor=colors.HexColor('#4a5568'),
        spaceAfter=20,
        alignment=TA_CENTER,
        fontName='Helvetica'
    )
    
    section_style = ParagraphStyle(
        'SectionTitle',
        parent=styles['Heading2'],
        fontSize=16,
        textColor=colors.HexColor('#667eea'),
        spaceAfter=12,
        spaceBefore=20,
        fontName='Helvetica-Bold'
    )
    
    contact_style = ParagraphStyle(
        'Contact',
        parent=styles['Normal'],
        fontSize=10,
        textColor=colors.HexColor('#4a5568'),
        alignment=TA_CENTER
    )
    
    # === HEADER ===
    story.append(Paragraph("Jehad Qassem", title_style))
    story.append(Paragraph("Full-Stack Entwickler", subtitle_style))
    
    # Kontakt
    contact_info = [
        ["📧 qassemjehad@gmail.com", "📍 Berlin, Deutschland"],
        ["💼 github.com/je2700", "🌐 je2700.github.io"]
    ]
    contact_table = Table(contact_info, colWidths=[9*cm, 9*cm])
    contact_table.setStyle(TableStyle([
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('TEXTCOLOR', (0, 0), (-1, -1), colors.HexColor('#4a5568')),
    ]))
    story.append(contact_table)
    story.append(Spacer(1, 0.5*cm))
    
    # Quick Skills
    skills_text = "Vue.js • React • TypeScript • Node.js • PostgreSQL • Express"
    story.append(Paragraph(skills_text, contact_style))
    story.append(Spacer(1, 0.8*cm))
    
    # === BERUFSERFAHRUNG ===
    story.append(Paragraph("💼 Berufserfahrung", section_style))
    
    experiences = [
        {
            "period": "2024 – heute",
            "title": "Full-Stack Web-Developer",
            "company": "Freiberuflich",
            "description": "Entwicklung moderner, responsiver Webanwendungen mit Vue.js 3, Vuetify und TypeScript. Aufbau skalierbarer Backend-Systeme mit Node.js, Express und PostgreSQL. Implementierung von REST-APIs mit JWT-Authentifizierung und Fokus auf Clean Code sowie Best Practices.",
            "tags": "Vue 3, TypeScript, Node.js, PostgreSQL, Express, Vuetify"
        },
        {
            "period": "2023 – 2024",
            "title": "Mobile & Web App Developer",
            "company": "Freiberuflich",
            "description": "Entwicklung hybrider mobiler Anwendungen mit Apache Cordova für iOS und Android. Erstellung von Progressive Web Apps (PWA) mit modernen Web-Technologien. Integration von REST-APIs, Implementierung von Offline-Funktionalität und Push-Benachrichtigungen.",
            "tags": "Apache Cordova, PWA, JavaScript, HTML5, CSS3, REST API"
        },
        {
            "period": "2023 – 2024",
            "title": "Frontend Developer",
            "company": "Freiberuflich",
            "description": "Entwicklung interaktiver Single Page Applications mit React und Angular. Implementierung responsiver Benutzeroberflächen, State Management mit Redux und Angular Services. Arbeit mit modernen Build-Tools und Component-Libraries.",
            "tags": "React, Angular, TypeScript, Redux, Responsive Design"
        },
        {
            "period": "2022 – 2023",
            "title": "Web-App Developer Ausbildung",
            "company": "SGD Darmstadt",
            "description": "Intensives Fernstudium zum Web-App Developer mit Schwerpunkt auf moderne JavaScript-Frameworks. Erlernen von Full-Stack-Entwicklung, Datenbank-Design, RESTful APIs und agilen Entwicklungsmethoden. Abschluss mit Zertifizierung in allen relevanten Web-Technologien.",
            "tags": "JavaScript, Node.js, jQuery, Datenbanken, Webdesign"
        }
    ]
    
    job_style = ParagraphStyle(
        'JobStyle',
        parent=styles['Normal'],
        fontSize=10,
        leading=14,
        spaceBefore=6,
        spaceAfter=6
    )
    
    for exp in experiences:
        # Period und Title als Überschrift
        story.append(Paragraph(f"<b>{exp['period']}</b> | <b>{exp['title']}</b> – <i>{exp['company']}</i>", job_style))
        
        # Beschreibung
        story.append(Paragraph(exp['description'], job_style))
        
        # Tags
        story.append(Paragraph(f"<font color='#667eea'><i>Technologien: {exp['tags']}</i></font>", job_style))
        story.append(Spacer(1, 0.5*cm))
    
    # === TECHNISCHE FÄHIGKEITEN ===
    story.append(Paragraph("⚙️ Technische Fähigkeiten", section_style))
    
    skills = [
        ["Vue.js (Vuetify-latest)", "95%"],
        ["TypeScript", "90%"],
        ["JavaScript (ES6+) & HTML5/CSS3", "85%"],
        ["Node.js", "80%"],
        ["React & Angular", "70%"],
        ["PostgreSQL", "65%"]
    ]
    
    skills_table = Table(skills, colWidths=[14*cm, 4*cm])
    skills_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 6),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 6),
        ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
        ('TEXTCOLOR', (1, 0), (1, -1), colors.HexColor('#667eea')),
        ('FONTNAME', (1, 0), (1, -1), 'Helvetica-Bold'),
    ]))
    story.append(skills_table)
    story.append(Spacer(1, 0.6*cm))
    
    # === AUSBILDUNG ===
    story.append(Paragraph("🎓 Fernstudium", section_style))
    
    education_data = [
        [Paragraph("<b>2022 – 2023</b>", styles['Normal'])],
        [Paragraph("<b>Web-App Developer</b>", styles['Normal'])],
        [Paragraph("SGD (Studiengemeinschaft Darmstadt)", styles['Normal'])],
        [Paragraph("• Schwerpunkt Softwareentwicklung", styles['Normal'])],
        [Paragraph("• Full-Stack Zertifizierung", styles['Normal'])],
    ]
    edu_table = Table(education_data, colWidths=[18*cm])
    edu_table.setStyle(TableStyle([
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#f7fafc')),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
    ]))
    story.append(edu_table)
    story.append(Spacer(1, 0.6*cm))
    
    # === ZERTIFIZIERUNGEN ===
    story.append(Paragraph("🏆 Zertifizierungen (2023)", section_style))
    
    cert_topics = [
        "• Konzepte und Werkzeuge",
        "• Responsive Webdesign-Websites",
        "• JavaScript, Node.js, jQuery und jQuery Mobile",
        "• Angular, Vue.js, React",
        "• Apache Cordova",
        "• Progressive Web Apps (PWA)",
        "• Komplexere Web-Anwendungen"
    ]
    
    for topic in cert_topics:
        story.append(Paragraph(topic, styles['Normal']))
    
    story.append(Spacer(1, 0.6*cm))
    
    # === SPRACHEN ===
    story.append(Paragraph("🌍 Sprachen", section_style))
    
    languages = [
        ["Kurdisch", "Muttersprache"],
        ["Deutsch", "Fließend"],
        ["Arabisch", "Fließend"],
        ["Englisch", "Grundkenntnisse"]
    ]
    
    lang_table = Table(languages, colWidths=[9*cm, 9*cm])
    lang_table.setStyle(TableStyle([
        ('FONTNAME', (0, 0), (-1, -1), 'Helvetica'),
        ('FONTSIZE', (0, 0), (-1, -1), 10),
        ('LEFTPADDING', (0, 0), (-1, -1), 8),
        ('RIGHTPADDING', (0, 0), (-1, -1), 8),
        ('TOPPADDING', (0, 0), (-1, -1), 4),
        ('BOTTOMPADDING', (0, 0), (-1, -1), 4),
        ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
        ('TEXTCOLOR', (1, 0), (1, -1), colors.HexColor('#667eea')),
    ]))
    story.append(lang_table)
    story.append(Spacer(1, 0.6*cm))
    
    # === INTERESSEN ===
    story.append(Paragraph("❤️ Interessen", section_style))
    interests_text = "Open Source • Lesen • Wandern • Musik"
    story.append(Paragraph(interests_text, styles['Normal']))
    
    # Footer
    story.append(Spacer(1, 1*cm))
    footer_style = ParagraphStyle(
        'Footer',
        parent=styles['Normal'],
        fontSize=8,
        textColor=colors.HexColor('#a0aec0'),
        alignment=TA_CENTER
    )
    story.append(Paragraph("───────────────────────────────────", footer_style))
    story.append(Paragraph("Erstellt: Dezember 2025 | Mehr Informationen: je2700.github.io", footer_style))
    
    # PDF erstellen
    doc.build(story)
    print(f"✅ Lebenslauf erfolgreich erstellt: {output_file}")

if __name__ == "__main__":
    create_resume()
