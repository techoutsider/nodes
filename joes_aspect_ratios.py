# basic aspect ratios

class JoesAspectRatios:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(s):
        return {
                "required": {
                    "aspectRatio": ([
                    "1:1  - 1024x1024 Square", 
                    "3:4  - 896x1152 Portrait", 
                    "4:3  - 1152x896 Landscape", 
                    "16:9 - 1344x768 Widescreen"],)
            }
        }
    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("Width", "Height")
    FUNCTION = "Joes_AspectRatioFunction"
    CATEGORY = "image"

    def Joes_AspectRatioFunction(self, aspectRatio):
        if aspectRatio == "1:1  - 1024x1024 Square":
            width, height = 1024, 1024
        elif aspectRatio == "3:4  - 896x1152 Portrait":
            width, height = 896, 1152
        elif aspectRatio == "4:3  - 1152x896 Landscape":
            width, height = 1152, 896
        elif aspectRatio == "16:9 - 1344x768 Widescreen":
            width, height = 1344, 768
        return(width, height)
            
NODE_CLASS_MAPPINGS = {
    "JoesAspectRatios": JoesAspectRatios
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "JoesAspectRatios": "Joe's Aspect Ratios"
}
