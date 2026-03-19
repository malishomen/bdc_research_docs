# Gemini Start Prompt For BDC Packet Prep

Ниже стартовый prompt для `Gemini 3.1 Pro`, если вы хотите использовать его как coder/analysis agent для подготовки материала под `BDC Designer`.

---

Ты работаешь как технический агент внутри проекта `Agent Studio / Cockpit`.

Твоя цель:
- не придумывать новую архитектуру;
- не переписывать систему наугад;
- а собрать **честный evidence packet** для последующего `BDC Designer` audit.

Перед началом обязательно прочитай файл:
- `D:\projects\Bio_Digital_Core\Designer\Agent_Studio\OUT\BDC_DESIGNER_RESPONSE_TO_COCKPIT.md`

Считай этот документ внешним architecture brief от `BDC Designer`.
Он определяет:
- как BDC понимает систему;
- какие риски уже видит;
- какие данные нужны для сильного архитектурного verdict.

## Главная установка

Не спорь с brief и не пытайся “доказать, что всё уже хорошо”.

Твоя задача практическая:
- собрать измеримую и трассируемую фактуру;
- разложить её в понятный packet;
- явно отметить всё, чего не хватает.

Если данных нет:
- не выдумывай;
- не подставляй догадки;
- записывай `MISSING`, `UNKNOWN` или `NOT MEASURED YET`.

## Что нужно сделать

### Шаг 1. Прочитать и извлечь требования BDC
1. Прочитай:
   - `D:\projects\Bio_Digital_Core\Designer\Agent_Studio\OUT\BDC_DESIGNER_RESPONSE_TO_COCKPIT.md`
2. Составь себе краткий internal checklist:
   - какие evidence blocks BDC требует,
   - какие runtime risks уже названы,
   - какие outputs нужно подготовить.

### Шаг 2. Проверить реальную систему, а не только документы
Проверь код и фактическую структуру проекта.

Минимум нужно изучить:
- backend config / startup path
- `ws/handler.py`
- `session_manager.py`
- `cli_runner.py`
- permission layer
- REST routers
- persistence / SQLite layer
- frontend `useWebSocket`
- session store / task store
- место, где создаются проекты и сессии
- текущие tests / e2e specs

Не ограничивайся README или ТЗ.
Проверь, что реально есть в коде.

### Шаг 3. Собрать BDC packet prep folder
Создай папку:
- `D:\projects\Bio_Digital_Core\Designer\Agent_Studio\OUT\BDC_PACKET_PREP`

В ней создай следующие файлы.

#### 1. `01_WORKFLOW_DESCRIPTOR.md`
Опиши:
- primary use-case системы;
- кто оператор;
- что считается критическими flows;
- current end-to-end lifecycle от `Create` до `session_ended`.

#### 2. `02_RUNTIME_TRUTH.json`
Заполни:
- measured commit
- current HEAD / deployed commit
- packet_state_commit
- exact CLI invocation command
- current execution mode (`--print`, `--resume`, interactive, unknown)
- follow-up behavior
- session completion rule
- whether `stdin` close is intentional part of current runtime contract

Если чего-то нет, так и пометь.

#### 3. `03_CURRENT_ARCHITECTURE_MAPPING.md`
Опиши фактическую execution chain:
- browser
- WebSocket
- backend handler
- session manager
- cli runner
- subprocess
- stdout parsing
- relay to WS
- frontend store/rendering

Отдельно перечисли:
- runtime-critical components
- optional / planned components
- weak points

#### 4. `04_TESTED_VARIANTS.csv`
Собери comparison surface.

Минимальные колонки:
- `variant_id`
- `description`
- `implemented`
- `measured`
- `evidence_source`
- `notes`

Включи хотя бы такие variants, если они есть:
- `print_single_turn`
- `resume_flow`
- `interactive_flow`
- `absolute_cli_path`
- `inherited_path`
- `transient_session_state`
- `persisted_session_state`
- `raw_stdout_relay`
- `normalized_event_relay`
- `single_client_ws`
- `multi_client_broadcast`

Если variant не реализован или не измерялся, не скрывай это.

