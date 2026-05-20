# enum-extracter
Extract enumerations from a LinkML model file.

## Process
- YAML files from [Common Access Model](https://github.com/include-dcc/common-access-model/blob/main/src/common_access_model/schema/common_access_model.yaml) copied into input folder
- Run `python scripts/extract_enums.py`
  - The script will place the extracted enums into an output folder
## Install
For using on a local machine, it is recommended to add the dev dependencies: 

```bash
pip install -e ".[dev]" 
```

This enables rich output which can be helpful.
