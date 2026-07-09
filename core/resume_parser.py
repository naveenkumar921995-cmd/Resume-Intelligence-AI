"""
===========================================================
Resume Intelligence AI
Resume Parser Module
Author : Naveen Kumar
Version : 5.0
===========================================================
"""

import os
import re
import pdfplumber
import docx


class ResumeParser:

    def __init__(self):
        pass

    # ---------------------------------------------
    # Detect File Type
    # ---------------------------------------------
    def parse(self, uploaded_file):

        filename = uploaded_file.name.lower()

        if filename.endswith(".pdf"):
            return self.extract_pdf(uploaded_file)

        elif filename.endswith(".docx"):
            return self.extract_docx(uploaded_file)

        else:
            raise ValueError("Unsupported File Format")

    # ---------------------------------------------
    # PDF Extraction
    # ---------------------------------------------
    def extract_pdf(self, uploaded_file):

        text = ""

        try:

            with pdfplumber.open(uploaded_file) as pdf:

                for page in pdf.pages:

                    extracted = page.extract_text()

                    if extracted:
                        text += extracted + "\n"

        except Exception as e:

            print(e)

        return text

    # ---------------------------------------------
    # DOCX Extraction
    # ---------------------------------------------
    def extract_docx(self, uploaded_file):

        text = ""

        try:

            doc = docx.Document(uploaded_file)

            for para in doc.paragraphs:

                text += para.text + "\n"

        except Exception as e:

            print(e)

        return text

    # ---------------------------------------------
    # Basic Cleaning
    # ---------------------------------------------
    def clean_text(self, text):

        text = text.lower()

        text = re.sub(r"\n", " ", text)

        text = re.sub(r"\t", " ", text)

        text = re.sub(r"\s+", " ", text)

        return text.strip()

    # ---------------------------------------------
    # Word Count
    # ---------------------------------------------
    def word_count(self, text):

        return len(text.split())

    # ---------------------------------------------
    # Character Count
    # ---------------------------------------------
    def character_count(self, text):

        return len(text)

    # ---------------------------------------------
    # Line Count
    # ---------------------------------------------
    def line_count(self, text):

        return len(text.split("\n"))

    # ---------------------------------------------
    # Email Extraction
    # ---------------------------------------------
    def extract_email(self, text):

        pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

        emails = re.findall(pattern, text)

        return emails[0] if emails else "Not Found"

    # ---------------------------------------------
    # Phone Number
    # ---------------------------------------------
    def extract_phone(self, text):

        pattern = r"(\+91[-\s]?)?[6-9]\d{9}"

        phones = re.findall(pattern, text)

        if phones:

            return phones[0]

        return "Not Found"

    # ---------------------------------------------
    # LinkedIn
    # ---------------------------------------------
    def extract_linkedin(self, text):

        pattern = r"(https?://)?(www\.)?linkedin\.com/in/[A-Za-z0-9_-]+"

        linkedin = re.findall(pattern, text)

        if linkedin:

            return "LinkedIn Found"

        return "Not Found"

    # ---------------------------------------------
    # GitHub
    # ---------------------------------------------
    def extract_github(self, text):

        pattern = r"(https?://)?(www\.)?github\.com/[A-Za-z0-9_-]+"

        github = re.findall(pattern, text)

        if github:

            return "GitHub Found"

        return "Not Found"

    # ---------------------------------------------
    # Portfolio
    # ---------------------------------------------
    def extract_portfolio(self, text):

        websites = re.findall(r'https?://\S+', text)

        return websites

    # ---------------------------------------------
    # Complete Analysis
    # ---------------------------------------------
    def analyze(self, uploaded_file):

        raw_text = self.parse(uploaded_file)

        clean = self.clean_text(raw_text)

        result = {

            "raw_text": raw_text,

            "clean_text": clean,

            "word_count": self.word_count(raw_text),

            "character_count": self.character_count(raw_text),

            "line_count": self.line_count(raw_text),

            "email": self.extract_email(raw_text),

            "phone": self.extract_phone(raw_text),

            "linkedin": self.extract_linkedin(raw_text),

            "github": self.extract_github(raw_text),

            "portfolio": self.extract_portfolio(raw_text)

        }

        return result