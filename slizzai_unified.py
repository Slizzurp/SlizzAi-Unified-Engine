# slizzai_unified.py

from engines.vision import VisionEngine
from engines.nlp import NLPEngine
from engines.speech import SpeechEngine
from engines.logic import LogicEngine
from engines.retrieval import RetrievalEngine
from engines.generation import GenerationEngine

class UnifiedAI:
    def __init__(self):
        self.engines = {
            "vision": VisionEngine(),
            "nlp": NLPEngine(),
            "speech": SpeechEngine(),
            "logic": LogicEngine(),
            "retrieval": RetrievalEngine(),
            "generation": GenerationEngine()
        }

    def route(self, input_data):
        task_type = self.detect_task(input_data)
        engine = self.engines.get(task_type)

        if engine:
            return engine.run(input_data)
        else:
            raise ValueError(f"No engine found for task: {task_type}")

    def detect_task(self, input_data):
        # Simple task detection logic (can be replaced with ML classifier)
        if isinstance(input_data, bytes):
            return "vision"
        elif isinstance(input_data, str):
            if input_data.startswith("speak:"):
                return "speech"
            elif "generate:" in input_data:
                return "generation"
            elif "retrieve:" in input_data:
                return "retrieval"
            elif "logic:" in input_data:
                return "logic"
            else:
                return "nlp"
        else:
            return "nlp"

    def run(self, input_data):
        try:
            result = self.route(input_data)
            return result
        except Exception as e:
            return {"error": str(e)}

# Example usage
if __name__ == "__main__":
    ai = UnifiedAI()
    sample_input = "generate: a poem about fusion"
    output = ai.run(sample_input)
    print(output)