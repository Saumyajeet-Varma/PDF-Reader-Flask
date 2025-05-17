# PDF-Raeder-Flask

A simple web application built with **Flask** and **pdfplumber** that allows users to upload a PDF file and extract its text content. The extracted text is then displayed in the browser for easy reading or copy-pasting.

## Tech Stack

- **Frontend**: HTML, Tailwind CSS
- **Backend**: Python, Flask
- **PDF Parsing**: pdfplumber

## Directory Structure

```md
Directory structure:
└── saumyajeet-varma-pdf-reader-flask/
    ├── README.md
    ├── main.py
    ├── requirements.txt
    ├── static/
    │   ├── scripts/
    │   │   └── script.js
    │   └── uploads/
    │       └── .gitkeep
    └── templates/
        ├── index.html
        └── result.html
```


## 📦 Installation

### 1. Clone the repository
```bash
git clone https://github.com/your-username/pdf-text-extractor.git
cd pdf-text-extractor
```

### 2. Create a virtual environment
```bash
python -m venv .venv
.venv/Scripts/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run the App
```bash
python main.py
```

> Then visit http://127.0.0.1:5000 in your browser.

## Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.