import gradio as gr
import requests

backend_url = "http://localhost:8000"

def upload_doc(file):
    response = requests.post(f"{backend_url}/upload", files={"file": file})
    return response.json()["summary"]

def ask_anything(q):
    res = requests.post(f"{backend_url}/ask", json={"query": q})
    return res.json()["answer"] + "\n\n" + res.json()["justification"]

def challenge():
    res = requests.get(f"{backend_url}/challenge")
    return res.json()["questions"]

def evaluate(ans1, ans2, ans3):
    data = {"answers": [ans1, ans2, ans3]}
    res = requests.post(f"{backend_url}/evaluate", json=data)
    return res.json()["feedback"]

doc = gr.File()
sum_output = gr.Textbox()
question = gr.Textbox()
answer = gr.Textbox()
q1, q2, q3 = gr.Textbox(), gr.Textbox(), gr.Textbox()
eval_output = gr.Textbox()

demo = gr.Blocks()
with demo:
    gr.Markdown("## Smart Assistant for Research Summarization")
    doc.upload(upload_doc, inputs=doc, outputs=sum_output, label="Upload Document")
    question.submit(ask_anything, inputs=question, outputs=answer, label="Ask Anything")
    gr.Button("Challenge Me").click(challenge, outputs=[q1, q2, q3])
    gr.Button("Submit Answers").click(evaluate, inputs=[q1, q2, q3], outputs=eval_output)

demo.launch()
