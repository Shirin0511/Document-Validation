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
