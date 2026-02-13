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
│   ├── create_pdf.py            # Main PDF generator
│   ├── styles.py                # Customizable styling configuration
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
- Name: 25pt, green (#397249), bold, centered
- Contact info: 10pt, gray (#727272), centered
- Section headers: 12pt, green, bold, uppercase
- Job titles: 10pt, bold
- Body text: 9.5pt

### Customizing Styles

All styling is controlled by `styles.py`. To customize your PDF appearance:

1. Open `styles.py` in a text editor
2. Modify the values at the top of the file:

```python
# Example: Make your name larger
FONT_SIZE_NAME = 28              # Default: 25

# Example: Change colors
COLOR_NAME = HexColor('#0066CC')  # Default: #397249 (green)

# Example: Adjust margins
MARGIN_TOP = 0.5 * inch          # Default: 0.35
```

3. Save the file and regenerate your PDF

**Common customizations:**
- **Font sizes**: Adjust `FONT_SIZE_*` values (in points)
- **Colors**: Change `COLOR_*` values (hex format: `#RRGGBB`)
- **Spacing**: Modify `SPACE_*` and `MARGIN_*` values
- **Line height**: Adjust `LEADING_*` values

See `styles.py` for all available settings and detailed comments.

## Troubleshooting

If you get "command not found":
- Make sure Python 3 is installed: `python3 --version`
- Use `python3` instead of `python` if needed

If fonts look wrong:
- The script uses Helvetica (built into ReportLab)
- No additional fonts need to be installed
