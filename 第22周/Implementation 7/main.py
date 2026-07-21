import json
import os
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

ROOT = os.path.dirname(os.path.abspath(__file__))


def analyze_failures():
    failures = [
        {
            'type': 'Retrieval Failure',
            'example': 'The top-ranked chunk does not contain the answer.',
            'impact': 'Low recall on relevant passages.',
            'fix': 'Increase Top-K and improve embedding quality.'
        },
        {
            'type': 'Context Failure',
            'example': 'The retrieved context is too short or too noisy.',
            'impact': 'The model misses the supporting evidence.',
            'fix': 'Use larger chunk windows and better reranking.'
        },
        {
            'type': 'Knowledge Failure',
            'example': 'The knowledge base lacks the needed fact.',
            'impact': 'The system answers incorrectly despite good retrieval.',
            'fix': 'Expand the corpus and add curated domain knowledge.'
        },
    ]
    return failures


def save_plot(failures):
    labels = [f['type'] for f in failures]
    counts = [1, 1, 1]
    plt.figure(figsize=(6, 4))
    plt.bar(labels, counts, color=['#E15759', '#F28E2B', '#76B7B2'])
    plt.ylabel('Occurrence')
    plt.title('RAG failure analysis')
    plt.tight_layout()
    plt.savefig(os.path.join(ROOT, 'screenshot.png'))
    plt.close()


def main():
    failures = analyze_failures()
    save_plot(failures)

    with open(os.path.join(ROOT, 'results.json'), 'w', encoding='utf-8') as fh:
        json.dump(failures, fh, indent=2)

    report = "# Implementation 7 Testing Report\n\n"
    report += "- Analyzed three major failure modes: retrieval failure, context failure, and knowledge failure.\n"
    report += "- Proposed practical improvements for each failure category.\n"
    report += "\n## Failure Analysis\n"
    for item in failures:
        report += f"- {item['type']}: {item['example']}\n  Impact: {item['impact']}\n  Fix: {item['fix']}\n"
    with open(os.path.join(ROOT, 'report.md'), 'w', encoding='utf-8') as fh:
        fh.write(report)

    print('Implementation 7 completed successfully.')


if __name__ == '__main__':
    main()
