[DEPRECATED] Superseded by:
- `docs/project/project_main_doc.md` (master project document)
- `docs/project/project_roadmap.md` (active roadmap)

This file is preserved for historical continuity and must not be treated as current roadmap authority.

---

Ниже - полная дорожная карта до состояния "Инфузория-туфелька / Paramecium MVP (TRL-3)": к концу будет полностью рабочий контур для старта первичных тестов (детерминизм, сидирование PiStream, прогоны N?30 сидов, метрики, kill-criteria, артефакты результатов).



Definition of Done для состояния "Инфузория-туфелька" (TRL-3)



Готово, если одновременно выполнено:



Симулятор 2D-среды (препятствия, градиенты ресурса/токсина, статический/динамический режим) детерминирован по ENV_PISTREAM.



Агент: кинематика + столкновения + сенсоры (3-5 "ресничек"-лучей, 1-2 градиентных датчика) + контролируемый шум по NOISE_PISTREAM.



qcore (S={T,F,MY,MN} + conflict_flag) реализован как библиотека, с truth tables и unit/regression тестами.



Геном + VM: четверичный алфавит, задокументированные правила интерпретации, покрытие тестами.



Регенерация: формализованные "малые повреждения" + измерение Recovery rate, целевой порог ? 70%.



Evolution loop: популяция/селекция/мутации, строго детерминированные MUT_DECISION_PISTREAM и MUT_MAGNITUDE_PISTREAM.



