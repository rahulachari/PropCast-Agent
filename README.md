# 🏗️ WallCraft — Lokesh Precast Walls

> A premium, single-file business website for **Lokesh Precast Walls** — a precast compound wall manufacturer and architectural concrete supplier based in India.

🌐 **Live Demo:** [https://glittery-selkie-dcfb25.netlify.app/](https://glittery-selkie-dcfb25.netlify.app/)

---

## 🚀 About the Project

**WallCraft** is a fully responsive, zero-dependency business website designed and built for Lokesh Mudaliar (B.Arch), founder of Lokesh Precast Walls. The goal was to give the business a strong online presence — professional enough to attract contractors, builders, and developers, while being simple enough to host anywhere without a backend.

The entire site lives in **one HTML file** — no frameworks, no build tools, no npm install. Just open it in a browser and it works.

---

## ✨ Features

### 🎨 Visual Design
- Custom animated cursor with hover state feedback
- Full-screen parallax hero with animated grid lines and scanning effect
- Smooth scroll-triggered reveal animations (CSS `@keyframes` + IntersectionObserver)
- Auto-scrolling ticker banner with key business highlights
- Dark/light section alternation for visual rhythm
- Responsive layout down to mobile (375px)

### 🧱 Interactive Wall Builder (Canvas)
- Click-to-place compound wall panels, RCC pillars, and gate openings on a grid
- Right-click or erase tool to remove elements
- Click-drag to draw walls in a single stroke
- Live stats: panel count, pillar count, gate count, % coverage
- ⚡ Auto-fill boundary button that fills the plot perimeter
- "Get This Quote" button triggers the contact form

### 📐 Smart Project Estimator (Calculator)
- Input: plot length (ft), width (ft), wall height, product type, number of gates
- Output: perimeter, area, estimated unit count with a detailed note
- Supports: Compound Walls, Cement Tiles, Paver Blocks
- One-click redirect to the contact/quote form

### 🗂️ Product Showcase
Six product cards with full specifications:
| Product | Details |
|---|---|
| Compound Walls | 4–7 ft heights, 8 ft panels, M25/M30 grade |
| Cement Tiles | 12×12 to 24×24, multiple finishes |
| RCC Pillars | 5–8 ft, Fe500 TMT steel |
| Precast Slabs | 8–20 ft span, up to 5 kN/m² load |
| Paver Blocks | Zigzag / Brick / Hex, 60–80 mm |
| Custom Precast | Designed by Lokesh B.Arch, 7–14 day lead time |

### 📍 Location & Contact
- Embedded Google Maps iframe
- WhatsApp direct link with pre-filled message
- Contact form with name, phone, email, product interest, and project details fields
- "Send on WhatsApp" button opens a prefilled WhatsApp message

### 🖼️ Gallery
- Horizontal drag-to-scroll photo gallery
- 6 categorised project photos (Production, Installation, Structure, Architecture, Completed, Detail)

---

## 🛠️ Tech Stack

- HTML5
- CSS3 (custom properties, Grid, Flexbox, animations)
- Vanilla JavaScript (Canvas API, IntersectionObserver, scroll events)
- Google Fonts — Bebas Neue, DM Sans, Space Mono
- Google Maps embed
- Netlify (hosting)

**Zero dependencies. No npm. No build step.**

---

## ⚙️ How to Run

No installation required.

```bash
# Clone the repo
git clone https://github.com/rahulachari/PROJECT-LOKESH.git

# Open in browser
open lokesh_precast_FINAL_v4.html
```

Or just double-click the file. That's it.

---

## 🌐 Deployment

Deployed on **Netlify** via drag-and-drop:

1. Go to [netlify.com](https://netlify.com)
2. Drag the `.html` file onto the deploy area
3. Done — live in under 30 seconds

Since it's a single file, no build configuration is needed.

---

## 🔮 Potential Improvements

- [ ] Backend form submission (Formspree / EmailJS integration)
- [ ] Replace placeholder Unsplash images with real factory photos
- [ ] Add WhatsApp Business API for automated quote responses
- [ ] SEO meta tags + Open Graph for social sharing
- [ ] Add more product SKUs and a price list section
- [ ] Progressive Web App (PWA) for offline access

---

## 👤 About the Client

**Lokesh Mudaliar** is a qualified architect (B.Arch) and founder of Lokesh Precast Walls. His factory produces RCC compound walls, cement tiles, paver blocks, precast slabs, and custom architectural concrete elements. The business serves residential, commercial, and industrial clients across the region.

---

## 👨‍💻 Built By

**Rahul Achari** — Frontend Developer  
[GitHub](https://github.com/rahulachari) · [LinkedIn](https://www.linkedin.com/in/rahulyc/)

---

## 📄 License

MIT — free to fork, adapt, and use as a template for other business websites.
