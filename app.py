from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
from utils.pdf_parser import parse_document
from utils.summarizer import summarize_text
from utils.qa_engine import answer_question
from utils.logic_generator import generate_questions, evaluate_answers

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

cache = {"content": ""}

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    content = await parse_document(file)
    cache["content"] = content
    summary = summarize_text(content)
    return {"summary": summary}

@app.post("/ask")
async def ask_question(query: str):
    answer, ref = answer_question(cache["content"], query)
    return {"answer": answer, "justification": ref}

@app.get("/challenge")
def challenge():
    questions = generate_questions(cache["content"])
    return {"questions": questions}

@app.post("/evaluate")
def evaluate(data: dict):
    user_answers = data.get("answers", [])
    feedback = evaluate_answers(cache["content"], user_answers)
    return {"feedback": feedback}
