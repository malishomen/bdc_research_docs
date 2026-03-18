# TASK-1000 REPRO RUN COMMANDS (L0)

## Exact command to deploy Hive
```bash
cd ~/bdc/Bio_digital_core/tools/hive_core_mvp
docker compose up -d --build
docker compose ps
curl -sS http://127.0.0.1:8080/v1/ping
```

## Exact command to restart Hive
```bash
cd ~/bdc/Bio_digital_core/tools/hive_core_mvp
docker compose restart hive-core postgres redis
docker compose ps
```

## Exact command to run local training
```powershell
cd d:\projects\Bio_Digital_Core\Bio_digital_core
python experiments/exp_0017_comprehension_v0_cloze/src/train.py `
  --dataset_root D:\datasets\bdc\simplified_wiki_v0\20260201\full_build `
  --max_steps 2000 `
  --seed 12345 `
  --log_every 50 `
  --eval_every 200 `
  --run_tag main
```

## Exact command to run Drone manually
```powershell
cd d:\projects\Bio_Digital_Core\Bio_digital_core\tools\hive_core_mvp\drone_client
.\START_HIVE.bat
```

## Exact command to clean environment
```bash
cd ~/bdc/Bio_digital_core/tools/hive_core_mvp
docker compose logs --tail 100
docker image prune -f
docker container prune -f
```

## Exact command to full reset
```bash
cd ~/bdc/Bio_digital_core/tools/hive_core_mvp
docker compose down -v --remove-orphans
docker volume prune -f
docker network prune -f
```

## Exact command to reproduce API tests
```powershell
cd d:\projects\Bio_Digital_Core\Bio_digital_core
python -m pytest -q tests/test_localhost_server_loopback_only.py tests/test_localhost_stop_endpoint_loopback_token.py
curl.exe -i https://viz.bdc-hive.com/v1/ping
curl.exe -i https://viz.bdc-hive.com/dist/LATEST.json
```

## Notes
- Commands above are copied from current runbooks/specs and verified command history.
- `full reset` is destructive and should be used only by operator decision.
