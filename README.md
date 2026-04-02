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
