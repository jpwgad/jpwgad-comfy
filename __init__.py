from .nodes import SizeInput, OutputPath, AutoSelector

NODE_CLASS_MAPPINGS = {
    "SizeInput": SizeInput,
    "OutputPath": OutputPath,
    "AutoSelector": AutoSelector,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SizeInput": "Image Size Input",
    "OutputPath": "Output Path",
    "AutoSelector": "Auto Selector",
}

__all__ = ["NODE_CLASS_MAPPINGS"]