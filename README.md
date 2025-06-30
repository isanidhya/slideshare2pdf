
# SlideShare2PDF 📄

A Python-based tool to download and convert SlideShare-like presentations into high-quality PDFs.

> 🚀 No login, no subscription — just paste the URL and download the presentation as a PDF!

---

## 🔧 Features

- ✅ Extracts **highest-quality** slide images using `srcset`
- ✅ Converts slides to a **PDF** using `Pillow`
- ✅ Supports both:
  - 🟢 **Online Mode**: Directly fetch slides from the webpage
  - 🔵 **Offline Mode**: Use previously downloaded images
- ✅ Organizes slides in correct numeric order
- ✅ CLI-based, no setup required beyond Python and pip

---

## 💻 Usage

### 🔹 Step 1: Clone the Repo

```bash
git clone https://github.com/yourusername/slideshare2pdf.git
cd slideshare2pdf
````

### 🔹 Step 2: Install Requirements

```bash
pip install -r requirements.txt
```

### 🔹 Step 3: Run the Script

```bash
python slideshare2pdf.py
```

You’ll be prompted to choose:

```
Enter 
online : 1
offline : 0
```

* **Online Mode (1)**: Enter the SlideShare URL, and it will extract + convert the slides.
* **Offline Mode (0)**: Enter the path to a folder containing slide images (e.g., `slide_1.jpg`, `slide_2.jpg`, ...)

---

## 📌 Requirements

* Python 3.6+
* Libraries:

  * `requests`
  * `beautifulsoup4`
  * `Pillow`
  * `tqdm`

Install all at once:

```bash
pip install requests beautifulsoup4 Pillow tqdm
```

---

## 📦 Coming Soon

* [x] CLI Mode
* [x] `.exe` for Windows (no Python required)
* [ ] Chrome Extension (1-click on SlideShare to download as PDF)
* [ ] Drag & Drop GUI

---

## 🧑‍💻 Author

**Sanidhya Sahu**

---

## 🛡️ License

This project is licensed under the [MIT License](LICENSE).

---

## 🙌 Support

Give this repo a ⭐ if you found it helpful!

