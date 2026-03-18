# Исследовательский отчёт: применимость внешних материалов к проекту BDC

Дата обновления: 2026-03-18
Источник набора: `D:\projects\Bio_Digital_Core\Temp\research\external`

## 1. Цель отчёта

Разобрать весь внешний набор как рабочий исследовательский пакет для продолжения BDC, а не как формальную библиографию.

Ключевой вопрос:
- что из набора можно прямо импортировать в `BDC Designer`;
- что можно перенести в новую научную линию BDC после reboot;
- какие материалы достаточно надёжны для опоры уже сейчас;
- какие материалы являются восстановленными surrogate-источниками и требуют аккуратной маркировки.

## 2. Главный вывод

После обновления папки набор стал существенно лучше и теперь даёт 5 сильных прикладных направлений:

1. `Calibration + Proper Scoring + Selective Prediction`
- для confidence layer, abstention, guardian, risk-aware routing и evaluation discipline в `BDC Designer`.

2. `Belnap / Many-Valued Semantics`
- для строгой формализации четырёхзначной логики проекта и evidence reasoning.

3. `Diversity Preservation in Evolutionary Optimization`
- для research reboot, особенно для `Selection Physics Rebuild`, speciation и anti-premature-convergence политики.

4. `Error-Correcting Coding`
- для noise-aware memory, control redundancy, packet integrity и защищённого хранения состояния.

5. `DNA Storage / Addressability / Channel Modeling`
- для адресуемой, шумоустойчивой и динамически управляемой памяти в DNA-inspired линии BDC.

Ключевой практический вывод:
- для `BDC Designer` самый прямой следующий импорт: calibration + abstention + generalized risk evaluation;
- для research reboot самый сильный импорт: diversity taxonomy + channel-aware memory + formal four-valued semantics.

## 3. Integrity-аудит обновлённого набора

## 3.1. Канонически читаемые и содержательно релевантные

1. `01_Guo_et_al_2017_On_Calibration_of_Modern_Neural_Networks.pdf`
2. `03_Geifman_ElYaniv_2017_Selective_Classification_for_Deep_Neural_Networks.pdf`
3. `04_Traub_et_al_2024_Overcoming_Common_Flaws_Evaluation_Selective_Classification.pdf`
4. `06_Many_Valued_Logic_SEP_Reference.html`
5. `07_Geisel_Tutorial_Reed_Solomon_Error_Correction_Coding.pdf`
6. `08_Freeman_1996_Introduction_Forward_Error_Correcting_Coding.pdf`
7. `09_Organick_et_al_2018_Random_Access_Large_Scale_DNA_Data_Storage.pdf`
8. `10_Lin_et_al_2020_Dynamic_Scalable_DNA_Information_Storage.pdf`
9. `11_Heckel_et_al_2019_Characterization_DNA_Data_Storage_Channel.pdf`
10. `12_Squillero_Tonda_2016_Divergence_Character_Premature_Convergence.pdf`

## 3.2. Восстановленные surrogate-источники

1. `02_Brier_1950_Verification_Forecasts_Probability.md`
- это не оригинальный facsimile статьи;
- это восстановленная note с корректной библиографией, формулой и вторичным содержательным summary;
- для инженерного исследования использовать можно;
- для строгого академического цитирования желательно позже добыть оригинал или точную репринт-копию.

2. `05_Belnap_1977_A_Useful_Four-Valued_Logic.md`
- это не original PDF chapter;
- это восстановленная note по источнику и вторичным материалам;
- как guide для проектной формализации использовать можно;
- для окончательной академической опоры нужен первичный текст главы.

## 3.3. Что изменилось по сравнению с прошлой ревизией

Исправлены два крупных source defects:
- `04_Traub...pdf` теперь действительно содержит paper про selective classification;
- `12_Squillero_Tonda...pdf` теперь действительно содержит survey по diversity preservation.

Следовательно, прошлое замечание о подмене этих двух файлов больше не актуально.

## 4. Тематический анализ: что именно можно применить

## 4.1. Калибровка, proper scoring и selective prediction

### Источники
- `01_Guo_et_al_2017_On_Calibration_of_Modern_Neural_Networks.pdf`
- `02_Brier_1950_Verification_Forecasts_Probability.md`
- `03_Geifman_ElYaniv_2017_Selective_Classification_for_Deep_Neural_Networks.pdf`
- `04_Traub_et_al_2024_Overcoming_Common_Flaws_Evaluation_Selective_Classification.pdf`

### Что подтверждается по содержанию

#### Guo et al.
Подтверждается:
- современные модели часто overconfident;
- accuracy недостаточна как proxy for trustworthiness;
- temperature scaling — сильный и простой post-hoc baseline;
- ECE, reliability diagrams, NLL, Brier-like tools нужны для оценки confidence.

