class EntityCoreEngine:
    def __init__(self, model_name):
        self.model_name = model_name
        # Load the required model for inference and training

    def train(self, data):
        # Implement training logic for the specific model
        pass

    def infer(self, input_data):
        # Implement inference logic for the specific model
        pass

    @staticmethod
    def is_offline():
        # Check if the models can run offline
        return True  # Replace with actual logic

class Llama3(EntityCoreEngine):
    def __init__(self):
        super().__init__('Llama 3')

class Mixtral(EntityCoreEngine):
    def __init__(self):
        super().__init__('Mixtral')

class Phi3(EntityCoreEngine):
    def __init__(self):
        super().__init__('Phi-3')

class Gemma(EntityCoreEngine):
    def __init__(self):
        super().__init__('Gemma')