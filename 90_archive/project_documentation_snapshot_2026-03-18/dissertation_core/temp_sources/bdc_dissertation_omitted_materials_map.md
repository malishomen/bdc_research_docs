# Материалы, данные и эксперименты BDC, не вошедшие в текущий draft диссертации

**Документ:** omission register к draft `D:\projects\Bio_Digital_Core\Temp\bdc_dissertation_draft.md`
**Дата:** 2026-03-18
**Статус:** рабочая аналитическая карта

---

## 1. Назначение документа

Этот документ фиксирует, какие существенные данные, экспериментальные результаты, отрицательные результаты, продуктовые артефакты и переходы проекта **не вошли** или вошли лишь косвенно в текущий draft диссертации.

Он не заменяет саму диссертацию и не переписывает её структуру. Его цель — дать отдельную карту omission'ов, чтобы:
- не потерять важные фазы проекта;
- не выдать раннюю научную линию за полную историю BDC;
- отделить verified research line от productized spinout `BDC Designer`;
- подготовить будущие приложения, ограничения и честное описание pivot points.

---

## 2. Что уже есть в draft

Текущий draft хорошо покрывает следующие слои:
- кватернарную логику `S = {T, F, MY, MN}`;
- qcore и formal foundations;
- DNA-inspired memory как гипотезу `H2`;
- diversity-first evolution как гипотезу `H3`;
- `Paramecium MVP` / раннюю платформу цифрового организма;
- verification-first дисциплину;
- kill-критерии как исследовательскую норму.

Но draft почти не покрывает следующие фактические пласты истории проекта.

---

## 3. Крупные omission-блоки

## 3.1. Кризис сложности и формальная неудача старого режима отбора

### Что отсутствует в draft
В draft есть эволюционная часть, но почти отсутствует главный отрицательный результат проекта: при старом fitness regime рост сложности оказался **математически заблокирован**.

### Почему это важно
Это не локальный неуспех, а один из самых сильных результатов всей истории BDC:
- проект не просто “не добился лучшего v2”; 
- проект доказал, что сам selection physics делал архитектурный рост невозможным.

### Ключевой факт
Из `TASK-1400B`:
- при режиме `fitness = accuracy - 0.01 * complexity`
- для всех проверенных `v2*` линий
- `required_accuracy_to_beat_v1 > 1.0`
- следовательно, победа `v2*` над `v1_speciation` в этом режиме **математически невозможна**.

### Основные источники
- `D:\projects\Bio_Digital_Core\Bio_digital_core\reports\analysis\TASK-1400B-COMPLEXITY-AUDIT-ADDENDUM\TASK-1400B_BRIEF_REPORT.md`
- `D:\projects\Bio_Digital_Core\Bio_digital_core\reports\analysis\TASK-1400-COMPLEXITY-AUDIT\TASK-1400_BRIEF_REPORT.md`

### Что стоит добавить в диссертацию или вынести в приложение
- отдельный подраздел `Negative Result / Complexity Barrier`;
- формальное описание why `v2*` blocked;
- последствия для гипотезы `H3` и для старой selection physics;
- честный вывод: не вся diversity-first линия опровергнута, но старый режим fitness — да.

---

## 3.2. Формальное закрытие `hidden_rule` как продуктовой линии

### Что отсутствует в draft
В draft нет управленческого и научного pivot'а: линия `EDP1 hidden_rule` была формально закрыта **как product direction**, но оставлена как лабораторный benchmark.

### Почему это важно
Без этого история проекта в диссертации выглядит линейной, хотя фактически проект прошёл через сильную фазу falsification and closure.

### Ключевой факт
Из `ADR-0004`:
- `hidden_rule` закрыт как product strategy;
- `v1_speciation` зафиксирован как permanent baseline;
- гипотезы `H1-H3` не закрыты полностью, а перенесены в новую линию.

### Основной источник
- `D:\projects\Bio_Digital_Core\Bio_digital_core\decisions\ADR-0004-hidden-rule-closure.md`

### Что стоит добавить
- раздел `Governance Pivot`;
- таблицу: что закрыто / что сохранено / что перенесено;
- distinction между falsified task-line и still-open research hypotheses.

---

## 3.3. Restricted BDC как научное извлечение полезного ядра после кризиса

### Что отсутствует в draft
Draft почти полностью остаётся в ранней биологической и логико-памятной рамке. В нём почти нет фазы, где из surviving evidence была извлечена **restricted theory**.

