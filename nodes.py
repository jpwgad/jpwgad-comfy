from time import strftime

"""
ComfyUI カスタムノード: SizeInput
- width, height を整数入力
- wh_swap トグル (BOOL)
- 出力: width, height（wh_swap=True のとき入れ替え）
"""
# Image Size Input : from https://github.com/hayde0096/Comfyui-EasySettingpipes
class SizeInput:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "width": ("INT", {"default": 1024, "min": 32, "max": 8192, "step": 16}),
                "height": ("INT", {"default": 1024, "min": 32, "max": 8192, "step": 16}),
                "swap_wh": ("BOOLEAN", {"default": False, "label_on": "Swap", "label_off": "Keep"}),
            },
        }

    RETURN_TYPES = ("INT", "INT")
    RETURN_NAMES = ("WIDTH", "HEIGHT")
    FUNCTION = "sizeinput"
    CATEGORY = "jpwgad"

    def sizeinput(self, width, height, swap_wh=False):
        try:
            w = int(width)
            h = int(height)
        except Exception:
            return (0, 0)

        if swap_wh:
            return (h, w)
        else:
            return (w, h)


# OutputPath: `strftime()` formatted output path
class OutputPath:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "filename": ("STRING", {
                    "default": "%y%m%d%H%M%S",
                    "tooltip": "year:%Y(4-digit) or %y(2-digit), month:%m, day:%d, hour:%H, min:%M, sec:%S"
                }),
                "subdir": ("STRING", {
                    "default": "%Y-%m-%d",
                    "tooltip": "year:%Y(4-digit) or %y(2-digit), month:%m, day:%d, hour:%H, min:%M, sec:%S"
                }),
            },
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING")
    RETURN_NAMES = ("FILENAME", "SUBDIR", "COMBINED")
    OUTPUT_TOOLTIPS = ("formatted filename", "formatted subdir", "formatted subdir/filename")
    FUNCTION = "outputpath"
    CATEGORY = "jpwgad"

    def outputpath(self, subdir, filename):
        try:
            str_subdir = strftime(subdir)
            str_filename = strftime(filename)

            if subdir == "":
                str_combined = str_filename
            else:
                str_combined = str_subdir + "/" + str_filename
            return (str_filename, str_subdir, str_combined)
        except ValueError as e:
            raise ValueError(f"Invalid format: {str(e)}")

    @classmethod
    def IS_CHANGED(cls, **kwargs):
        return float("NaN")


# AutoSelector: Outputs the first valid input
class AlwaysEqualProxy(str):
    def __eq__(self, _):
        return True

    def __ne__(self, _):
        return False

any_type = AlwaysEqualProxy("*")

class AutoSelector:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "optional": {
                "in1": (any_type,),
                "in2": (any_type,),
                "in3": (any_type,),
            },
        }

    RETURN_TYPES = (any_type,)
    RETURN_NAMES = ("OUT",)
    OUTPUT_TOOLTIPS = ("first valid input",)
    FUNCTION = "autoselect"
    CATEGORY = "jpwgad"

    def autoselect(self, in1=None, in2=None, in3=None):
        if in1 is not None:
            return (in1,)
        elif in2 is not None:
            return (in2,)
        else:
            return (in3,)
