# Sample Selection — FTSE 350 Climate-Sensitive Firms

**Study:** Quantified and Financially Connected Climate Disclosure in Climate-Sensitive FTSE 350 Firms (7015SOM, Route 1)
**Freeze date:** 7 October 2026 (constituent list and market caps frozen on this date)

## 1. Source of the constituent list

FTSE 350 constituents as published on the London Stock Exchange website
(`londonstockexchange.com`, "FTSE 350 Constituents" page), accessed 7 October 2026.
All 40 selected firms were verified as constituents on that page on the freeze date.

## 2. Exclusion criteria

- **Financial firms excluded:** banks, insurers, asset managers, investment trusts, private-equity
  vehicles, pension/wealth managers, and real-estate/property companies (REITs) — i.e. all firms
  whose primary business is financial intermediation or property investment. Although the TCFD
  places real-estate management & development in "Materials and Buildings", property companies were
  excluded here as financial-sector-adjacent, keeping the sample to operating companies.
- Firms that have delisted or been acquired (e.g. DS Smith, Britvic, Ashtead, CRH, Darktrace,
  Hargreaves Lansdown) do not appear on the freeze-date constituent list and are therefore out
  of the sampling frame by construction.

## 3. TCFD group mapping logic

Firms were mapped to the four TCFD non-financial groups using TCFD industry descriptions as the
guide (industries treated as indicative, not exhaustive):

- **Energy:** oil & gas (integrated, exploration & production), oil & gas refining & marketing,
  electric/gas utilities, renewable power. DCC plc (energy & LPG distribution) mapped here.
- **Transportation:** airlines, maritime/shipping services, rail & bus operators, automobiles
  (manufacturing and distribution value chain), vehicle rental/leasing. Inchcape (auto
  distribution) and Zigup (vehicle rental/leasing) included on value-chain grounds; Aston Martin
  (auto manufacturing) included under automobiles.
- **Materials and Buildings:** metals & mining, chemicals, construction materials, capital
  goods / industrial engineering. Diploma, Smiths Group, IMI, Weir Group and Spirax-Sarco
  included as capital-goods firms.
