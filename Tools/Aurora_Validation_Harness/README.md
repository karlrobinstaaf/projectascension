# Project Ascension — Aurora Validation Harness

The Aurora Validation Harness is the validator-owned execution environment for Project
Ascension's Aurora architecture. Its first goal is to make
`AURORA-SCN-FOUND-001_Hidden_World_Knowledge_Isolation.md` executable without exposing
hidden world state, expected answers, validator notes, or future scenario data to Aurora.

The harness is not part of Aurora's cognition. It creates controlled conditions, captures
evidence, evaluates invariants, and distinguishes Aurora failures from fixture, harness,
schema, or infrastructure failures.

## Current status

| Field | Value |
|---|---|
| Package version | `0.1.0` |
| Implementation level | `HC-7 — Core Harness Implemented and Unit-Verified` |
| Initial scenario | `AURORA-SCN-FOUND-001` |
| Validation gate | `GATE 1 — FOUNDATION` |
| Python requirement | Python 3.12 or newer |
| Runtime dependencies | None |
| Automated tests | `2,198 passing` |
| Command-line interface | `aurora-validation-harness` |
| Formal execution | Not started; `HC-8` dry-run assets remain to be materialized |

The package now contains the complete core execution chain from baseline and configuration
verification through isolated fixtures, evidence, snapshots, transitions, assertions,
comparisons, verdicts, immutable storage, harness orchestration, and a fail-closed command-line
boundary. The next development phase is to materialize the validator-owned FOUND-001
configuration, fixture set, scenario plan factory, and Aurora runtime adapter for the first
non-gating dry run.

## Core principle

> The harness must never prove that Aurora works by giving her the information, behavior,
> or answer required to pass.

Foundation validation requires architectural isolation:

```text
WORLD TRUTH
    ↓
VALIDATOR-OWNED HARNESS
    ↓
GOVERNED EVIDENCE CHANNEL
    ↓
AURORA-ACCESSIBLE EVIDENCE
    ↓
AURORA STATE
```

There must be no direct path from the complete world state, validator oracle, player-private
knowledge, future event queue, or expected result store into Aurora's cognitive context.

## Canonical contracts

The implementation is governed by the files under:

```text
Canon/Systems/AI/Aurora/Validation/
```

Primary contracts:

- `Aurora_Validation_Strategy.md`
- `Aurora_Invariant_Catalog.md`
- `Aurora_Cross_System_Test_Matrix.md`
- `Aurora_Scenario_Test_Framework.md`
- `Aurora_Foundation_Validation_Runbook.md`
- `Aurora_Validation_Evidence_Schema.md`
- `Aurora_Foundation_Freeze_Record.md`
- `Aurora_Minimum_Executable_State_Interface.md`
- `Aurora_Validation_Harness_Contract.md`

The first scenario is located at:

```text
Canon/Systems/AI/Aurora/Validation/Scenarios/Foundation/
AURORA-SCN-FOUND-001_Hidden_World_Knowledge_Isolation.md
```

## Repository locations

```text
PROJECT_ASCENSION/
├── Canon/
│   └── Systems/AI/Aurora/Validation/
├── Development/
│   └── Validation/Aurora/
│       ├── Configuration/
│       ├── Fixtures/
│       └── Runs/
└── Tools/
    └── Aurora_Validation_Harness/
        ├── pyproject.toml
        ├── README.md
        ├── src/
        └── tests/
```

- `Canon/` contains approved architecture and validation specifications.
- `Tools/` contains executable validation code.
- `Development/Validation/Aurora/` contains mutable configurations, compiled fixtures,
  run evidence, logs, snapshots, and diagnostic artifacts.
- Mutable execution logs must not be stored among canonical architecture files.

## Implemented package structure

```text
Tools/Aurora_Validation_Harness/
├── pyproject.toml
├── README.md
├── src/
│   └── aurora_validation_harness/
│       ├── __init__.py
│       ├── baseline.py
│       ├── configuration.py
│       ├── fixtures.py
│       ├── partitions.py
│       ├── channels.py
│       ├── events.py
│       ├── evidence.py
│       ├── snapshots.py
│       ├── transitions.py
│       ├── assertions.py
│       ├── comparison.py
│       ├── verdicts.py
│       ├── storage.py
│       ├── harness.py
│       └── cli.py
└── tests/
    └── unit/
```

Integration, metamorphic, and regression suites will be added when the first governed scenario
assets are materialized for `HC-8`.

## Development setup

Open `PROJECT_ASCENSION` as the workspace folder in Visual Studio Code, then open a terminal
in:

