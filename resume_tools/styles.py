"""
PDF Style Configuration

Customize the appearance of your resume PDF by modifying the values below.
All sizes are in points (pt). Colors use hex format.

Inspired by style.css with professional green (#397249) theme.
"""

from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch

# ============================================================================
# COLORS
# ============================================================================

COLOR_NAME = HexColor('#397249')        # Green for name and section headers
COLOR_CONTACT = HexColor('#727272')     # Gray for contact info
COLOR_TEXT = HexColor('#000000')        # Black for body text

# ============================================================================
# MARGINS
# ============================================================================

MARGIN_TOP = 0.35 * inch
MARGIN_BOTTOM = 0.35 * inch
MARGIN_LEFT = 0.55 * inch
MARGIN_RIGHT = 0.55 * inch

# ============================================================================
# FONT SIZES
# ============================================================================

FONT_SIZE_NAME = 25              # Your name at the top
FONT_SIZE_CONTACT = 10           # Contact information
FONT_SIZE_SECTION_HEADER = 12    # Section headers (WORK EXPERIENCE, etc.)
FONT_SIZE_JOB_TITLE = 10         # Job titles and company names
FONT_SIZE_BODY = 9.5             # Bullet points and paragraphs

# ============================================================================
# LINE SPACING (LEADING)
# ============================================================================

LEADING_BODY = 11                # Line spacing for body text
LEADING_BULLET = 11              # Line spacing for bullet points

# ============================================================================
# VERTICAL SPACING
# ============================================================================

SPACE_AFTER_NAME = 6             # Space below name
SPACE_AFTER_CONTACT = 5          # Space below contact info
SPACE_BEFORE_SECTION = 3         # Space before section headers
SPACE_AFTER_SECTION = 1          # Space after section headers
SPACE_AFTER_JOB_TITLE = 1        # Space after job titles
SPACE_AFTER_BULLET = 0.5         # Space after each bullet point
SPACE_AFTER_PARAGRAPH = 0.5      # Space after paragraphs

SPACE_SECTION_DIVIDER = 0.03 * inch   # Extra space after section header
SPACE_EMPTY_LINE = 0.02 * inch        # Space for empty lines in markdown

# ============================================================================
# FONT FAMILIES
# ============================================================================

FONT_NAME_BOLD = 'Helvetica-Bold'
FONT_NAME_NORMAL = 'Helvetica'

# ============================================================================
# STYLE DEFINITIONS
# ============================================================================
# These are used internally by create_pdf.py - modify values above instead

def get_style_config():
    """
    Returns a dictionary of style configurations.
    Used by create_pdf.py to generate PDF styles.
    """
    return {
        'name': {
            'fontSize': FONT_SIZE_NAME,
            'textColor': COLOR_NAME,
            'spaceAfter': SPACE_AFTER_NAME,
            'fontName': FONT_NAME_BOLD,
        },
        'contact': {
            'fontSize': FONT_SIZE_CONTACT,
            'textColor': COLOR_CONTACT,
            'spaceAfter': SPACE_AFTER_CONTACT,
        },
        'section_header': {
            'fontSize': FONT_SIZE_SECTION_HEADER,
            'textColor': COLOR_NAME,
            'spaceAfter': SPACE_AFTER_SECTION,
            'spaceBefore': SPACE_BEFORE_SECTION,
            'fontName': FONT_NAME_BOLD,
        },
        'job_title': {
            'fontSize': FONT_SIZE_JOB_TITLE,
            'textColor': COLOR_TEXT,
            'spaceAfter': SPACE_AFTER_JOB_TITLE,
            'fontName': FONT_NAME_BOLD,
        },
        'body': {
            'fontSize': FONT_SIZE_BODY,
            'textColor': COLOR_TEXT,
            'leading': LEADING_BODY,
            'spaceAfter': SPACE_AFTER_PARAGRAPH,
        },
        'bullet': {
            'fontSize': FONT_SIZE_BODY,
            'textColor': COLOR_TEXT,
            'leading': LEADING_BULLET,
            'spaceAfter': SPACE_AFTER_BULLET,
        },
        'margins': {
            'topMargin': MARGIN_TOP,
            'bottomMargin': MARGIN_BOTTOM,
            'leftMargin': MARGIN_LEFT,
            'rightMargin': MARGIN_RIGHT,
        },
        'spacing': {
            'section_divider': SPACE_SECTION_DIVIDER,
            'empty_line': SPACE_EMPTY_LINE,
        }
    }
