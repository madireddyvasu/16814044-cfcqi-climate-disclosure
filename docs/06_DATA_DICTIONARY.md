# Data Dictionary — `data/processed/cfcqi_dataset.csv`

**Grain:** one row per firm–report–year (unit of analysis). 80 rows: 40 firms × 2 reporting cycles.
**Produced by:** `scripts/01_validate_and_compute.py` from `data/interim/coding.csv` (validation: all item columns ∈ {0,1,2}; no missing firm_id).
**Codebook:** `docs/CFCQI_Codebook.md` (frozen v1.0).

## Identifiers and design

| Column | Definition | Values / unit | Source |
|---|---|---|---|
| `firm_id` | Unique firm code | F001–F040 | `docs/SAMPLE_SELECTION.md`, `data/sample_register.csv` |
| `firm_name` | Legal/group name as listed | text | FTSE 350 constituent list (LSE), frozen 2026-10-07 |
| `tcfd_group` | TCFD non-financial group | Energy / Transportation / Materials and Buildings / Agriculture Food and Forest Products | Researcher mapping (see `docs/SAMPLE_SELECTION.md` §3; Transportation n=9, Materials n=11 — documented rebalancing) |
| `cycle` | Reporting cycle | T = most recent annual report available at data cut-off; T1 = prior consecutive annual report | `data/sample_register.csv` (report_T / report_T1 columns) |

## CFCQI items (content-analysis coding)

Each item scored on the fixed 0–2 scale from the frozen codebook:
- **0** = no relevant financial connection identified
- **1** = qualitative or generic financial connection (mentioned, not quantified)
- **2** = quantified financial effect (£ figure, %, or specific link to a financial-statement item, assumption, budget or planning process)

Tie-breaks (codebook §2): higher score wins when both qualitative and quantified statements exist; carbon-emissions volume (tCO₂e) alone with no £ implication = 0; explicit "no material impact" on a specific item = 1. Every score carries a verbatim quote + printed page number in `data/interim/evidence/<firm_id>_<cycle>.md`.

| Column | Item label | What counts |
|---|---|---|
| `item1` | Current financial performance | Climate-attributed effect on in-year revenue, costs, operating profit or margins |
| `item2` | Current financial position | Climate-attributed effect on in-year balance-sheet items (assets, liabilities, equity) |
| `item3` | Current cash flows | Climate-attributed effect on in-year operating/investing/financing cash flows |
| `item4` | Anticipated future financial performance | Forward-looking climate link to future revenue, costs or profit |
| `item5` | Anticipated future financial position | Forward-looking climate link to future assets, liabilities or equity (e.g. stranded assets) |
| `item6` | Anticipated future cash flows | Forward-looking climate link to future cash generation or outflows |
| `item7` | Capital expenditure / allocation | Climate-related capex plans, transition-capex amounts or % of capex |
| `item8` | Asset valuations & impairment | Climate in impairment testing, useful lives, residual values, fair-value assumptions |
| `item9` | Provisions, contingencies & commitments | Climate-related provisions, contingent liabilities, contractual commitments |
| `item10` | Carbon pricing / ETS / regulatory costs | Quantified/described effect of carbon prices, ETS, carbon taxes, offsets |
| `item11` | Financial planning integration | Explicit link between climate strategy and budgets, business plans, capital allocation |
| `item12` | Quantified scenario analysis | Climate scenario analysis reporting quantified (£ or %) financial outcomes |

## Firm-level variables (extracted once per firm–year from the same annual report)

| Column | Definition | Unit / scale | Source & transformation |
|---|---|---|---|
| `size` | Firm size | ln(total assets in £m) | Consolidated balance sheet. **FX rule:** non-GBP reporters converted at the ECB euro foreign-exchange reference rate on the balance-sheet date; rate + date recorded per row in `notes` and evidence files (e.g. USD→GBP 0.74264 @ 31 Dec 2025; EUR→GBP 0.87260 @ 31 Dec 2025; Diageo 0.75587 @ 29 Jun 2026). ECB rates were not independently re-verified — cite ECB directly in the dissertation. |
| `assurance` | External sustainability assurance obtained | 1 / 0 (binary) | 1 = independent assurance over sustainability/environmental subject matter (limited or reasonable, even on selected metrics only); statutory financial-statement audit alone = 0. Evidence quote in evidence file. |
| `board_oversight` | Board-level sustainability/climate oversight | 1 / 0 (binary) | 1 = dedicated board-level committee OR named board committee with an explicit sustainability/climate/environment remit; 0 = full-board oversight only, or management-level committees only. Committee name + remit quoted in evidence file. |
| `leverage` | Financial leverage | ratio (total debt / total assets) | **Supervisor ruling 2026-10-07** (`docs/decision_log.md` R1): total debt = current + non-current interest-bearing borrowings **including bank overdrafts**; lease liabilities excluded where separately disclosed (included only where inseparable from the borrowings line — F015 Wizz Air, documented). Components shown per row in evidence files. |
| `roa` | Profitability | ratio (net income attributable to owners / total assets) | Income statement + balance sheet. Negative where the firm reported a loss. |
| `coder` | Coder identifier | coderA–coderK, coderM, pilot | Which coder produced the row (audit trail). 15% blind re-code performed by an independent coder — see `data/interim/reliability_recode.csv`, `results/tables/reliability.csv`. |
| `notes` | Row-level caveats | free text | FX rates/dates, debt components, year-end changes (F019 15-month T), cross-report discrepancies, MISSING flags (none remaining). |

## Computed outcome

| Column | Definition | Unit / scale | Formula |
|---|---|---|---|
| `raw_score` | CFCQI raw score | integer 0–24 | Σ(item1..item12) |
| `cfcqi` | Climate Financial Connectivity and Quantification Index | 0–100 (1 decimal) | (raw_score / 24) × 100 |

**Interpretation warning (must appear in the dissertation):** a CFCQI of 62.5 means the firm achieved 62.5% of the maximum score available under this research instrument — it is **not** a measure of regulatory compliance with UK SRS S2 / IFRS S2, which permit qualitative disclosure in some circumstances.

## Known data quirks (own these in the methodology chapter)

1. **F019 (Mobico) T** is a 15-month period to 31 Mar 2026 (year-end change Dec→Mar); figures used as reported, not annualised. Sensitivity analysis excluding F019: `results/tables/robustness.txt`.
2. **F027 (Smiths Group):** FY2026 AR unpublished at data cut-off → T=FY2025, T1=FY2024 (two most recent consecutive ARs available).
3. **F035 (M&S) T/T1** were first coded from partial PDFs (strategic report missing); invalidated and fully re-coded from complete reports on 2026-10-07 (coderM). Originals preserved as `data/raw/F035_*_partial_ORIGINAL.pdf`; source deviation (mirror access, figure cross-verification) logged in `docs/decision_log.md` R2.
4. **Transportation n=9 / Materials n=11:** only 9 FTSE 350 firms mappable to TCFD Transportation; 10th slot reallocated to Materials (see `docs/SAMPLE_SELECTION.md` §5).
5. F015 (Wizz Air) leverage includes lease liabilities (inseparable from reported borrowings line) — documented exception to the leases-excluded convention.
