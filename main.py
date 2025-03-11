from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from gpt_docs import work_ai

app = FastAPI(
    title='DocGPT API2',
    redoc_url=None,
    # lifespan=lifespan
)

# Модель данных для входящего запроса
class MessageRequest(BaseModel):
    chat_id: int
    msg: str

# Роут для обработки запроса
@app.post("/process")
async def process_message(data: MessageRequest):
    try:
        # Вызываем функцию work_ai с полученными данными
        result = work_ai(data.chat_id, data.msg)
        return result
    except Exception as e:
        return {"chat_id": f"{data.chat_id}", "answer": f"Ошибка: {e}"}
        #raise HTTPException(status_code=500, detail=str(e))
