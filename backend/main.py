from fastapi import FastAPI

app = FastAPI(title='AI App Factory')

@app.get('/')
def health():
    return {'status':'running','service':'AI-App-Factory'}

@app.post('/generate')
def generate(request: dict):
    return {'status':'queued','request':request}
