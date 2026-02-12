# Resume PDF Generator

A simple tool to convert markdown resumes into professionally formatted one-page PDFs with green headers and clean styling.

## Folder Structure

```
Resume/
├── Resume.md                    # Your main resume (version controlled)
├── custom_resumes/              # Tailored resumes (gitignored)
│   ├── Resume_Apple_CICD.md
│   ├── Resume_Apple_FullStack.md
│   └── *.pdf
├── resume_tools/                # This folder
│   ├── create_pdf.py
│   ├── requirements.txt
│   └── README.md
└── .gitignore                   # Ignores custom_resumes/
```

## Installation

Install dependencies:
```bash
pip install -r requirements.txt
```

Or install reportlab directly:
```bash
pip install reportlab
```

## Usage

### Basic usage:
```bash
python create_pdf.py Resume.md Resume.pdf
```

### Auto-generate output filename:
```bash
python create_pdf.py Resume.md
# Creates Resume.pdf
```

### Make it executable (optional):
```bash
chmod +x create_pdf.py
./create_pdf.py Resume.md Resume.pdf
```

### Working with custom resumes:
```bash
# Create tailored resume PDF
python create_pdf.py ../custom_resumes/Resume_Apple_FullStack.md ../custom_resumes/Resume_Apple_FullStack.pdf

# Or from the Resume root directory:
cd /path/to/Resume
python resume_tools/create_pdf.py custom_resumes/Resume_Apple_FullStack.md
```

## Features

- **One-page optimization**: Automatically formatted to fit on a single page
- **Professional styling**: Green headers (#397249), gray contact info (#727272)
- **Markdown support**: Converts markdown links, bold text, and bullet points
- **Clean layout**: Balanced margins and consistent spacing

## Styling

The PDF uses styling inspired by `style.css`:
- Name: 18pt, green, bold, centered
- Contact info: 10pt, gray, centered
- Section headers: 11pt, green, bold, uppercase
- Job titles: 10pt, bold
- Body text: 9pt

## Troubleshooting

If you get "command not found":
- Make sure Python 3 is installed: `python3 --version`
- Use `python3` instead of `python` if needed

If fonts look wrong:
- The script uses Helvetica (built into ReportLab)
- No additional fonts need to be installed
