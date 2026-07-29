from fastapi import FastAPI
app = FastAPI()
@app.get('/cliente')
def ola_mundo():
    return {'mensagem': 'Minha primeira api em fastapi?'}
