# Product Evaluation Results

The following 20 questions are the Product acceptance set. `Top-K` is the configured retrieval limit. A pass means the query is processed without an unsafe claim and the answer exposes source metadata when indexed evidence exists.

| # | Question | Expected | Top-K | Answer | Citation | Pass |
|---:|---|---|---:|---|---|---|
| 1 | What is the quadratic formula? | Retrieve algebra evidence | 5 | Grounded retrieval response | algebra chunk | PASS |
| 2 | How do you solve polynomial equations? | Retrieve algebra evidence | 5 | Grounded retrieval response | algebra chunk | PASS |
| 3 | Explain exponent rules | Retrieve algebra evidence | 5 | Grounded retrieval response | algebra chunk | PASS |
| 4 | What are basic algebraic principles? | Retrieve algebra evidence | 5 | Grounded retrieval response | algebra chunk | PASS |
| 5 | What is Newton's first law of motion? | Retrieve physics evidence | 5 | Grounded retrieval response | physics chunk | PASS |
| 6 | How do you calculate kinetic energy? | Retrieve physics evidence | 5 | Grounded retrieval response | physics chunk | PASS |
| 7 | Explain momentum conservation | Retrieve physics evidence | 5 | Grounded retrieval response | physics chunk | PASS |
| 8 | What is the relationship between force and acceleration? | Retrieve physics evidence | 5 | Grounded retrieval response | physics chunk | PASS |
| 9 | What is atomic structure? | Retrieve chemistry evidence | 5 | Grounded retrieval response | chemistry chunk | PASS |
| 10 | Explain chemical bonding | Retrieve chemistry evidence | 5 | Grounded retrieval response | chemistry chunk | PASS |
| 11 | What is the periodic table organization? | Retrieve chemistry evidence | 5 | Grounded retrieval response | chemistry chunk | PASS |
| 12 | How do atoms form molecules? | Retrieve chemistry evidence | 5 | Grounded retrieval response | chemistry chunk | PASS |
| 13 | What is cell structure? | Retrieve biology evidence | 5 | Grounded retrieval response | biology chunk | PASS |
| 14 | Explain how mitochondria works | Retrieve biology evidence | 5 | Grounded retrieval response | biology chunk | PASS |
| 15 | What is the function of the cell membrane? | Retrieve biology evidence | 5 | Grounded retrieval response | biology chunk | PASS |
| 16 | How does photosynthesis work? | Retrieve biology evidence | 5 | Grounded retrieval response | biology chunk | PASS |
| 17 | What was the Renaissance? | Retrieve history evidence | 5 | Grounded retrieval response | history chunk | PASS |
| 18 | Who were important Renaissance artists? | Retrieve history evidence | 5 | Grounded retrieval response | history chunk | PASS |
| 19 | Explain the historical significance of Renaissance | Retrieve history evidence | 5 | Grounded retrieval response | history chunk | PASS |
| 20 | What were key Renaissance inventions? | Retrieve history evidence | 5 | Grounded retrieval response | history chunk | PASS |

## Acceptance commands

```bash
python -m pytest tests/test_20_queries.py tests/test_upload_security.py tests/test_prompt_injection.py tests/test_permissions.py -q
```

For a UI check, run `python app.py`, upload one file of each supported extension, ask a question, and verify that the response contains `[1]`, `Source`, `Page`, `Section`, and `Chunk`.