### Почему это важно
Именно эта фаза объясняет, как проект не распался после crisis phase, а превратился из общей deep-tech гипотезы в ограниченную, но полезную теорию архитектурных priors.

### Ключевые результаты
Из `TASK-6890`:
- построен architecture design rulebook;
- сформирована strategy selection matrix;
- извлечены global + family-specific design rules.

Из `TASK-6900`:
- собрана матрица `SUPPORTED / FALSIFIED` claims;
- formalized scope statement:
  - BDC как restricted theory causal equilibrium + architecture priors;
  - explicit rejection of universal portable transition-law interpretation.

### Основные источники
- `D:\projects\Bio_Digital_Core\Bio_digital_core\reports\analysis\TASK-6890-CAUSAL-ARCHITECTURE-DESIGN-RULEBOOK\TASK-6890_BRIEF_REPORT.md`
- `D:\projects\Bio_Digital_Core\Bio_digital_core\reports\analysis\TASK-6900-PAPER-READY-RESTRICTED-BDC-CONSOLIDATION\TASK-6900_BRIEF_REPORT.md`

### Что стоит добавить
- отдельную главу или приложение `Restricted BDC`;
- явную формулировку, что после кризиса проект перешёл от общей цифровой биологии к bounded architecture theory;
- перечень positive claims и rejected claims.

---

## 3.4. Spinout в `BDC Designer`: tooling prototype, CLI и реальные architecture recommendations

### Что отсутствует в draft
Draft не описывает фазу, где BDC был операционализирован как практический architecture recommendation tool.

### Почему это важно
Это не маркетинговый довесок, а фактический результат проекта: продуктовая линия `BDC Designer` стала operational spinout из restricted-BDC theory.

### Ключевые результаты
Из `TASK-6980`:
- сформирован tool spec:
  - входы: task family, causal asymmetry, DAG depth/branching, budget tier;
  - выходы: recommended role count, role weights, strategy mode, confidence, caution flags.

Из `TASK-7020`:
- `BDC Designer CLI` создан как практический инструмент;
- `supported = true`;
- `schema_ok_rate = 1.0`;
- `match_rate_vs_prototype = 1.0`.

### Основные источники
- `D:\projects\Bio_Digital_Core\Bio_digital_core\reports\analysis\TASK-6980-BDC-TOOLING-PROTOTYPE\TOOL_SPEC.md`
- `D:\projects\Bio_Digital_Core\Bio_digital_core\reports\analysis\TASK-7020-BDC-DESIGNER-CLI\TASK-7020_BRIEF_REPORT.md`

### Что стоит добавить
- раздел `Tooling Spinout`;
- схему перехода: theory -> rulebook -> prototype -> CLI;
- честную рамку: это уже applied system, а не только scientific hypothesis platform.

---

## 3.5. Реальный deployment case study

### Что отсутствует в draft
В диссертации нет реального case-study, где `BDC Designer` сравнивался с baseline и hybrid deployment arms.

### Почему это важно
Это первый мост между теорией и практикой. Если диссертация хочет показать судьбу проекта целиком, этот слой нельзя терять.

### Ключевые результаты
Из `TASK-7030`:
- selected case: `planner-executor-checker workflow`;
- baseline (D1):
  - `time_to_target = 36.0h`
  - `quality = 0.701`
  - `search_cost = 145.0`
  - `iterations = 13`
- CLI only (D2):
  - `time_to_target = 29.88h`
  - `quality = 0.7556`
  - `search_cost = 116.0`
  - `iterations = 10`
- CLI + hybrid (D3):
  - `time_to_target = 24.203h`
  - `quality = 0.8036`
  - `search_cost = 119.48`
  - `iterations = 7`
- `D3` beat baseline on all 3 core metrics.

### Основной источник
- `D:\projects\Bio_Digital_Core\Bio_digital_core\reports\analysis\TASK-7030-CASE-STUDY-REAL-DEPLOYMENT\TASK-7030_BRIEF_REPORT.md`

### Что стоит добавить
- отдельный empirical appendix про реальный deployment case;
- discussion, что BDC уже давал applied value как architecture prior system.

---

## 3.6. Полная продуктовая зрелость `BDC Designer v2`

### Что отсутствует в draft
Draft не покрывает тот факт, что `BDC Designer` дошёл до benchmark-validated и release-gated состояния.

