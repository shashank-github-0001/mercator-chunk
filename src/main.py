from semantic_text_splitter import TextSplitter
from tokenizers import Tokenizer
from typing import Dict, Literal
from fastapi import FastAPI
import os

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

    port = os.getenv("PORT")
    if port is None:
        print("no env variable")
    else:
        try:
            port = int(port)
        except ValueError:
            raise ValueError("please give a valid number as PORT")
        else:
            uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
