A simple Streamlit and LLM-based tool that transforms informal patient complaints into clear, formal medical language.  
It supports both Arabic and English while preserving the original language.

## Example

**Input:**
> My stomach is killing me and I feel like I'm gonna throw up.

**Output:**
> Patient reports severe abdominal pain accompanied by nausea.

## Requirements

- Python 3.10+
- Google Gemini API Key

## Deployment

The app is deployed using Streamlit Community Cloud.

### Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