#### Brier
Подтверждается:
- Brier score — proper scoring rule для вероятностных прогнозов;
- он поощряет честную вероятность, а не только бинарную правильность;
- он естественно подходит для calibration audit.

#### Geifman & El-Yaniv
Подтверждается:
- reject option — полноценная часть классификатора;
- система может управлять `risk vs coverage`;
- high-stakes deployment требует легального abstention mode.

#### Traub et al.
Подтверждается:
- evaluation selective-classification систем на фиксированных working points недостаточна;
- нужна multi-threshold evaluation;
- AURC имеет методологические дефекты;
- generalized risk и `AUGRC` лучше соответствуют задаче, чем простая агрегация selective risk;
- вводятся 5 требований к метрике: task alignment, monotonicity, ranking interpretability, CSF flexibility, error flexibility.

### Что применять в BDC Designer

#### A. Calibration audit
Нужно добавить в `BDC Designer`:
- `Brier score`
- `ECE`
- `reliability table/diagram`
- post-hoc recalibration audit

Объекты оценки:
- architecture recommendation confidence
- deployability confidence
- caution / insufficiency flags

#### B. Selective recommendation
Нужно формализовать класс исходов:
- `recommend`
- `recommend_with_caution`
- `warm_start_only`
- `abstain_need_more_evidence`

Это уже частично есть по смыслу, но не оформлено как полноценная selective-prediction contract.

#### C. Generalized-risk evaluation
Текущий BDC оценивает решения достаточно локально по кейсам.
Следующий уровень зрелости:
- считать не только fixed-threshold success/failure;
- оценивать aggregated risk across decision thresholds;
- уйти от местами слишком грубого reading по `confidence band`.

### Что применять в research reboot
- calibrated accept/reject as part of selection physics;
- система может не принимать решение при слабом evidence;
- это может смягчить старую проблему hard complexity suppression.

### Конкретные шаги
1. Выпустить note `BDC_DESIGNER_CALIBRATION_AND_ABSTENTION_PLAN.md`.
2. Добавить calibration/coverage-risk metrics в benchmark suite.
3. Протестировать generalized-risk evaluation на existing BDC cases.

## 4.2. Четырёхзначная логика и формальная семантика

### Источники
- `05_Belnap_1977_A_Useful_Four-Valued_Logic.md`
- `06_Many_Valued_Logic_SEP_Reference.html`

### Что подтверждается по содержанию

Belnap-line и SEP-обзор вместе дают:
- четыре состояния `T / F / B / N`;
- различие между truth-order и knowledge-order;
- отсутствие explosion при contradiction;
- suitability для inconsistent/incomplete knowledge bases;
- matrix semantics и designated-value reasoning как формальный каркас.

### Что применять в BDC

#### A. Формализация `T/F/MY/MN`
Проект исторически опирается на четырёхзначную логику, но формальная канонизация ещё слабая.
Нужно явно определить:
- чему соответствует `MY` и `MN` относительно Belnap-style space;
- как устроены designated states for action;
- как устроены negation / conjunction / aggregation in qcore.

#### B. Evidence logic в BDC Designer
Самое сильное прикладное применение прямо сейчас:
- `measured`
- `inferred`
- `missing`
- `conflicted`

Это можно оформить как evidence-state logic, а не просто как labels.

#### C. Memory and cell logic
Для reboot-линии это особенно важно в локальных decision nodes:
- клетка / модуль / агент не обязан жить в бинарной логике;
- конфликт и отсутствие сигнала должны различаться явно.

### Конкретные шаги
1. Выпустить `BDC_QCORE_BELNAP_ALIGNMENT.md`.
2. Формально описать evidence lattice.
3. Проверить, где current semantics BDC расходится с bilattice interpretation.

## 4.3. Diversity preservation и anti-premature-convergence

### Источник
- `12_Squillero_Tonda_2016_Divergence_Character_Premature_Convergence.pdf`

### Что подтверждается по содержанию

Источник даёт:
- diversity problem — системная проблема почти всех evolutionary optimizers;
- premature convergence трактуется как lack of speciation;
- survey сводит методы в unified framework;
- вводится трёхосевая taxonomy;
- различаются lineage-based, genotype-based, phenotype-based подходы;
- обсуждаются niching, crowding, speciation, population- and individual-diversity measures.

### Почему это особенно важно для BDC
Старый кризис BDC был не только в penalty regime, но и в том, что рост сложности не сопровождался зрелой diversity policy.

Этот источник полезен потому, что позволяет перестать мыслить diversity как один scalar heuristic. Вместо этого можно рассматривать:
- где именно сохранять diversity: lineage, genotype, phenotype;
- как именно её мерить;
- какой ценой поддерживать divergence;
- когда разнообразие реально помогает, а когда просто создаёт шум.

### Что применять в research reboot