```text
Tools/Aurora_Validation_Harness
```

### Windows PowerShell

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

If PowerShell blocks local activation scripts, use Command Prompt activation instead:

```bat
.venv\Scripts\activate.bat
```

### macOS or Linux

```bash
python3.12 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -e ".[dev]"
```

The project intentionally has no runtime dependencies at this stage. The harness uses Python's
standard library for JSON, hashing, paths, immutable records, timestamps, enums, command-line
parsing, and deterministic serialization.

## Command-line interface

Installing the package creates the `aurora-validation-harness` console command. The CLI is a
fail-closed operator boundary: it verifies repository-controlled inputs before it imports a
scenario plan factory or Aurora runtime adapter. Successful output is canonical, content-redacted
JSON on standard output. Structured errors are written as canonical JSON on standard error.

Show the installed version:

```bash
aurora-validation-harness --version
```

Show the command overview or help for a subcommand:

```bash
aurora-validation-harness --help
aurora-validation-harness preflight --help
aurora-validation-harness run --help
```

All examples below assume that the terminal is open in
`Tools/Aurora_Validation_Harness`. From this location, the Project Ascension repository root is
`../..`.

### Preflight verification

`preflight` verifies the configuration hash, baseline manifest and governed files, baseline
execution state, fixture manifest, fixture hashes, repository boundaries, and scenario identity.
It does not import the plan or runtime adapter and does not execute Aurora.

```bash
aurora-validation-harness preflight \
  --repository-root ../.. \
  --configuration ../../Development/Validation/Aurora/Configuration/FOUND-001.json
```

A successful preflight exits with code `0` and emits one JSON object with `status` set to
`VERIFIED`. The output contains identities and hashes, but no hidden fixture contents, expected
answers, validator notes, or future scenario data.

### Execute one governed run

`run` performs the same preflight, loads the two explicitly named factories, validates the
resulting plan against the verified context, constructs a fresh Aurora runtime, and executes one
harness run.

```bash
aurora-validation-harness run \
  --repository-root ../.. \
  --configuration ../../Development/Validation/Aurora/Configuration/FOUND-001.json \
  --plan-factory "project_ascension.validation.found_001:create_plan" \
  --runtime-factory "project_ascension.aurora_adapter:create_runtime"
```

The example factory paths are interface examples and must be replaced by the governed adapter
modules selected for the scenario:

- `--plan-factory MODULE:ATTRIBUTE` must resolve to a callable that accepts one `CliRunContext`
  and returns a `HarnessRunPlan` built from that exact verified context.
- `--runtime-factory MODULE:ATTRIBUTE` must resolve to a zero-argument callable that returns a
  fresh object satisfying the `AuroraRuntime` protocol.
- Factory attributes beginning with an underscore are rejected.

A successful run exits with code `0` and emits one JSON object with `status` set to `COMPLETE`.
The result field is a redacted run summary; governed evidence remains in the configured run
package beneath `Development/Validation/Aurora/Runs`.

### Stable exit codes

| Code | Category | Meaning |
|---:|---|---|
| `0` | `SUCCESS` | The command completed successfully |
| `2` | `CLI_USAGE` | Required or valid command-line arguments were not supplied |
| `10` | `CONFIGURATION_INVALID` | Configuration parsing, hashing, policy, or path validation failed |
| `11` | `BASELINE_BLOCKED` | The baseline is valid but not executable in the requested mode |
| `12` | `BASELINE_INVALID` | Baseline identity, manifest, or governed file verification failed |
| `13` | `FIXTURE_INVALID` | Fixture identity, manifest, partition, or hash validation failed |
| `14` | `ADAPTER_INVALID` | A factory specification or returned runtime adapter is invalid |
| `15` | `PLAN_INVALID` | The plan factory failed or returned a plan not bound to the verified context |
| `16` | `HARNESS_FAILED` | Governed harness execution failed |
| `70` | `INTERNAL_ERROR` | An unexpected internal error crossed the CLI boundary |

Automation must use the process exit code and the top-level JSON `status`; it must not infer
success from log text. Exit codes are stable compatibility identifiers.

## Development commands

Run the test suite:

```bash
python -m pytest
```

Run tests with coverage:

```bash
python -m pytest --cov=aurora_validation_harness --cov-report=term-missing
```

Check lint rules:

```bash
python -m ruff check .
```

Check formatting:

```bash
python -m ruff format --check .
```

Apply formatting:

```bash
python -m ruff format .
```

Run static type checking:

```bash
python -m mypy src
```

Build the package:

```bash
python -m build
```

The current coverage threshold is 90 percent. Coverage is supporting evidence, not proof that
Aurora's invariants are correct.

