import pandas as pd
import pickle

from flask import Flask, request, Response
from rossmann.Rossmann import Rossmann

# loading model
model = pickle.load(open('/Users/gtvmi/OneDrive/Documentos/Repos/projeto_portifplio_hossmann_bot/model/model_rossmann.pkl', 'rb'))

app = Flask( __name__ )

@app.route('/rossmann/predict', methods=['POST'])

def rossmann_predict():
    test_json = request.get_json()
    
    if test_json: # there is data
        if isinstance(test_json, dict): #unique example
            test_raw = pd.DataFrame(test_json, index=[0])
        else:
            test_raw = pd.DataFrame(test_json, columns=test_json[0].keys())
            
        # Instantiate Rossmann Class
        pipeline = Rossmann()
        
        # data cleaning
        df_cleaning = pipeline.data_cleaning(test_raw)
        
        # feature engineering
        df_fe = pipeline.feature_engineering(df_cleaning)
        
        # data preparation
        df_preparation = pipeline.data_preparation(df_fe)
        
        # prediction
        df_response = pipeline.get_prediction(model, test_raw, df_preparation)
        
        return df_response
        
        
        
    else: 
        return Response('{}', status=200, mimetype='application/json')
    

if __name__ == "__main__":
    app.run('0.0.0.0')