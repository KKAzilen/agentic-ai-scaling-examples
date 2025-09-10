import redis, hashlib
from openai import OpenAI

client = OpenAI()
cache = redis.Redis(host="localhost", port=6379, db=0)

def cached_llm_call(prompt: str):
    key = hashlib.sha256(prompt.encode()).hexdigest()
    if (result := cache.get(key)):
        return result.decode()
    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )
    answer = response.choices[0].message.content
    cache.set(key, answer, ex=3600)
    return answer
