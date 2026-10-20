# Decision Log — CFCQI coding

Examiner-facing record of ambiguous coding cases and rule refinements. Append-only; newest entries at the bottom.

---

## 2026-10-07 — Pilot (5 reports: F001 Shell, F008 Harbour, F011 IAG, F020 Rio Tinto, F031 Diageo) — codebook v1.0 frozen

### Rule refinements adopted
1. **Item 2 = 2 for quantified % of carrying value.** Shell: "Over 12% (based on the carrying value) of physical assets tested are considered to be exposed to climate-related physical risks" (p.80) → 2. A quantified exposure as a % of the asset base counts as 2 even without a £ figure.
2. **Dual scoring permitted.** The same evidence may support multiple items; each item is scored on its own definition. Examples: Shell's scenario-quantified asset effects score under both item 5 and item 12; IAG's carbon obligations score under items 1, 2, 9 and 10.
3. **Item 11 = 2 for standing mechanisms.** A standing decision rule or ongoing mechanism = 2: Shell "Our Operating Plan includes carbon cost forecasts and targets" (Note 4, p.247); Harbour "All new economic investment decisions include the cost of carbon" + climate target in annual bonus (pp.52, 141); Rio Tinto "We apply an internal carbon price ... to inform investment decisions" (p.79). A one-off analysis = 1: IAG "Updated internal carbon pricing modelling to assess the contribution of new, more fuel-efficient aircraft" (p.278).
4. **Item 9 requires a specific provision/contingency figure.** Generic assumption lists do not score. An auditor's KAM mentioning climate in provision inputs (Rio Tinto closure provisions, "not significant to warrant separate discussion") is not a management disclosure → 0.
5. **"No material impact" = 1, not 0.** An explicit statement that climate testing found no material FS impact evidences the assessment: Harbour item 2 ("No material impairments were identified through the analysis", p.54); Diageo item 8 ("identified no material financial impact to the current year impairment assessments", p.165).
6. **Board oversight — strict reading.** Full-board oversight without a dedicated/named committee = 0 (Shell: Sustainability Management Committee is management-level; ARC discusses climate but has no explicit climate remit). Named board committee with explicit climate/environment remit = 1 (Harbour HSES Committee, p.52; IAG Environmental and Corporate Responsibility Committee, p.92; Rio Tinto Sustainability Committee).
7. **Assurance = 1** for external assurance over sustainability/environmental subject matter, even on selected metrics only (IAG: reasonable assurance on Scope 1, p.261; Diageo: PwC limited assurance on selected metrics, p.5). Statutory financial audit alone = 0.
8. **FX rule.** Non-GBP total assets convert at the ECB euro foreign exchange reference rate on the balance-sheet date; record rate + source in notes. 31 Dec 2025: USD→GBP 0.74264, EUR→GBP 0.87260.
9. **Page numbers** in evidence files are the report's printed page numbers (footer/contents), not PDF-viewer page numbers.
10. **Carbon volume alone (tCO₂e) = 0** on all items (reaffirmed; no pilot case scored on volume).

### Pilot score summary
| Firm | TCFD group | Raw | CFCQI |
|---|---|---|---|
| F001 Shell | Energy | 17 | 70.8 |
| F008 Harbour | Energy | 12 | 50.0 |
| F011 IAG | Transportation | 14 | 58.3 |
| F020 Rio Tinto | Materials & Buildings | 16 | 66.7 |
| F031 Diageo | Agri/Food/Forest | 4 | 16.7 |

### Judgement calls
- **Rio Tinto item 1 = 1 (not 0 or 2):** the $122m pre-tax RTITQO impairment charge was recognised after an impairment test whose cash flows explicitly included carbon costs and carbon-abatement opportunities, but the charge itself was not attributed to climate (trigger was market conditions). Scored 1 = qualitative linkage to a recognised P&L charge.
- **Rio Tinto item 12 = 2:** the "+25% carbon tax from 2040 → US$250m lower NPV" sensitivity is treated as a quantified scenario outcome (sensitivity on the key climate input with a £ outcome).
- **IAG item 3 = 2:** "Purchase of carbon-related assets net of the change in carbon-related obligations (118)" is a carbon-specific line in the cash flow statement (€m, p.37).
- **Shell board_oversight = 0:** deliberate strict application — tests the discriminant validity of the variable (high discloser, no dedicated committee).

