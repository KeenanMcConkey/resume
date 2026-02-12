#!/usr/bin/env python3
"""
Resume PDF Generator
Converts markdown resumes to professionally formatted one-page PDFs.
Uses styling inspired by style.css with green headers and clean layout.

Usage:
    python create_pdf.py input.md output.pdf
    python create_pdf.py input.md  (outputs to input.pdf)
"""

import sys
import os
import re
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import inch
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer
from reportlab.lib.colors import HexColor


def create_resume_pdf(input_md, output_pdf):
    """Create a one-page resume PDF from markdown content."""

    # Read markdown file
    if not os.path.exists(input_md):
        print(f"Error: Input file '{input_md}' not found")
        sys.exit(1)

    with open(input_md, 'r') as f:
        content = f.read()

    # Set up PDF with balanced margins
    doc = SimpleDocTemplate(
        output_pdf,
        pagesize=letter,
        topMargin=0.35*inch,
        bottomMargin=0.35*inch,
        leftMargin=0.55*inch,
        rightMargin=0.55*inch
    )

    # Define custom styles
    styles = getSampleStyleSheet()

    # Header/Name style - inspired by style.css
    styles.add(ParagraphStyle(
        name='Name',
        parent=styles['Heading1'],
        fontSize=18,
        textColor=HexColor('#397249'),  # Green from style.css
        spaceAfter=1,
        alignment=TA_CENTER,
        fontName='Helvetica-Bold'
    ))

    # Contact info style - inspired by style.css h5
    styles.add(ParagraphStyle(
        name='Contact',
        parent=styles['Normal'],
        fontSize=10,
        textColor=HexColor('#727272'),  # Gray from style.css
        spaceAfter=5,
        alignment=TA_CENTER
    ))

    # Section header style - inspired by style.css h2
    styles.add(ParagraphStyle(
        name='SectionHeader',
        parent=styles['Heading2'],
        fontSize=11,
        textColor=HexColor('#397249'),  # Green from style.css
        spaceAfter=1,
        spaceBefore=3,
        fontName='Helvetica-Bold',
        borderWidth=0,
        borderColor=HexColor('#000000'),
        borderPadding=0,
        borderRadius=0
    ))

    # Job title style
    styles.add(ParagraphStyle(
        name='JobTitle',
        parent=styles['Normal'],
        fontSize=10,
        textColor=HexColor('#000000'),
        spaceAfter=1,
        fontName='Helvetica-Bold'
    ))

    # Regular text style - inspired by style.css body
    styles.add(ParagraphStyle(
        name='ResumeBody',
        parent=styles['Normal'],
        fontSize=9,
        textColor=HexColor('#000000'),
        leading=11,
        spaceAfter=0.5
    ))

    # Bullet point style - inspired by style.css body
    styles.add(ParagraphStyle(
        name='ResumeBullet',
        parent=styles['Normal'],
        fontSize=9,
        textColor=HexColor('#000000'),
        leading=11,
        leftIndent=0,
        spaceAfter=0.5
    ))

    # Build story
    story = []

    # Parse markdown content
    lines = content.split('\n')
    i = 0

    while i < len(lines):
        line = lines[i].strip()

        # Skip YAML frontmatter
        if line.startswith('---'):
            i += 1
            while i < len(lines) and not lines[i].strip().startswith('---'):
                if lines[i].strip().startswith('title:'):
                    name = lines[i].strip().replace('title:', '').strip()
                    story.append(Paragraph(name, styles['Name']))
                i += 1
            i += 1
            continue

        # Contact info (##### format)
        if line.startswith('#####'):
            contact = line.replace('#####', '').strip()
            story.append(Paragraph(contact, styles['Contact']))

        # Section headers (##)
        elif line.startswith('## '):
            section_name = line.replace('##', '').strip()
            # Add section header
            story.append(Paragraph(f'<b>{section_name.upper()}</b>', styles['SectionHeader']))
            story.append(Spacer(1, 0.03*inch))

        # Job titles (###)
        elif line.startswith('### '):
            job_line = line.replace('###', '').strip()
            # Parse markdown links
            job_line = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'<i>\1</i>', job_line)
            story.append(Paragraph(f'<b>{job_line}</b>', styles['JobTitle']))

        # Bullet points
        elif line.startswith('- '):
            bullet_text = line[2:].strip()
            # Convert markdown links to plain text with italics for company names
            bullet_text = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'<i>\1</i>', bullet_text)
            story.append(Paragraph(f'• {bullet_text}', styles['ResumeBullet']))

        # Regular paragraphs
        elif line and not line.startswith('#'):
            # Convert markdown links
            line = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'<i>\1</i>', line)
            # Bold text
            line = re.sub(r'\*\*([^\*]+)\*\*', r'<b>\1</b>', line)
            story.append(Paragraph(line, styles['ResumeBody']))

        # Empty lines - minimal spacing
        elif not line:
            story.append(Spacer(1, 0.02*inch))

        i += 1

    # Build PDF
    doc.build(story)
    print(f"✓ PDF created successfully: {output_pdf}")


def main():
    """Main CLI entry point."""
    if len(sys.argv) < 2:
        print(__doc__)
        print("\nExamples:")
        print("  python create_pdf.py Resume.md Resume.pdf")
        print("  python create_pdf.py Resume.md")
        sys.exit(1)

    input_md = sys.argv[1]

    # If output not specified, use input filename with .pdf extension
    if len(sys.argv) > 2:
        output_pdf = sys.argv[2]
    else:
        output_pdf = os.path.splitext(input_md)[0] + '.pdf'

    create_resume_pdf(input_md, output_pdf)


if __name__ == "__main__":
    main()
