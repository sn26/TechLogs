
class ModelWeights: 

    weights = None  
    
    @staticmethod 
    def set_weights(weights ):
        print("SETTING INITIAL WEIGHTS...")
        ModelWeights.weights = weights 
        return