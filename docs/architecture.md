# Architecture (offline-first)

## Overview
The system has two major parts:
1. **Data pipeline** (scripts/) that builds a bundled SQLite database from source datasets.
2. **iOS app** (ios/) that ships with that SQLite database and maintains a writable user database/state for SRS.

## Data stores
### 1) Bundled read-only dictionary DB (SQLite)
- Produced by scripts/build_dictionary_db.py
- Contains catalog words derived from CC-CEDICT, plus enrichment (HSK, frequency).
- Shipped in the app bundle.

### 2) User writable store
Use SwiftData (or Core Data) inside the app to store:
- user settings
- user-added custom words
- per-word SRS state (due dates, ease, interval)

## Suggested iOS modules
- DictionaryDB (read-only queries to bundled SQLite)
- UserStore (SwiftData)
- SRScheduler (pure logic)
- WordSelectionEngine (pure logic)

## Data model sketch
### CatalogWord (SQLite)
- id (int)
- hanzi_simplified (text)
- hanzi_traditional (text nullable)
- pinyin (text)
- english (text)
- hsk_level (int nullable)
- frequency_rank (int nullable)

### UserWord (SwiftData)
- id (uuid)
- catalogWordId (int nullable)
- customHanziSimplified (string nullable)
- customPinyin (string nullable)
- customEnglish (string nullable)
- createdAt

### ReviewState (SwiftData)
- userWordId
- repetitions
- intervalDays
- easeFactor
- dueDate
- lastReviewedAt

### DailyMixRule (SwiftData)
- id
- count
- grammarType (enum nullable)
- domain (string nullable)
- strictness (enum: strict | allowFill)

## Offline-first guarantees
- All study flows must function without network.
- Any optional online features must not block core flows.
