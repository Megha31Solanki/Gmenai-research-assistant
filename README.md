# Gmenai-research-assistant
# Smart Assistant for Research Summarization

## Setup Instructions

1. Clone this repo:
```bash
git clone <your_repo_url>
cd <your_repo_folder>
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Run backend:
```bash
uvicorn app:app --reload
```

4. Run frontend:
```bash
python interface/ui.py
```

## Architecture

- **Frontend**: Gradio-based UI
- **Backend**: FastAPI handling PDF parsing, summarization, question answering, and logic evaluation
- **Utils**:
  - `pdf_parser.py`: Parses PDF into text
  - `summarizer.py`: Summarizes the document
  - `qa_engine.py`: Answers questions using embeddings
  - `logic_generator.py`: Generates and evaluates logic-based questions

## Notes
- All responses are grounded in document content
- Challenge questions are logic-based and evaluated with feedback
