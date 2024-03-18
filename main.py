
# 1. Library Imports
import uvicorn      ## For ASGI(Asynchronous Server Gateway Interface)
from fastapi import FastAPI


# 2. Create App Object
app = FastAPI()


# 3. Index route, opens automatically on http://127.0.0.1:8000
@app.get('/')
def index():
    return {'message': 'Hello World'}


# 4. Route with a single parameter, returns the parameter within a message
#    Located at : http://127.0.0.1:8000/AnyNameHere
@app.get('/Welcome')
def get_name(name:str):
    return {'Welcome to FastAPI Tutorial' : f'{name}'}


# 5. Run the API with uvicorn
if __name__ == "__main__":
    uvicorn.run(app, host='127.0.0.1', port=8000)
# uvicorn main:app --reload
    

## You can use /docs to see and edit and alsoe excute it.   http://127.0.0.1:8000/docs


