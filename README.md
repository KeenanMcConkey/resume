# Resume

Professional resume with automated PDF generation tools.

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

## Requirements

- Python 3.x
- reportlab (see `resume_tools/requirements.txt`)

## License

This resume and associated tools are for personal use.
