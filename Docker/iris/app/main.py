from fastapi import FastAPI, Request, UploadFile, File, Form, HTTPException
from fastapi.responses import HTMLResponse, StreamingResponse, JSONResponse, PlainTextResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.exceptions import RequestValidationError
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import uvicorn
from model import IrisModel, IrisSpecies
import io

app = FastAPI()
model = IrisModel()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def inicio(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/obtener-iris", response_class=HTMLResponse)
def obtener_iris(request: Request):
    url ='https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
    iris = pd.read_csv(url)
    iris_html = iris.to_html()
    return templates.TemplateResponse("obtener_iris.html", {"request": request, "iris_html": iris_html})

@app.get("/graficar-iris")
def graficar_iris():
    url ='https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv'
    iris = pd.read_csv(url)

    plt.scatter(iris['sepal_length'], iris['sepal_width'])
    plt.savefig('iris.png')

    return {"url": "/imagen-iris"} 

@app.get("/imagen-iris")
async def imagen_iris():
    archivo = open('iris.png', mode="rb")
    return StreamingResponse(archivo, media_type="image/png")

@app.get("/pagina-iris", response_class=HTMLResponse)
async def pagina_iris(request: Request):
    return templates.TemplateResponse("pagina_iris.html", {"request": request})

@app.get("/predict-page", response_class=HTMLResponse)
async def predict_page(request: Request):
    return templates.TemplateResponse("predict_page.html", {"request": request})

@app.post("/predict")
def predict_species(request: Request, sepal_length: float = Form(...), sepal_width: float = Form(...), petal_length: float = Form(...), petal_width: float = Form(...)):
    try:
        prediction, prediction_proba = model.predict_species(sepal_length, sepal_width, petal_length, petal_width)
        return {
            'prediction': prediction,
            'probability': prediction_proba        
        }
    except ValueError as e:
        raise ValueError(str(e))


@app.post("/prediction-result", response_class=HTMLResponse)
async def prediction_result(request: Request, sepal_length: float = Form(...), sepal_width: float = Form(...), petal_length: float = Form(...), petal_width: float = Form(...)):
    data = {"sepal_length": sepal_length, "sepal_width": sepal_width, "petal_length": petal_length, "petal_width": petal_width}
    prediction, prediction_proba = model.predict_species(data['sepal_length'], data['sepal_width'], data['petal_length'], data['petal_width'])
    return templates.TemplateResponse("prediction_result.html", {"request": request, "prediction": prediction, "probability": prediction_proba})


@app.get("/cargar-archivo", response_class=HTMLResponse)
async def cargar_archivo(request: Request):
    return templates.TemplateResponse("upload_file.html", {"request": request})

@app.post("/predict-file")
async def predict_species_file(file: UploadFile = File(...)):
    # Leer el archivo csv en un DataFrame de Pandas
    content = await file.read()
    df = pd.read_csv(io.StringIO(content.decode("utf-8")))
    
    # Realizar las predicciones para cada fila en el DataFrame
    predictions = []
    for _, row in df.iterrows():
        prediction, prediction_proba = model.predict_species(row['sepal_length'], row['sepal_width'], row['petal_length'], row['petal_width'])
        predictions.append({
            'prediction': prediction[0],
            'probability': prediction_proba[0]
        })

    # Agregar las predicciones al DataFrame original
    predictions_df = pd.DataFrame(predictions)
    result_df = pd.concat([df, predictions_df], axis=1)

    # Devolver el DataFrame de resultados como una respuesta JSON
    return JSONResponse(result_df.to_dict(orient="records"))


@app.exception_handler(ValueError)
async def value_error_exception_handler(request: Request, exc: ValueError):
    return templates.TemplateResponse("422.html", {"request": request, "detail": str(exc)})

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return PlainTextResponse(str(exc), status_code=400)

@app.exception_handler(HTTPException)
async def http_exception_handler(request: Request, exc: HTTPException):
    return templates.TemplateResponse("422.html", {"request": request})

@app.exception_handler(RequestValidationError)
async def validation_exception_handler(request: Request, exc: RequestValidationError):
    return templates.TemplateResponse("422.html", {"request": request})