Экспериментальный прогон одной командой: N?30 сидов  RESULTS/*.csv + детерминированный расчёт метрик + REPORT.md + фиксированные пороги/kill-criteria до запуска.



В репо есть RUN_COMMANDS.md, EXPERIMENT_SPEC.md, DECISIONS/:, и всё логируется в AGENTS_LOG.md.



Всё в ветке test, main не трогаем.



Milestone M0 - Инфраструктура "воспроизводимость по умолчанию"



Цель: чтобы дальше каждое изменение было проверяемым и воспроизводимым.



TASK-0100: Repo hardening под дисциплину



Артефакты



.editorconfig, LICENSE (если нужен), CODEOWNERS (опц.)



RUN_COMMANDS.md (пустой шаблон + правила заполнения)



EXPERIMENT_SPEC.md (шаблон фиксации методики)



DECISIONS/0001-governance.md (main запрещён, работа в test, протокол логов)



Verify



git branch  default test



Файлы присутствуют, AGENTS_LOG.md обновлён



Rollback



revert commit



TASK-0101: CI-гейты (минимум)



Артефакты



GitHub Actions: lint, typecheck, unit-tests, smoke-run (пустой пока)



Verify



PR/Push в test зелёный по gates



Milestone M1 - Библиотека qcore (TRL1-2 внутри TRL-3)



Цель: закрыть базовую математику S={T,F,MY,MN}+conflict строго тестами.



TASK-0200: qcore API + truth tables



Артефакты



qcore/ модуль: NOT/AND/OR/CONSENSUS/CONFLICT + conflict_flag



qcore/__tests__/truth_tables.test.* (референс-таблицы)



Verify



pnpm test (или npm test)  PASS



snapshot/табличные тесты на все комбинации



TASK-0201: qcore regression pack



Артефакты



qcore/__tests__/regression.seeded.test.* (фиксированные кейсы)



Verify



повторный запуск даёт идентичный вывод



Milestone M2 - PiStream и сидирование (детерминизм как контракт)



Цель: единый источник воспроизводимости и разделение потоков.



TASK-0300: PiStream core + split streams



Артефакты



env/pistream.ts (или pistream.py - но выбрать один и закрепить в DECISIONS)



Поддержка потоков: ENV/INIT/NOISE/MUT_DECISION/MUT_MAGNITUDE



unit-тесты на стабильность последовательностей (по фиксированным seed'ам)



Verify



тест "один и тот же seed  те же значения"



тест "разные потоки  разные подпоследовательности, без пересечения контрактов"



TASK-0301: Spec сидов (протокол)



Артефакты



docs/seed-protocol.md (как формируется master seed, как получаются stream-seeds)



Verify



любой эксперимент пишет seed_manifest.json



Milestone M3 - Симулятор среды 2D



Цель: мир + динамика мира + детерминированная генерация.



TASK-0400: World model + генерация (ENV_PISTREAM)



Артефакты



env/world.ts: поле, препятствия, ресурсный градиент, токсин-градиент



env/generate.ts: генерация по ENV_PISTREAM



тест: одинаковый seed  одинаковая world hash (например, stable JSON hash)



Verify



worldHash(seed=123) стабилен



TASK-0401: Step/update (static/dynamic режимы)



Артефакты



env/step.ts (обновление градиентов во времени)



smoke-тест: 1k шагов без NaN/вылетов



Verify



pnpm smoke:env



Milestone M4 - Агент: движение, сенсоры, контроллер



Цель: агент реально "живёт" в мире, сенсит шум, выдаёт решения в qcore-формате.



TASK-0500: Kinematics + collisions



Артефакты



agent/kinematics.ts: движение/поворот, столкновения с препятствиями



Verify



property tests: не проходит сквозь стены; стабильность на 10k шагов



TASK-0501: Сенсоры (ciliary rays + gradient sensors) + NOISE_PISTREAM



Артефакты



agent/sensors.ts



шум строго из NOISE_PISTREAM



тесты: при noise=0 показания детерминированы; при noise>0 - детерминированы относительно seed



Verify



"noise on/off" regression



TASK-0502: Controller skeleton (FSM/мал. сеть) + conflict rule



Артефакты



agent/controller.ts: выдаёт S и conflict_flag



правило: если conflict_flag=1  обязательный safe-override (MVP: снижение скорости/поворот/скан)



Verify



unit-тесты на принудительный override



Milestone M5 - Геном + VM + регенерация



Цель: четверичный геном управляет параметрами/автоматом/регенерацией, всё задокументировано и тестируется.



TASK-0600: Genome encoding (четверичный алфавит) + parser



Артефакты



agent/genome.ts: представление, валидатор, парсер



docs/genome-spec.md: каноническая спецификация интерпретации



Verify



parser round-trip; invalid genome  controlled error



TASK-0601: VM (простая) для исполнения генома



Артефакты



agent/vm.ts: минимальный ISA/интерпретатор (закрепить в docs/genome-spec.md)



тесты на инструкции + детерминизм



Verify



golden tests на вход/выход VM



TASK-0602: Регенерация (ECC/резерв/чексум) + формализация "малых повреждений"



Артефакты



agent/regen.ts: механизм обнаружения повреждений и восстановления



experiments/damage-model.ts: формальные повреждения (bit flips, удаление сегмента длины L, etc.) - фиксируются в EXPERIMENT_SPEC.md



метрика Recovery rate



Verify



unit-тесты на каждый тип повреждения



воспроизводимость восстановления по seed



Milestone M6 - Evolution loop + бейзлайны



Цель: популяция/селекция/мутации детерминированы и сравнимы с baseline.



TASK-0700: Population + selection



Артефакты



evolution/loop.ts: цикл поколений, оценка fitness/utility



UNVERIFIED (нужно зафиксировать в EXPERIMENT_SPEC.md): точная формула utility.

План фиксации: в TASK-0800 (ниже) закрепить формулу utility и штрафы (энергия/токсины/столкновения/"воздержание" при MY/MN если применимо).



Verify



одинаковый seed  одинаковая траектория fitness по поколениям



TASK-0701: Mutations (MUT_DECISION/MUT_MAGNITUDE PiStreams)



Артефакты



evolution/mutate.ts



тест: одинаковые потоки  идентичные мутации (позиции/величины)



Verify



golden mutation log



TASK-0702: Baselines



Артефакты



baseline agents: random walk, greedy gradient-follow (минимум 2)



baseline regen: none / trivial checksum-only



Verify



baseline run produces results CSV



Milestone M7 - Эксперименты "1 командой" + отчёт + kill-criteria



Цель: старт первичных тестов без ручной магии.



TASK-0800: EXPERIMENT_SPEC.md (фиксация методики до запуска)



Артефакты



EXPERIMENT_SPEC.md заполнен:



utility (точная формула)



damage model (типы/параметры L, p)



пороги kill-criteria (в т.ч. Recovery rate ?70%, критерии устойчивого выигрыша по utility)



N=30 сидов, CI/статистика



Verify



документ содержит все пороги до запуска



TASK-0801: Runner + seed manifest + результаты



Артефакты



scripts/run_paramecium.ts (или аналог)



вывод:



RESULTS/run_<timestamp>/seed_manifest.json



RESULTS/run_<timestamp>/raw.csv



Verify



два запуска с одинаковым master seed  байт-в-байт одинаковый raw.csv



TASK-0802: Analysis + Report



Артефакты



analysis/analysis.ts (или analysis.py) - детерминированные метрики



REPORT.md (ссылки на файлы, сводка CI, вывод по kill-criteria)



Verify



pnpm exp:paramecium создаёт полный пакет артефактов



TASK-0803: CI artifact upload



Артефакты



workflow сохраняет RESULTS/ и REPORT.md как CI artifacts



Verify



artifacts доступны в GitHub Actions run



Финальный чек-лист "готово к первичным тестам"



pnpm test  PASS



pnpm lint / pnpm typecheck  PASS



pnpm exp:paramecium --seed <X> --n 30  генерирует RESULTS/*.csv, seed_manifest.json, REPORT.md



Детерминизм подтверждён: повтор запуска с тем же seed даёт те же артефакты



AGENTS_LOG.md содержит записи по всем TASK-xxxx



Все изменения в test, main не тронут



Kill-criteria для "Инфузория-туфелька" (фиксируются заранее в EXPERIMENT_SPEC)



Recovery rate < 70% на "малых повреждениях"  фаза считается проваленной (правим regen/spec, не "подкручиваем пороги").



Ошибки ускоряются по поколениям (positive feedback без коррекции)  стоп/пересбор регенерации.



"Тепличность": работает без шума, ломается при минимальном шуме  стоп/пересмотр сенсоров/контроллера.
