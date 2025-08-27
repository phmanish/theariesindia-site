import sys, os, json
from pathlib import Path
import fitz  # PyMuPDF
from PIL import Image

PDF_PATH = "/Users/manish.parihar/Manish_Att/Aries India Profile.pdf"
OUT_IMG_DIR = Path("assets/img/company-profile")
OUT_TXT_DIR = Path("content/company-profile")
OUT_IMG_DIR.mkdir(parents=True, exist_ok=True)
OUT_TXT_DIR.mkdir(parents=True, exist_ok=True)

summary = {"pages": [], "images_saved": 0}

with fitz.open(PDF_PATH) as doc:
    for page_index in range(len(doc)):
        page = doc[page_index]
        text = page.get_text("text")
        txt_file = OUT_TXT_DIR / f"page-{page_index+1:02d}.txt"
        txt_file.write_text(text or "")
        page_info = {"page": page_index+1, "text_chars": len(text or ""), "images": []}
        # extract images
        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            pix = fitz.Pixmap(doc, xref)
            if pix.alpha:  # remove alpha if present
                pix = fitz.Pixmap(fitz.csRGB, pix)
            img_path = OUT_IMG_DIR / f"p{page_index+1:02d}_img{img_index+1:02d}.png"
            pix.save(str(img_path))
            page_info["images"].append(img_path.name)
            summary["images_saved"] += 1
        summary["pages"].append(page_info)

(Path("content/company-profile/summary.json")).write_text(json.dumps(summary, indent=2))
print(json.dumps(summary, indent=2))