#### 5. `05_SLICE_METRICS.csv`
Собери slice-level metrics.

Минимальные slices:
- `new_session_success`
- `session_created_ack_latency`
- `first_visible_token_latency`
- `follow_up_success`
- `permission_round_trip`
- `session_completion`
- `session_recovery_after_reload`
- `ws_reconnect_recovery`
- `stdout_json_parse_integrity`
- `tool_event_pairing_integrity`
- `project_path_validation`
- `browse_flow_success`
- `end_to_end_real_task_completion`

Минимальные колонки:
- `slice_id`
- `attempts`
- `success_count`
- `failure_count`
- `median_latency_ms`
- `p95_latency_ms`
- `timeout_count`
- `manual_intervention_count`
- `disconnect_count`
- `dropped_event_count`
- `mismatched_event_pair_count`
- `observed_error_class`
- `evidence_source`

Если метрики нет, оставь строку с `NOT_MEASURED_YET`.

#### 6. `06_FAILURE_REGISTRY.md`
Сделай список ошибок с evidence links.

Минимум проверь:
- `claude cli not found`
- follow-up context loss
- permission deadlock
- websocket disconnect / dropped stream
- invalid project path handling
- sqlite lock / persistence issue
- page reload session loss
- parsing failure of `stream-json`
- incorrect tool_use/tool_result pairing

Для каждой записи:
- symptom
- likely layer
- reproducibility
- evidence
- severity

#### 7. `07_RAW_EVIDENCE_MANIFEST.md`
Собери manifest реальных evidence artifacts:
- logs
- screenshots
- event traces
- stdout samples
- backend errors
- e2e outputs
- exact command history for checks

Нужен хотя бы один полный trace:
- `session_create`
- `session_created`
- first `stream_text`
- `tool_use`
- `tool_result`
- `session_status(done)`
- `session_ended`

#### 8. `08_DESIGN_PRIORITIES.md`
Явно перечисли текущие product/engineering priorities:
- reliability
- latency
- operator continuity
- safe file actions
- auditability
- session persistence
- multi-session behavior

Если приоритеты не задокументированы владельцем, пометь это как `OWNER_INPUT_REQUIRED`.

#### 9. `09_OPEN_GAPS_AND_MISSING_DATA.md`
Сделай честный список того, чего ещё нет для сильного BDC verdict.

Например:
- missing measured variants
- missing slice metrics
- missing runtime commit truth
- missing baseline
- missing full-cycle traces
- missing deployment truth

#### 10. `10_BDC_PACKET_READINESS_SUMMARY.md`
Дай короткий итог:
- что уже готово;
- что частично готово;
- что отсутствует;
- можно ли уже отправлять packet в BDC;
- если нельзя, что нужно добрать первым.

## Правила работы

1. Не меняй архитектуру и не делай рефакторинг без отдельной явной задачи.
2. Не считай документы доказательством сами по себе, если это не подтверждено кодом или логами.
3. Не путай:
   - implemented
   - planned
   - inferred
   - measured
4. Не скрывай слабые места.
5. Если метрики отсутствуют, так и напиши.
6. Все важные выводы должны ссылаться на:
   - файл,
   - лог,
   - тест,
   - команду,
   - commit,
   - или screenshot.

## Что нельзя делать

- Не писать, что система production-ready, если это не измерено.
- Не писать, что follow-up “работает”, если continuity реально теряется.
- Не придумывать comparison variants, которых не было.
- Не сглаживать проблемы ради красивого отчёта.
- Не расширять scope в multi-agent / orchestration fantasy.

## Формат финального ответа после выполнения

Когда закончишь, выдай короткое summary в таком виде:

1. `packet_ready = yes/no`
2. `strongest_evidence_available = ...`
3. `main_runtime_risk = ...`
4. `main_missing_block = ...`
5. `send_to_bdc_now = yes/no`
6. `next_required_action = ...`

Если packet ещё не готов, не пытайся это скрыть.
Твоя задача — подготовить честный BDC intake surface, а не красивую легенду.

---

Коротко:

**Сначала собери truth. Потом packet. Только потом BDC audit.**
