import gdown
import os
import pickle

def download_similarity_model():
    #url = "https://drive.google.com/file/d/1PPNhvS118H2IXwHS5b5Pant3VzUMIZPA/view?usp=sharing"
    url = "https://drive.google.com/uc?id=1PPNhvS118H2IXwHS5b5Pant3VzUMIZPA"
    output = "movierecomendation/ml_model/similarity.pkl"
    #os.makedirs("./ml_model", exist_ok=True)
    if not os.path.exists(output):
        os.makedirs("movierecomendation/ml_model", exist_ok=True)
        gdown.download(url, output, quiet=False)

def download_movies_dict_model():
    #url = "https://drive.google.com/file/d/1XrUPrVCO-UEDic7a7u3U0KGWGQ-lGNMb/view?usp=sharing"
    url = "https://drive.google.com/uc?id=1XrUPrVCO-UEDic7a7u3U0KGWGQ-lGNMb"
    output = "movierecomendation/ml_model/movies_dict.pkl"
    
    if not os.path.exists(output):
        gdown.download(url, output, quiet=False)

def load_similarity_model():
    download_similarity_model()
    model_path = os.path.join(os.path.dirname(__file__), 'ml_model', 'similarity.pkl')
    with open(model_path, 'rb') as file:
        print(file)
        model = pickle.load(file)
    return model

def load_movies_dict_model():
    download_movies_dict_model()
    model_path = os.path.join(os.path.dirname(__file__), 'ml_model', 'movies_dict.pkl')
    with open(model_path, 'rb') as file:
        model = pickle.load(file)
    return model
