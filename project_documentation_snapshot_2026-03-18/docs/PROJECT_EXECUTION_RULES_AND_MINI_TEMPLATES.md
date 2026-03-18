# BDC: Единый свод правил ведения проекта, логов и GitHub + мини-шаблоны

Дата актуализации: 2026-02-17

## 1. Что проверено (источники правил)

Приоритет источников (сверху вниз):
1. `CANON.md`
2. Корневые нормативные файлы: `SEMANTICS.md`, `SEED_POLICY.md`, `KILL_CRITERIA.yaml`, `REPRODUCIBILITY.md`, `VERSIONING.md`
3. ADR: `decisions/ADR-0001-docs-sources-of-truth.md`, `decisions/ADR-0002-bep1-scope-gating.md`, `decisions/ADR-0003-append-only-agents-weekly.md`
4. Политики: `docs/GIT_ARTIFACT_POLICY.md`, `docs/TRAINING_RUNTIME_RULES.md`
5. Операционные отчеты/чеклисты: `README.md`, `WEEKLY_STATUS.md`, `AGENTS_LOG.md`, `docs/GITHUB_SETTINGS_REPORT_2026-01-07.md`

## 2. Краткий результат проверки (as-is)

- Правило append-only для `AGENTS_LOG.md` и `WEEKLY_STATUS.md` зафиксировано в ADR-0003 и в заголовках файлов.
- Требование "без артефактов нет утверждений" закреплено в `CANON.md` и фактически поддерживается структурой `reports/analysis/TASK_*`.
- Политика внешнего хранения тяжелых артефактов явно есть (`docs/GIT_ARTIFACT_POLICY.md`, `docs/TRAINING_RUNTIME_RULES.md`, `.gitignore`).
- Правила GitHub-настроек в репозитории описаны как чеклист, но их фактическая верификация в `docs/GITHUB_SETTINGS_REPORT_2026-01-07.md` отмечена как `UNVERIFIED`.
- В `AGENTS_LOG.md` шаблонная секция `Entry Template` расположена не в самом конце файла (историческое отклонение от ADR-0003).
- В `README.md` рабочей веткой указан `test`, но фактически в репозитории уже есть работа в `main` и `hive` (операционная практика шире изначального правила).

## 3. Единые правила ведения задач (обязательно)

### 3.1. Доказательность и L0-first
- Любое утверждение о результате должно опираться на артефакты, логи, метрики и ссылки на коммит/тег.
- Нельзя публиковать выводы "успех/улучшение/масштаб" без проверяемых данных.

### 3.2. Обязательный пакет после каждой задачи
После завершения задачи должны быть обновлены/созданы:
- Код/конфиги (если задача кодовая).
- `AGENTS_LOG.md`: новая строка в конце таблицы.
- `WEEKLY_STATUS.md`: новая `##` секция в конце файла.
- Отчет задачи в `reports/analysis/` (минимум `*_BRIEF_REPORT.md`; при необходимости `*_MONITORING_COMMANDS.md`, `*_L0_*`, `*_MAIN_MERGE_REPORT.md`).
- Если изменен принцип/архитектурное решение: ADR в `decisions/` или `docs/adr/`.
- Если изменились команды/зависимости/среда воспроизведения: обновить `REPRODUCIBILITY.md` тем же коммитом.

### 3.3. Append-only дисциплина логов
- `AGENTS_LOG.md`: только добавление новых строк таблицы в конец, без редактирования старых строк.
- `WEEKLY_STATUS.md`: только добавление новых `##` секций в конец, без переписывания предыдущих.
- При конфликте мержа: сохраняется объединение обеих сторон (union append-only), ничего не теряется.

### 3.4. Git/ветки/коммиты
- Один логический смысл = один атомарный коммит.
- Формат коммита: с Task ID (`TASK-XXXX` или `TASK-XXXX: ...`).
- Перед long-run: `git status` чистый, `.gitignore` проверен.
- `main` используется как стабильный checkpoint; активная разработка обычно в рабочей ветке (`test`/feature/`hive` по задаче).

### 3.5. Политика артефактов
Запрещено коммитить:
- `results/`, `checkpoints/`, `artifacts/`, большие runtime-логи.
- модельные файлы (`*.pt`, `*.ckpt`, `*.bin`) и любые файлы >50MB.
Разрешено:
- исходники, конфиги, документация, компактные метрики/отчеты.

### 3.6. Change control (R0/R1/R2)
- `R0`: рефактор без изменения численных результатов, нужен регресс.
- `R1`: изменение метода/метрик/порогов, нужна новая версия эксперимента.
- `R2`: изменение гипотезы/kill-criteria, нужна ревизия roadmap + ADR.

