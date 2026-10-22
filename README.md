# DairyLife 360｜V18.5.17.11 P1 蹄病與跛行 L3 測試版

本測試分支延續 V18.5.17.10，保留原網站、牛寶、PVD／PMN、DHI、TMR、SOP 等功能，**未合併 main**。

## 預覽方式

- 線上預覽（第三方 RawGitHack；僅供公開分支測試）：
  https://raw.githack.com/topmiru221-sys/dairylife360/dev/v18.5.17.11-hoof-l3/index.html
- 離線驗收：從 GitHub 下載本分支 ZIP，解壓縮後以 Chrome／Edge 開啟根目錄 `index.html`。
- GitHub 的 `blob/index.html` 是原始碼檢視頁，**不會渲染成網頁**。

## 本版 P1 功能

進入「問題解決中心」→「V18.5.17.11 P1 蹄病與跛行 L3 現場 SOLUTION」。
- AHDB 0–3 跛行分級及緊急警訊分流。
- 常見病灶鑑別、處置禁忌、治療後複查與群體根因 KPI。
- 個別病灶不能只靠跛行分數或圖片確診。
- 不儲存輸入；非獸醫診斷或處方工具。

## 優先驗收項目

- [ ] 進入 Problems，P1 工作區正常呈現。
- [ ] 評分 0、1、2、3 各自提供不同現場建議。
- [ ] 勾選無法站立或全身病徵時，即使分數為 0 也顯示緊急警示。
- [ ] 未選分數又無緊急警訊時，不提供判斷結果。
- [ ] 病灶辨識、處置、複查與 KPI 收合展開正常。
- [ ] 桌機與手機版排版正確。
- [ ] 原有牛寶、20 Portal 路由、Fresh PVD／PMN、DHI、TMR、SOP 正常。
- [ ] 版本標題與側欄顯示 V18.5.17.11。

## 範圍及限制

此版**只有 P1 第一階段現場工作區**，尚須進行完整瀏覽器互動及模組交叉串接測試。P2 熱緊迫、PR #11、頁面架構均未變動。未經使用者驗收，不合併 main。

原始內容規劃：`planning/p1-hoof-l3-content.md`
結構檢查工具：`tools/verify_html_integrity.py`