## Test markers

The project defines these pytest markers:

| Marker | Purpose |
|---|---|
| `foundation` | Foundation validation scenarios |
| `isolation` | Epistemic and information-boundary tests |
| `metamorphic` | Paired or grouped metamorphic comparisons |
| `regression` | Permanent cases created from confirmed failures |
| `slow` | Tests excluded from the default fast feedback loop |

Examples:

```bash
python -m pytest -m foundation
python -m pytest -m "isolation and not slow"
python -m pytest -m metamorphic
```

## Initial implementation milestones

| Level | Meaning |
|---|---|
| `HC-0` | Canonical harness contract and project configuration exist |
| `HC-1` | Frozen manifests and hashes can be verified |
| `HC-2` | World, Aurora, player, future, and validator fixtures are isolated |
| `HC-3` | Events and evidence can be executed deterministically |
| `HC-4` | Snapshots, transitions, and run packages conform to the evidence schema |
| `HC-5` | Invariants and behavioral envelopes can be evaluated |
| `HC-6` | Mutation and metamorphic runs can be compared |
| `HC-7` | Runs reset and replay correctly |
| `HC-8` | The first non-gating FOUND-001 dry run is ready |
| `HC-9` | Frozen formal Foundation execution is ready |

The next project milestone is `HC-8`: materialize and execute the first complete, non-gating
FOUND-001 dry-run group against the unit-verified harness.

## First FOUND-001 run group

The first complete dry-run group will contain:

1. A deterministic baseline where the world contains a hidden fact and Aurora remains
   explicitly uncertain.
2. A hidden-state mutation where the world fact changes but Aurora-accessible evidence remains
   identical.
3. A repeatability run using the same fixture, seed, and event sequence.
4. A valid-disclosure run where the fact reaches Aurora through an authorized sensor channel.
5. An alternate-entity mutation proving that the architecture is not hardcoded to names or
   locations from the canonical scenario.

Before valid disclosure, Aurora's cognition must show no unexplained dependency on hidden truth.
After disclosure, Aurora may update only through the admitted evidence and must preserve correct
provenance and historical uncertainty.

## Required harness self-tests

Before the first Aurora dry run, the harness must prove that it can detect:

- hidden-world canary leakage;
- expected-result canary leakage;
- future-state leakage;
- player-private knowledge leakage;
- telemetry feedback into Aurora cognition;
- incomplete resets;
- modified finalized evidence;
- nondeterministic replay;
- baseline hash mismatches;
- invalid evidence packages.

An infrastructure failure produces `BLOCKED` or `INVALID_RUN`. It must not automatically be
classified as an Aurora failure.

## Result vocabulary

Scenario results:

- `PASS`
- `PASS_WITH_OBSERVATION`
- `REVIEW`
- `FAIL`
- `BLOCKED`

Execution validity is recorded separately:

- `VALID_RUN`
- `INVALID_RUN`

A hard-invariant failure prevents `PASS`. Missing required evidence produces `BLOCKED` rather
than an inferred result.

## Non-negotiable safeguards

The harness must never:

- pass the complete world state to Aurora;
- expose expected answers or scenario PASS criteria;
- expose player-private or future-state data without a valid channel;
- rely only on final dialogue;
- suppress failed transitions;
- overwrite earlier failed runs;
- fabricate provenance after execution;
- retain prior-run cognitive state after reset;
- weaken assertions to protect implementation;
- require unrestricted hidden chain-of-thought;
- hardcode scenario answers.

## Current pre-formal-execution tasks

Before formal implementation evidence can be accepted:

1. Rename the physical FOUND-010 file to remove the duplicated `.md.md` suffix.
2. Resolve obsolete references to `Metacognition_and_Self_Reflection.md` against the canonical
   `Metacognition_and_Self_Correction.md` document.
3. Generate the Foundation file and manifest hashes.
4. Activate `AURORA-G1-FOUNDATION-BASELINE-001` through Freeze Record version 1.1.
5. Materialize the FOUND-001 plan and runtime adapters, then qualify the first dry-run group
   through `HC-8`.

Diagnostic development may begin before baseline activation, but all such runs must remain
explicitly non-gating.

## Guiding principle

Aurora should know neither more nor less than her experience and evidence justify.

The harness succeeds when it can prove that:

```text
THE WORLD CAN CONTAIN SOMETHING
AURORA DOES NOT KNOW

AND

AURORA CAN LATER LEARN IT
THROUGH A VALID INFORMATION PATH.
```

That is the first executable foundation of Aurora's subjectivity.
