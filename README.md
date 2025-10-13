# jpwgad-comfy
ComfyUI nodes for my convenience.

## custom nodes

- SizeInput: Image Size Input
    inputs:
    - `width`
    - `height`
    - `wh_swap` - swap width/height for output

    outputs:
    - `WIDTH` - `inputs.width` or `inputs.height`
    - `HEIGHT` - `inputs.height` or `inputs.width`

    from https://github.com/hayde0096/Comfyui-EasySettingpipes
- OutputPath: Date/Time based output path
    generate date/time based directory and file name
    inputs:
    - `filename`
    - `subdir`
    
    outputs:
    - `FILENAME` - formatted `inputs.filename`
        year:`yyyy`(or `YY`), month:`MM`, day:`dd`, hour:`hh`, min:`mm`, sec:`ss`
    - `SUBDIR` - formatted `inputs.subdir`
        year:`yyyy`(or `YY`), month:`MM`, day:`dd`, hour:`hh`, min:`mm`, sec:`ss`
    - `COMBINED` - `SUBDIR`/`FILENAME`
        if `SUBDIR` is empty, simply `FILENAME`

## sample workflow
- simple_sdxl
    ![workflow/simple_sdxl.json](workflow/simple_sdxl.jpg)