import json
import qrcode
import svgwrite
from PIL import Image

# CONFIG
LINKS_FILE = '../links.json'
ASSETS_DIR = '../assets/'
OVERLAY_SVG = 'placeholder.svg'
ERROR_CORRECTION = qrcode.constants.ERROR_CORRECT_H
QR_SIZE = 512
CENTER_PANEL_RATIO = 0.26

def load_links():
    with open(LINKS_FILE, 'r') as f:
        return json.load(f)

def make_qr(url, box_size, border):
    qr = qrcode.QRCode(
        version=1,
        error_correction=ERROR_CORRECTION,
        box_size=box_size,
        border=border,
    )
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white").convert('RGBA')
    return img

def overlay_panel_png(qr_img, panel_path):
    panel = Image.open(panel_path).convert('RGBA')
    size = int(CENTER_PANEL_RATIO * qr_img.size[0])
    panel = panel.resize((size, size), Image.ANTIALIAS)
    x = (qr_img.size[0] - size) // 2
    y = (qr_img.size[1] - size) // 2
    qr_img.paste(panel, (x, y), panel)
    return qr_img

def overlay_panel_svg(qr_svg, panel_svg_path):
    # Naive SVG overlay: embed panel SVG centered
    panel_svg = open(panel_svg_path, 'r').read()
    qr_svg.embed(panel_svg, insert=(QR_SIZE*(1-CENTER_PANEL_RATIO)/2, QR_SIZE*(1-CENTER_PANEL_RATIO)/2))
    return qr_svg

def gen_all():
    links = load_links()
    for pid, target in links.items():
        qr_url = f'https://t.github.io/qr-art/redirect.html?to={target}'
        # PNG QR
        img = make_qr(qr_url, box_size=10, border=4)
        img_overlay = overlay_panel_png(img, OVERLAY_SVG)
        img_overlay.save(f"{ASSETS_DIR}qr-{pid}.png")
        # SVG QR
        qr_svg = qrcode.make(qr_url, image_factory=qrcode.image.svg.SvgImage)
        qr_svg.save(f"{ASSETS_DIR}qr-{pid}.svg")
        # TODO: SVG overlay - more advanced SVG composition can be added here.

if __name__ == "__main__":
    gen_all()
