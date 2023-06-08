from src.predictor import Predictor
from src.utils.image_utils import Image_Processor
from src.model.class_names import class_names


def predict_handler(tf_model, image_file):
    # Prepare the image
    image = Image_Processor(image_file)
    image.save('src/temp', image_file.filename)
    
    # Predict the image
    predictor = Predictor(tf_model, class_names, image.path)
    result = predictor.predict()
    
    image.delete()
    return str(result)
