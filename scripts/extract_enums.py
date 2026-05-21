import logging
from pathlib import Path

import yaml

import tweaver as weaver

COMMON_ACCESS_MODEL = Path("input/common_access_model.yaml")
CAM_IMPORTS_MODEL = Path("input/cam_imports_model.yaml")
OUTPUT_DIR = Path("output/")


class IndentedDumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow=flow, indentless=False)


def extract_enums(
    local_filepath: Path | None = None,
    model_filepath: Path | None = None,
    output_filepath: Path | None = None,
):
    """Extract Enums from a monolithic LinkML model into individual YAML files
    Args:
        local_filepath: The file containing the monolithic linkml model
        model_filepath: The file containing master LinkML model, used to get the id property to reuse for enums
        output_filepath: The directory where the enum YAMLs are to be written
    Returns:
        list of enum names
    """
    with local_filepath.open("rt") as enums:
        parsed = yaml.safe_load(enums)
    with model_filepath.open() as f:
        model_parsed = yaml.safe_load(f)

    model_id = model_parsed.get("id")
    enums = parsed.get("enums")

    output_filepath.mkdir(parents=True, exist_ok=True)

    for name, enum in enums.items():
        with (output_filepath / f"{name}.yaml").open("wt") as extracted:
            extracted.write("---\n")
            yaml.dump(
                {"id": f"{model_id}/{name}", "name": name, "enums": {name: enum}},
                extracted,
                Dumper=IndentedDumper,
                indent=2,
                default_flow_style=False,
                sort_keys=False,
            )
    return enums.keys()


def update_imports(enum_list: list[str], model_filepath: Path):
    """
    Writes the name of each enum to "imports" property in model file.

    Opens file containing the master LinkML model and gets the data under the 'imports' key.
    Appends the name of each extracted enumeration to any imports that may already exist, if it is not already there.
    Writes the file with enum updates to the same filepath.
    """

    with model_filepath.open() as imports:
        imports_parsed = yaml.safe_load(imports)

    existing_imports = imports_parsed.get("imports", [])
    updated_imports = existing_imports + [
        n for n in enum_list if n not in existing_imports
    ]
    imports_parsed["imports"] = updated_imports

    with model_filepath.open("w") as f:
        yaml.dump(imports_parsed, f)


if __name__ == "__main__":
    weaver.init_logging("INFO")
    logging.debug(f"Extracting enums from input/common_access_model.yaml")

    enums = extract_enums(
        local_filepath=COMMON_ACCESS_MODEL,
        model_filepath=CAM_IMPORTS_MODEL,
        output_filepath=OUTPUT_DIR,
    )

    update_imports(enum_list=enums, model_filepath=CAM_IMPORTS_MODEL)
    logging.error(enums)