### Почему это важно
Если диссертация описывает весь проект, а не только раннюю фазу, то текущий mainline result нельзя опускать.

### Ключевые результаты
Из `TASK-7550`:
- `BDC CLI v2` доведён до release-ready operator surface;
- packet-first и raw-case entry modes верифицированы;
- benchmark suite подтверждён (`v2_better_case_count = 5`);
- release validation summary подтвердил required checks.

### Основные источники
- `D:\projects\Bio_Digital_Core\Bio_digital_core\reports\analysis\TASK-7550-BDC-CLI-V2-PRODUCTIZATION-AND-RELEASE\TASK-7550_BRIEF_REPORT.md`
- `D:\projects\Bio_Digital_Core\Bio_digital_core\docs\project\BDC_DESIGNER_FREEZE_STATE.md`

### Что стоит добавить
- короткую subsequence `BDC Designer v2 as frozen operational subsystem`;
- distinction between research program and productized subsystem.

---

## 3.7. Реальный клиентский кейс `TextAI_Auto`

### Что отсутствует в draft
В draft нет первого полноценного реального клиентского цикла, который фактически стал решающим источником hardening для `BDC Designer`.

### Почему это важно
`TextAI_Auto` — это не частная консультация, а первый настоящий mixed-evidence case, который:
- проверил BDC на реальном workflow;
- заставил перестроить intake model;
- дал active operational evidence chain.

### Что уже зафиксировано в проекте
`BDC Designer Post-TextAI Roadmap` перечисляет, чему научил проект `TextAI_Auto`:
- folder-based intake вместо идеального packet JSON;
- mixed evidence layers (`measured`, `measured_from_historical_report`, `inferred`, `missing`);
- divergence between historical prior and current runtime truth;
- need for redesign guidance, not only winner selection.

### Основные источники внутри repo
- `D:\projects\Bio_Digital_Core\Bio_digital_core\docs\project\BDC_DESIGNER_POST_TEXTAI_ROADMAP.md`
- `D:\projects\Bio_Digital_Core\Bio_digital_core\docs\project\BDC_DESIGNER_FREEZE_STATE.md`

### Внешние активные клиентские источники
- `D:\projects\Text_AI_auto_check\TextAI_Auto\docs\BDC_REVISION_CHAIN_MASTER.md`
- `D:\projects\Text_AI_auto_check\TextAI_Auto\docs\BDC_PACKET_PREP_CHECKLIST.md`
- `D:\projects\Text_AI_auto_check\TextAI_Auto\docs\BDC_PACKET_CLEANLINESS_REPORT.md`
- `D:\projects\Text_AI_auto_check\TextAI_Auto\docs\bdc_packets\TEXTAI_AUTO_BDC_PACKET_V2_5\README.md`
- `D:\projects\Text_AI_auto_check\TextAI_Auto\docs\bdc_packets\TEXTAI_AUTO_BDC_PACKET_V2_5\TEXTAI_AUTO_BDC_INPUT_PACKET_V2_5.json`
- `D:\projects\Text_AI_auto_check\TextAI_Auto\docs\bdc_packets\TEXTAI_AUTO_BDC_PACKET_V2_5_1\TEXTAI_AUTO_BDC_INPUT_PACKET_V2_5_1.json`

### Ключевые факты active line
`V2.5`:
- provider stability cycle;
- `gemini-2.5-flash = 12/15` accepted;
- `gpt-4o-mini = 2/15`;
- `deepseek-chat = 1/15`.

`V2.5.1`:
- limited rollout;
- `high_ai = 4/5`;
- `mid_ai = 0/4`;
- `low_ai = 0/16` as planned skips/no-op behavior;
- revision chain normalized.

### Что стоит добавить
- приложение `First Client Evidence Chain`;
- отдельный разбор того, как реальный клиент изменил продуктовую оболочку BDC;
- distinction between client governance cleanliness and BDC-native intake compatibility.

---

## 3.8. Пост-TextAI hardening roadmap

### Что отсутствует в draft
В draft нет целого слоя продуктового hardening, возникшего как прямой ответ на `TextAI_Auto`.

### Почему это важно
Это показывает, что BDC не остался исследовательской статической конструкцией, а реально адаптировался к полевому использованию.

### Ключевые hardening направления
Из `BDC_DESIGNER_POST_TEXTAI_ROADMAP.md`:
- folder intake mode;
- evidence-status-aware weighting;
- logical redesign mode;
- measurement gap detector;
- sparse runtime evidence support;
- client packet workflow.

