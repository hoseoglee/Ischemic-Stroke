
import markdown
from weasyprint import HTML
import sys
import re
import base64
import zlib

def convert_md_to_html_pdf(input_md, output_html, output_pdf):
    # Read Markdown
    with open(input_md, 'r', encoding='utf-8') as f:
        text = f.read()

    # Pre-process: Convert Mermaid to Images (Removed: Now using local assets)
    # text = mermaid_to_img(text)

    # Convert to HTML
    # Using 'extra' extension for tables, fences, etc.
    html_content = markdown.markdown(text, extensions=['extra', 'toc', 'tables'])

    # Add some basic CSS for styling
    styled_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
        <meta charset="utf-8">
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@400;700&display=swap');
            body {{ font-family: 'Noto Sans KR', sans-serif; line-height: 1.6; padding: 40px; max-width: 800px; margin: 0 auto; }}
            h1, h2, h3 {{ color: #2c3e50; font-weight: 700; }}
            h1 {{ border-bottom: 2px solid #2c3e50; padding-bottom: 10px; font-size: 2em; }}
            h2 {{ border-bottom: 1px solid #eee; padding-bottom: 5px; margin-top: 30px; font-size: 1.5em; }}
            table {{ border-collapse: collapse; width: 100%; margin: 20px 0; }}
            th, td {{ border: 1px solid #ddd; padding: 12px; text-align: left; }}
            th {{ background-color: #f2f2f2; font-weight: 700; }}
            blockquote {{ border-left: 4px solid #3498db; margin: 20px 0; padding-left: 20px; color: #555; background-color: #f0f7fb; padding: 15px; }}
            code {{ background-color: #f8f8f8; padding: 2px 5px; border-radius: 3px; font-family: monospace; }}
            pre {{ background-color: #f8f8f8; padding: 15px; border-radius: 5px; overflow-x: auto; }}
            img {{ max-width: 100%; height: auto; display: block; margin: 20px auto; border: 1px solid #ddd; border-radius: 5px; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

    # Write HTML
    with open(output_html, 'w', encoding='utf-8') as f:
        f.write(styled_html)
    print(f"Generated {output_html}")

    # Write PDF
    HTML(string=styled_html).write_pdf(output_pdf)
    print(f"Generated {output_pdf}")

if __name__ == "__main__":
    convert_md_to_html_pdf(
        "수도권_전원_전략_가이드.md", 
        "수도권_전원_전략_가이드.html", 
        "수도권_전원_전략_가이드.pdf"
    )
