# Spaced repetition scheduling (MVP)

## Algorithm
Use an SM-2-style algorithm (Anki-like) with four buttons:
- Again
- Hard
- Good
- Easy

## State tracked per user word
- repetitions (int)
- intervalDays (int)
- easeFactor (double, e.g. start 2.5)
- dueDate (date)
- lastReviewedAt (date)

## Update rules (starter)
This file documents expected behavior; implementation details will live in the iOS app.

- If Again: reset repetitions to 0; set intervalDays to 1; reduce easeFactor
- If Hard: small interval increase; small easeFactor decrease
- If Good: standard interval growth
- If Easy: larger interval growth; increase easeFactor
