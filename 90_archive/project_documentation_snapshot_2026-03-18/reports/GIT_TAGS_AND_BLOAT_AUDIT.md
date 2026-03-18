# Аудит: теги, push и тяжёлые объекты в git

**Дата:** 2026-01-24  
**Запрос:** проверить проблему с тегами при `git push origin test --tags` и `git push origin main --tags`, кэширование лишних данных.

---

## 1. Вывод

- **Теги сами по себе не кэшируют лишние данные.** Они хранят только маленькие объекты (annotated tag + указатель на коммит).
- **При `git push --tags` передаётся всё, что нужно для коммитов, на которые ссылаются теги, и их предков.** «Лишний» объём идёт не от тегов, а от **больших файлов, уже попавших в историю**.
- В `.git` сейчас **~1.53 GiB** loose-объектов. Основная причина — один **1.86 GiB**-файл в истории и несколько мегабайтов results/backup/datasets.

---

## 2. Что именно раздувает репозиторий

### 2.1. Крупнейшие объекты в истории (по размеру)

| Размер      | Путь |
|------------|------|
| **1 863 897 814 B (~1.86 GiB)** | `results/trl10_gpu_optimized/checkpoints/checkpoint_final.pt` |
| 13 588 227 B (~13.6 MiB)        | `datasets/wiki_prepared.jsonl` |
| 1 812 976 B (~1.8 MiB)          | `results/trl10_wikidata/metrics.json` |
| 721 155 B (~721 KiB)            | `backup/2026_01_24/trl6_fitness_drift_summary.png` |
| 692 425 B                      | `results/trl9_meta_cognition/metrics.json` |
| 692 181 B                      | `results/trl9.1_reflection/metrics.json` |
| 253 146 B                      | `results/trl9_meta_cognition/meta_cognition_analysis.json` |
| 253 000 B                      | `results/trl9.1_reflection/meta_cognition_analysis.json` |
| ~100 KiB × 20                  | `results/trl10_wikidata/checkpoints/checkpoint_ep*.json` |
| …                              | прочие `results/`, `backup/` |

### 2.2. Где и когда они попали в историю

| Файл / каталог | Коммит | Комментарий |
|----------------|--------|-------------|
| `results/trl10_gpu_optimized/checkpoints/checkpoint_final.pt` | `3efef29` (feat(trl10): GPU trainer 15m health monitoring + streamlit validation) | Чекпоинт обучения. В `.gitignore` есть `results/`, `checkpoints/`, `*.pt`, но файл был добавлен до ужесточения правил или через `git add -f`. **Не должен храниться в репо.** |
| `datasets/wiki_prepared.jsonl` | `b116a66` (feat(trl10): Wikipedia real-data training complete) | Датасет для TRL-10. Для воспроизводимости полезен, но ~13.6 MiB. Решение — оставить, вынести в LFS или во внешнее хранилище. |
| `results/trl10_wikidata/`, `results/trl9*`, `backup/` | Разные коммиты | Артефакты и бэкапы. `results/` и `*.pt` в `.gitignore` есть; `backup/` в `.gitignore` не было — при `git add` мог попасть. |

### 2.3. Связь с тегами и ветками

- `v1.0.1-trl10-gpu-optimized` указывает на коммит `3efef29`, в котором есть **checkpoint_final.pt (1.86 GiB)**.
- `3efef29` входит в историю `test`, `main`, `feature/trl8_bootstrap`.
- При `git push origin test --tags` или `git push origin main --tags` Git передаёт все объекты, достижимые из этих веток и из указанных тегов. В том числе — большой `checkpoint_final.pt` и остальные перечисленные файлы.
- Теги **не дублируют** эти объекты: они только ссылаются на коммиты. Дополнительный объём при push даёт именно **история коммитов**.

---

## 3. Что в репо лишнее (не должно храниться в git)

| Категория | Примеры | Рекомендация |
|-----------|---------|--------------|
| Чекпоинты обучения | `*.pt`, `results/.../checkpoints/checkpoint_final.pt` | Не коммитить. Хранить вне репо или в LFS, если нужно. |
| `backup/` | `backup/2026_01_24/`, `backup/TRL8_ENTRY_*/` | Игнорировать. В `.gitignore` нет `backup/` — добавить. |
| Крупные `results/*` | `results/trl10_wikidata/checkpoints/*.json`, часть `metrics.json` | Уже прикрыто `results/` в `.gitignore`; важно не добавлять через `-f` без явной необходимости. |
| `datasets/wiki_prepared.jsonl` | 13.6 MiB | Решить: оставить, LFS или внешнее хранилище. |