#### A. Rebuild selection physics
Для `Phase R1` это один из главных внешних источников.
Нужно строить новый selection regime, где:
- сложность не душится слепо;
- divergence не оставляется на самотёк;
- есть explicit diversity mechanisms.

#### B. Многоуровневая diversity policy
Не ограничиваться population diversity вообще.
Разнести по уровням:
- lineage diversity
- genotype diversity
- phenotype diversity
- behavioral / outcome diversity

#### C. Anti-collapse mechanics
Из survey логично импортировать как минимум идею controlled niching/crowding family, но не копировать её вслепую.
Нужно проверять, какой тип diversity-механизма лучше подходит под цифровой организм BDC.

### Конкретные шаги
1. Выпустить `BDC_SELECTION_DIVERSITY_POLICY_NOTE.md`.
2. В `Selection Physics Rebuild` включить отдельные arms для:
- lineage-preserving mechanisms
- genotype-distance mechanisms
- phenotype/outcome diversity mechanisms
3. Убрать допущение, что diversity = просто “небольшой шум мутаций”.

## 4.4. Error-correcting coding и отказоустойчивая память

### Источники
- `07_Geisel_Tutorial_Reed_Solomon_Error_Correction_Coding.pdf`
- `08_Freeman_1996_Introduction_Forward_Error_Correcting_Coding.pdf`

### Что подтверждается по содержанию

Из Geisel:
- Reed-Solomon основан на символах над конечными полями;
- важны erasures, burst errors, interleaving, syndrome-based decoding;
- исправление потерь и ошибок нужно разделять.

Из Freeman:
- код должен соответствовать профилю канала;
- полезны concatenated schemes;
- FEC — это не изолированный алгоритм, а часть общей architecture-for-noise.

### Что применять в BDC

#### A. Memory robustness
Для reboot-линии памяти нужны не только “геномы”, но и error model:
- block corruption
- erasure
- burst loss
- address corruption

#### B. Packet integrity
Для `BDC Designer` можно заимствовать логику различения:
- missing block = erasure
- contradiction/corruption = error
- partially recoverable packet vs unrecoverable packet

#### C. Experiment archival
Для долгих научных прогонов полезно:
- защищённое хранение population snapshots;
- checksummed state bundles;
- recovery after partial artifact loss.

### Конкретные шаги
1. Выпустить `BDC_MEMORY_ERROR_MODEL.md`.
2. Добавить packet integrity classes по модели `error / erasure / burst defect`.
3. Рассмотреть block-level redundancy для serialized experiment states.

## 4.5. DNA storage, random access и channel-aware memory

### Источники
- `09_Organick_et_al_2018_Random_Access_Large_Scale_DNA_Data_Storage.pdf`
- `10_Lin_et_al_2020_Dynamic_Scalable_DNA_Information_Storage.pdf`
- `11_Heckel_et_al_2019_Characterization_DNA_Data_Storage_Channel.pdf`

### Что подтверждается по содержанию

#### Organick et al.
- масштабируемое random access критично;
- selective retrieval нужен для real storage;
- outer RS code и randomization помогают бороться с pathological patterns;
- addressability — центральная feature, а не cosmetic add-on.

#### Lin et al.
- memory architecture зависит от physical addressing;
- overhang/address domains поддерживают `lock / unlock / rename / delete`;
- repeatable access without destructive read — важная модель для живой памяти.

#### Heckel et al.
- DNA channel = unordered pool + sampling + indels + substitutions + molecule loss;
- sampling bias и dropout столь же важны, как локальные base errors;
- без channel model storage theory неполна.

### Что применять в BDC

#### A. Addressable memory units
Проекту нужна не просто “ДНК-метафора”, а memory unit вида:
- address/header
- payload
- control/meta bits
- state of accessibility

#### B. Dynamic memory states
Нужно рассматривать состояния модулей памяти:
- active
- locked
- retired
- renamed
- deleted / tombstoned

#### C. Noise-aware replication and retrieval
В reboot-line нельзя считать копирование идеальным.
Нужно моделировать:
- sampling loss
- retrieval bias
- corruption during replication
- address failure.

### Конкретные шаги
1. Выпустить `BDC_MEMORY_ADDRESSABILITY_NOTE.md`.
2. Для reboot-line включить explicit noise channel.
3. Спроектировать addressable memory prototype для modules/genomes/protocols.

## 5. Что даёт набор именно для достижения целей BDC

## 5.1. Для operational линии (`BDC Designer`)

Наиболее ценно прямо сейчас:

1. `Calibration discipline`
- confidence больше нельзя оценивать только внутренней эвристикой;
- нужен benchmark-calibration layer.

2. `Selective decision making`
- lawful abstention должен стать частью канона рекомендаций.

3. `Generalized risk`
- текущая оценка по working points недостаточна для зрелого сравнения confidence systems.

