from elfi.methods.inference.parameter_inference import ParameterInference
from main import app

def Generator():
    with app.app_context():
        yield Generator

