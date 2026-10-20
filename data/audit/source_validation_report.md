# Source-Validation Report — Vasu CFCQI Annual-Report Corpus

**Date:** 8 October 2026
**Corpus:** 80 annual reports, 40 FTSE 350 firms x 2 consecutive cycles
**Register:** `Vasu_Master_Annual_Report_Register.xlsx` / `.csv`

## 1. What was verified for every report

Each PDF was opened and inspected (7 Oct 2026, during download and coding):

1. **Company name** - programmatic cover-text check passed for all 80 (firm token present on
   pages 1-3); every report was additionally read in full during CFCQI coding, with verbatim
   evidence quotes and page references recorded in `data/interim/evidence/F###_T.md`.
2. **Report title and fiscal year** - the requested reporting cycle appears on the cover/title
   of every report; year tokens verified on pages 1-3 for all 80.
3. **Consolidated group status** - all 80 are consolidated group annual reports (group
   financial statements coded, not parent-company-only or subsidiary accounts).
4. **Full annual report** - page counts 108-481; each contains strategic report, governance,
   and audited financial statements. Partial/extract documents were rejected (see incidents).
5. **Listed-group entity** - confirmed for every firm; special attention cases below.

## 2. Entity verification - flagged firms

| Firm | Verified entity | Evidence |
|---|---|---|
| Coca-Cola HBC | **Coca-Cola HBC AG** (group) | "Integrated Annual Report 2025"; "Coca-Cola HBC AG" in report text; 368pp group report - not a financing subsidiary |
| Rio Tinto | **Rio Tinto plc** (Group) | "Rio Tinto plc financial statements" in the report; dual-listed Group reporting |
| IAG | **International Consolidated Airlines Group, S.A.** | Named in full in the report ("...S.A. (hereinafter 'International Airlines Group', 'IAG' or 'the Group')") |
| National Grid | National Grid plc | Group annual report and accounts 2025/26 |
| Aston Martin | **Aston Martin Lagonda Global Holdings plc** | Named in full; Strategic Report per Companies Act 2006 |
| RHI Magnesita | n/a | Not in the frozen sample (below market-cap boundary) |
| Ithaca Energy | **Ithaca Energy plc** | Cover: "ITHACA ENERGY PLC - ANNUAL REPORT AND ACCOUNTS 2025" |
| Spirax-Sarco | **Spirax Group plc** (renamed from Spirax-Sarco Engineering plc) | Both covers read "Spirax Group plc"; LSE ticker SPX unchanged |

No finance-subsidiary, parent-only, or subsidiary accounts are in the corpus.

## 3. Source priority compliance

- **Tier 1 (official company IR website):** the large majority of reports, downloaded direct.
- **Tier 3/4 recoveries** (bot-blocked official sites - Cloudflare/Akamai), all verified as the
  company's own official documents:
  - Aston Martin 2024: Wayback snapshot (2025-03-26) of the official IR page; identical official PDF.
  - Smiths Group 2024: official smiths.com media URL (verified serving live).
  - IMI 2025/2024: live-browser fetch from imiplc.com/investors (Cloudflare-blocked for scripts).
  - Tesco 2026/2025, Coca-Cola HBC 2025/2024, ABF 2025/2024: Wayback captures of the official
    company DAM/media URLs (Tesco URLs quoted verbatim in Tesco's own 3 Jul 2026 prospectus RNS).
  - Sainsbury's 2025: Sainsbury's own official "accessible" full version (first download was a
    truncated 111-page split - replaced).
  - Ocado 2024: Ocado's official Webflow CDN (host serving ocadogroup.com).
- No random document-upload sites were used. Where the exact PDF URL was not retained at
  download, the register says so explicitly rather than reconstructing a URL.

## 4. Sampling cut-off (31 August 2026)

All 80 reports were publicly available by the cut-off. The latest-publishing report in the
corpus is **Diageo Annual Report 2026** (year ended 30 June 2026), published **18 August 2026**
(RNS 1770R) - 13 days inside the cut-off. All other T reports cover periods ending
December 2025-March 2026 and were published February-June 2026. **No requested report was
unavailable at the cut-off; no substitution was made.**

Note on Ithaca Energy: the FY2025 Annual Report and Accounts (year ended 31 Dec 2025) was
published in Q1 2026 and was available well before the cut-off - no sampling issue arose.

## 5. Rejected documents

- 1 wrong-year duplicate (Smiths FY2025 saved as FY2024) - replaced, see duplicate-hash audit.
- 2 partial PDFs (M&S 90/91-page strategic-report-only files) - invalidated; full 208/224-page
  reports obtained and re-coded from scratch.
- 1 truncated split (Sainsbury's 111 pages) - replaced with the official full version.
- Details in `Missing_or_Excluded_Reports.xlsx`.

## 6. Methodological issues and residual risks

1. **Reporting-period length:** Mobico T is a **15-month** period (year-end changed Dec->Mar
   2026); Tesco T is a **53-week** period (12.2 months). Recorded exactly, not normalised;
   sensitivity analysis drops F019 (`06_robustness.py`).
2. **Sample vs draft list:** the frozen sample was selected by market-cap ranking (top 10 per
   TCFD group, Transportation rebalanced to 9+11) and differs from the earlier draft company
   list (e.g. Diversified Energy, Croda, Premier Foods, Barratt Redrow, Rolls-Royce below the
   boundary; DCC, Inchcape, Clarkson, Zigup, Diploma, Smiths, IMI, Weir, Spirax-Sarco,
   Fresnillo, Endeavour, Tesco, M&S, Sainsbury's, Ocado above it). Fully documented in
   `docs/SAMPLE_SELECTION.md`; close calls recorded.
3. **Mondi titling:** "Integrated report and financial statements" is the company's primary
   annual report including full audited financial statements - accepted as the annual report
   and accounts (not an ESG-only report).
4. **Smiths Group T=FY2025:** FY2026 AR not published at the 7 Oct 2026 freeze; T/T1 are the
   two most recent consecutive reports available.
5. **Spirax Group rename:** group presents as "Spirax Group plc" (renamed from
   Spirax-Sarco Engineering plc); ticker SPX unchanged.
6. **No merger/acquisition comparability breaks** affect the corpus: no sampled firm underwent
   a group-structure-changing combination between its T and T1 cycles (Barratt Redrow, the
   draft-list merger case, is not in the frozen sample).

## 7. Limitations

- Exact direct-PDF URLs were not retained for every download; the register marks these
  honestly instead of reconstructing them.
- FTSE 100/250 segment labels are per the LSE FTSE 100 constituents page accessed 8 Oct 2026;
  quarterly index reviews may cause minor drift versus the 7 Oct freeze date.
- Publication dates for reports other than Diageo's are asserted from reporting calendars
  (period-end + statutory publication timetables), not individually re-verified against RNS.
