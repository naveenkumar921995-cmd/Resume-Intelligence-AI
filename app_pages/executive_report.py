I reviewed your current `executive_report.py`. 

Right now it's only generating a **hard-coded sample PDF**. It doesn't use your upgraded ATS, Similarity, ML, DL, or `HiringScoreEngine`.

I recommend replacing the entire file with this version.

---

## `app_pages/executive_report.py` (Replace Entire File)

```python
"""
=========================================================
NEXUS AI
Enterprise Executive Report
Version : 11.0 Enterprise
Author : Naveen Kumar
=========================================================
"""

import streamlit as st

from core.report_generator import ReportGenerator
from core.hiring_score import HiringScoreEngine


def executive_report_page():

    st.title("📑 Executive AI Report")

    st.markdown(
        "Generate a complete AI-powered executive hiring report."
   
```
