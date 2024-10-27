from semantic_text_splitter import TextSplitter
from tokenizers import Tokenizer
from typing import Dict
from fastapi import FastAPI

app = FastAPI()

@app.post("/")
async def main(full_string: str) -> Dict[str, str]:
  max_tokens = 50
  tokenizer = Tokenizer.from_pretrained("bert-base-uncased")
  splitter = TextSplitter.from_huggingface_tokenizer(tokenizer, max_tokens)
  chunks = splitter.chunks(full_string)

  return_chunks = dict()

  for i, chunk in enumerate(chunks):
    return_chunks[f"chunk: {i}"] = chunk

  print(return_chunks)

  return return_chunks 

if __name__ == "__main__":
  import uvicorn
  uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
