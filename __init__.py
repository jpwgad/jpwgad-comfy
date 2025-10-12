from .nodes import SizeInput, OutputPath

NODE_CLASS_MAPPINGS = {
    "SizeInput": SizeInput,
    "OutputPath": OutputPath,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SizeInput": "Image Size Input",
    "OutputPath": "Date/Time based output path",
}

__all__ = ["NODE_CLASS_MAPPINGS"]