# План внедрения: создание `docs/adoption-roadmap.md`

> **Для агентов-исполнителей:** REQUIRED SUB-SKILL — `superpowers:subagent-driven-development` (рекомендуется) либо `superpowers:executing-plans`. Шаги используют чекбоксы (`- [ ]`) для трекинга.

**Goal:** Создать `docs/adoption-roadmap.md` — универсальный roadmap внедрения библии для трёх профилей; поглотить Appendix B библии; сжать §9; обновить project `CLAUDE.md`.

**Architecture:** Документационный репо. Девять задач в строгом порядке: создание скелета → наполнение секций по порядку (общие части → три профиля → финальные главы) → удаление Appendix B → сжатие §9 → обновление маппинга в project CLAUDE.md. Каждая задача — единый коммит. Source of truth содержания — spec в `docs/superpowers/specs/2026-05-10-adoption-roadmap-design.md`.

**Tech Stack:** Markdown. Verification — `grep`, `wc -l`, `git diff`. Conventional Commits.

**Spec:** `docs/superpowers/specs/2026-05-10-adoption-roadmap-design.md`

**Замечания по style guide** (применяются ко всем задачам наполнения):
- Краткость > полноты. Императив > описание. Конкретика > идеология.
- Без эмодзи в файлах.
- Только русский язык.
- Шорткоды грехов — `#sandbox-bypass`, `#trifecta`, `#promptable`, `#test-del`, `#merge-pray`, `#workslop`, `#hidden-ai`, `#slot-machine`, `#self-auto`, `#confident-wrong`, `#tautological`, `#sycophancy`, `#zombie-t0` — в исходном виде с обратной кавычкой.
- Никаких новых ссылок в Appendix D библии не вводить (acceptance criterion 7 spec'а).

---

## Task 1: Создать скелет `docs/adoption-roadmap.md`

**Files:**
- Create: `docs/adoption-roadmap.md`

- [ ] **Step 1: Написать заголовок и оглавление с пустыми секциями**

Содержимое нового файла:

```markdown
# План внедрения «Библии вайб-кодинга»

> Универсальный roadmap внедрения подхода из «Библии вайб-кодинга» для трёх размеров организаций: малая (1–10), средняя (10–100), крупная (100+, особенно >1000). Документ строится по принципу параллельных треков: пройди decision tree в §4 и читай **только свой профиль**; склейка best of из всех трёх — антипаттерн (см. §8).

## 1. TL;DR и как читать

_(заполняется в Task 2)_

## 2. KPI внедрения

_(заполняется в Task 2)_

## 3. Принципы внедрения

_(заполняется в Task 2)_

## 4. Как выбрать профиль

_(заполняется в Task 2)_

## 5. Профиль I. Малая команда (1–10)

_(заполняется в Task 3)_

## 6. Профиль II. Средняя команда (10–100)

_(заполняется в Task 4)_

## 7. Профиль III. Крупная организация (100+, особенно >1000)

_(заполняется в Task 5)_

## 8. Anti-patterns внедрения

_(заполняется в Task 6)_

## 9. Риски и контрмеры

_(заполняется в Task 6)_

## 10. Связь с библией

_(заполняется в Task 6)_
```

- [ ] **Step 2: Структурная проверка**

Run:
```bash
grep -c '^## ' /Users/aoprudchenko/CursorAI_projects/vibible/docs/adoption-roadmap.md
```
Expected: `10`

Run:
```bash
grep -E '^## (1\. TL;DR|10\. Связь)' /Users/aoprudchenko/CursorAI_projects/vibible/docs/adoption-roadmap.md
```
Expected: две строки (первая и последняя секции).

- [ ] **Step 3: Commit**

```bash
cd /Users/aoprudchenko/CursorAI_projects/vibible
git add docs/adoption-roadmap.md
git commit -m "docs(adoption): скелет плана внедрения с 10 секциями"
```

---

## Task 2: Заполнить общие части (§§1–4)

**Files:**
- Modify: `docs/adoption-roadmap.md` (секции 1–4)

**Source of truth:** spec §5 (`### §1`, `### §2`, `### §3`, `### §4`).

- [ ] **Step 1: Заменить секцию `## 1. TL;DR и как читать`**

Текст:

```markdown
## 1. TL;DR и как читать

- Внедрение библии = переключение команды из режима «AI используют, но никто не знает кто, как и с какими гарантиями» в режим «AI используют, и это видно в git, в каталоге, в DoD, в ревью».
- Документ построен по профилям. Пройди decision tree в §4, читай только свой раздел; склеивать best of из трёх — антипаттерн внедрения (см. §8).
```

- [ ] **Step 2: Заменить секцию `## 2. KPI внедрения`**

Текст:

```markdown
## 2. KPI внедрения

Главный KPI — в §9 библии (время от идеи до зарегистрированного прототипа; доля прототипов, прошедших T1 → T3 за год). Здесь не дублируем — здесь добавляем специфику замера:

- **Baseline до старта.** Зафиксировать текущие значения обоих KPI в первую неделю Фазы 1 каждого профиля. Без baseline сдвиг не виден.
- **Ожидаемое время до сдвига.** Малая — 1–2 месяца. Средняя — 3–6 месяцев. Крупная — 6–12 месяцев. Раньше — шум, не сигнал.
- **Compliance-проценты** (% сервисов с CLAUDE.md, % AI-PR с тегом `[ai]`, % T3 с PRR) — вторичные. Пока главные KPI не растут, рост compliance — ритуал, не результат.
```

- [ ] **Step 3: Заменить секцию `## 3. Принципы внедрения`**

Текст:

```markdown
## 3. Принципы внедрения

- Paved road > мандат (Spotify Golden Paths, Charity Majors).
- Advisory → hard gate, никогда наоборот.
- Сначала фиксация терминов и ролей — потом инфраструктура — потом метрики.
- Внедряй на одном пилотном репо до раскатки на всю организацию.
- Champions ≠ эскалаторы; их задача — устранять трение, не штрафовать.
- Внедрение измеряется месяцами, не неделями. Кварталы — нормальный шаг для крупной.
```

- [ ] **Step 4: Заменить секцию `## 4. Как выбрать профиль`**

Текст:

```markdown
## 4. Как выбрать профиль

| Признак | Профиль |
|---|---|
| Один человек или команда из 2–10, нет отдельной платформы/security | I. Малая |
| 10–100 человек, есть общий бэклог, общий CI, нет paved-road-команды как роли | II. Средняя |
| 100+ (особенно >1000), есть платформа, security-governance, формальный релизный процесс | III. Крупная |

В крайних случаях (быстрый рост 5→50 за полгода) — берётся средний профиль и поэтапно повышается.
```

- [ ] **Step 5: Структурная проверка**

Run:
```bash
grep -c "_(заполняется в Task 2)_" /Users/aoprudchenko/CursorAI_projects/vibible/docs/adoption-roadmap.md
```
Expected: `0` (все четыре плейсхолдера Task 2 заменены).

Run:
```bash
grep -E "Baseline до старта|Paved road > мандат|decision tree" /Users/aoprudchenko/CursorAI_projects/vibible/docs/adoption-roadmap.md
```
Expected: три попадания минимум.

- [ ] **Step 6: Commit**

```bash
cd /Users/aoprudchenko/CursorAI_projects/vibible
git add docs/adoption-roadmap.md
git commit -m "docs(adoption): общие части (TL;DR, KPI, принципы, decision tree)"
```

---

## Task 3: Заполнить Профиль I (Малая команда)

**Files:**
- Modify: `docs/adoption-roadmap.md` (секция 5)

**Source of truth:** spec §5, подраздел `### §5. Профиль I. Малая команда (1–10)`. Включает 5.1, 5.2, 5.3.

- [ ] **Step 1: Заменить плейсхолдер секции 5 на полное содержание**

Скопировать из spec §5/`### §5. Профиль I…` весь текст (5.1 «Старт», 5.2 «Фаза 1. Bootstrap», 5.3 «Фаза 2. Sustain»). Подзаголовки в новом документе — `### 5.1.`, `### 5.2.`, `### 5.3.` (трёхуровневая иерархия внутри секции).

Внутри каждой фазы соблюдать единый шаблон:
- **Цель.**
- **Что появляется.**
- **Роли.**
- **Gate-критерий выхода.**
- **KPI фазы.**
- **Главные риски.**

Ключевые элементы (для проверки полноты):
- Предусловия и оценка стартового состояния (30 минут) в 5.1.
- Bootstrap 1–2 недели в 5.2: CLAUDE.md (универсальный шаблон) + lifecycle-метка + sunset-дата для T1+ + Conventional Commits.
- Sustain постоянно в 5.3: квартальный обзор, обновление §8 при 3+ повторах, обзор Appendix D раз в полгода.
- Шорткод `#zombie-t0` — упоминается в 5.1.
- Bus factor 1 — риск 5.3.

- [ ] **Step 2: Структурная проверка**

Run:
```bash
grep -c "_(заполняется в Task 3)_" /Users/aoprudchenko/CursorAI_projects/vibible/docs/adoption-roadmap.md
```
Expected: `0`.

Run:
```bash
grep -E "Bootstrap \(1–2 недели\)|Sustain|#zombie-t0|Bus factor 1" /Users/aoprudchenko/CursorAI_projects/vibible/docs/adoption-roadmap.md
```
Expected: четыре попадания.

Run:
```bash
grep -cE "^\*\*(Цель|Что появляется|Роли|Gate|KPI|Главные риски)" /Users/aoprudchenko/CursorAI_projects/vibible/docs/adoption-roadmap.md
```
Expected: ≥ 12 (две фазы × ~6 шаблонных подзаголовков).

- [ ] **Step 3: Commit**

```bash
cd /Users/aoprudchenko/CursorAI_projects/vibible
git add docs/adoption-roadmap.md
git commit -m "docs(adoption): профиль I (малая команда, 1–10)"
```

---

## Task 4: Заполнить Профиль II (Средняя команда)

**Files:**
- Modify: `docs/adoption-roadmap.md` (секция 6)

**Source of truth:** spec §5, подраздел `### §6. Профиль II. Средняя команда (10–100)`. Включает 6.1, 6.2, 6.3, 6.4.

- [ ] **Step 1: Заменить плейсхолдер секции 6 на полное содержание**

Скопировать из spec §5/`### §6. Профиль II…` весь текст (6.1 «Старт», 6.2 «Assessment», 6.3 «Paved road, AI-Gateway, единые ворота», 6.4 «Hardening и метрики»). Подзаголовки — `### 6.1.`, `### 6.2.`, `### 6.3.`, `### 6.4.`.

**Критичный пункт правки vs изначального дизайна:** AI-Gateway в Фазе 2 (6.3) — обязательный артефакт, а не опция. Включить полностью блок про **Minimal viable AI-Gateway** с тремя обязательными функциями: (а) фильтрация секретов, (б) аудит-лог промптов/ответов, (в) единая точка для allow-list. Кандидаты — open-source (LiteLLM, Portkey, Helicone) или SaaS внутри корп-аккаунта (Anthropic Console workspace, OpenAI Org workspace) с принудительным SSO. Развёртывание 1–2 человеко-недели.

В §4.1 шаблона CLAUDE.md команда фиксирует «вызовы LLM — только через `<имя AI-Gateway>`» — это упоминается как часть «Что появляется» Фазы 2.

В Gate-критерий Фазы 2 включить «AI-Gateway работает; ≥80% корпоративных AI-запросов идут через него». В KPI Фазы 2 — «% AI-запросов через Gateway».

В риски Фазы 2 включить два специфичных AI-Gateway-риска: (в) разрастание проекта до квартала; (г) Gateway как fence без paved road (latency overhead ≤200 мс).

- [ ] **Step 2: Структурная проверка**

Run:
```bash
grep -c "_(заполняется в Task 4)_" /Users/aoprudchenko/CursorAI_projects/vibible/docs/adoption-roadmap.md
```
Expected: `0`.

Run:
```bash
grep -E "Minimal viable AI-Gateway|LiteLLM|≤200 мс|Hardening и метрики" /Users/aoprudchenko/CursorAI_projects/vibible/docs/adoption-roadmap.md
```
Expected: четыре попадания.

Run:
```bash
grep -E "Assessment \(2–4 недели\)|Paved road, AI-Gateway, единые ворота" /Users/aoprudchenko/CursorAI_projects/vibible/docs/adoption-roadmap.md
```
Expected: два попадания.

- [ ] **Step 3: Commit**

```bash
cd /Users/aoprudchenko/CursorAI_projects/vibible
git add docs/adoption-roadmap.md
git commit -m "docs(adoption): профиль II (средняя команда, 10–100), с AI-Gateway в Фазе 2"
```

---

## Task 5: Заполнить Профиль III (Крупная организация)

**Files:**
- Modify: `docs/adoption-roadmap.md` (секция 7)

**Source of truth:** spec §5, подраздел `### §7. Профиль III. Крупная организация (100+, особенно >1000)`. Включает 7.1, 7.2, 7.3, 7.4, 7.5.

- [ ] **Step 1: Заменить плейсхолдер секции 7 на полное содержание**

Скопировать из spec §5/`### §7. Профиль III…` весь текст. Подзаголовки — `### 7.1.`, `### 7.2.`, …, `### 7.5.`.

Ключевые элементы по фазам:
- **Фаза 0. Mandate (0–4 недели)**: корпоративный AI-Gateway (с атрибуцией расходов и SSO), allow-list AI-инструментов и MCP-серверов (учитывая CVE-2025-* из Appendix D библии), библия как корпоративный стандарт, AI-Code Guild. Роли: Executive sponsor (CTO/Chief Architect), Guild lead, Platform lead, Security lead (CISO), Comms.
- **Фаза 1. AI-Gateway корпоративный + paved road (1–3 месяца)**: Backstage с метаданными (owner, lifecycle, T-зона, sunset), Scaffolder, CI-laws advisory, paved-road языки (3–5).
- **Фаза 2. Каталог + Soundcheck advisory (3–6 месяцев)**: Soundcheck advisory, Champions (1 senior+ на Tribe), mutation testing на критичных модулях T3 (mutmut/Stryker/PIT, ночные прогоны), threat model basic для T2 / full для T3, ≥10 archived `openspec/changes/`.
- **Фаза 3. Hard gates + DORA + sunset (6–12 месяцев)**: hard gate (PR не мержится без CLAUDE.md, без `[ai]`-tag — переход warn → fail после стабильного adoption за ≥3 квартала, без OpenSpec proposal для T2+ из скоупа §6 библии); ежеквартальные DORA отдельно по AI-PR vs human-only; квартальная sunset-«охота»; Guild-ритм.

Никаких упоминаний ИФТ/НТ/PoB/ЦКБ как обязательной части плана внедрения — это часть T3-релиза (Appendix A библии); план внедрения только ссылается, что профиль III применим, если такой процесс есть.

- [ ] **Step 2: Структурная проверка**

Run:
```bash
grep -c "_(заполняется в Task 5)_" /Users/aoprudchenko/CursorAI_projects/vibible/docs/adoption-roadmap.md
```
Expected: `0`.

Run:
```bash
grep -E "Executive sponsor|Soundcheck|DORA|Backstage|AI-Code Guild" /Users/aoprudchenko/CursorAI_projects/vibible/docs/adoption-roadmap.md
```
Expected: пять попаданий.

Run:
```bash
grep -E "Фаза 0\. Mandate|Hard gates \+ DORA \+ sunset" /Users/aoprudchenko/CursorAI_projects/vibible/docs/adoption-roadmap.md
```
Expected: два попадания.

- [ ] **Step 3: Commit**

```bash
cd /Users/aoprudchenko/CursorAI_projects/vibible
git add docs/adoption-roadmap.md
git commit -m "docs(adoption): профиль III (крупная организация, 100+)"
```

---

## Task 6: Заполнить Anti-patterns, риски, связь с библией (§§8–10)

**Files:**
- Modify: `docs/adoption-roadmap.md` (секции 8, 9, 10)

**Source of truth:** spec §5, подразделы `### §8`, `### §9`, `### §10`.

- [ ] **Step 1: Заменить плейсхолдер секции 8 на полное содержание**

Текст:

```markdown
## 8. Anti-patterns внедрения

1. **Big-bang rollout** — пилот → раскатка, никогда наоборот.
2. **Hard gate с первого дня** — advisory → hard gate; gate включается при ≥95% advisory-compliance без gaming.
3. **Mandate без paved road** — paved road first; правила — следствие, не причина.
4. **Compliance-метрика как главный KPI** — главные KPI всегда главные (см. §2).
5. **AI-Code Guild без executive sponsor** — Guild lead имеет прямой канал; квартальный sponsor-review.
6. **Champion как полицейский** — хартия явная: устранять трение, не штрафовать; эскалация в Guild.
7. **Склейка best of из всех профилей** — один профиль (см. §4), без подсматривания в соседние.
8. **Внедрение без baseline главного KPI** — baseline в первую неделю Фазы 1, не позже.
```

- [ ] **Step 2: Заменить плейсхолдер секции 9 на полное содержание**

Текст:

```markdown
## 9. Риски и контрмеры

| # | Риск | Контрмера |
|---|---|---|
| 1 | Бизнес-приоритеты сместились на полпути; внедрение бросают | Executive sponsor + ежеквартальный sponsor-review с явной go/no-go-точкой |
| 2 | Champion-burnout: ключевой Champion уходит, Tribe откатывается | 2 Champion-а на Tribe (минимум для крупной); явная замена в хартии |
| 3 | Толерантность к нарушениям: первый раз сквозь пальцы → норма | Грехи §4½ библии — нормированный шорткод-язык; решение «закрыть/не закрыть PR» по таблице, не по ситуации |
| 4 | Drift: библия эволюционирует, шаблоны и CLAUDE.md в репо — нет | Quarterly diff `library/CLAUDE.md.template.md` vs `ваш/CLAUDE.md` в каталоге; алёрт при расхождении |
| 5 | Vendor-lock-in AI-Gateway на одного провайдера | Provider-agnostic API внутри Gateway (LiteLLM как абстрактный слой); миграционный path в backlog |
| 6 | Регуляторное изменение (AI Act, отраслевое) в середине внедрения | Appendix D библии — точка отслеживания публикаций; ежеквартальный обзор Guild «что нового среди источников?» |
```

- [ ] **Step 3: Заменить плейсхолдер секции 10 на полное содержание**

Текст:

```markdown
## 10. Связь с библией

**Что цитируется** (живёт в библии, ссылка отсюда):
- Главный KPI — §9 библии.
- Восемь заповедей — §4.
- Тринадцать грехов (шорткоды) — §4½.
- DoD-таблица по T0–T3 — §5.
- Spec-driven workflow — §6.
- Чек-лист ревьюера AI-кода — §7.
- Шаблоны `CLAUDE.md.template.md` и `CLAUDE.md.template.enterprise.md` — §8 библии + сами файлы.
- T3-релиз для крупной орг (ИФТ/НТ/PoB/4 заключения) — Appendix A.
- Источники цифр и CVE — Appendix D.

**Что поглощено** этим документом из библии:
- Appendix B (12-месячный план развёртывания в крупной орг) — удалён из библии при коммите этого документа.
- §9 библии теперь содержит 3 абзаца общей рамки + указатель на этот документ.
- Роли Delivery Manager / PO / QA / ЦКБ / Эксперт сопровождения — остаются в Appendix A библии (привязаны к T3-релизу, не к процессу внедрения).

**Правила обновления.** Любая правка ядра §§1–7 библии требует прохода по этому документу — не появилось ли расхождений в фазах? Любая правка этого документа, влияющая на роли или DoD, требует прохода по библии. Семантическая связь зафиксирована в `CLAUDE.md` проекта.
```

- [ ] **Step 4: Структурная проверка**

Run:
```bash
grep -c "_(заполняется в Task 6)_" /Users/aoprudchenko/CursorAI_projects/vibible/docs/adoption-roadmap.md
```
Expected: `0`.

Run:
```bash
grep -E "Big-bang rollout|Vendor-lock-in|Что цитируется|Что поглощено" /Users/aoprudchenko/CursorAI_projects/vibible/docs/adoption-roadmap.md
```
Expected: четыре попадания.

Run:
```bash
grep -c '_(заполняется' /Users/aoprudchenko/CursorAI_projects/vibible/docs/adoption-roadmap.md
```
Expected: `0` (никаких плейсхолдеров не осталось во всём документе).

Run:
```bash
wc -l /Users/aoprudchenko/CursorAI_projects/vibible/docs/adoption-roadmap.md
```
Expected: 250–450 строк (порядок величины; жёсткой границы нет).

- [ ] **Step 5: Commit**

```bash
cd /Users/aoprudchenko/CursorAI_projects/vibible
git add docs/adoption-roadmap.md
git commit -m "docs(adoption): антипаттерны, риски, связь с библией"
```

---

## Task 7: Удалить Appendix B из библии

**Files:**
- Modify: `vibe-engineering-bible.md` (удаление строк 368–393, Appendix B целиком)

**Контекст:** до правки в библии есть `## Appendix B. Внедрение в крупной организации (>1000 человек)` со всеми Фазами 0–3 и таблицей ролей. Поглощён `docs/adoption-roadmap.md` (Профиль III).

- [ ] **Step 1: Прочитать текущую структуру библии**

Run:
```bash
grep -nE '^## Appendix' /Users/aoprudchenko/CursorAI_projects/vibible/vibe-engineering-bible.md
```
Expected (приблизительно): четыре строки — Appendix A, B, C, D со своими номерами строк. Зафиксировать актуальные номера.

- [ ] **Step 2: Удалить Appendix B полностью**

Использовать Edit на `vibe-engineering-bible.md`. Старый текст (строки от заголовка `## Appendix B.` до строки прямо перед `---` отделяющим B от C):

```
## Appendix B. Внедрение в крупной организации (>1000 человек)

Для команды до 100 человек этот раздел — справочный; основная программа — в §9.

[…весь текст Appendix B вплоть до и включая горизонтальный разделитель `---` перед Appendix C…]
```

После Edit между Appendix A и Appendix C должна остаться **только одна** разделительная линия `---`.

Если технически удобнее — заменить весь блок Appendix B (включая хвостовой `---`) на пустую строку, а затем убрать дублирующиеся подряд `---` с помощью второго Edit. Главное — итоговая структура библии: A → C → D без Appendix B.

- [ ] **Step 3: Структурная проверка**

Run:
```bash
grep -c '^## Appendix B\.' /Users/aoprudchenko/CursorAI_projects/vibible/vibe-engineering-bible.md
```
Expected: `0`.

Run:
```bash
grep -E '^## Appendix' /Users/aoprudchenko/CursorAI_projects/vibible/vibe-engineering-bible.md
```
Expected: три строки — Appendix A, Appendix C, Appendix D.

Run:
```bash
grep -cE 'Soundcheck|AI-Code Guild|Champions-программа' /Users/aoprudchenko/CursorAI_projects/vibible/vibe-engineering-bible.md
```
Expected: возможны 0–2 совпадения (упоминания в §9, глоссарии или Appendix C допустимы; обширного Appendix-B-блока быть не должно).

Run:
```bash
grep -nE '^---$' /Users/aoprudchenko/CursorAI_projects/vibible/vibe-engineering-bible.md
```
Expected: разделители всё ещё разделяют Appendix-ы и финальный блок; нет двух `---` подряд.

- [ ] **Step 4: Commit**

```bash
cd /Users/aoprudchenko/CursorAI_projects/vibible
git add vibe-engineering-bible.md
git commit -m "docs(bible): удалить Appendix B (поглощён docs/adoption-roadmap.md)"
```

---

## Task 8: Сжать §9 библии до 3 абзацев + указатель

**Files:**
- Modify: `vibe-engineering-bible.md` (раздел `## 9. Масштабирование`)

**Контекст:** до правки §9 — три тематических абзаца (главный KPI, под размер команды с упоминанием Appendix B, paved road > мандат). Текст про «12-месячный план… в Appendix B» становится stale после Task 7.

- [ ] **Step 1: Прочитать текущий §9**

Run:
```bash
grep -nA 30 '^## 9\. Масштабирование' /Users/aoprudchenko/CursorAI_projects/vibible/vibe-engineering-bible.md | head -40
```

Зафиксировать актуальный текст.

- [ ] **Step 2: Заменить §9 на новую версию**

Использовать Edit. Новый текст §9 целиком:

```markdown
## 9. Масштабирование

**Главный KPI** — не процент соблюдения правил, а: (1) скорость от идеи до зарегистрированного прототипа (цель — минуты, не дни) и (2) доля прототипов, успешно прошедших T1 → T3 в течение года. Здоровое прототипное кладбище — то, где смерть происходит явно и быстро.

**Под размер команды.** Маленькой команде (1–10 человек) достаточно §§1–8 + §10 + чек-листа §7. Не нужны ни Soundcheck-метрики, ни Champions-программа, ни ежеквартальные DORA-замеры — это инструменты для большой организации, и на маленькой выборке они дают шум, не сигнал. Команде среднего размера (10–100) полезен общий каталог сервисов с lifecycle-метаданными и единый AI-Gateway. Большой организации (100+, особенно >1000) — план развёртывания на 12 месяцев с фазами 0–3, AI-Code Guild как явный owner политики, Soundcheck-метрики.

**Внедрение через paved road, не через мандат.** Большие изменения в инженерной культуре работают, когда правильный путь — самый лёгкий (Spotify Golden Paths, Netflix paved road). Жёсткие гейты без paved road загоняют команды в большие батчи и увеличивают blast radius на изменение (Charity Majors). Если у вас нет ресурса сначала построить paved road — начните с §4 + §5 ядра + §7 как advisory; гейты включаются позже.

> **Подробный план внедрения для всех трёх профилей** (малая 1–10 / средняя 10–100 / крупная 100+): `docs/adoption-roadmap.md`. Документ раскрывает фазы по неделям/месяцам, gate-критерии перехода, KPI на фазу, anti-patterns внедрения и риски с контрмерами.
```

Старый второй абзац содержит хвост `; всё это — в Appendix B.` — этот хвост должен исчезнуть; его заменяет финальный blockquote с указателем на `docs/adoption-roadmap.md`.

- [ ] **Step 3: Структурная проверка**

Run:
```bash
grep -c 'Appendix B' /Users/aoprudchenko/CursorAI_projects/vibible/vibe-engineering-bible.md
```
Expected: `0`.

Run:
```bash
grep -c 'docs/adoption-roadmap.md' /Users/aoprudchenko/CursorAI_projects/vibible/vibe-engineering-bible.md
```
Expected: `≥1` (минимум одна ссылка из §9; возможно ещё одна — из §8 «CLAUDE.md baseline» или иного места, если решит редактор; обязательная — в §9).

Run:
```bash
grep -A 2 '^## 9\. Масштабирование' /Users/aoprudchenko/CursorAI_projects/vibible/vibe-engineering-bible.md | head -3
```
Expected: первая строка — `## 9. Масштабирование`; следующая непустая — заголовок «Главный KPI» в формате жирным.

- [ ] **Step 4: Commit**

```bash
cd /Users/aoprudchenko/CursorAI_projects/vibible
git add vibe-engineering-bible.md
git commit -m "docs(bible): §9 — короткая рамка + указатель на docs/adoption-roadmap.md"
```

---

## Task 9: Обновить project `CLAUDE.md` (семантическая связь файлов)

**Files:**
- Modify: `CLAUDE.md` (раздел «Семантическая связь файлов», блок «Что это за репозиторий», «Что НЕ делать»)

**Контекст:** project `CLAUDE.md` сейчас описывает три документа — библию + два шаблона. Появляется четвёртый — план внедрения. Все ссылки на Appendix B становятся stale.

- [ ] **Step 1: Прочитать текущий CLAUDE.md**

Run:
```bash
grep -nE 'Appendix B|adoption-roadmap' /Users/aoprudchenko/CursorAI_projects/vibible/CLAUDE.md
```

Зафиксировать все строки, которые упоминают Appendix B (их нужно либо удалить, либо переписать как ссылку на новый документ).

- [ ] **Step 2: Обновить раздел «Что это за репозиторий»**

Найти буллет про библию в этом разделе. Сейчас он заканчивается фразой про «Appendix B (12-месячный план развёртывания в крупной орг)». Удалить упоминание Appendix B из перечисления (Appendix A — оставить, C — оставить, D — оставить). Добавить отдельный буллет:

```markdown
- **`docs/adoption-roadmap.md`** — универсальный roadmap внедрения подхода библии для трёх профилей: малая (1–10), средняя (10–100), крупная (100+). Поглотил Appendix B библии. Содержит фазы по неделям/месяцам с gate-критериями, KPI на фазу, anti-patterns внедрения, риски с контрмерами. Команды читают только свой профиль.
```

- [ ] **Step 3: Обновить раздел «Семантическая связь файлов»**

Добавить новый подпункт в маппинг (после пункта про spec-driven, перед пунктом про §9 «Масштабирование»):

```markdown
  - **§9 библии «Масштабирование» → `docs/adoption-roadmap.md`.** §9 — общая рамка (главный KPI, под размер команды, paved road > мандат). Конкретный план внедрения для всех трёх профилей — в отдельном документе. Правишь фазу/KPI/риск в roadmap — проверь §9 на согласованность; правишь §9 — проверь, не появились ли расхождения с фазами в roadmap.
  - **Appendix A библии (роли T3-релиза) → Профиль III roadmap.** Делitery Manager / PO / QA / ЦКБ / Эксперт сопровождения остаются в Appendix A; план внедрения только ссылается, что профиль III применим, если такой процесс есть. Дублировать роли в roadmap не надо.
```

Также удалить из «Семантической связи» абзац, упоминающий Appendix B как отдельный файл маппинга, если он там есть.

- [ ] **Step 4: Обновить раздел «Что НЕ делать»**

Найти строку «Не вноси корпоративную пристёжку обратно в ядро…» — она содержит упоминание Backstage/Soundcheck/AI-Code Guild со ссылкой «только в Appendix A/B/C». Заменить на «только в Appendix A/C или в `docs/adoption-roadmap.md` для крупного профиля».

Найти строку про Appendix D и проверки цифр — оставить без изменений.

Если есть строка специально про Appendix B — удалить её или переписать как «План внедрения теперь живёт в `docs/adoption-roadmap.md`; не возвращай его в библию».

- [ ] **Step 5: Обновить раздел «Терминология (минимум для навигации)»**

Найти определение `[ENT]`-маркер и Appendix A — оставить.

Если есть упоминание Appendix B (например в каком-то определении) — заменить на «`docs/adoption-roadmap.md` (Профиль III)».

- [ ] **Step 6: Структурная проверка**

Run:
```bash
grep -c 'Appendix B' /Users/aoprudchenko/CursorAI_projects/vibible/CLAUDE.md
```
Expected: `0`.

Run:
```bash
grep -c 'docs/adoption-roadmap.md' /Users/aoprudchenko/CursorAI_projects/vibible/CLAUDE.md
```
Expected: `≥3` (минимум: один раз — в перечислении файлов; один раз — в семантической связи; один раз — в «Что НЕ делать»).

Run:
```bash
grep -E 'универсальный roadmap внедрения' /Users/aoprudchenko/CursorAI_projects/vibible/CLAUDE.md
```
Expected: одно попадание.

- [ ] **Step 7: Финальная проверка по всему репо**

Run:
```bash
grep -rn 'Appendix B' /Users/aoprudchenko/CursorAI_projects/vibible --include='*.md'
```
Expected: пусто (нигде в репо нет упоминания Appendix B; все мигрировали либо удалены).

Run:
```bash
grep -rln 'docs/adoption-roadmap.md' /Users/aoprudchenko/CursorAI_projects/vibible --include='*.md'
```
Expected: минимум 3 файла — `vibe-engineering-bible.md`, `CLAUDE.md`, сам `docs/adoption-roadmap.md` (self-reference в §10 при обращении «этот документ» допустим). Возможны ещё ссылки из шаблонов, если решит редактор.

- [ ] **Step 8: Commit**

```bash
cd /Users/aoprudchenko/CursorAI_projects/vibible
git add CLAUDE.md
git commit -m "docs(meta): добавить docs/adoption-roadmap.md в семантическую связь файлов"
```

---

## Self-Review

**Spec coverage** (по acceptance criteria из §7 spec'а):

1. Все три профиля по единому шаблону фазы — Tasks 3, 4, 5 покрывают; шаблон явно проверяется через `grep` на ключевые буллеты в Step 2 каждой задачи.
2. Decision tree однозначен — Task 2 Step 4.
3. AI-Gateway в профилях II и III — Tasks 4, 5; для профиля II это критичный пункт правки, явно отмечен в Task 4 Step 1.
4. §10 явно перечисляет цитаты и поглощения — Task 6 Step 3.
5. Appendix B удалён, §9 указывает на новый документ, project CLAUDE.md обновлён — Tasks 7, 8, 9.
6. Главный KPI и заповеди не дублируются — Task 2 Step 2 (только ссылка на §9 библии).
7. Никаких новых ссылок в Appendix D — выполняется по умолчанию (план не вводит их).

**Placeholder scan:** проведён. Плейсхолдеры есть только внутри документа в виде `_(заполняется в Task N)_` — это намеренный механизм отслеживания прогресса между Tasks 1–6, и каждая задача содержит явную проверку их обнуления.

**Type consistency:** имена секций согласованы между Task 1 (скелет) и Tasks 2–6 (наполнение). Наименование `docs/adoption-roadmap.md` идентично во всех Tasks 1, 8, 9, в spec и в CLAUDE.md. Шорткоды грехов (`#zombie-t0`) — единообразно.

---

## Execution Handoff

Plan complete and saved to `docs/superpowers/plans/2026-05-10-adoption-roadmap.md`. Two execution options:

**1. Subagent-Driven (recommended)** — отдельный subagent на каждую задачу, ревью между задачами, быстрая итерация.

**2. Inline Execution** — выполняем задачи в этой же сессии через `executing-plans`, batch с чекпоинтами для ревью.

Которое выбираем?
