# GIT ARTIFACT POLICY — Bio_Digital_Core

## 🚫 Запрещено хранить в Git
- Model checkpoints (*.pt, *.ckpt, *.bin)
- Training artifacts (results/, checkpoints/, artifacts/)
- GPU logs, profiler outputs
- Any file > 50 MB

## ✅ Разрешено хранить в Git
- Source code
- Configuration files
- metrics.json (≤ 10 MB)
- Reports (*.md, *.txt)
- Documentation

## 🧠 Правило проекта
Git = knowledge & structure  
Artifacts = external storage only

Нарушение этого правила считается критической ошибкой процесса.
