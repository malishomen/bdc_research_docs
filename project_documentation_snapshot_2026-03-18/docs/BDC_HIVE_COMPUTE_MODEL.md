# BDC HIVE Compute Model — CPU Queen + GPU Drones Architecture

**Version:** 1.0  
**Status:** ARCHITECTURE EXTENSION  
**Last Updated:** 2026-01-27  
**Type:** Architecture Extension  
**Related:** BDC_HIVE_ARCHITECTURE.md, ARCHITECTURE.md, POPULATION_AND_SCALING.md

---

## Executive Summary

BDC HIVE Compute Model extends the distributed island-model architecture (BDC_HIVE_ARCHITECTURE.md) with a **CPU-Queen + GPU-Drones** compute model. CPU servers act as Queens (orchestration, storage, validation), while clients with GPU act as Drones (parallel computation, hypothesis exploration).

**Core Innovation:** Separation of orchestration (CPU) and computation (GPU) enables scalable distributed learning while maintaining security and validation through the Queen's authoritative control.

---

## Architecture Overview

### Node Roles (Extended)

#### Queen Node (CPU Server)

**Responsibilities:**
- **Orchestration:** Coordinate distributed experiments across Drones.
- **Storage:** Maintain canonical state and checkpoints.
- **Validation:** Validate all Drone results before acceptance.
- **API Management:** Provide web interface for task submission.
- **Resource Management:** Allocate tasks to Drones based on availability.

**Characteristics:**
- **Hardware:** CPU-focused (orchestration, not computation).
- **Storage:** Persistent, authoritative (canonical state).
- **Trust:** Trusted (runs canonical BDC code).
- **Availability:** High availability (redundancy, failover).

**Compute Model:**
- **Primary:** CPU-based orchestration.
- **Secondary:** Minimal GPU (optional, for validation only).

#### Drone Node (GPU Client)

**Responsibilities:**
- **Parallel Computation:** Execute GPU-accelerated training runs.
- **Hypothesis Exploration:** Test multiple hypotheses in parallel.
- **Result Reporting:** Report results to Queen for validation.
- **Checkpoint Management:** Request/upload checkpoints from/to Queen.

**Characteristics:**
- **Hardware:** GPU-focused (computation, not orchestration).
- **Storage:** Ephemeral (can be replaced).
- **Trust:** Untrusted (may run modified code).
- **Availability:** Stateless (can be replaced).

**Compute Model:**
- **Primary:** GPU-accelerated computation.
- **Secondary:** CPU (for coordination with Queen).

---

## Compute Model: CPU Queen + GPU Drones

### Design Principle

**Separation of Concerns:**
- **CPU (Queen):** Orchestration, validation, storage (low compute, high coordination).
- **GPU (Drones):** Parallel computation, exploration (high compute, low coordination).

**Benefits:**
- **Scalability:** Add GPU Drones as needed (horizontal scaling).
- **Security:** Queen maintains control (authoritative state).
- **Efficiency:** GPU Drones optimized for computation.

### Compute Flow

```
User submits task via web interface
    ↓
Queen validates task (CPU)
    ↓
Queen allocates task to available GPU Drone
    ↓
GPU Drone executes computation (GPU)
    ↓
GPU Drone reports results to Queen
    ↓
Queen validates results (CPU)
    ↓
Queen accepts/rejects results
    ↓
Queen updates canonical state (CPU)
```

---

## Web Interface for Task Submission

### User Interface

**Task Submission Form:**
- **Experiment Type:** Select experiment (PiStream v3, Quaternary Logic, etc.).
- **Parameters:** Configure experiment parameters.
- **Resource Limits:** Set time/resource constraints.
- **Priority:** Set task priority (normal/high/low).

**Task Status Dashboard:**
- **Queued Tasks:** Tasks waiting for Drone allocation.
- **Running Tasks:** Tasks currently executing on Drones.
- **Completed Tasks:** Tasks finished (with results).
- **Failed Tasks:** Tasks that failed (with error messages).

