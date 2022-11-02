import torch
import logging
from transformers import AutoTokenizer

log = logging.getLogger(__name__)

class __texttaggermodel:

  def __init__(self):
    self.model = None
    self._instance = None
    self.pathmodel = 'app/models/text-tagger.h5py'
    self.model = torch.load(self.pathmodel, map_location=torch.device('cpu'))
    log.info("Model Loaded")
    self.pathtokenizer =  'app/models/text-tagger-tokenizer'
    self.tokenizer = AutoTokenizer.from_pretrained(self.pathtokenizer)
    log.info("Tokenizer Loaded")
    self.LABEL_COLUMNS = ["toxic", "severe_toxic", "obscene", "threat", "insult", "identity_hate"]
    self.threshold = 0.5
    self.pred = []
    

  def predictsentence(self, sentence):
    log.info("The comment is ",str(sentence))

    encoding = self.tokenizer.encode_plus(
      sentence,
      add_special_tokens=True,
      max_length=512,
      return_token_type_ids=False,
      padding="max_length",
      return_attention_mask=True,
      return_tensors='pt',
    )
    
    self.model.eval()
    _, test_prediction = self.model(encoding["input_ids"], encoding["attention_mask"])
    test_prediction = test_prediction.flatten().numpy()
    toxic = {}
    for label, prediction in zip(self.LABEL_COLUMNS, test_prediction):
      if prediction > self.threshold:
        toxic[label] = prediction
    if toxic == {}:
      toxic['Normal Comment'] = 0.90

    return toxic


def Text_Tagging_Service():
    """Factory function for __texttaggermodel class. Singleton
    :return __texttaggermodel._instance (__texttaggermodel):
    """
    # ensure an instance is created only the first time the factory function is called
    if __texttaggermodel._instance is None:
        log.info("No insance created")
        __texttaggermodel._instance = __texttaggermodel()
    return __texttaggermodel._instance