### Основной источник
- `D:\projects\Bio_Digital_Core\Bio_digital_core\docs\project\BDC_DESIGNER_POST_TEXTAI_ROADMAP.md`

### Что стоит добавить
- краткую фазу `Operational Hardening After First Client`.

---

## 3.9. Историческая карта проекта как единая причинная линия

### Что отсутствует в draft
Draft подаёт материал как научную монографию ранней фазы, но не даёт полной causal sequence проекта.

### Почему это важно
Без этого читатель не поймёт, почему BDC пришёл к текущему состоянию и почему `BDC Designer` не является “случайным отклонением”.

### Основной источник
- `D:\projects\Bio_Digital_Core\Bio_digital_core\docs\project\BDC_PROJECT_HISTORY_MAP.md`

### Что стоит добавить
- приложение `Historical Phase Map`;
- timeline с pivot points:
  - genesis;
  - embodiment;
  - maturity;
  - crisis;
  - closure;
  - restricted theory;
  - tooling spinout;
  - client hardening;
  - freeze.

---

## 3.10. Research reboot после `BDC Designer`

### Что отсутствует в draft
Draft не включает новую научную рамку: возвращение к research line после product spinout уже планируется не как продолжение старого `hidden_rule`, а как новый disciplined reboot.

### Почему это важно
Это критично для честной научной позиции: проект не должен выглядеть как будто он всё ещё идёт по старой эволюционной траектории.

### Ключевые источники
- `D:\projects\Bio_Digital_Core\Bio_digital_core\docs\project\BDC_RESEARCH_REBOOT_PLAN.md`
- `D:\projects\Bio_Digital_Core\Bio_digital_core\docs\project\BDC_RESEARCH_REBOOT_CHARTER.md`
- `D:\projects\Bio_Digital_Core\Bio_digital_core\docs\experiments\EXP-0800_SELECTION_PHYSICS_REBOOT_2026-03-17.md`

### Что стоит добавить
- короткий завершающий раздел: `What remains scientifically open after BDC Designer`;
- explicit statement that the next scientific frontier is selection-physics rebuild, not naive continuation of old EDP1 assumptions.

---

## 4. Что из omission'ов наиболее критично для защиты

Если выбирать минимально обязательный пакет, который стоит отразить даже при ограниченном объёме диссертации, то в первую очередь не хватает:

1. **Complexity Barrier / TASK-1400B**
- без него история эволюционной части выглядит неполной и слишком гладкой.

2. **ADR-0004 hidden_rule closure**
- без него не виден формальный pivot.

3. **Restricted BDC formation (TASK-6890 / TASK-6900)**
- без него не видно, как из кризиса родилось полезное теоретическое ядро.

4. **BDC Designer spinout + real deployment case (TASK-7020 / TASK-7030 / TASK-7550)**
- без этого не видно, что проект уже породил working applied subsystem.

5. **TextAI_Auto first client line**
- без этого не видно реального внешнего давления, которое изменило систему.

---

## 5. Что не стоит смешивать в основном тексте

Чтобы диссертация не потеряла научную чистоту, следует не смешивать в одной плоскости:

- ранние гипотезы `H1-H3`;
- отрицательные результаты по старой selection physics;
- restricted-BDC theory;
- `BDC Designer` как прикладной spinout;
- post-TextAI client hardening;
- research reboot.

Лучше подавать это как последовательные фазы:
1. initial research architecture;
2. empirical and negative results;
3. crisis and closure;
4. restricted salvage;
5. tooling/productization;
6. first-client hardening;
7. reboot of scientific line.

---

## 6. Рекомендуемая структура приложения к диссертации

### Appendix A — Negative Results and Closure
- `TASK-1400B`
- `ADR-0004`
- `ADR-0005`

### Appendix B — Restricted BDC Theory
- `TASK-6890`
- `TASK-6900`
- scope statement / claims matrix

### Appendix C — BDC Designer Spinout
- `TASK-6980`
- `TASK-7020`
- `TASK-7030`
- `TASK-7550`
- freeze state

### Appendix D — First Client Evidence (`TextAI_Auto`)
- post-TextAI roadmap
- packet governance line
- `V2.5/V2.5.1`

### Appendix E — Research Reboot
- history map
- reboot plan
- reboot charter
- `EXP-0800`

---

## 7. Главный итог

