import uvicorn
from fastapi import FastAPI, Request
from starlette.templating import Jinja2Templates

from src.scramble import get_training_scramble
from src.rotation import CubeRotation


app = FastAPI(debug=True)

templates = Jinja2Templates('templates')


@app.get('/')
async def read_root(request: Request):
    output = get_training_scramble()
    scramble = ' '.join(output['scramble'])
    trigger = ' '.join(output['trigger'])
    cube_rotation: CubeRotation = output['cube_rotation']

    return templates.TemplateResponse('index.j2',
                                      context={
                                          'request': request,
                                          'scramble': scramble,
                                          'trigger': trigger,
                                          'eo_axis': cube_rotation.front_color
                                      })

@app.get('/easy')
async def read_root(request: Request):
    output = get_training_scramble(scramble_mode='easy')
    scramble = ' '.join(output['scramble'])
    trigger = ' '.join(output['trigger'])
    cube_rotation: CubeRotation = output['cube_rotation']

    return templates.TemplateResponse('index.j2',
                                      context={
                                          'request': request,
                                          'scramble': scramble,
                                          'trigger': trigger,
                                          'eo_axis': cube_rotation.front_color
                                      })


@app.get('/health')
async def get_health(request: Request):
    return 'OK'


if __name__ == '__main__':
    uvicorn.run(app, port=3033)
