# EXPERIMENT: Visualization — Pac-Man Learning Metaphor

**Version:** 1.0  
**Status:** UX SPECIFICATION  
**Last Updated:** 2026-01-27  
**Type:** User Experience Specification  
**Related:** ui/, ARCHITECTURE.md, WEEKLY_STATUS.md

---

## Executive Summary

Pac-Man visualization provides a simple, intuitive real-time visualization of BDC learning processes using the Pac-Man game metaphor. Agents are represented as Pac-Man characters navigating a maze, with colors indicating their quaternary logic states (YES/NO/MAYBE_YES/MAYBE_NO).

**Core Innovation:** Visual metaphor makes complex learning dynamics accessible to non-technical users while maintaining separation from computation (visualization runs independently).

---

## Motivation: Accessible Learning Visualization

### Problem Statement

**Current State:**
- Learning metrics stored in JSON files.
- Requires technical knowledge to interpret.
- No real-time feedback during training.

**Solution:**
- Visual representation of learning dynamics.
- Real-time updates during training.
- Intuitive metaphor (Pac-Man game).

### Use Cases

1. **Real-Time Monitoring:** Watch learning progress during long training runs.
2. **Debugging:** Identify learning issues visually (stuck agents, convergence problems).
3. **Presentation:** Demonstrate BDC capabilities to non-technical audiences.
4. **Analysis:** Visualize learning patterns and trends.

---

## Pac-Man Metaphor

### Visual Representation

**Agents as Pac-Man Characters:**
- Each agent represented as a Pac-Man character.
- Position in maze represents agent state.
- Movement represents learning progress.

**Maze as Learning Environment:**
- Maze represents problem space.
- Paths represent possible solutions.
- Goals represent optimal solutions.

**Colors as Quaternary States:**
- **Green (YES):** Agent confident, moving toward goal.
- **Red (NO):** Agent avoiding, moving away from goal.
- **Yellow (MAYBE_YES):** Agent exploring, uncertain but optimistic.
- **Blue (MAYBE_NO):** Agent cautious, uncertain and pessimistic.

### Visual Elements

**Pac-Man Characters:**
- Size: Proportional to agent fitness (larger = better).
- Color: Based on quaternary state (green/red/yellow/blue).
- Direction: Movement direction indicates learning direction.

**Maze:**
- Static background (does not change during learning).
- Represents problem structure.
- Goals marked as bright spots.

**Trails:**
- Agent movement trails show learning path.
- Color-coded by state transitions.
- Fade over time (recent paths brighter).

**Metrics Display:**
- Current fitness (average, best, worst).
- Diversity index.
- Entropy.
- Generation/episode number.

---

## Data Source and Updates

### Data Source

**Real Training Logs:**
- Reads from actual experiment results (JSON files).
- No synthetic data generation.
- Ground truth from BDC experiments.

**Supported Formats:**
- `results/wp7_4_extended/metrics.json` (WP7.4 format).
- `results/wp7_5_advanced/metrics.json` (WP7.5 format).
- `results/trl8_cognitive/metrics.json` (TRL-8 format).
- `results/trl9_meta_cognition/metrics.json` (TRL-9 format).

### Update Frequency

**Real-Time Updates:**
- Updates every 1-5 minutes (configurable).
- Reads latest metrics from JSON files.
- Smooth animation between updates.

**Update Strategy:**
- **Polling:** Check file modification time.
- **File Watching:** Watch for file changes (if supported).
- **Manual Refresh:** User-triggered refresh button.

---

## Implementation Architecture

### Separation from Computation

**Design Principle:** Visualization runs independently from computation.

**Computation Layer:**
- Training runs write metrics to JSON files.
- No direct communication with visualization.
- File-based interface only.

**Visualization Layer:**
- Reads metrics from JSON files.
- No impact on training performance.
- Can run on separate machine/client.

### Technology Stack

**Frontend:**
- **Web-Based:** HTML5 + JavaScript (browser-based).
- **Framework:** React or Vue.js (optional, for interactivity).
- **Graphics:** Canvas API or WebGL (for rendering).

**Backend (Optional):**
- **Server:** Lightweight HTTP server (if needed).
- **File Serving:** Serve JSON files to frontend.
- **WebSocket:** Real-time updates (optional).

**Minimal Implementation:**
- Static HTML + JavaScript.
- Reads JSON files directly (CORS permitting).
- No backend required.

---

## User Interface Design

### Main View

**Layout:**
- **Left Panel:** Maze visualization (Pac-Man agents).
- **Right Panel:** Metrics and controls.

**Maze Visualization:**
- Canvas-based rendering.
- Smooth animation (60 FPS target).
- Zoom/pan controls.

**Metrics Panel:**
- Current generation/episode.
- Average fitness.
- Best/worst fitness.
- Diversity index.
- Entropy.
- Agent count.

### Controls

**Playback Controls:**
- **Play/Pause:** Start/stop animation.
- **Speed:** Adjust playback speed (1x, 2x, 5x, 10x).
- **Step:** Step through generations/episodes.
- **Reset:** Return to beginning.

**Display Options:**
- **Show Trails:** Toggle agent movement trails.
- **Show Labels:** Toggle agent ID labels.
- **Color Scheme:** Toggle color coding.
- **Metrics:** Toggle metrics display.