## 2026-10-07 — Corrections during full coding

1. **Diageo presentation currency (pilot correction).** The pilot coded F031_T size as a GBP reporter (ln(46,845) = 10.7546). coderF verified the FY2026 financial statements are "presented in US dollar" (p.151); Diageo switched presentation currency to USD. Corrected: size = ln(46,845 × 0.75587) = 10.4747 (ECB USD→GBP 0.75587, 29 Jun 2026 — closest published rate to the 30 Jun 2026 balance-sheet date). Leverage and ROA are currency-neutral and unchanged. T1 (coderF) uses 30 Jun 2025 USD→GBP 0.72995.
2. **Smiths Group (F027) cycle correction.** F027_T.pdf and the recovered F027_T1.pdf were byte-identical — both the Smiths FY2025 AR (year ended 31 Jul 2025); the FY2026 AR was not published as of 2026-10-07 (only FY2025 AR + FY2026 results materials on smiths.com). Resolution: T = FY2025 (coderF's coding retained), T1 = FY2024 (fresh download + coding commissioned 2026-10-07). Sample register updated accordingly.

3. **Board-oversight borderline: Audit & Risk Committee with climate wording.** Pilot (Shell): ARC "discusses climate change and the energy transition" in FS oversight → 0 (no explicit remit). coderC (Clarkson): ARC "monitors the impact of climate change on our principal risks" → 1 (explicit climate remit in described role). Both retained as coded; the wording difference is genuine (oversight-of-risk vs discussion-in-FS-review). Flagged for reliability review.

## 2026-10-07 — Reliability: 15% blind re-code results

- 12 reports re-coded blind by coderR (independent; coded none of the 12). Pooled: 66.7% agreement, weighted κ = **0.631** ≥ 0.60 target. Item κ range: −0.286 (item 1) to 0.757 (item 8).
- Systematic patterns: re-coder stricter on item 12 (quantified scenario outcomes; several 2→1) and item 1 (current P&L; several 1→0/2→1), but more generous on items 5/7 for Harbour T.
- Spot-check F019_T1 item 1 (orig 0 → recode 2): the £4.9m/£2.1m/£2.6m diesel depreciation figures are forward-looking sensitivities ("would be required from 1 January 2025"), correctly placed under items 4/8 by coderD; they are not current-year recognised effects. Original coding retained.
- Conclusion: disagreements are 0/1/2 boundary judgments, not clear errors; pooled κ meets the pre-registered threshold. No reconciliation changes made; item-level κ table retained in results/tables/reliability.csv for the technical appendix / audit record.

## 2026-10-07 — Final batch (coderH): Energean plc (F010) + IMI plc (F028)

Both firms scored **identically across cycles** — no within-firm change to note for RQ3 on these cases (Energean raw 17 / CFCQI 70.8 both years; IMI raw 9 / CFCQI 37.5 both years).

**Energean (F010), Energy, USD reporter.** Item pattern `[2,0,2,1,2,1,1,2,0,2,2,2]`:
1. Items 1 & 3 = 2 via dual scoring of the purchased-carbon-allowance figure (£1.3m T / £0.7m T1) with item 10 — follows the pilot IAG precedent (carbon obligations scored across items 1, 2, 9, 10); item 3 matches the codebook's item-3 example verbatim.
2. Item 5 = 2 via dual scoring of the NZE-scenario NPV10 outcome (−17% T / −19% T1 vs base case) with item 12 — follows the pilot Shell precedent. Source text verified: "Under the NZE, Group NPV10 is reduced by 17%". Without dual scoring, item 5 would fall to 1 (qualitative stranded-asset statements only).
3. Item 7 = 1, not 2: the $2.5m/$2.4m "environmental expenditure" is footnoted as general environmental capex (oil-spill readiness, waste, permitting, methane monitoring), not transition-specific, so it does not meet the 2-level. Qualitative climate-investment statements support 1.
4. Item 8 = 2: Note 4 — carbon pricing explicitly incorporated in DCF valuations for impairment (forecast carbon price × estimated Scope 1&2 emissions).
5. Item 9 = 0: the $835m decommissioning provision is not climate-attributed; management concludes climate "does not currently represent a key source of estimation uncertainty" for decommissioning.
6. **Cross-report discrepancy:** T's comparative column shows 2024 purchased allowances as £0.8m, but T1's own table shows £0.7m. Each cycle was coded from its own report (T1 = £0.7m).
7. Board_oversight = 1: ESSR Committee — named board committee explicitly "delegated responsibility for climate change oversight on behalf of the Board". Assurance = 1: EY Greece climate change and sustainability assurance statement (limited-level subject-matter assurance).
8. FX: T = ln(5,589.29 × 0.74264) = 8.3311 (ECB 31 Dec 2025); T1 = ln(5,924.624 × 0.79813) = 8.4614 (ECB 31 Dec 2024). No non-controlling interest in either year — profit fully attributable to owners.

**IMI (F028), Materials and Buildings, GBP reporter.** Item pattern `[0,1,0,2,0,0,0,1,0,1,2,2]`:
1. Item 4 = 2 via dual scoring of Table 3 (p.202) with item 12: % impact bands (Low 0–3% / Med 3–6% / High >6%) on Group adjusted operating profit under IEA NZE and STEPS for 2030/2050. The bands are coarse and the underlying analysis is flagged as based on FY2022/23 data, but the codebook's 2-level item-4 example is a %-of-profit figure and imposes no recency requirement — kept at 2 as a boundary call.
2. Items 2 and 8 = 1 per the "no material impact" rule: the FS climate-change note (T p.146) explicitly states climate was considered in goodwill/intangible carrying-value assessment and tangible-asset useful lives, "no material impact identified".
3. Item 10 = 1: CBAM financial-impact monitoring described qualitatively (no £ figure).
4. Item 11 = 2: 10% of the LTIP award subject to CO₂ intensity reduction — a standing mechanism (matches the Harbour pilot precedent); sustainability-linked RCF recorded as a corroborating mechanism. The internal carbon price is only planned ("evaluate options to develop") — not scored.
5. Item 9 = 0: £1.6m environmental & legal provisions are contaminated-land only, no climate link; auditor's KAM on provisions does not mention climate.
6. Leverage excludes the bank overdraft (£43.5m T / £91.0m T1): it is presented as a separate balance-sheet line, and the codebook defines total debt as "interest-bearing borrowings, current + non-current". Including overdraft would give T = 0.2280, T1 = 0.2435.
7. Board_oversight = 1: Board-level Sustainability Committee (chaired by Thomas Thune Andersen; established 2024). Assurance = 1: Ricardo limited-level ISO 14064-3 verification of SECR Scope 1&2 data.
8. roa uses profit after tax fully attributable to owners (309.9/2480.1 = 0.1250; 248.5/2490.5 = 0.0998).

## Locked methodological rulings — 2026-10-07 (full implementation audit)

### R1. Leverage definition — bank overdrafts INCLUDED (MAJOR, fixed)
**Issue:** Codebook defines leverage = "total debt / total assets (total debt = interest-bearing borrowings, current + non-current)". coderH (IMI, F028) excluded bank overdrafts as a "separate line"; coders for F030 (Spirax-Sarco) and F034 (ABF) included overdrafts in borrowings. Dataset was inconsistent.
**Ruling:** Bank overdrafts ARE interest-bearing borrowings (repayable on demand, interest-bearing; IAS 32 financial liabilities) and MUST be included in total debt. Lease liabilities: EXCLUDED where separately disclosed (uniform convention across 12+ evidence files); included ONLY where inseparable from the reported borrowings line (F015 Wizz Air — documented exception, balance sheet aggregates them).
**Fix applied:** F028_T leverage 0.2105 → 0.2281 (added £43.5m overdraft); F028_T1 0.2069 → 0.2435 (added £91.0m overdraft). Updated in data/interim/coding.csv, data/processed/cfcqi_dataset.csv, and both F028 evidence files. Impact on RQ2: negligible (control variable; see scripts/06_robustness.py re-run) — but consistency is now internally consistent and auditable.

### R2. F035 (M&S) partial-PDF rows INVALIDATED (CRITICAL, fixed)
**Issue:** data/raw/F035_T.pdf and F035_T1.pdf were 90/91-page extracts (auditor's report → financial statements only); the strategic report incl. the TCFD section was missing. coderG correctly flagged items 4,5,6,7,10,12 as "not assessable" and assurance/board_oversight as 0 — but these rows entered the dataset with CFCQI 12.5/16.7 as if the zeros were real. Two of 80 rows were invalid.
**Fix applied:** Full official-content reports obtained (F035_T1 = 224pp FY2024/25 AR; F035_T = 208pp FY2025/26 AR). Official M&S site bot-blocks automated download; verified genuine via companiesmarketcap.com mirror (financial-statement figures cross-checked against the official extract: total assets £8,821.4m matches). Originals preserved as F035_*_partial_ORIGINAL.pdf. Both reports re-coded from scratch per frozen codebook v1.0 (coderM); rows replaced in data/interim/coding.csv; pipeline re-run.
**Methodological note:** document the source deviation transparently (official content, mirror access, figure cross-verification).

### R3. data/sample_register.csv — malformed row + stale F019 period (MINOR, fixed)
F027's notes field contained an unquoted comma (broke strict CSV parsing; pandas raised ParserError). Quoted. F019's register row still showed "FY2025 (Dec YE)" for T although the coded T is the 15-month period to 31 Mar 2026 — corrected to "15m to 31 Mar 2026 (year-end change)" with note. Also corrected an in-progress edit that had briefly placed the label in the wrong column (caught before any analysis used the register).

### R4. Currency documentation (MINOR, verified — no fix needed)
All non-GBP reporters document ECB rate + balance-sheet date in evidence files (USD: 0.74264 @ 31 Dec 2025 / 0.79813 @ 31 Dec 2024; EUR: 0.87260/0.82918 @ 31 Dec; Diageo USD 0.75587 @ 29 Jun 2026 / 0.72995 @ 30 Jun 2025; Wizz EUR 0.8684 @ 31 Mar 2026 / 0.83536 @ 31 Mar 2025). F015's coder used a secondary ECB-fixings table ("cambridgecurrencies") rather than the ECB Official Journal — downstream reporting should cite the ECB directly. ECB rates themselves were NOT independently re-verified — flagged as residual risk.

### R5. Borderline judgments left standing (documented, for Vasu to confirm)
- F009 board_oversight=1 (Audit Committee climate-risk oversight, no dedicated committee) — logged by coderB as borderline; defensible either way under the codebook's "named board committee with explicit remit" clause.
- F012 item10=2 for quoted carbon prices (£37/t, €68/t) rather than a firm cost figure — generous but within the item's "quantified carbon-price" wording.
- F023 item1=1 on "continuity of operations" (operational, not explicitly financial) — defensible.
- F034 item11=2 on "embedded in budgets and long-term plans" — defensible.
None overturned; all within reasonable coder judgment. Vasu should confirm the F009 board_oversight call as it feeds H3, the study's strongest result.

## coderM — F035 M&S full-report re-code (2026-10-07)

Ambiguous/borderline calls on the two re-coded rows (T = FY2025/26 AR, T1 = FY2024/25 AR):

1. **Item 10 = 2 on EPR/PRN regulatory costs (T):** "£24.5m Extended Producer Responsibility (EPR) charges" (p.17) and "c. £38m incurred in FY 2025/26 for EPR and PRNs" (p.31) scored 2 under the item's "related regulation" wording ("Carbon pricing, ETS and regulatory cost quantification"). EPR/PRN are environmental (not carbon) regulatory costs — a stricter reading could score 0/1. Kept at 2 given the item's broad "regulatory cost quantification" clause.
2. **Item 10 = 2 on modelled 2030 carbon tax (T1):** the £115m–£165m figure is a forward-looking scenario quantification (Table 2, p.47), not an incurred cost. Item 10 does not restrict to current-period effects; scored 2, dual-scored with items 4 and 12.
3. **Item 6 = 2 (T1):** "Potential impact of £30-40m if not mitigated" for low-carbon technology/infrastructure (p.43) — described as "increase in capital and operational expenditure", not explicitly cash flows. Scored 2 as a forward-looking quantified future outflow; dual-scored with Item 4.
4. **Item 6 = 2 (T):** Plan A Accelerator Fund "commits £1m annually" (p.35) — quantified but immaterial vs group scale (£17bn revenue). Codebook sets no materiality threshold for 2; scored 2.
5. **Item 3 = 1 (both cycles):** via the no-material-impact rule on the impairment note quote "with no material impact on cash flows" (T p.148; T1 p.156). The T-year in-year £748k energy-efficiency savings (p.38) were treated as Item 1 support, not Item 3, since not framed as a cash-flow effect.
6. **Item 7 asymmetry across cycles:** T = 2 on £40.3m "other property investments, including energy efficiency and store environment improvements" (financial review, p.22); T1 = 1 — the equivalent capex ("Capital investment through proactive asset replacement... integrated into the three-year financial plan", p.42) carries no £ figure, and no £ figure was found in the T1 financial review capex breakdown.
7. **Leverage (R1 ruling applied):** lease liabilities EXCLUDED as separately disclosed — T: borrowings £3,419.4m − leases £2,750.0m = £669.4m → 0.0662; T1: £2,944.5m − £2,227.4m = £717.1m → 0.0813. No bank overdrafts separately disclosed (searched; nil). Note: the earlier partial-PDF coding had included lease liabilities (0.3381/0.3338) — corrected per R1.
8. **Item 5 = 1 (both cycles):** flood-risk financial impact stated as "immaterial" (T p.33; T1 Table 2 p.47) treated as an explicit no-material-impact statement per codebook rule; warehouses "would not expect to be physically impacted" (T p.148) corroborates.

### R6. F035 (M&S) re-code completed from full reports (CRITICAL fix closed) — 2026-10-07
**Action:** Full reports obtained — F035_T = 208pp FY2025/26 AR (ended 28 Mar 2026), F035_T1 = 224pp FY2024/25 AR (ended 29 Mar 2025). Official M&S site bot-blocks automated downloads; documents sourced via companiesmarketcap.com mirror and verified genuine (financial-statement figures cross-checked against the official extract: total assets £10,114.8m T / £8,821.4m T1 match). Original partials preserved as `data/raw/F035_*_partial_ORIGINAL.pdf`. Both reports re-coded from scratch per frozen codebook v1.0 (coderM); rows replaced in place in `data/interim/coding.csv` (80 rows, no duplicates); evidence files rewritten (PARTIAL warnings removed); 8 ambiguous calls appended by coderM.
**New scores:** F035_T raw 17 → CFCQI 70.8 (was 12.5); F035_T1 raw 14 → CFCQI 58.3 (was 16.7). assurance 0→1 both cycles (Deloitte limited assurance on GHG data); board_oversight 0→1 both cycles (board-level ESG Committee, all NEDs). Leverage recomputed per R1 ruling (leases excluded): T 0.0662, T1 0.0813 (old partial-based values 0.3381/0.3338 had included lease liabilities — the large swing is M&S's £2.75bn lease book incl. Ocado consolidation).
**Impact on results:** RQ1 mean 50.46→51.77; Agri group mean 40.62→45.82; RQ2 H2 p 0.094→0.185 (assurance now clearly non-significant); R² 0.539→0.478; RQ3 p 0.952→0.896 (still null). All headline conclusions unchanged. Pipeline re-run end-to-end (scripts 01–06); findings summary, results tables and README refreshed.
**Borderline calls by coderM (Vasu to confirm):** item 10 on EPR/PRN regulatory costs (T); item 10 on forward carbon-tax scenario figure (T1); item 6 (T1) "potential impact" capex/opex figure; £1m annual fund treated as quantified.