---

## 4. Проверка .gitignore

Текущие правила (по сути):

- `results/`, `checkpoints/`, `*.pt`, `*.pkl`, `*.bin` — есть.
- `backup/` — **нет**. Нужно добавить, чтобы `backup/` больше не попадал.

---

## 5. Рекомендации

### 5.1. Сразу (без переписывания истории)

1. **Добавить в `.gitignore`:**
   - `backup/`
2. **Проверить** перед каждым `git add`, что не тянете `results/`, `checkpoints/`, `*.pt`, `backup/`, большие `datasets/*` без согласованного исключения в `.gitignore` или LFS.

### 5.2. Удалить тяжёлые артефакты из истории (уменьшить размер репо и push)

Чтобы убрать `checkpoint_final.pt` и при желании другие артефакты из истории:

1. Установить `git-filter-repo` (рекомендуется) или использовать BFG Repo-Cleaner.
2. Удалить из истории, например:
   - `results/trl10_gpu_optimized/checkpoints/` (в т.ч. `checkpoint_final.pt`);
   - при необходимости — `backup/`, часть `results/trl10_wikidata/checkpoints/` и т.п.
3. Выполнить:
   ```bash
   git reflog expire --expire=now --all
   git gc --prune=now --aggressive
   ```
4. **Важно:** после перезаписи истории хэши коммитов изменятся. Теги, указывающие на старые коммиты (например, `v1.0.1-trl10-gpu-optimized` → `3efef29`), станут неверными. Нужно:
   - пересоздать такие теги на новые коммиты;
   - при push в общий remote — согласовать force-push и обновление тегов с другими разработчиками.

### 5.3. Push и теги

- `git push origin test` и `git push origin main` уже несут всю достижимую историю, включая большие файлы. `--tags` добавляет только передачу самих тегов (малый объём).
- Если на `origin` этой истории ещё нет — первый push будет большим (~1.5 GiB и больше) из‑за `checkpoint_final.pt` и остального. После удаления этого файла из истории и `git gc` объём и время push уменьшатся.
- «Кэширование» при push со стороны Git — это в первую очередь передача всех достижимых объектов. На стороне `origin` кэш (уже полученные объекты) как раз уменьшает повторную передачу при следующих push.

---

## 6. Список тегов (на момент аудита)

| Тег | Коммит | Примечание |
|-----|--------|------------|
| v0.6.0-trl6-complete | 04a52cf | — |
| v0.7.0-trl7-complete | 7a850c4 → c6307a1 | — |
| v0.8.1-trl8-bootstrap | c8174b3 → 569f6ea | — |
| v0.9.3-gpu-precheck | 0f80b3c → 31224f6 | — |
| v0.9.4-trl9.1-auto | 8b2bc53 → 31224f6 | — |
| v1.0.0-trl10-wikidata | 98cc99a → 31224f6 | — |
| v1.0.1-trl10-gpu-optimized | 386258c → **3efef29** | **В предках — коммит с checkpoint_final.pt (1.86 GiB).** |
| v1.0.2-pre-train | 33f86a5 → 1a131f2 | — |
| v1.0.3-trl10.1-complete | f318b22 → 9e2b36e | — |

Все — annotated. Лишних или «мусорных» тегов не видно; лишний объём дают не теги, а блобы в указанных коммитах.

---

## 7. Краткий чеклист

- [ ] Добавить `backup/` в `.gitignore`.
- [ ] Решить судьбу `datasets/wiki_prepared.jsonl` (оставить / LFS / внешнее хранилище).
- [ ] (Опционально) Удалить из истории `results/trl10_gpu_optimized/checkpoints/` и при необходимости `backup/` через `git-filter-repo` / BFG.
- [ ] После переписывания истории: пересоздать затронутые теги, выполнить `git gc`, согласовать force-push с участниками.
- [ ] Не использовать `git add -f` для `results/`, `checkpoints/`, `*.pt`, `backup/` без явной договорённости.
