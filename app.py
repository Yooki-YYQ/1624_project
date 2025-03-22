from langflow.main import load_flow_from_json
from langflow.processing.process import process_file
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn
import os

# load flow
flow_path = "chatbot.flow.json"
flow = load_flow_from_json(flow_path)

# load Word
data_dir = "docs"
if os.path.exists(data_dir):
    for file in os.listdir(data_dir):
        file_path = os.path.join(data_dir, file)
        try:
            print(f"Loading: {file_path}")
            process_file(file_path)
        except Exception as e:
            print(f"Failed to load {file_path}: {e}")

# open API
app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def root():
    return """
    <h1>✅ Langflow Chatbot is Running!</h1>
    <p>Try it in the Hugging Face UI or deploy with custom UI.</p>
    """

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=7860)
