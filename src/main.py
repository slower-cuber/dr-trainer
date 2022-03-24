import uvicorn
from fastapi import FastAPI, Request
from starlette.templating import Jinja2Templates


app = FastAPI(debug=True)

templates = Jinja2Templates('templates')


@app.get('/')
async def read_root(request: Request):
    return templates.TemplateResponse('index.j2',
                                      context={
                                          'request': request
                                      })


@app.get('/health')
async def get_health(request: Request):
    return 'OK'


if __name__ == '__main__':
    uvicorn.run(app, port=3033)
