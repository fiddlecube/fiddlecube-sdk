# FiddleCube - Generate ideal question-answers for testing RAG

FiddleCube generates an ideal question-answer dataset for testing your LLM. Run tests on this dataset before pushing any prompt or RAG upgrades.

## Quickstart

### Install FiddleCube

```bash
pip3 install fiddlecube
```

### API Key

Get the API key [here](https://dashboard.fiddlecube.ai/api-key).

### Usage

```python
from fiddlecube import FiddleCube

fc = FiddleCube(api_key="<api-key>")
dataset = fc.generate(
    [
        "The cat did not want to be petted.",
        "The cat was not happy with the owner's behavior.",
    ],
    10,
)
dataset
```

```json
{
  "results": [
    {
      "query": "Question: Why did the cat not want to be petted?",
      "contexts": ["The cat did not want to be petted."],
      "answer": "The cat did not want to be petted because it was not in the mood for physical affection at that moment.",
      "score": 0.8,
      "question_type": "SIMPLE"
    },
    {
      "query": "Was the cat pleased with the owner's actions?",
      "contexts": ["The cat was not happy with the owner's behavior."],
      "answer": "No, the cat was not pleased with the owner's actions.",
      "score": 0.8,
      "question_type": "NEGATIVE"
    }
  ],
  "status": "COMPLETED",
  "num_tokens_generated": 44,
  "rate_limited": false
}
```

## Ensuring diversity and correctness

- The questions are spread across the vector embeddings to ensure completeness of testing.
- The queries and responses are evaluated for correctness and context relevancy.
- Citations to the database context are maintained for ease of testing and auditing.

## Roadmap

- [x] Question-answers, complex reasoning from RAG
- [ ] Multi-turn conversations
- [ ] Evaluation Setup - Integrate metrics
- [ ] CI setup - Run as part of CI/CD pipeline
- [ ] Diagnose failures - step-by-step analysis of failed queries

## More Questions?

[Book a demo](https://cal.com/kaushiks/fc)  
Contact us at [founders@fiddlecube.ai](mailto:founders@fiddlecube.ai) for any feature requests, feedback or questions.
