# TASK-QUEEN-OPT BRIEF REPORT

## Scope
Remote optimization of Queen server (laptop, Ubuntu 24.04 LTS) to reduce fan noise,
disable dead GPU, minimize unnecessary services, and establish baseline monitoring.

## Changes Applied

### 1. GPU: nouveau blacklisted (GT 740M — physically dead)
- Created `/etc/modprobe.d/blacklist-nouveau.conf`
- Updated initramfs
- **Verified post-reboot:** `lsmod | grep nouveau` → empty (module not loaded)

### 2. Swappiness: 60 → 10
- Runtime: `sysctl vm.swappiness=10`
- Persistent: `/etc/sysctl.d/99-bdc-swappiness.conf`
- **Verified post-reboot:** `cat /proc/sys/vm/swappiness` → `10`

### 3. Disabled unnecessary services
- `ModemManager.service` → stopped + disabled + masked
- `snapd.service` → stopped + disabled + masked
- `snapd.socket` → stopped + disabled + masked
- `snapd.apparmor.service` → stopped + disabled + masked
- `snapd.snap-repair.timer` → stopped + disabled + masked
- **Verified:** `systemctl is-enabled` → `masked` for all

### 4. lm-sensors installed
- `apt-get install lm-sensors` + `sensors-detect` (auto-accept)
- **Verified:** `sensors` output shows CPU temp, fan RPM, battery voltage

### 5. Docker cleanup
- `docker image prune -a -f` — removed unused images

### 6. Monitoring deployed (prior session)
- `~/bdc/monitoring/queen_health.sh` — JSONL telemetry (CPU temp, fan, load, RAM, GPU, Docker)
- `bdc-queen-health.timer` — systemd user timer, runs every 5 minutes
- `~/bdc/monitoring/queen_health_report.sh` — parses JSONL, generates summary

## Verification (L0)

### Pre-reboot
```
swappiness: 10 ✓
ModemManager: masked ✓
snapd: masked ✓
lm-sensors: /usr/bin/sensors ✓
blacklist-nouveau.conf: exists ✓
initramfs: updated ✓
nouveau module: still loaded (expected, needs reboot)
```

### Post-reboot
```
uptime: 05:33:16 up 6 min, load average: 1.29, 0.87, 0.36
nouveau: NOT LOADED ✓
sensors: CPU 56°C, fan 2600 RPM (post-boot normal)
swappiness: 10 ✓
Docker containers: all 4 UP (cloudflared, postgres, redis, core) ✓
Cloudflare tunnel: registered (fra10, fra12) ✓
Memory: 628Mi / 11Gi used ✓
Swap: 0B used ✓
```

## Queen Server Specs (post-optimization)
| Parameter | Value |
|---|---|
| CPU | Intel Core i5-4200U @ 1.60GHz (2C/4T, max 2.6GHz) |
| RAM | 12 GB (628 MB used idle) |
| Swap | 4 GB (swappiness=10) |
| GPU | DISABLED (GT 740M dead, nouveau blacklisted) |
| Disk | 98 GB total, 9.1 GB used (10%) |
| OS | Ubuntu 24.04 LTS, kernel 6.8.0-101-generic |
| Network | WiFi wlp3s0f0 @ 192.168.1.100 |
| Docker | 4 containers (cloudflared, postgres, redis, hive-core) |
| CF Tunnel | Active, registered fra10/fra12 |

## Compute Topology Summary

| Node | Role | CPU | GPU | RAM | Location | Access |
|---|---|---|---|---|---|---|
| **Queen** (laptop) | Orchestrator | i5-4200U 2C/4T | None (disabled) | 12 GB | LAN .100 | SSH + CF tunnel |
| **Local PC** (workstation) | Compute | i7-6700 4C/8T | GTX 1080 Ti 11GB | 24 GB | Local | Direct |
| **MacBook M4 Pro** | Future compute | M4 Pro | M4 Pro GPU | TBD | Remote city | CF tunnel (planned) |

## Artifacts
- `/etc/modprobe.d/blacklist-nouveau.conf` (on Queen)
- `/etc/sysctl.d/99-bdc-swappiness.conf` (on Queen)
- `/tmp/queen_optimize_20260228T052243Z.log` (on Queen)
- `~/bdc/monitoring/queen_health.sh` (on Queen)
- `~/bdc/monitoring/queen_optimize.sh` (on Queen)
- `tools/hive_core_mvp/tools/monitoring/queen_optimize.sh` (repo)
- `tools/hive_core_mvp/tools/monitoring/queen_health.sh` (repo)
- `tools/hive_core_mvp/tools/monitoring/install_health_timer.sh` (repo)
- `tools/hive_core_mvp/tools/monitoring/queen_health_report.sh` (repo)

## Risks / Limitations
- **WiFi-only networking**: Queen uses WiFi (`wlp3s0f0`), which is less reliable than Ethernet.
  Mitigation: CF tunnel reconnects automatically.
- **Fan noise diagnosis ongoing**: Need 24-48h of monitoring data to establish baseline and
  identify peak triggers. Current post-boot: 2600 RPM @ 56°C is normal.
- **Physical maintenance needed**: Laptop is ~12 years old; thermal paste replacement and
  dust cleaning would further reduce temps/noise (requires physical access).
- **PyTorch not installed on Local PC**: GTX 1080 Ti is available but PyTorch/CUDA not yet configured.

## Rollback
- `nouveau`: remove `/etc/modprobe.d/blacklist-nouveau.conf` + `sudo update-initramfs -u` + reboot
- `swappiness`: remove `/etc/sysctl.d/99-bdc-swappiness.conf` + `sudo sysctl vm.swappiness=60`
- Services: `sudo systemctl unmask <service> && sudo systemctl enable <service>`
