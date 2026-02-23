# ML Document Validation & Confidence Scoring Pipeline

An end-to-end intelligent document validation system for PAN and Aadhaar cards using OCR, rule-based validation, and weighted confidence scoring.

This project simulates a real-world KYC (Know Your Customer) workflow used in fintech and banking systems.

---

## Features

- OCR-based text extraction (Tesseract)
- Automatic document type detection (PAN vs Aadhaar)
- Field extraction (Name, DOB, ID number, Address)
- Rule-based validation engine
- Weighted confidence scoring system
- Automated decision engine:
  - AUTO_PASS
  - MANUAL_REVIEW
  - REJECT
- Modular and production-style architecture

---

## System Architecture

```

Document Image
     ↓
OCR (Tesseract)
     ↓
Document Type Detection
     ↓
Field Extraction
     ↓
Validation Engine
     ↓
Confidence Scoring
     ↓
Final Decision

```


---

## 🗂 Project Structure

```
## 🗂 Project Structure

Document_Validation_ML/
│
├── data/
│   ├── synthetic/             
│   │   ├── aadhaar/
│   │   └── pan/
│   │
│   └── processed/             
│       ├── aadhaar/
│       └── pan/
│
├── src/
│   │
│   ├── generate_documents.py  
│   ├── pdf_to_img.py          
│   ├── ocr_engine.py          
│   ├── document_detector.py   
│   ├── confidence_engine.py   
│   ├── main_pipeline.py       
│   ├── ocr_test.py            
│   │
│   └── validation/
│       ├── common_validation.py   
│       ├── pan_validation.py      
│       └── aadhar_validation.py  
│
├── requirements.txt

```
---

📊 Confidence Scoring Logic

Each document type uses weighted scoring.

PAN Weights

pan_valid → 0.50

name_valid → 0.30

dob_valid → 0.20

Aadhaar Weights

aadhaar_valid → 0.40

name_valid → 0.25

dob_valid → 0.20

address_valid → 0.15

Final Decision:

≥ 90% → AUTO_PASS

60% – 89% → MANUAL_REVIEW

< 60% → REJECT

🏦 Real-World Relevance

This system mimics real KYC validation pipelines used in:

Banking

Fintech

Loan underwriting

Identity verification systems

Key production concepts implemented:

Modular architecture

Separation of extraction and validation

Confidence-based routing

Fail-safe OCR handling

Document classification layer

🔮 Future Enhancements

Fraud detection heuristics

Batch processing

Streamlit UI

FastAPI deployment

Logging & audit trail system

👩‍💻 Author

Shirin Gupta
Data Scientist | ML Engineer

📌 Disclaimer

Synthetic documents were generated for testing purposes.
No real personal data is used in this project.


---

# 🎯 After adding this

1. Paste into `README.md`
2. Commit & push:

```bash
git add README.md
git commit -m "Added professional README"
git push

If you want, I can also:

Make a shorter version (clean & minimal)

Or make a more technical version (for serious ML audience)

Or add an architecture diagram image

Just tell me which style you prefer.

attached is how my project structure looks like, can u please update the readme's project structure part and provide me the updated version? 

Perfect 👌 thanks for sharing the structure — this looks clean and professional.

Below is the updated Project Structure section exactly matching your current folder layout.
You can replace only the "Project Structure" part in your README with this.

🗂 Updated Project Structure
## 🗂 Project Structure

Document_Validation_ML/
│
├── .venv/                     # Virtual environment (ignored in Git)
│
├── data/
│   ├── synthetic/             # Generated synthetic documents (PDFs)
│   │   ├── aadhaar/
│   │   └── pan/
│   │
│   └── processed/             # Converted PNG images for OCR testing
│       ├── aadhaar/
│       └── pan/
│
├── src/
│   │
│   ├── generate_documents.py  # Synthetic document generator
│   ├── pdf_to_img.py          # PDF → Image converter
│   ├── ocr_engine.py          # Tesseract OCR wrapper
│   ├── document_detector.py   # PAN vs Aadhaar classifier
│   ├── confidence_engine.py   # Weighted confidence scoring logic
│   ├── main_pipeline.py       # End-to-end validation pipeline
│   ├── ocr_test.py            # OCR testing utility
│   │
│   └── validation/
│       ├── common_validation.py   # Shared validation logic (name, dob, etc.)
│       ├── pan_validation.py      # PAN extraction & validation pipeline
│       └── aadhar_validation.py   # Aadhaar extraction & validation pipeline
│
├── requirements.txt
├── .gitignore
└── README.md


## 📊 Confidence Scoring Logic

Each document type uses weighted scoring.

### 🪪 PAN Weights
- **pan_valid** → 0.50  
- **name_valid** → 0.30  
- **dob_valid** → 0.20  

### 🆔 Aadhaar Weights
- **aadhaar_valid** → 0.40  
- **name_valid** → 0.25  
- **dob_valid** → 0.20  
- **address_valid** → 0.15  

### 🏁 Final Decision Logic
- **≥ 90%** → AUTO_PASS  
- **60% – 89%** → MANUAL_REVIEW  
- **< 60%** → REJECT  

---

## 🏦 Real-World Relevance

This system mimics real-world KYC validation pipelines used in:

- Banking  
- Fintech  
- Loan underwriting  
- Identity verification systems  

### 🔧 Key production concepts implemented
- Modular architecture  
- Separation of extraction and validation  
- Confidence-based routing  
- Fail-safe OCR handling  
- Document classification layer  

---

## 🔮 Future Enhancements

- Fraud detection heuristics  
- Batch processing support  
- Streamlit UI for document upload & validation  
- FastAPI deployment for real-time API usage  
- Logging & audit trail system  
