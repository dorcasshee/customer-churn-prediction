from flask import Flask, request, render_template
from input_processing import validate, format_model_inputs
from model import Model

app = Flask(__name__)

# Method 1: Via HTML Form
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        form_input = dict(request.form)               
        errors = validate(form_input)
        
        if len(errors) > 0:
            return render_template('index.html', errors=errors, form=request.form)

        model_inputs = format_model_inputs(form_input)
        prediction = Model().predict(model_inputs)
        
        return render_template('index.html', prediction=prediction, form=request.form)

    return render_template('index.html', form={})

# Method 2: Via POST API (one prediction at a time)
@app.route('/api/predict_one', methods=['POST'])
def predict_one():
    request_data = request.get_json(force=True)
    errors = validate(request_data)
    if len(errors) > 0:
        return {'errors': errors}, 400

    model_inputs = format_model_inputs(request_data)
    prediction = Model().predict(model_inputs)
    return {'prediction': int(prediction)}


# Method 2: Via POST API (many predictions at a time)
@app.route('/api/predict', methods=['POST'])
def predict_many():
    request_data = request.get_json(force=True)

    predictions = []
    model = Model()
    for row in request_data:
        errors = validate(row)
        if len(errors) > 0:
            return {'record': row, 'errors': errors}, 400

        model_inputs = format_model_inputs(row)
        predictions.append(int(model.predict(model_inputs)))

    return {'predictions': predictions}

if __name__ == '__main__':
    app.run()