### 3.7. GitHub как ведем (репо-практика)
Целевое состояние (из чеклиста в `docs/GITHUB_SETTINGS_REPORT_2026-01-07.md`):
- Default branch: рабочая ветка проекта (исторически `test`).
- PR settings: auto-delete head branches ON, squash merge ON, merge commit OFF.
- Security: Dependency graph + Dependabot alerts/updates включены.

Важно: статус GitHub-настроек в репозитории нужно периодически пере-валидировать вручную (UI/API), так как последний отчет содержит `UNVERIFIED`.

## 4. Мини-чеклист завершения задачи

Использовать как DoD-шаблон:
- [ ] Код/документы задачи готовы.
- [ ] Прогоны/проверки выполнены, команды и выходы зафиксированы.
- [ ] Создан/обновлен `reports/analysis/TASK_xxxx_*`.
- [ ] Добавлена строка в `AGENTS_LOG.md`.
- [ ] Добавлена `##` секция в `WEEKLY_STATUS.md`.
- [ ] Проверено, что тяжелые артефакты не попали в git.
- [ ] При необходимости обновлены `REPRODUCIBILITY.md`/ADR/спеки.

## 5. Мини-шаблоны

### 5.1. Шаблон commit message
```text
TASK-XXXX: краткая суть изменения
```
или
```text
feat(TASK-XXXX): краткая суть
fix(TASK-XXXX): краткая суть
chore(TASK-XXXX): краткая суть
```

### 5.2. Шаблон строки AGENTS_LOG
```markdown
| YYYY-MM-DDTHH:MM:SSZ | AGENT_NAME | TASK-XXXX | SUCCESS/FAILURE/PARTIAL | branch_name | commit_hash | artifact1, artifact2, ... | cmd1; cmd2; ... | notes |
```

### 5.3. Шаблон секции WEEKLY_STATUS
```markdown
## TASK-XXXX: Краткое название (YYYY-MM-DD)

- **Status:** SUCCESS/FAILURE/PARTIAL
- **Branch/HEAD:** <branch> @ <short_hash>
- **Что сделано:** <1-3 пункта>
- **Проверки:** <команды и итог>
- **Артефакты:** `path1`, `path2`, ...
- **Риски/что дальше:** <кратко>
```

### 5.4. Шаблон BRIEF_REPORT
```markdown
# TASK-XXXX BRIEF REPORT

## Scope
- Что входило в задачу
- Что не входило

## Changes
- Файл/модуль: что изменено и зачем

## Verification (L0)
- Команда: `...`
- Результат: PASS/FAIL + факты

## Artifacts
- `path/to/file1`
- `path/to/file2`

## Risks / Limitations
- ...

## Rollback
- Шаги отката
```

### 5.5. Шаблон MONITORING_COMMANDS
```markdown
# TASK-XXXX MONITORING COMMANDS

## Environment
- cwd: `...`
- branch: `...`

## Commands
1. `command_1`
2. `command_2`
3. `command_3`

## Expected signals
- Что считаем PASS
- Что считаем FAIL
```

### 5.6. Шаблон MAIN_MERGE_REPORT
```markdown
# TASK-XXXX MAIN MERGE REPORT

## Merge metadata
- source branch: `...`
- target branch: `main`
- pre-merge HEADs: `...`
- merge commit: `...`

## Conflict resolution
- Какие файлы конфликтовали
- Как решено

## Post-merge checks
- `pytest -q` -> PASS/FAIL
- дополнительные проверки

## Included artifacts
- `...`
```

### 5.7. Шаблон ADR
```markdown
## ADR-XXXX: Название

Date: YYYY-MM-DD

## Context
...

## Decision
...

## Alternatives
...

## Consequences
...

## Revisit criteria
...
```

## 6. Рекомендуемая операционная конвенция (с 2026-02)

Чтобы убрать расхождения между старым README и текущей практикой:
- Фиксировать в отчете каждой задачи фактическую рабочую ветку (`test`, feature-ветка, `hive` и т.д.).
- Для merge в `main` всегда делать отдельный merge-report + release notes.
- Раз в неделю делать короткий "repo-process audit":
  - актуальность GitHub settings,
  - соблюдение append-only,
  - отсутствие крупных артефактов в git.

## 7. Быстрый anti-fail список

- Не коммитить runtime-логи и датасеты.
- Не менять старые записи в `AGENTS_LOG.md` и `WEEKLY_STATUS.md`.
- Не объявлять SUCCESS без проверочных команд и артефактов.
- Не менять методику эксперимента без обновления спеки/ADR.
- Не оставлять `pending-commit` без follow-up записи с реальным hash.
