# Polyglot Codebase Knowledge Graph

> Generated offline by **readmenator**. Supports C, C++, Python, Go, Rust, JS/TS, Java, C#, Shell, PHP, Dart, GDScript, Nim, ASM.
> No LLMs. No tokens. Pure static analysis.

**Total Files Parsed:** 2 | **Total Symbols Extracted:** 1 | **Total Imports:** 3

## Structural Knowledge Map
```mermaid
graph TD
    classDef mod fill:#1e1e1e,stroke:#ff6666,stroke-width:2px,color:#fff;
    classDef cls fill:#2d2d2d,stroke:#4ec9b0,stroke-width:2px,color:#fff;
    classDef fn fill:#333,stroke:#dcdcaa,stroke-width:1px,color:#dcdcaa;
    classDef ext fill:#111,stroke:#666,stroke-dasharray: 5 5,color:#aaa;
    main_py["main.py (py)"]
    class main_py mod;
    main_py_main["main"]
    class main_py_main fn;
    main_py --> main_py_main
    simulator_py["simulator.py (py)"]
    class simulator_py mod;
    ext_qiskit["qiskit"]
    class ext_qiskit ext;
    main_py -.->|imports| ext_qiskit
    ext_qiskit_visualization["qiskit.visualization"]
    class ext_qiskit_visualization ext;
    main_py -.->|imports| ext_qiskit_visualization
    ext_numpy["numpy"]
    class ext_numpy ext;
    main_py -.->|imports| ext_numpy
```

---

## Architecture Reference

### PY (2 files)

#### `main.py`
**Path:** `main.py`

**Functions:**
- `main` (line 5)

#### `simulator.py`
**Path:** `simulator.py`

*No symbols extracted*
