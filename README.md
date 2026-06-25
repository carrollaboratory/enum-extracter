# enum-extracter
Extract enumerations from a LinkML model file. 

## Install
For using on a local machine, it is recommended to add the dev dependencies: 

```bash
pip install -e ".[dev]" 
```

This enables rich output which can be helpful.

## Process
- Run:
  ```bash
  python scripts/extract_enums.py
  ```
  - The script will place the extracted enums into an output folder
 
### Manual Actions
Currently, the following tasks are performed manually:
- YAML files from [Common Access Model](https://github.com/include-dcc/common-access-model/blob/main/src/common_access_model/schema/common_access_model.yaml) copied into input folder
- cam_imports_model.yaml file manually created and populated with modified contents from [Common Access Model YAML file](https://github.com/include-dcc/common-access-model/blob/main/src/common_access_model/schema/common_access_model.yaml) 
