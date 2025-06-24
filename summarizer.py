def summarize_text(text):
    from transformers import pipeline
    summarizer = pipeline("summarization")
    summary = summarizer(text[:1000])[0]['summary_text']
    return summary
