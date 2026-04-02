# magi-but-chatgpt-gemini-deepseek

![Status: Work in Progress](https://img.shields.io/badge/status-WIP--Planning-orange)
![License: MIT](https://img.shields.io/badge/license-MIT-green)
![Theme: Evangelion](https://img.shields.io/badge/inspired--by-Evangelion-blue)

> 這是一個基於 [fshiori/magi](https://github.com/fshiori/magi) 的 Fork 專案。  
> 原版 MAGI 使用三個便宜模型；我們相信透過三個頂級且「異質化」的模型對抗，能觸及單一模型無法達到的邏輯巔峰。

---

## 🛰️ 專案願景 (Vision)
傳統的投票機制容易陷入「集體平庸」。本專案旨在將 **MAGI** 的結構化辯論協議（ICE）應用於目前世界上最強的三個不同體系：
* **Melchior (ChatGPT/GPT-4o mini):** 代表通用邏輯與穩定性。
* **Balthasar (Gemini 1.5 Pro):** 代表廣大的脈絡理解與跨模態洞察。
* **Casper (DeepSeek V3):** 代表強悍的數理推理與性價比極限。

---

## 🗺️ 啟動路徑 (Roadmap)

目前的狀態是：**[預研與規劃階段]**。以下是預計開發的里程碑：

### 🏁 Phase 1: 基礎對接 (Base Integration)
- [ ] **多 API 介面適配:** 支援 OpenRouter 統一調用或各家 SDK 獨立串接。
- [ ] **環境變數重構:** 支援同時載入 `OPENAI_API_KEY`, `GEMINI_API_KEY`, 與 `DEEPSEEK_API_KEY`。
- [ ] **Persona 定義:** 針對這三個模型的特性重新設計「人格預設」。

### ⚔️ Phase 2: 核心引擎優化 (Engine Tuning)
- [ ] **Reasoning Content 提取:** 專門針對 DeepSeek 的思維鏈（Think Tag）進行結構化解析。
- [ ] **跨模型權重演算法:** 根據任務類型（Code/Logic/Creative）調整三個模型的投票權重。
- [ ] **Token 成本追蹤:** 即時計算這三巨頭辯論一次到底要花多少錢。

### 🖥️ Phase 3: 視覺化與工具 (UI/UX)
- [ ] **NERV Dashboard 適配:** 確保三種不同廠牌的模型在儀表板上顯示各自的 Logo 與狀態。
- [ ] **CLI 強化:** 支援 `magi-but ask --trio` 直接啟動三巨頭對戰。

---

## 🛠️ 安裝與使用 (Coming Soon)
目前專案處於 WIP 狀態，尚未發布至 PyPI。

```bash
# 開發者模式安裝
git clone [https://github.com/你的帳號/magi-but-chatgpt-gemini-deepseek.git](https://github.com/你的帳號/magi-but-chatgpt-gemini-deepseek.git)
cd magi-but-chatgpt-gemini-deepseek
pip install -e .

📜 聲明
此專案純屬技術研究，旨在探索不同 LLM 供應商之間的「集體智慧」極限。
Inspired by Neon Genesis Evangelion.
God's in his heaven. All's right with the world.

---
| `escalate` | Forced decision on high-disagreement topics | Critique with 2-round limit, highest-trust node makes final call |
| `adaptive` | Default for most use cases | Auto-selects based on agreement score: high=vote, medium=critique, low=escalate |

## Persona Presets

MAGI comes with 5 built-in perspective sets:

```
$ magi presets

  code-review     Security Analyst / Performance Engineer / Code Quality Reviewer
  eva             Melchior / Balthasar / Casper
  research        Methodologist / Domain Expert / Devil's Advocate
  strategy        Optimist / Pessimist / Pragmatist
  writing         Editor / Reader Advocate / Fact Checker
```

## Benchmark Results

Tested on **MMLU (Massive Multitask Language Understanding)** "Hell Mode" (Abstract Algebra, Professional Law, Formal Logic):

| Group | Accuracy | Strategy | Verdict |
|-------|----------|----------|---------|
| Claude Sonnet 4.6 (Single) | 83.3% | Single Shot | Peak individual performance |
| **MAGI Critique (3x Cheap)** | **83.3%** | **ICE Protocol** | **Matched.** Beats Sonnet on Logic |

**Models used:** Xiaomi MiMo-v2-pro, MiniMax M2.7, DeepSeek V3.2.
**Judge:** Verified by Gemini 3.1 Pro via OpenRouter.

## Fault Tolerance

MAGI keeps working when models fail:

- **1 of 3 fails** — continues with 2 nodes, marks decision as degraded
- **2 of 3 fail** — falls back to single model response
- **All 3 fail** — raises `MagiUnavailableError` (never guesses)
- **Timeouts** — 60s default per node, exponential backoff on rate limits
- **Reasoning models** — automatically extracts from `reasoning_content` (e.g., MiniMax M2.7)

## Project Structure

```
magi/
├── core/
│   ├── engine.py       # MAGI engine, coordinates nodes
│   ├── node.py         # LLM node wrapper with persona
│   └── decision.py     # Decision dossier dataclass
├── protocols/
│   ├── vote.py         # Structured voting with position extraction
│   ├── critique.py     # ICE (Iterative Consensus Ensemble)
│   └── adaptive.py     # Dynamic protocol selection
├── commands/
│   ├── diff.py         # Multi-model code review
│   ├── judge.py        # Multi-model answer scoring
│   └── analytics.py    # Trace analysis and replay
├── web/
│   ├── server.py       # FastAPI + WebSocket server
│   └── static/         # NERV Command Center UI
├── presets/             # Persona preset definitions
├── bench/              # Benchmark runner and datasets
├── trace/              # JSONL trace logging
└── cli.py              # Click CLI entry point
```

## Name

In Evangelion, MAGI is a trio of supercomputers created by Dr. Naoko Akagi. Each embodies a different aspect of her personality: **Melchior** (the scientist), **Balthasar** (the mother), and **Casper** (the woman). Decisions are made by majority vote among the three.

MAGI applies this concept to LLMs: same question, three different perspectives, structured disagreement produces better decisions than any single model alone.

## License

MIT
