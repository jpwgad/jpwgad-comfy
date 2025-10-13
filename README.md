# jpwgad-comfy
ComfyUI nodes for my convenience.

## custom nodes

### SizeInput
Image Size Input  
from https://github.com/hayde0096/Comfyui-EasySettingpipes
- inputs:
    - `width`
    - `height`
    - `wh_swap` - swap width/height for output

- outputs:
    - `WIDTH` - `inputs.width` or `inputs.height`
    - `HEIGHT` - `inputs.height` or `inputs.width`

### OutputPath
generate `strftime()` formatted output path
- inputs:
    - `filename` - default: `%y%m%d%H%M%S`  
        year:`%Y`, 2-digit year:`%y`, month:`%m`, day:`%d`,  
        hour:`%H`, min:`%M`, sec:`%S`
    - `subdir` - default: `%Y-%m-%d`  
        year:`%Y`, 2-digit year:`%y`, month:`%m`, day:`%d`,  
        hour:`%H`, min:`%M`, sec:`%S`
   
- outputs:
    - `FILENAME` - formatted `inputs.filename`
    - `SUBDIR` - formatted `inputs.subdir`
    - `COMBINED` - `SUBDIR`/`FILENAME`  
        if `SUBDIR` is empty, simply `FILENAME`

## sample workflow
- simple_sdxl
    ![workflow/simple_sdxl.json](workflow/simple_sdxl.jpg)