**Data Selection:**
- **Experiment:** Select experiment to visualize.
- **Time Range:** Select generation/episode range.
- **Refresh:** Manual refresh from file.

---

## Performance Requirements

### Client-Side Performance

**Target Performance:**
- **Frame Rate:** 60 FPS (smooth animation).
- **Update Latency:** < 100ms (responsive controls).
- **Memory:** < 100MB (lightweight client).

**Optimization Strategies:**
- **Canvas Optimization:** Efficient rendering (requestAnimationFrame).
- **Data Caching:** Cache parsed JSON data.
- **Lazy Loading:** Load data on demand.
- **Throttling:** Throttle updates to prevent overload.

### Server-Side Performance (If Applicable)

**Target Performance:**
- **Response Time:** < 50ms (fast file serving).
- **Concurrent Users:** Support 10+ simultaneous viewers.
- **Bandwidth:** Minimal (JSON files only).

---

## Data Format Compatibility

### Supported Metrics Formats

**WP7.4 Format:**
```json
{
  "episodes": [...],
  "final_avg_fitness": 0.5847,
  "diversity": 0.2147,
  "agents": [...]
}
```

**WP7.5 Format:**
```json
{
  "metrics": {
    "episodes": [...],
    "final_avg_fitness": 0.6169,
    "diversity": 0.1234
  },
  "agents": [...]
}
```

**TRL-8 Format:**
```json
{
  "episodes": [...],
  "final_fitness": 0.5805,
  "diversity": 0.2147,
  "agents": [...]
}
```

### Data Mapping

**Agent State → Pac-Man State:**
- Fitness → Pac-Man size.
- Quaternary state → Pac-Man color.
- Position → Maze position (computed from metrics).

**Metrics → Display:**
- Fitness → Numeric display + visual size.
- Diversity → Numeric display + visual spread.
- Entropy → Numeric display + visual uncertainty.

---

## Kill-Criteria

### Primary Kill-Criteria

**1. Performance Degradation:**
```
IF visualization causes > 10% training slowdown:
    KILL: Visualization degrades training performance
```

**2. Client Overload:**
```
IF client memory > 500MB OR frame rate < 30 FPS:
    KILL: Visualization too resource-intensive
```

**3. Data Incompatibility:**
```
IF visualization cannot read > 50% of experiment formats:
    KILL: Visualization incompatible with BDC experiments
```

**4. User Confusion:**
```
IF user testing shows > 30% confusion rate:
    KILL: Visualization fails to communicate learning dynamics
```

### Success Criteria

**Minimum Requirements:**
- Frame rate > 30 FPS.
- Client memory < 200MB.
- Supports > 80% of experiment formats.
- User testing confusion rate < 20%.

**Target Metrics:**
- Frame rate > 60 FPS.
- Client memory < 100MB.
- Supports 100% of experiment formats.
- User testing confusion rate < 10%.

---

## Relationship to BDC Architecture

### Task Class Alignment

**Visualization belongs to Infrastructure:**
- Not core validation (Class 1).
- Not cognitive layer (Class 2).
- Not knowledge layer (Class 3).
- Infrastructure tool for monitoring and analysis.

### Integration Points

- **ui/:** Existing UI components (evolution_monitor.py).
- **ARCHITECTURE.md:** Infrastructure layer.
- **WEEKLY_STATUS.md:** Status tracking.
- **results/:** Experiment results (data source).

### Separation from Computation

**Critical:** Visualization must not impact computation.

- **No Direct Coupling:** File-based interface only.
- **Independent Execution:** Can run on separate machine.
- **Optional:** Training works without visualization.

---

## Implementation Roadmap

### Phase 1: Prototype

- Basic Pac-Man rendering (static).
- Simple metrics display.
- File reading (one format).

### Phase 2: Animation

- Smooth agent movement.
- Trail rendering.
- Playback controls.

### Phase 3: Multi-Format Support

- Support all experiment formats.
- Format detection.
- Data mapping.

### Phase 4: Optimization

- Performance optimization.
- Memory management.
- Smooth 60 FPS rendering.

### Phase 5: Polish

- UI/UX improvements.
- User testing.
- Documentation.

---

## Future Enhancements

### Extensions

1. **3D Visualization:** Three-dimensional maze representation.
2. **VR Support:** Virtual reality visualization (future).
3. **Interactive Exploration:** Click agents for detailed info.
4. **Comparison Mode:** Compare multiple experiments side-by-side.

### Research Questions

1. **Metaphor Effectiveness:** Does Pac-Man metaphor improve understanding?
2. **Update Frequency:** What update frequency maximizes usefulness?
3. **Visual Complexity:** What level of detail is optimal?
4. **User Preferences:** What features do users find most valuable?

---

## References

- **ui/evolution_monitor.py:** Existing visualization (Streamlit-based).
- **ARCHITECTURE.md:** BDC architecture and infrastructure.
- **WEEKLY_STATUS.md:** Status tracking and reporting.
- **results/:** Experiment results directory.

---

**EXPERIMENT_VISUALIZATION_PACMAN.md Status:** UX SPECIFICATION  
**Next Review:** After prototype implementation or major design changes  
**Implementation Priority:** LOW (infrastructure tool, optional)
