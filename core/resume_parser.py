"""
=========================================================
NEXUS AI
Enterprise Resume Parser
Version : 10.0 Enterprise
Author : Naveen Kumar
=========================================================
"""

import re
import pdfplumber
import docx


class ResumeParser:

    def extract_text(self, uploaded_file):

        if uploaded_file.name.endswith(".pdf"):

            text = ""

            with pdfplumber.open(uploaded_file) as pdf:

                for page in pdf.pages:
                    text += page.extract_text() or ""

            return text

        elif uploaded_file.name.endswith(".docx"):

            doc = docx.Document(uploaded_file)

            return "\n".join([p.text for p in doc.paragraphs])

        return ""

    # -------------------------------------------------

    def extract_email(self, text):

        m = re.search(r'[\w\.-]+@[\w\.-]+\.\w+', text)

        return m.group(0) if m else ""

    # -------------------------------------------------

    def extract_phone(self, text):

        m = re.search(r'(\+91[\-\s]?)?[6-9]\d{9}', text)

        return m.group(0) if m else ""

    # -------------------------------------------------

    def extract_linkedin(self, text):

        m = re.search(r'https?://(www\.)?linkedin\.com/\S+', text)

        return m.group(0) if m else ""

    # -------------------------------------------------

    def extract_github(self, text):

        m = re.search(r'https?://(www\.)?github\.com/\S+', text)

        return m.group(0) if m else ""

    # -------------------------------------------------

    def extract_skills(self, text):

        master = [

            "Python","SQL","Pandas","NumPy",

            "Machine Learning","Deep Learning",

            "TensorFlow","PyTorch","Power BI",

            "Excel","AWS","Azure","Docker",

            "Kubernetes","Git","Linux"

        ]

        found=[]

        lower=text.lower()

        for skill in master:

            if skill.lower() in lower:

                found.append(skill)

        return sorted(found)

    # -------------------------------------------------

    def extract_name(self,text):

        lines=text.split("\n")

        for line in lines[:5]:

            if len(line.split())<=4 and len(line)>3:

                return line.strip()

        return "Unknown"

    # -------------------------------------------------

    def reading_time(self,text):

        words=len(text.split())

        return round(words/200,1)

    # -------------------------------------------------

    def resume_score(self,text):

        score=50

        if self.extract_email(text):
            score+=10

        if self.extract_phone(text):
            score+=10

        if self.extract_linkedin(text):
            score+=5

        if self.extract_github(text):
            score+=5

        score+=min(len(self.extract_skills(text))*2,20)

        return min(score,100)

    # -------------------------------------------------

    def analyze(self,uploaded_file):

        text=self.extract_text(uploaded_file)

        return{

            "raw_text":text,

            "name":self.extract_name(text),

            "email":self.extract_email(text),

            "phone":self.extract_phone(text),

            "linkedin":self.extract_linkedin(text),

            "github":self.extract_github(text),

            "portfolio":[],

            "skills":self.extract_skills(text),

            "resume_score":self.resume_score(text),

            "reading_time":self.reading_time(text),

            "word_count":len(text.split()),

            "character_count":len(text),

            "line_count":len(text.splitlines())

        }