import uvicorn
from fastapi import FastAPI
from predict import Text_Tagging_Service
from pydantic import BaseModel


class sentItem(BaseModel):
    sentence: str

app = FastAPI()

@app.get("/msg")
def index():
    return { "message": "Up and running"}
    

@app.route("/predict", methods=["POST"])
def predict(sentItem: sentItem):
    """Endpoint to predict sentence
        :return (json): This endpoint returns a json file with the following format:
            {
                "Intent": "hate"
            }
    """
    # get sentence
    sentenceSupplied = sentItem.sentence
    print(sentenceSupplied)

    # instantiate keyword spotting service singleton and get prediction
    tts = Text_Tagging_Service()
    predicted_intent = tts.predict(sentenceSupplied)

    # send back result as a json file
    result = {"Intent": predicted_intent}
    return result

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)