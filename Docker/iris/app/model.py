# 1. Importación de bibliotecas
import pandas as pd 
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from pydantic import BaseModel
import joblib

# 2. Clase que describe las medidas de una única flor
class IrisSpecies(BaseModel):
    sepal_length: float 
    sepal_width: float 
    petal_length: float 
    petal_width: float

# 3. Clase para entrenar el modelo y hacer predicciones
class IrisModel:
    # Constructor de la clase, carga el conjunto de datos y carga el modelo
    # si existe. Si no, llama al método _train_model y 
    # guarda el modelo
    def __init__(self):
        self.df = pd.read_csv('https://gist.githubusercontent.com/curran/a08a1080b88344b0c8a7/raw/0e7a9b0a5d22642a06d3d5b9bcbad9890c8ee534/iris.csv')
        self.model_fname_ = 'iris_model.pkl'
        try:
            self.model = joblib.load(self.model_fname_)
        except Exception as _:
            self.model = self._train_model()
            joblib.dump(self.model, self.model_fname_)

    # 4. Entrena el modelo usando el clasificador RandomForest
    def _train_model(self):
        X = self.df.drop('species', axis=1)
        y = self.df['species']
        X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)
        model = RandomForestClassifier(n_estimators=100)
        model.fit(X_train, y_train)
        return model

    # 5. Realiza una predicción utilizando el modelo entrenado
    def predict_species(self, sepal_length, sepal_width, petal_length, petal_width):
        if sepal_length <= 0 or sepal_width <= 0 or petal_length <= 0 or petal_width <= 0:
            raise ValueError("Los valores deben ser mayores que cero.")
        
        data_in = [[sepal_length, sepal_width, petal_length, petal_width]]
        prediction_proba = self.model.predict_proba(data_in).tolist()
        prediction = self.model.predict(data_in).tolist()
        return prediction, prediction_proba

    def predict_species_multiple(self, data_list):
        predictions = []
        for data in data_list:
            prediction, prediction_proba = self.predict_species(data['sepal_length'], data['sepal_width'], data['petal_length'], data['petal_width'])
            predictions.append({
                'prediction': prediction,
                'probability': prediction_proba
            })
        return predictions