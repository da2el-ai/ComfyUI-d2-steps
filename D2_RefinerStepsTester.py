class D2_RefinerStepsTester:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "steps": ("INT", {"forceInput":True}),
            },
            "optional": {
                "start": ("INT", {"forceInput":True}),
                "end": ("INT", {"forceInput":True}),
                "refiner_start": ("INT", {"forceInput":True}),
            }
        }

    # INPUT_IS_LIST = True
    RETURN_TYPES = ()
    OUTPUT_NODE = True
    FUNCTION = "execute"
    CATEGORY = "D2"


    # def execute(self, seed, steps=0, start=0, end=0, refiner_start=0):
    def execute(self, steps=0, start=0, end=0, refiner_start=0):
        text = f"stesps: {steps}\nstart: {start}\nend: {end}\nrefiner_start: {refiner_start}"
        return {"ui": {"text": text}, "result": (text,)}
