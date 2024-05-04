
class D2_RefinerSteps:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "steps": ("INT", {"default": 25, "min":0}),
                "start": ("INT", {"default": 0, "min":0}),
                "end": ("INT", {"default": 5, "min":0}),
            }
        }
    RETURN_TYPES = ("INT", "INT", "INT", "INT",)
    RETURN_NAMES = ("steps", "start", "end", "refiner_start",)
    FUNCTION = "steps"
    CATEGORY = "D2"

    def steps(self, steps, start, end):
        refiner_start = end + 1

        return(steps, start, end, refiner_start,)
