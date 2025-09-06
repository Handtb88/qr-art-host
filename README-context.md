## 🧠 Context for GitHub AI Assistant

### 🔹 Project Goal
Architect a **self-hosted, dynamic QR code redirect system** using GitHub Pages. The system should:
- Host placeholder QR code art
- Redirect scans to product URLs (e.g., Gumroad)
- Be modular, editable, and zero-cost
- Support future automation (e.g., QR generation from manifest)

---

### 🔹 Repo Details
- **Repo name**: `qr-art`
- **Owner**: `t`
- **Branch**: `main`
- **GitHub Pages**: Enabled via `main` branch, root folder
- **Live URL**: `https://t.github.io/qr-art/`

---

### 🔹 Required Files & Structure

```plaintext
qr-art/
├── index.html               # Optional landing page
├── redirect.html            # JS-based redirect handler
├── links.json               # Manifest of product IDs → target URLs
├── assets/
│   ├── qr-pack001.png       # Placeholder QR code image
│   ├── qr-pack001.svg       # Scalable vector version
├── templates/
│   ├── placeholder.svg      # Overlay panel design
│   └── qr-generator.py      # Script to generate QR + overlay
└── README.md                # Project documentation
```

---

### 🔹 Redirect Logic (redirect.html)

```html
<!DOCTYPE html>
<html>
<head>
  <meta charset="UTF-8">
  <title>Redirecting...</title>
  <script>
    const params = new URLSearchParams(window.location.search);
    const target = params.get("to");
    if (target) {
      window.location.href = decodeURIComponent(target);
    } else {
      document.body.innerHTML = "<h1>No redirect target provided.</h1>";
    }
  </script>
</head>
<body></body>
</html>
```

**Example QR embed URL**:
```
https://t.github.io/qr-art/redirect.html?to=https%3A%2F%2Fgumroad.com%2Fl%2Fpack001
```

---

### 🔹 Manifest Format (links.json)

```json
{
  "pack001": "https://gumroad.com/l/pack001",
  "pack002": "https://gumroad.com/l/pack002"
}
```

---

### 🔹 QR Generator Requirements

- Read from `links.json`
- Generate QR codes with embedded redirect URLs
- Overlay placeholder panel (SVG or PNG)
- Save to `/assets` folder
- Output both PNG and SVG formats
- Use high error correction (level H)
- Center panel size: ~26% of QR canvas
- Optional: Add text label or logo in overlay

---

### 🔹 Automation Goals

- GitHub Actions or Make/Zapier flow to:
  - Auto-generate QR codes when `links.json` updates
  - Push new assets to `/assets`
- Future: Allow buyers to remix overlay panels while keeping QR intact

---

### 🔹 User Profile (Mike)

- Expert in reverse-engineering workflows, QR systems, and automation
- Building modular asset packs for Gumroad
- Wants scalable, editable QR code art with dynamic redirects
- Prefers zero-cost, frictionless hosting
- Values transparency, modularity, and buyer autonomy
