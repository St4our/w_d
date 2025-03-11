# from langdetect import detect
# from transformers import pipeline, BitsAndBytesConfig

# import torch
# print(torch.cuda.is_available()) 
# print(torch.cuda.get_device_name(0))

# def what_lang(msg):
#     language = detect(msg)
#     print(f"Определенный язык: {language}")
#     return language


# def work_ai(chat_id, msg):
#     language = what_lang(msg)
#     quest = f"Ты — юрист и полезный AI-помощник. Отвечай исключительно на {language} языке.\n"+ f'{msg}'
#     messages = quest
#     # messages = [
#     #     {"role": "user", "content": quest},
#     # ]
#     #pipe = pipeline("text-generation", model="deepseek-ai/DeepSeek-R1", trust_remote_code=True, return_full_text=False,)
#      # Загрузка модели с квантованием
#     bnb_config = BitsAndBytesConfig(
#         load_in_4bit=True,
#         bnb_4bit_quant_type="nf4",
#         bnb_4bit_compute_dtype=torch.float16
#     )
#     pipe = pipeline(
#         "text-generation",
#         model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",  # или microsoft/phi-2
#         device_map="auto",
#         quantization_config=bnb_config,
#         torch_dtype=torch.float16
#     )
#     answer = pipe(messages, pad_token_id=pipe.tokenizer.eos_token_id) 

#     #answer = pipe[0]['generated_text'].strip()
#     print('\n\n', answer)
#     answer = {"chat_id": chat_id, "answer": answer}
#     return answer

# chat_id= 123
# msg = f"Кто ты?"
# work_ai(chat_id, msg)


from langdetect import detect
from transformers import pipeline
import torch

def translate(msg, lang):
    msg = msg.replace("\n", "")
    print('----------\nTake:', msg, '\n--------------')
    # prompt = f"Сохрани смысл текста и переведи на {lang} язык текст: {msg}"
    prompt = f"Переведи на {lang} язык текст: {msg}"
    messages = [
        {"role": "user", "content": prompt},
    ]
    pipe = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0")
    answer = pipe(messages, 
                    return_full_text=False, 
                    pad_token_id=pipe.tokenizer.eos_token_id) 
    print('------\nне обработанный текст:\n', answer)
    answer = answer[0]['generated_text']#.strip()
    print('-----\nобработанный текст:\n', answer,'\n-----')
    return answer

def work_ai(chat_id, msg):
    language_first = detect(msg)
    prompt = f"Твоя роль и задача: Ты — юрист и полезный AI-помощник, "
    prompt += f"отвечай однозначно на {language_first} языке.\nДай ответ на:\n{msg}"
    prompt += f""
    messages = [
        {"role": "user", "content": prompt},
    ]
    pipe = pipeline("text-generation", model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",)
    answer = pipe(messages, 
                    return_full_text=False, 
                    pad_token_id=pipe.tokenizer.eos_token_id) 
    answer = answer[0]['generated_text'].strip()
    print('\n\nПервый текст:', answer)
    print('\n-----------------------')
    language = detect(answer)

    if language_first == language:
        answer = {"chat_id": chat_id, "answer": answer}
        return answer
    else:
        answer = translate(answer, language_first)
        return answer
    # pipe = pipeline(
    #     "text-generation",
    #     model="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    #     device_map="auto",
    #     torch_dtype=torch.float16
    # )
    
    # answer = pipe(prompt, max_new_tokens=100)[0]['generated_text']
    # return {"chat_id": chat_id, "answer": answer}

# f = work_ai(123, "Сколько будет 3+3")
# print(f)