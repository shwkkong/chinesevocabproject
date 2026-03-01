"""
Build the bundled SQLite dictionary database.

This script is intended to:
1) import CC-CEDICT entries into a normalized SQLite schema
2) enrich with HSK level and frequency rank
3) output a single SQLite file suitable for bundling into the iOS app

MVP approach:
- keep schema minimal (catalog words only)
- store english as a single text field (raw gloss) initially
"""

from __future__ import annotations

import argparse
import sqlite3
from pathlib import Path

def build_db(output_db: Path) -> None:
    output_db.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(output_db)
    try:
        cur = conn.cursor()
        cur.execute(
            '''
            CREATE TABLE IF NOT EXISTS catalog_words (
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              hanzi_simplified TEXT NOT NULL,
              hanzi_traditional TEXT,
              pinyin TEXT NOT NULL,
              english TEXT NOT NULL,
              hsk_level INTEGER,
              frequency_rank INTEGER
            );
            '''
        )
        cur.execute("CREATE INDEX IF NOT EXISTS idx_catalog_hanzi_s ON catalog_words(hanzi_simplified);")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_catalog_pinyin ON catalog_words(pinyin);")
        cur.execute("CREATE INDEX IF NOT EXISTS idx_catalog_hsk ON catalog_words(hsk_level);")
        conn.commit()
    finally:
        conn.close()

def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output", required=True, help="Path to output SQLite DB")
    args = parser.parse_args()

    build_db(Path(args.output))
    print(f"Created/updated DB schema at {args.output}")

if __name__ == "__main__":
    main()
