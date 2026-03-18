# HIVE Laptop Queen Ubuntu Migration (Runbook)

Date: 2026-02-18
Scope: preparation-only. This document does not claim OS install was executed by Codex.

## 1. Target Architecture
- New Queen host: laptop with Ubuntu LTS (recommended 24.04 LTS).
- Runtime: Docker Compose stack from `tools/hive_core_mvp`.
- Public ingress: Cloudflare Tunnel (`queen.bdc-hive.com`, `viz.bdc-hive.com`, `control.bdc-hive.com`).
- Backups: every 30 minutes to external disk label `HIVE`.

## 2. BIOS/UEFI and Install Checklist
1. Enable UEFI boot.
2. Disable vendor fast-boot if it blocks USB/Linux boot.
3. Install Ubuntu LTS (minimal install acceptable).
4. Partition guidance (HDD):
- `/` ext4: 80-120 GB minimum
- `swap`: 8-16 GB (if RAM <=16GB use 16GB)
- `/var/lib/docker`: allocate enough free space for images/volumes
5. Create admin user and set strong password.

## 3. First Boot Hardening
```bash
sudo apt update && sudo apt -y upgrade
sudo apt -y install openssh-server ufw ca-certificates curl gnupg git jq
sudo systemctl enable --now ssh
sudo ufw allow OpenSSH
sudo ufw enable
```

## 4. Docker + Compose
```bash
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
sudo chmod a+r /etc/apt/keyrings/docker.gpg
echo \
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \
  $(. /etc/os-release && echo $VERSION_CODENAME) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt -y install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
sudo usermod -aG docker $USER
newgrp docker
```

## 5. Clone and Deploy
```bash
mkdir -p ~/projects && cd ~/projects
git clone <YOUR_GITHUB_REPO_URL> Bio_digital_core
cd Bio_digital_core
git checkout hive
cd tools/hive_core_mvp
cp .env.example .env
```

Edit local `.env` (never commit secrets):
- `POSTGRES_PASSWORD`
- `HIVE_INVITE_CODE`
- `STATS_ADMIN_TOKEN`
- `CONTROL_OWNER_TOKEN`
- `CLOUDFLARED_TUNNEL_TOKEN` (if using integrated ingress profile)

Bring up stack:
```bash
docker compose up -d --build
docker compose ps
curl -sS http://127.0.0.1:8080/v1/ping
```

## 6. Cloudflare Tunnel Bring-Up
Prepare local `.env` files (not committed):
- `tools/hive_core_mvp/tools/ingress/cloudflared/.env`
- `tools/hive_core_mvp/tools/ingress/cloudflared_viz/.env`
- `tools/hive_core_mvp/tools/ingress/cloudflared_control/.env`

Start ingress containers:
```bash
cd ~/projects/Bio_digital_core/tools/hive_core_mvp/tools/ingress/cloudflared
docker compose up -d
cd ../cloudflared_viz && docker compose up -d
cd ../cloudflared_control && docker compose up -d
```

Verify endpoints:
```bash
curl -i https://queen.bdc-hive.com/v1/ping
curl -i https://viz.bdc-hive.com/LATEST.json
curl -i -X POST https://viz.bdc-hive.com/control/stop_emergency -H 'Content-Type: application/json' -d '{"mode":"emergency"}'
```
Expected: viz JSON works; volunteer stop endpoint denied (404/403).

## 7. Linux Backup Automation (30 min)
Scripts:
- `tools/hive_core_mvp/tools/backup/linux/hive_backup.sh`
- `tools/hive_core_mvp/tools/backup/linux/install_systemd_timer.sh`
- `tools/hive_core_mvp/tools/backup/linux/restore_verify.sh`

Mount external disk label HIVE (example):
```bash
sudo mkdir -p /mnt/HIVE
sudo mount -L HIVE /mnt/HIVE
```

Manual backup test:
```bash
cd ~/projects/Bio_digital_core
bash tools/hive_core_mvp/tools/backup/linux/hive_backup.sh --backup-root /mnt/HIVE/HIVE_BACKUPS --compose-dir tools/hive_core_mvp
```

Install timer:
```bash
bash tools/hive_core_mvp/tools/backup/linux/install_systemd_timer.sh
systemctl --user list-timers | grep bdc-hive-backup
```

Restore verification (safe test DB):
```bash
bash tools/hive_core_mvp/tools/backup/linux/restore_verify.sh /mnt/HIVE/HIVE_BACKUPS/db/<latest>.sql.gz
```

## 8. GitHub Update / Redeploy Procedure
Manual safe update:
```bash
cd ~/projects/Bio_digital_core
git fetch origin
git checkout hive
git pull --ff-only origin hive
cd tools/hive_core_mvp
docker compose up -d --build
```

Rollback:
```bash
cd ~/projects/Bio_digital_core
git log --oneline -n 20
git reset --hard <known_good_commit>
cd tools/hive_core_mvp
docker compose up -d --build
```

## 9. Done-When Checklist
- [ ] Ubuntu boots and SSH reachable.
- [ ] `docker compose up -d --build` healthy on laptop.
- [ ] `https://queen.bdc-hive.com/v1/ping` reachable externally.
- [ ] `https://viz.bdc-hive.com/LATEST.json` works, stop endpoint denied.
- [ ] Backups appear every 30 minutes on external disk.
- [ ] Weekly restore verification executed and logged.

## 10. Cutover Safety
- Keep current PC as active Queen until all checklist items are green.
- If laptop fails, revert DNS/tunnel traffic to current PC and continue operations.
