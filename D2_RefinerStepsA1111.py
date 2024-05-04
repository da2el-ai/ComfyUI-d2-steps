import math

class D2_RefinerStepsA1111:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "steps": ("INT", {"default": 25}),
                "denoise": ("FLOAT", {"default": 1, "min":0, "max":1, "step":0.01}),
                "switch_at": ("FLOAT", {"default": 0.2, "min":0, "max":1, "step":0.01}),
            }
        }
    RETURN_TYPES = ("INT", "INT", "INT", "INT",)
    RETURN_NAMES = ("steps", "start", "end", "refiner_start",)
    FUNCTION = "steps"
    CATEGORY = "D2"

    def steps(self, steps, denoise, switch_at):
        real_steps = math.floor(steps / denoise)
        start = real_steps - steps
        end = math.floor((real_steps - start) * switch_at) + start
        refiner_start = end + 1

        return(real_steps, start, end, refiner_start,)
