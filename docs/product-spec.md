# ChineseVocabProject — Product Spec (MVP)

## Goal
An offline-capable iPhone app for native English speakers learning Chinese. The app provides:
- daily new vocabulary selected by user-configurable criteria
- spaced repetition reviews (SRS)
- ability for users to add custom words

## Target platform
- iOS (iPhone), SwiftUI
- Offline-first: core study experience works without network

## Key concepts
- **Catalog word**: an entry from the bundled dictionary database (CC-CEDICT-derived)
- **User word**: a word the user is learning (may reference a catalog word or be fully custom)
- **Review**: an SRS event for a user word
- **Daily mix rule**: an allocation of today’s new words to a filter (grammar type, domain, or both)

## Onboarding / Setup
### Settings captured
1. Included HSK levels (1–6)
2. New words per day (minimum 5)
3. Daily mix rules
   - user defines multiple rules; each rule has:
     - count (integer)
     - grammar type filter (optional)
     - domain filter (optional)
     - strictness: strict or allow-fill
   - total counts should equal “new words per day”
4. Pinyin display
   - default show pinyin
   - optional hide pinyin until reveal

## Daily flow
### Today screen
- Reviews due today (SRS)
- New words available today (based on rules)

### Review session
For each due word:
- show Hanzi + (optionally) pinyin + English gloss
- user rates recall: Again / Hard / Good / Easy

### New word session
- app selects new words from the catalog and/or user custom words
- after first exposure, the word becomes a user word and enters SRS

## Vocabulary selection rules
- Default: **strict filters** per rule
- If insufficient matches, and rule is configured as allow-fill:
  - fill remainder from closest matches (same HSK constraints, then “general” domain)

## Data requirements (MVP)
Each catalog entry should have at minimum:
- simplified hanzi
- traditional hanzi (optional if available)
- pinyin
- English gloss
- HSK level (nullable)
- optional: frequency rank

## Non-goals (MVP)
- Online sync (may be added later)
- Audio, handwriting, OCR, camera lookup
