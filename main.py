from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates


app = FastAPI()
templates = Jinja2Templates(directory='templates')


@app.get('/')
async def home(request: Request):
    """
    Displays the Stock Screener homepage / dashboard.
    """
    return templates.TemplateResponse('home.html', {'request': request})


@app.post('/stock')
async def create_stock():
    """
    Creates a stock and stores it in the database.
    """
    return {'code': 'success', 'message': 'stock created'}