4. `Evidence-state logic`
- packet states должны иметь формальную, а не только описательную семантику.

5. `Packet integrity thinking`
- cleanliness, corruption, missingness стоит рассматривать как formal intake problem.

## 5.2. Для научной линии BDC

Наиболее ценно:

1. `Formal 4-valued semantics`
- связывает исторический qcore с полноценной логической традицией.

2. `Diversity taxonomy`
- закрывает слепое место старой линии EDP1/hidden_rule.

3. `Channel-aware memory`
- переводит DNA-inspired memory из метафоры в инженерную модель.

4. `Error/erasure model`
- даёт язык для устойчивого хранения и передачи состояния.

## 6. Что не следует делать на основе этих материалов

1. Не объявлять surrogate-notes по Brier и Belnap полными первичными источниками.
2. Не переносить niching/crowding механизмы в reboot без собственной адаптации к BDC physics.
3. Не считать, что presence of 4-valued logic papers автоматически валидирует текущую реализацию qcore.
4. Не внедрять новые confidence numbers без calibration audit.
5. Не использовать DNA storage papers как доказательство корректности текущей memory architecture BDC; они дают design constraints, а не validation нашей реализации.

## 7. Приоритетный roadmap импорта

## Priority 1. Немедленно применимо к `BDC Designer`
1. `BDC_DESIGNER_CALIBRATION_AND_ABSTENTION_PLAN.md`
2. `BDC_EVIDENCE_STATE_LOGIC_NOTE.md`
3. benchmark extension с:
- Brier score
- ECE
- reliability curves
- coverage-risk / generalized-risk evaluation

## Priority 2. Критично для reboot-линии
1. `BDC_QCORE_BELNAP_ALIGNMENT.md`
2. `BDC_SELECTION_DIVERSITY_POLICY_NOTE.md`
3. `BDC_MEMORY_ERROR_MODEL.md`
4. `BDC_MEMORY_ADDRESSABILITY_NOTE.md`

## Priority 3. Source hardening
1. Позже добыть оригинальную или репринтную копию Brier 1950.
2. Позже добыть оригинальную копию Belnap 1977.
3. При необходимости собрать ещё один внешний пакет specifically по:
- bilattices / Belnap-Dunn extensions
- modern diversity preservation after 2016
- memory/channel coding for indel-heavy environments.

## 8. Итог

Обновлённый внешний набор уже можно считать сильной исследовательской опорой.

Самое полезное для BDC сейчас:
- для `BDC Designer`: calibration, selective prediction, generalized risk, evidence-state semantics;
- для reboot-линии: diversity taxonomy, formal four-valued logic, channel-aware memory and error models.

Если формулировать жёстко:
- старый проект BDC страдал от недостаточно формализованной четырёхзначной логики, слабой calibration-discipline и незрелой diversity policy;
- этот внешний набор даёт прямые основания начать закрывать все три дефицита без возврата к старым нестрогим схемам.

## 9. Локальные источники набора

- `D:\projects\Bio_Digital_Core\Temp\research\external\01_Guo_et_al_2017_On_Calibration_of_Modern_Neural_Networks.pdf`
- `D:\projects\Bio_Digital_Core\Temp\research\external\02_Brier_1950_Verification_Forecasts_Probability.md`
- `D:\projects\Bio_Digital_Core\Temp\research\external\03_Geifman_ElYaniv_2017_Selective_Classification_for_Deep_Neural_Networks.pdf`
- `D:\projects\Bio_Digital_Core\Temp\research\external\04_Traub_et_al_2024_Overcoming_Common_Flaws_Evaluation_Selective_Classification.pdf`
- `D:\projects\Bio_Digital_Core\Temp\research\external\05_Belnap_1977_A_Useful_Four-Valued_Logic.md`
- `D:\projects\Bio_Digital_Core\Temp\research\external\06_Many_Valued_Logic_SEP_Reference.html`
- `D:\projects\Bio_Digital_Core\Temp\research\external\07_Geisel_Tutorial_Reed_Solomon_Error_Correction_Coding.pdf`
- `D:\projects\Bio_Digital_Core\Temp\research\external\08_Freeman_1996_Introduction_Forward_Error_Correcting_Coding.pdf`
- `D:\projects\Bio_Digital_Core\Temp\research\external\09_Organick_et_al_2018_Random_Access_Large_Scale_DNA_Data_Storage.pdf`
- `D:\projects\Bio_Digital_Core\Temp\research\external\10_Lin_et_al_2020_Dynamic_Scalable_DNA_Information_Storage.pdf`
- `D:\projects\Bio_Digital_Core\Temp\research\external\11_Heckel_et_al_2019_Characterization_DNA_Data_Storage_Channel.pdf`
- `D:\projects\Bio_Digital_Core\Temp\research\external\12_Squillero_Tonda_2016_Divergence_Character_Premature_Convergence.pdf`
