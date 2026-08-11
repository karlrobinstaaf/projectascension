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
| Implementation level | `HC-0 — Contract Only` |
| Initial scenario | `AURORA-SCN-FOUND-001` |
| Validation gate | `GATE 1 — FOUNDATION` |
| Python requirement | Python 3.12 or newer |
| Runtime dependencies | None |
| Formal execution | Not started |

The repository currently contains the project configuration and canonical implementation
contracts. Executable harness modules and tests are the next development phase.

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

## Planned package structure

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
    ├── unit/
    ├── integration/
    ├── metamorphic/
    └── regression/
```

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

The project intentionally has no runtime dependencies at this stage. The initial harness
should use Python's standard library for JSON, hashing, paths, immutable records, timestamps,
enums, command-line parsing, and deterministic serialization.

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

The next code milestone is `HC-1`: implement baseline and manifest verification.

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

## Current pre-implementation tasks

Before formal implementation evidence can be accepted:

1. Rename the physical FOUND-010 file to remove the duplicated `.md.md` suffix.
2. Resolve obsolete references to `Metacognition_and_Self_Reflection.md` against the canonical
   `Metacognition_and_Self_Correction.md` document.
3. Generate the Foundation file and manifest hashes.
4. Activate `AURORA-G1-FOUNDATION-BASELINE-001` through Freeze Record version 1.1.
5. Implement and qualify the harness through `HC-8`.

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
