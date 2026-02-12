# Resume

Professional resume with automated PDF generation tools.

## Overview

This repository contains my professional resume in multiple formats:
- **Markdown** (`Resume.md`) - Main resume source
- **HTML** (`Resume.html`) - Web-ready version
- **PDF** - Generated using the included tools

## Quick Start

### Generate PDF from Markdown

```bash
cd resume_tools
python create_pdf.py ../Resume.md ../Resume.pdf
```

### Install Dependencies

```bash
pip install -r resume_tools/requirements.txt
```

## Repository Structure

```
.
├── Resume.md                 # Main resume (markdown)
├── Resume.html              # HTML version
├── style.css                # Styling for HTML resume
├── resume_tools/            # PDF generation tools
│   ├── create_pdf.py        # CLI tool for PDF generation
│   ├── requirements.txt     # Python dependencies
│   └── README.md           # Tool documentation
├── custom_resumes/          # Tailored resumes (gitignored)
└── .gitignore
```

## Features

### Resume Tools

The `resume_tools/` directory contains a CLI tool for converting markdown resumes to professionally formatted PDFs:

- **One-page optimization** - Automatically fits content on a single page
- **Professional styling** - Green headers (#397249), clean layout
- **Offline usage** - Works completely offline once dependencies are installed
- **Easy CLI** - Simple command-line interface

See `resume_tools/README.md` for detailed usage instructions.

### Custom Resumes

The `custom_resumes/` folder (gitignored) is used for storing tailored versions of the resume for specific job applications. This keeps the main resume generic while allowing customization for different opportunities.

## Usage

### Creating a PDF

```bash
# Basic usage
python resume_tools/create_pdf.py Resume.md Resume.pdf

# Auto-generate output name
python resume_tools/create_pdf.py Resume.md
# Creates Resume.pdf

# From resume_tools directory
cd resume_tools
./create_pdf.py ../Resume.md
```

### Customizing for Job Applications

1. Create a tailored version in `custom_resumes/`:
   ```bash
   cp Resume.md custom_resumes/Resume_CompanyName.md
   ```

2. Edit the markdown file to emphasize relevant experience

3. Generate PDF:
   ```bash
   python resume_tools/create_pdf.py custom_resumes/Resume_CompanyName.md
   ```

## Styling

The PDF generator uses styling inspired by `style.css`:
- Name: 18pt, green (#397249), bold, centered
- Contact info: 10pt, gray (#727272), centered
- Section headers: 11pt, green, bold, uppercase
- Job titles: 10pt, bold
- Body text: 9pt

## Requirements

- Python 3.x
- reportlab (see `resume_tools/requirements.txt`)

## License

This resume and associated tools are for personal use.

---

**Keenan McConkey**
k.t.mcconkey@gmail.com | (415) 216-7605 | San Francisco, CA