**Results Viewing:**
- **Metrics:** View experiment metrics (fitness, diversity, etc.).
- **Visualizations:** View learning curves, agent performance.
- **Download:** Download results (JSON, CSV, etc.).

### API Endpoints

**Task Submission:**
```
POST /api/tasks/submit
Request: {
    "experiment_type": "pistream_v3",
    "parameters": {...},
    "resource_limits": {
        "max_time": 3600,
        "max_gpu_memory": 8192
    },
    "priority": "normal"
}
Response: {
    "task_id": "...",
    "status": "queued",
    "estimated_start": "2026-01-28T12:00:00Z"
}
```

**Task Status:**
```
GET /api/tasks/{task_id}/status
Response: {
    "task_id": "...",
    "status": "running",
    "progress": 0.65,
    "current_episode": 65,
    "estimated_completion": "2026-01-28T13:00:00Z"
}
```

**Results Retrieval:**
```
GET /api/tasks/{task_id}/results
Response: {
    "task_id": "...",
    "status": "completed",
    "metrics": {...},
    "results_url": "/api/tasks/{task_id}/results/download"
}
```

---

## Pre-Installed Configurations

### NVIDIA GPU Support

**Pre-Installed Packages:**
- CUDA toolkit (version TBD).
- cuDNN (version TBD).
- PyTorch with CUDA support.
- TensorFlow with GPU support (optional).

**Configuration:**
- GPU memory allocation limits.
- Power limit settings (75% default).
- Temperature monitoring.

**Validation:**
- GPU availability check.
- CUDA version verification.
- Memory capacity verification.

### AMD GPU Support

**Pre-Installed Packages:**
- ROCm toolkit (version TBD).
- PyTorch with ROCm support.
- TensorFlow with ROCm support (optional).

**Configuration:**
- GPU memory allocation limits.
- Power limit settings.
- Temperature monitoring.

**Validation:**
- GPU availability check.
- ROCm version verification.
- Memory capacity verification.

### CPU-Only Support

**Pre-Installed Packages:**
- CPU-only PyTorch.
- NumPy, SciPy (CPU-optimized).

**Configuration:**
- CPU core allocation.
- Memory limits.

**Validation:**
- CPU availability check.
- Memory capacity verification.

---

## User Resource Limits

### Time Limits

**Default Limits:**
- **Normal Priority:** 1 hour maximum.
- **High Priority:** 4 hours maximum.
- **Low Priority:** 15 minutes maximum.

**Enforcement:**
- Queen monitors task execution time.
- Automatic termination if limit exceeded.
- Graceful shutdown (save checkpoint before termination).

### Resource Limits

**GPU Memory Limits:**
- **Default:** 8GB per task.
- **Maximum:** 16GB per task (requires approval).
- **Enforcement:** Queen allocates tasks based on available GPU memory.

**CPU Limits:**
- **Default:** 4 cores per task.
- **Maximum:** 8 cores per task (requires approval).
- **Enforcement:** Queen allocates tasks based on available CPU cores.

### User Quotas

**Daily Quotas:**
- **Default:** 10 tasks per day.
- **Maximum:** 50 tasks per day (requires approval).
- **Enforcement:** Queen tracks user task counts.

**Monthly Quotas:**
- **Default:** 100 tasks per month.
- **Maximum:** 500 tasks per month (requires approval).
- **Enforcement:** Queen tracks user task counts.

---

## Security and Validation

### Result Validation

**All Drone results MUST be validated by Queen:**

1. **Cryptographic Proof:**
   - Signature verification.
   - Hash chain validation.

2. **Constraint Compliance:**
   - Check against kill-criteria.
   - Verify resource limits.
   - Validate parameter ranges.

3. **Reproducibility:**
   - Verify PiStream seeds (if applicable).
   - Validate deterministic execution.

4. **Statistical Validity:**
   - Check sample sizes.
   - Verify confidence intervals.

