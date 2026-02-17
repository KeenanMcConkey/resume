#!/usr/bin/env python3
"""
Resume PDF Generator
Converts markdown resumes to professionally formatted one-page PDFs.
Uses styling inspired by style.css with green headers and clean layout.

Usage:
    python create_pdf.py input.md output.pdf
    python create_pdf.py input.md  (outputs to input.pdf)

Customize styling by editing styles.py
"""

import sys
import os
import re
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer

# Import style configuration
try:
    from styles import get_style_config
except ImportError:
    print("Error: styles.py not found. Make sure it's in the same directory as create_pdf.py")
    sys.exit(1)


def create_resume_pdf(input_md, output_pdf):
    """Create a one-page resume PDF from markdown content."""

    # Read markdown file
    if not os.path.exists(input_md):
        print(f"Error: Input file '{input_md}' not found")
        sys.exit(1)

    with open(input_md, 'r') as f:
        content = f.read()

    # Load style configuration
    style_config = get_style_config()
    margins = style_config['margins']
    spacing = style_config['spacing']

    # Set up PDF with configured margins
    doc = SimpleDocTemplate(
        output_pdf,
        pagesize=letter,
        topMargin=margins['topMargin'],
        bottomMargin=margins['bottomMargin'],
        leftMargin=margins['leftMargin'],
        rightMargin=margins['rightMargin']
    )

    # Define custom styles from configuration
    styles = getSampleStyleSheet()

    # Header/Name style
    name_config = style_config['name']
    styles.add(ParagraphStyle(
        name='Name',
        parent=styles['Heading1'],
        fontSize=name_config['fontSize'],
        textColor=name_config['textColor'],
        spaceAfter=name_config['spaceAfter'],
        alignment=TA_CENTER,
        fontName=name_config['fontName']
    ))

    # Contact info style
    contact_config = style_config['contact']
    styles.add(ParagraphStyle(
        name='Contact',
        parent=styles['Normal'],
        fontSize=contact_config['fontSize'],
        textColor=contact_config['textColor'],
        spaceAfter=contact_config['spaceAfter'],
        alignment=TA_CENTER
    ))

    # Section header style
    section_config = style_config['section_header']
    styles.add(ParagraphStyle(
        name='SectionHeader',
        parent=styles['Heading2'],
        fontSize=section_config['fontSize'],
        textColor=section_config['textColor'],
        spaceAfter=section_config['spaceAfter'],
        spaceBefore=section_config['spaceBefore'],
        fontName=section_config['fontName'],
        borderWidth=0,
        borderColor=section_config['textColor'],
        borderPadding=0,
        borderRadius=0
    ))

    # Job title style
    job_config = style_config['job_title']
    styles.add(ParagraphStyle(
        name='JobTitle',
        parent=styles['Normal'],
        fontSize=job_config['fontSize'],
        textColor=job_config['textColor'],
        spaceAfter=job_config['spaceAfter'],
        fontName=job_config['fontName']
    ))

    # Regular text style
    body_config = style_config['body']
    styles.add(ParagraphStyle(
        name='ResumeBody',
        parent=styles['Normal'],
        fontSize=body_config['fontSize'],
        textColor=body_config['textColor'],
        leading=body_config['leading'],
        spaceAfter=body_config['spaceAfter']
    ))

    # Bullet point style
    bullet_config = style_config['bullet']
    styles.add(ParagraphStyle(
        name='ResumeBullet',
        parent=styles['Normal'],
        fontSize=bullet_config['fontSize'],
        textColor=bullet_config['textColor'],
        leading=bullet_config['leading'],
        leftIndent=0,
        spaceAfter=bullet_config['spaceAfter']
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
            contact = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'<a href="\2">\1</a>', contact)
            story.append(Paragraph(contact, styles['Contact']))

        # Section headers (##)
        elif line.startswith('## '):
            section_name = line.replace('##', '').strip()
            # Add section header
            story.append(Paragraph(f'<b>{section_name.upper()}</b>', styles['SectionHeader']))
            story.append(Spacer(1, spacing['section_divider']))

        # Job titles (###)
        elif line.startswith('### '):
            job_line = line.replace('###', '').strip()
            # Parse markdown links
            job_line = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'<a href="\2">\1</a>', job_line)
            story.append(Paragraph(f'<b>{job_line}</b>', styles['JobTitle']))

        # Bullet points
        elif line.startswith('- '):
            bullet_text = line[2:].strip()
            # Convert markdown links to plain text with italics for company names
            bullet_text = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'<a href="\2">\1</a>', bullet_text)
            story.append(Paragraph(f'• {bullet_text}', styles['ResumeBullet']))

        # Regular paragraphs
        elif line and not line.startswith('#'):
            # Convert markdown links
            line = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'<a href="\2">\1</a>', line)
            # Bold text
            line = re.sub(r'\*\*([^\*]+)\*\*', r'<b>\1</b>', line)
            story.append(Paragraph(line, styles['ResumeBody']))

        # Empty lines - minimal spacing
        elif not line:
            story.append(Spacer(1, spacing['empty_line']))

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