- **Agriculture, Food and Forest Products:** beverages, packaged foods & food ingredients,
  agriculture, paper & forest products. Food retailers (Tesco, Sainsbury's, M&S, Ocado) included
  on food-value-chain climate-exposure grounds (Scope 3 supply chains are their dominant climate
  linkage). Mondi mapped here as paper & forest products per TCFD.

## 4. Selection rule

Within each group, firms were ranked by market capitalisation from a **single consistent source**:
companiesmarketcap.com (individual company market-cap pages), accessed 7 October 2026; figures
recorded in USD billions in `data/sample_register.csv`. The 10 largest per group were selected.

## 5. Documented deviation — rebalancing

The Transportation group contained only **9 eligible** FTSE 350 firms (IAG, easyJet, Wizz Air,
Aston Martin, Clarkson, FirstGroup, Mobico, Zigup, Inchcape). No other FTSE 350 constituent
could be defensibly mapped to TCFD Transportation industries. To hold the total at n = 40,
the 10th Transportation slot was reallocated to Materials and Buildings (the largest eligible
group), giving 11 firms there: the 11th pick is Spirax-Sarco Engineering ($7.20B), the next
largest materials firm after Weir Group ($9.17B); the first excluded materials firm is
Croda International ($6.19B).

## 6. Close calls (inclusion boundaries)

- **Energy #10:** Energean ($1.75B) selected over Diversified Energy ($0.98B).
- **Agriculture #10:** Ocado ($2.91B) selected over Premier Foods ($2.14B). Greencore and C&C
  Group had no companiesmarketcap.com page; both are well below the boundary on any measure
  (~£1.1B and ~£0.4B respectively) and could not have displaced Ocado.
- **Materials #11:** Spirax-Sarco ($7.20B) selected over Croda ($6.19B); Johnson Matthey,
  Rotork, Berkeley, Persimmon and Taylor Wimpey all below $6B — none threatened the boundary.
- Coca-Cola HBC (LSE: CCH, $20.49B) verified as distinct from Coca-Cola Europacific Partners
  (CCEP); the LSE-listed HBC entity is the sample member.

## 7. Reporting cycles

- **T** = the most recent annual report available at the data cut-off; **T1** = the prior
  consecutive annual report. Expected periods per firm are recorded in
  `data/sample_register.csv` (e.g. FY2025/FY2024 for December year-ends; FY2025/26 for March
  year-ends) and were verified at download. Two firms (Smiths Group, Diageo) have non-December
  year-ends whose latest reports were flagged for availability verification at download.

## 8. Final sample (40 firms)

| ID | Firm | Group | MCap $B |
|---|---|---|---|
| F001 | Shell plc | Energy | 278.03 |
| F002 | BP plc | Energy | 115.92 |
| F003 | National Grid plc | Energy | 77.26 |
| F004 | SSE plc | Energy | 39.85 |
| F005 | Centrica plc | Energy | 8.87 |
| F006 | DCC plc | Energy | 7.28 |
| F007 | Ithaca Energy plc | Energy | 6.00 |
| F008 | Harbour Energy plc | Energy | 5.90 |
| F009 | Drax Group plc | Energy | 3.60 |
| F010 | Energean plc | Energy | 1.75 |
| F011 | International Consolidated Airlines Group SA | Transportation | 25.79 |
| F012 | easyJet plc | Transportation | 6.72 |
| F013 | Inchcape plc | Transportation | 3.48 |
| F014 | Clarkson plc | Transportation | 2.07 |
| F015 | Wizz Air Holdings plc | Transportation | 1.44 |
| F016 | Zigup plc | Transportation | 1.32 |
| F017 | FirstGroup plc | Transportation | 1.28 |
| F018 | Aston Martin Lagonda Global Holdings plc | Transportation | 0.47 |
| F019 | Mobico Group plc | Transportation | 0.19 |
| F020 | Rio Tinto plc | Materials and Buildings | 155.95 |
| F021 | Glencore plc | Materials and Buildings | 86.20 |
| F022 | Anglo American plc | Materials and Buildings | 59.05 |
| F023 | Antofagasta plc | Materials and Buildings | 50.10 |
| F024 | Fresnillo plc | Materials and Buildings | 27.08 |
| F025 | Endeavour Mining plc | Materials and Buildings | 13.44 |
| F026 | Diploma plc | Materials and Buildings | 13.98 |
| F027 | Smiths Group plc | Materials and Buildings | 10.53 |
| F028 | IMI plc | Materials and Buildings | 9.81 |
| F029 | Weir Group plc | Materials and Buildings | 9.17 |
| F030 | Spirax-Sarco Engineering plc | Materials and Buildings | 7.20 |
| F031 | Diageo plc | Agriculture, Food and Forest Products | 47.14 |
| F032 | Tesco plc | Agriculture, Food and Forest Products | 38.85 |
| F033 | Coca-Cola HBC AG | Agriculture, Food and Forest Products | 20.49 |
| F034 | Associated British Foods plc | Agriculture, Food and Forest Products | 16.99 |
| F035 | Marks and Spencer Group plc | Agriculture, Food and Forest Products | 10.59 |
| F036 | J Sainsbury plc | Agriculture, Food and Forest Products | 9.30 |
| F037 | Mondi plc | Agriculture, Food and Forest Products | 4.65 |
| F038 | Cranswick plc | Agriculture, Food and Forest Products | 3.53 |
| F039 | Tate & Lyle plc | Agriculture, Food and Forest Products | 3.29 |
| F040 | Ocado Group plc | Agriculture, Food and Forest Products | 2.91 |

Note: Diploma ($13.98B) is listed above Endeavour Mining ($13.44B) in the table but both are
selected; order within the table follows the register, not strict rank.