**Invalid Results:**
- Rejected by Queen.
- Drone marked as untrusted.
- Task requeued (if applicable).

### Redundancy Validation

**Multiple Drones run same task with different seeds:**

1. **Consensus:**
   - ≥(N+1)/2 Drones must agree (within tolerance).
   - N = number of redundant Drones (N≥3).

2. **Tolerance Thresholds:**
   - Fitness: ±0.05 (5% tolerance).
   - Diversity: ±0.02 (2% tolerance).
   - Signal-to-noise: ±0.01 (1% tolerance).

3. **Failure Handling:**
   - If consensus not reached: Reject results, mark Drones as untrusted.
   - If consensus reached: Accept results, update canonical state.

---

## Client Boundaries

### What Clients Can Do

**Allowed:**
- Submit tasks via web interface.
- View task status and results.
- Download results (read-only).
- Request experiments (via Queen validation).

**Restrictions:**
- Cannot modify canonical state.
- Cannot bypass kill-criteria.
- Cannot override resource limits.
- Cannot access other users' tasks (unless authorized).

### What Clients Cannot Do

**Forbidden:**
- Direct access to Queen state.
- Bypass validation.
- Modify checkpoints.
- Access other users' data (unless authorized).

**Enforcement:**
- Queen validates all requests.
- Authentication/authorization required.
- Rate limiting prevents abuse.

---

## Implementation Status

**Current Status:** DESIGN PHASE

**Not Yet Implemented:**
- Web interface for task submission.
- GPU Drone client code.
- CPU Queen orchestration logic.
- Resource limit enforcement.
- Pre-installed GPU configurations.

**Future Work:**
- Implement web interface (React/Vue.js frontend).
- Implement Queen orchestration (Python backend).
- Implement GPU Drone client (Python + CUDA/ROCm).
- Implement resource limit enforcement.
- Create pre-installed GPU configurations (Docker images).
- Implement redundancy validation.
- Implement user authentication/authorization.

---

## Relationship to Other Documents

### BDC_HIVE_ARCHITECTURE.md

**Extension:** This document extends BDC_HIVE_ARCHITECTURE.md with:
- CPU Queen + GPU Drones compute model.
- Web interface for task submission.
- Pre-installed GPU configurations.
- User resource limits.

**Compatibility:** Fully compatible with existing HIVE architecture.

### ARCHITECTURE.md

**Alignment:** Implements distributed scaling (BDC HIVE) as optional extension.

**Task Classes:** Supports all task classes (Class 1, 2, 3) via GPU Drones.

### POPULATION_AND_SCALING.md

**Integration:** Implements Population Governor concept for distributed scaling.

**Limits:** Enforces agent count limits per task class across distributed system.

---

## Future Enhancements

### Extensions

1. **Multi-Queen Consensus:** Multiple Queens with consensus-based state.
2. **Dynamic Drone Allocation:** Automatic Drone scaling based on workload.
3. **Priority Queues:** Advanced task prioritization and scheduling.
4. **Cost Tracking:** Track compute costs per user/task.

### Research Questions

1. **Optimal Queen/Drone Ratio:** What ratio maximizes throughput?
2. **Resource Allocation:** How to allocate resources optimally?
3. **Fault Tolerance:** How to handle Drone failures gracefully?
4. **Security:** How to prevent malicious Drones from compromising system?

---

## References

- **BDC_HIVE_ARCHITECTURE.md:** Base HIVE architecture (Queen/Drone roles, minimal-trust API).
- **ARCHITECTURE.md:** BDC architecture and task classes.
- **POPULATION_AND_SCALING.md:** Population limits and scaling rules.
- **RESEARCH_METHODOLOGY.md:** Validation requirements and kill-criteria.

---

**BDC_HIVE_COMPUTE_MODEL.md Status:** ARCHITECTURE EXTENSION  
**Next Review:** After implementation begins or major design changes  
**Implementation Priority:** MEDIUM (optional extension, post-core validation)
