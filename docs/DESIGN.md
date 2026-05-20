# Term Weaver

![status](https://img.shields.io/badge/status-draft-yellow) ![version](https://img.shields.io/badge/version-0.1.0-lightgrey)

| | |
|---|---|
| **Created** | 2026-05-13 |
| **Updated** | 2026-05-13 |
| **Reviewers** | — |


## 1. Overview

Automate the process of materializing the intensional enumerations for a  LinkML model and build out a functional LinkML model containing those extensional enums as standalone YAML model components.


### Goals

- Intensional enums will be remain independent of the actual LinkML model and never be replaced by extensional products of the materializations.
- Output from the materialization will be independent YAML files to minimize merge-conflicts and help with PR reviews.
- If there are enumerations present in the source YAML file, they will carry over untouched and be available alongisde the products of materialization.
- Output will be a 'complete' LinkML model that can be built and reviewed as any other model, even if there are no classes.
- Refreshing enums periodically to incorporate changes from external ontologies over time.
- Maintain the unmaterialized, intensional enumerations to accomadate changes over time.


### Non-Goals

- Full automation of the process


## 2. Context & Motivation


### Background

There is a real need for access to explicit terms for both validation and model use where possible.


### Motivation

The process of performing this manually is very time consuming and error prone and is likely to not to be entirely a "one off" task.


### References

- [Semantic Enumerations](https://linkml.io/linkml/schemas/enums.html)


## 3. Scope


### In Scope

- Materialize enumerations using [vskit](https://github.com/INCATools/ontology-access-kit)
- Build functional LinkML 'project' based on results from materialization using jinja


### Out of Scope

- General model definition and validation.


### Constraints

- For now, only those ontologies recognized by vskit (bioregistry) will be supported.


### Assumptions

- LinkML 'intensional' enumerations are well formed and 'complete' for this purpose.


## 4. Stakeholders

| Role | Name | Responsibilities |
|---|---|---|
| Developer | Yelena Cox | Author and Maintainer of the application |


## 5. Technical Design


### Architecture

LinkML 'model' will be maintained as part of a single YAML file. The output will be a functional LinkML model containing all materialized enums and can be tested and reviewed using any LinkML tooling.


#### Components

| Component | Technology | Description |
|---|---|---|
| **Spinner** | `python` | Extract key data points from the LinkML YAML source file to be used when building out the final YAML model files. |
| **Spool** | `python + vskit` | Automates the execution of the vskit |
| **Weave** | `python + jinja` | Build out the functional LinkML model that can be imported by downstream models |


### Interfaces


#### Inputs

| Name | Format | Description |
|---|---|---|
| `source YAML` | CLI Arg/filename | This houses the source YAML definitions that are to be materialized |


#### Outputs

| Name | Format | Description |
|---|---|---|
| `LinkML Schema` | multifile YAML | This will be a fully functional LinkML model that can be imported by downstream models |


### Dependencies

| Package | Version | Purpose | Docs |
|---|---|---|---|
| `LinkML` | — | Provide validation of resulting model components tooling for reviewing materialized output |  |
| `ontology-access-kit` | — | This does the heavy lifting of the materializations |  |
| `argparse` | stdlib | CLI argument parsing — Python's built-in equivalent of minimist/yargs |  — [docs](https://docs.python.org/3/library/argparse.html) |
| `pathlib` | stdlib | Python classes representing filesystem paths with semantics appropriate for different operating systems. |  — [docs](https://docs.python.org/3/library/pathlib.html) |
| `pyyaml` | — | Python library that provides ability to serialize python objects <=> YAML format. |  — [docs](https://pyyaml.org/) |
| `subprocess` | stdlib | Execute vskit and capture stderr and stdout to local variables |  — [Official Docs](https://docs.python.org/3/library/subprocess.html) · [Tutorial](https://www.geeksforgeeks.org/python/python-subprocess-module/) |


## 6. Implementation Approach


### Strategy

Parse the incoming YAML file for details required for final model construction. Run vskit and extract final model files from the end product to allow user to intiate a Pull Request.


### Phases

**Phase 1 — Initial MVP**

The first pass will automate the materialization of the model's terms suitable for github PR review. The tool will initially not be automated, and output can be reviewed directly by the user.


### Error Handling

Errors will be logged using standard python logging.


### Logging

All log-levels should be supported with a reasonable defult (INFO).  - At the DEBUG level, all information captured from the vskit should be provided. - At INFO, only highlights of what is being done and which files are read/written - All errors and warnings will be clearly noted as such in the logs.


## 7. Testing Strategy


### Approach

Basic tests from the application itself to confirm all relevant artifacts defined within the original YAML file were written to their corresponding location in the final model


### Acceptance Criteria

- Errors must be raised if these counts don't align exactly


## 8. Risks & Mitigations

| ID | Risk | Likelihood | Impact | Mitigation |
|---|---|---|---|---|
| R-001 | Materialization depends on an external tool which may not perform exactly as we need/expect. | low | low | By separating the materialization of these enumerations from the source models and requiring form review of all changes, we should be able to catch any surprises before the changes are incorporated into the final models. |


## 9. Open Questions

| ID | Question | Owner | Due |
|---|---|---|---|
| Q-001 | How does LinkML and vskit handle situations like 'All of this stuff under code xyz from SNOMED, but also all of these codes from FHIR null-flavor' | Robert | 2026-06-30 |


## 10. Decision Log


### D-001 — Input 'model' will be completely independet from the output model (separate repo). The relationship here is 1 to 1.

**Date:** 2026-05-13  
**Rationale:** Cleaner input/output. Keeps PR Review isolated. Downstream models can 'pick and choose' the relevant sets of enumerations to use.

**Alternatives considered:**
- Many input to 1 materialized repo. This was not well suited for the goals


## 11. Appendix


### Glossary

| Term | Definition |
|---|---|
| **materialization** | the process of computing, executing, and physically storing the concrete instances (the extension) derived from an abstract definition or rule (the intension) |
| **intensional** | Abstract definition of the model component containing rules, attributes, constraints and logic an object must satisfy. In our case, this is the unmaterialized enumeration |
| **extensional** | The realized data object. In our case, the extensional model components will have been materialized |
| **vskit** | The oaklib tool that provides the materialization of the enumerated values based on the linkml definitions provided |



---
*Generated from `design.yaml` on 2026-05-13*
