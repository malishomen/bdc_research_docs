# Verification of Forecasts Expressed in Terms of Probability

**Author:** Glenn W. Brier
**Affiliation:** U.S. Weather Bureau, Washington, D.C.
**Year:** 1950
**Source:** *Monthly Weather Review*, Vol. 78, No. 1, pp. 1–3.
**DOI:** 10.1175/1520-0493(1950)078<0001:VOFEIT>2.0.CO;2
**URL:** https://journals.ametsoc.org/view/journals/mwre/78/1/1520-0493_1950_078_0001_vofeit_2_0_co_2.xml
**Status:** PDF behind AMS paywall. Content reconstructed из открытых источников и вторичных описаний.

---

## Core Contribution

Brier (1950) предложил формальную метрику для оценки качества вероятностных прогнозов — **Brier Score**. Это одна из первых и наиболее широко используемых proper scoring rules для бинарных предсказаний.

## The Brier Score

### Definition

$$BS = \frac{1}{N} \sum_{t=1}^{N} (f_t - o_t)^2$$

Где:
- $N$ — количество прогнозов
- $f_t$ — вероятность, присвоенная прогнозом событию $t$ (от 0 до 1)
- $o_t$ — фактический исход: 1, если событие произошло; 0, если нет

### Interpretation

- **BS = 0** → идеальный прогноз (все вероятности совпали с исходами)
- **BS = 1** → наихудший возможный прогноз
- **BS = 0.25** → эквивалент постоянного прогноза 50% для равновероятных событий (baseline)

### Properties

1. **Proper scoring rule:** Brier Score минимизируется, когда предсказанные вероятности совпадают с истинными вероятностями. Это означает, что forecaster не может улучшить свой score путём намеренного искажения своих оценок.

2. **Strictly proper:** Единственный минимум достигается при $f_t = P(o_t = 1)$ для всех $t$.

3. **Decomposition (Murphy 1973):** Brier Score можно разложить на три компонента:

$$BS = \text{Reliability} - \text{Resolution} + \text{Uncertainty}$$

- **Reliability** — насколько хорошо предсказанные вероятности соответствуют наблюдаемым частотам (чем меньше, тем лучше)
- **Resolution** — насколько прогнозы отличаются для событий и не-событий (чем больше, тем лучше)
- **Uncertainty** — базовая неопределённость события, зависит только от base rate (не зависит от прогноза)

## Context: Why Proper Scoring Rules Matter

До Brier (1950) верификация прогнозов была в основном категориальной: прогноз либо "правильный", либо "неправильный". Это создавало два фундаментальных дефекта:

1. **Потеря информации:** Прогноз "60% вероятность дождя" и "99% вероятность дождя" оценивались одинаково, если дождь действительно шёл.

2. **Incentive misalignment:** Без proper scoring rule forecaster может улучшить свою оценку, сдвигая вероятности к 0 или 1 (hedging), даже если его истинная оценка неопределённости ближе к 50%.

Brier Score решает обе проблемы: он различает степени уверенности и стимулирует честную калибрацию.

## Relation to Modern Machine Learning

### Calibration Assessment
Brier Score стал стандартным инструментом для оценки **калибрации** классификаторов:
- Хорошо калиброванная модель: когда она предсказывает P=0.7, событие происходит ~70% случаев
- Brier Score количественно оценивает отклонение от идеальной калибрации

### Connection to Guo et al. (2017) — Source 01
Guo et al. показали, что современные нейросети (ResNet, DenseNet) **плохо калиброваны** — они систематически overconfident. Brier Score и его компоненты используются как один из инструментов диагностики этой проблемы.

### Connection to Geifman & El-Yaniv (2017) — Source 03
В selective classification Brier Score применяется для оценки качества прогнозов в подмножестве, которое модель "решила" классифицировать (не отклонила).

### Connection to Traub et al. (2024) — Source 04
Traub et al. предлагают AUGRC (Area under Generalized Risk Coverage curve) как метрику для selective classification, которая обобщает подход proper scoring rules к многопороговой оценке.

## Relevance to BDC Project

В контексте BDC, Brier Score применим к:
1. **EDP1 evolution engine** — оценка качества предсказаний стратегий
2. **Confidence signaling** — валидация калибрации confidence scores в BDC Designer CLI
3. **Restricted BDC theory** — формальная верификация SUPPORTED/FALSIFIED claims

---

## Bibliography

Brier, G. W. (1950). Verification of forecasts expressed in terms of probability. *Monthly Weather Review*, 78(1), 1–3.

Murphy, A. H. (1973). A new vector partition of the probability score. *Journal of Applied Meteorology*, 12(4), 595–600.
