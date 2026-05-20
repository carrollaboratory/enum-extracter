import logging
from pathlib import Path

import yaml
import tweaver as weaver


class IndentedDumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow=flow, indentless=False)


def extract_enums(
    local_filepath: Path | None = None,
    source_filepath: Path | None = None,
    output_filepath: Path | None = None,
):
    get_file = local_filepath if local_filepath else Path(path).stem
    with get_file.open("rt") as enums:
        parsed = yaml.safe_load(enums)

    with source_filepath.open() as f:
        source_parsed = yaml.safe_load(f)

    model_id = source_parsed.get("id")
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
            )

    return enums.keys()


def update_imports(enum_list: list[str], imports_filepath: Path):
    with imports_filepath.open() as imports:
        imports_parsed = yaml.safe_load(imports)

        existing_imports = imports_parsed.get("imports", [])
        updated_imports = existing_imports + [
            n for n in enum_list if n not in existing_imports
        ]
        imports_parsed["imports"] = updated_imports

    with imports_filepath.open("w") as f:
        yaml.dump(imports_parsed, f)


if __name__ == "__main__":
    weaver.init_logging("INFO")
    logging.debug(f"Extracting enums from input/common_access_model.yaml")
    enums = extract_enums(
        local_filepath=Path("input/common_access_model.yaml"),
        source_filepath=Path("input/cam_imports_model.yaml"),
        output_filepath=Path("output/"),
    )
    update_imports(
        enum_list=enums, imports_filepath=Path("input/cam_imports_model.yaml")
    )
    logging.error(enums)
