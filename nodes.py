import datetime

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
        return (w, h)


# OutputPath: date/time replacing
class OutputPath:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "filename": ("STRING", {
                    "default": "YYMMddhhmmss",
                    "tooltip": "year:yyyy(or YY), month:MM, day:dd, hour:hh, min:mm, sec:ss"
                }),
                "subdir": ("STRING", {
                    "default": "yyyy-MM-dd",
                    "tooltip": "year:yyyy(or YY), month:MM, day:dd, hour:hh, min:mm, sec:ss"
                }),
            },
        }

    RETURN_TYPES = ("STRING", "STRING", "STRING")
    RETURN_NAMES = ("FILENAME", "SUBDIR", "COMBINED")
    OUTPUT_TOOLTIPS = ("formatted filename", "formatted subdir", "formatted subdir/filename")
    FUNCTION = "outputpath"
    CATEGORY = "jpwgad"

    def outputpath(self, subdir, filename):
        fmt_subdir = subdir.strip().replace("yyyy", "%Y").replace("YY", "%y").replace("MM", "%m").replace("dd", "%d").replace("hh", "%H").replace("mm", "%M").replace("ss", "%S")
        fmt_filename = filename.strip().replace("yyyy", "%Y").replace("YY", "%y").replace("MM", "%m").replace("dd", "%d").replace("hh", "%H").replace("mm", "%M").replace("ss", "%S")

        try:
            current_time = datetime.datetime.now()
            str_subdir = current_time.strftime(fmt_subdir)
            str_filename = current_time.strftime(fmt_filename)

            if subdir == "":
                str_combined = str_filename
            else:
                str_combined = str_subdir + "/" + str_filename
            return (str_filename, str_subdir, str_combined)
        except ValueError as e:
            raise ValueError(f"Invalid format: {str(e)}")
    