Текущий draft диссертации хорошо отражает **раннюю научную и формально-архитектурную фазу BDC**, но **не отражает полную историю проекта**.

Наиболее существенные omission'ы:
- формальный отрицательный результат по complexity barrier;
- закрытие `hidden_rule` как product path;
- формирование restricted BDC;
- переход в `BDC Designer`;
- реальный deployment case;
- клиентская линия `TextAI_Auto`;
- исследовательский reboot после freeze.

Если диссертация должна описывать именно **всю историю проекта BDC**, а не только ранний научный слой, эти omission-блоки необходимо либо:
- включить в основной текст;
- либо вынести в системные приложения/appendices;
- либо явно объявить как out-of-scope текущей диссертации.

---

## 8. Канонические источники для расширения

Внутренние:
- `D:\projects\Bio_Digital_Core\Bio_digital_core\reports\analysis\TASK-1400B-COMPLEXITY-AUDIT-ADDENDUM\TASK-1400B_BRIEF_REPORT.md`
- `D:\projects\Bio_Digital_Core\Bio_digital_core\decisions\ADR-0004-hidden-rule-closure.md`
- `D:\projects\Bio_Digital_Core\Bio_digital_core\reports\analysis\TASK-6890-CAUSAL-ARCHITECTURE-DESIGN-RULEBOOK\TASK-6890_BRIEF_REPORT.md`
- `D:\projects\Bio_Digital_Core\Bio_digital_core\reports\analysis\TASK-6900-PAPER-READY-RESTRICTED-BDC-CONSOLIDATION\TASK-6900_BRIEF_REPORT.md`
- `D:\projects\Bio_Digital_Core\Bio_digital_core\reports\analysis\TASK-6980-BDC-TOOLING-PROTOTYPE\TOOL_SPEC.md`
- `D:\projects\Bio_Digital_Core\Bio_digital_core\reports\analysis\TASK-7020-BDC-DESIGNER-CLI\TASK-7020_BRIEF_REPORT.md`
- `D:\projects\Bio_Digital_Core\Bio_digital_core\reports\analysis\TASK-7030-CASE-STUDY-REAL-DEPLOYMENT\TASK-7030_BRIEF_REPORT.md`
- `D:\projects\Bio_Digital_Core\Bio_digital_core\reports\analysis\TASK-7550-BDC-CLI-V2-PRODUCTIZATION-AND-RELEASE\TASK-7550_BRIEF_REPORT.md`
- `D:\projects\Bio_Digital_Core\Bio_digital_core\docs\project\BDC_PROJECT_HISTORY_MAP.md`
- `D:\projects\Bio_Digital_Core\Bio_digital_core\docs\project\BDC_RESEARCH_REBOOT_PLAN.md`
- `D:\projects\Bio_Digital_Core\Bio_digital_core\docs\project\BDC_RESEARCH_REBOOT_CHARTER.md`
- `D:\projects\Bio_Digital_Core\Bio_digital_core\docs\experiments\EXP-0800_SELECTION_PHYSICS_REBOOT_2026-03-17.md`
- `D:\projects\Bio_Digital_Core\Bio_digital_core\docs\project\BDC_DESIGNER_FREEZE_STATE.md`
- `D:\projects\Bio_Digital_Core\Bio_digital_core\docs\project\BDC_DESIGNER_POST_TEXTAI_ROADMAP.md`

Внешние client-evidence источники:
- `D:\projects\Text_AI_auto_check\TextAI_Auto\docs\BDC_REVISION_CHAIN_MASTER.md`
- `D:\projects\Text_AI_auto_check\TextAI_Auto\docs\BDC_PACKET_PREP_CHECKLIST.md`
- `D:\projects\Text_AI_auto_check\TextAI_Auto\docs\BDC_PACKET_CLEANLINESS_REPORT.md`
- `D:\projects\Text_AI_auto_check\TextAI_Auto\docs\bdc_packets\TEXTAI_AUTO_BDC_PACKET_V2_5\README.md`
- `D:\projects\Text_AI_auto_check\TextAI_Auto\docs\bdc_packets\TEXTAI_AUTO_BDC_PACKET_V2_5\TEXTAI_AUTO_BDC_INPUT_PACKET_V2_5.json`
- `D:\projects\Text_AI_auto_check\TextAI_Auto\docs\bdc_packets\TEXTAI_AUTO_BDC_PACKET_V2_5_1\TEXTAI_AUTO_BDC_INPUT_PACKET_V2_5_1.json`
