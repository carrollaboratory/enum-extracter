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
- YAML files from [Common Access Model](https://github.com/include-dcc/common-access-model/) copied into input folder
- common_acess_model.yaml file copied into input folder from [Common Access Model](https://github.com/include-dcc/common-access-model/)
- cam_imports_model.yaml file manually created and populated with modified contents from common_access_model.yaml
- The following argument values are hardcoded at the top of `scripts/extract_enums.py` and must be updated as needed
  - COMMON_ACCESS_MODEL = The file containing the monolithic linkml model
  - CAM_IMPORTS_MODEL = The file containing master LinkML model, used to get the id property to reuse for enums
  - OUTPUT_DIR = The directory where the enum YAMLs are to be written
