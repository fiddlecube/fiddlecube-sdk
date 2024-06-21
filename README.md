# FiddleCube - Generate golden evaluation datasets for RAG

Generate golden datasets containing ideal outputs to evaluate RAG systems.

## How does it work?

Feed a set of chunks from your vector DB to Fiddlecube. Generate a wide range of queries to evaluate your LLM.
When evaluation fails, diagnose it step by step to come up with actionable insights.
Identify the root cause of failures: whether it is your prompt, RAG system or lack of correct context in the DB.

## Installation

```bash
pip3 install fiddlecube
```

## Usage

### Generate data

```python
from fiddlecube.fiddlecube import FiddleCube

fc = FiddleCube(api_key="<api-key>")
dataset = fc.generate(
    [
        "The cat did not want to be petted.",
        "The cat was not happy with the owner's behavior.",
    ],
    10,
)
print(dataset)
```

```json
{'results': [{'query': 'Question: Why did the cat not want to be petted?', 'contexts': ['The cat did not want to be petted.'], 'answer': 'The cat did not want to be petted because it was not in the mood for physical affection at that moment.', 'score': 0.8, 'question_type': 'SIMPLE'}, {'query': "Was the cat pleased with the owner's actions?", 'contexts': ["The cat was not happy with the owner's behavior."], 'answer': "No, the cat was not pleased with the owner's actions.", 'score': 0.8, 'question_type': 'NEGATIVE'}], 'status': 'COMPLETED', 'num_tokens_generated': 44, 'rate_limited': False}
```

### Diagnose Failures

Pass a set of:

- query
- prompt
- contexts
- answer

Get a step by step diagnosis of how the LLM came up with the answer.
Trace through the prompt, the RAG query to root cause the failure.
Iteratively improve the prompt, RAG accuracy to build a robust system.

```python
diagnosis = fc.diagnose(dataset["results"])
print("==diagnosis==", diagnosis)
```

```json
{
  "dataset": [
    {
      "c_b_a": "0",
      "related": "0",
      "t_c": "answering hard questions",
      "t_q": "capital of France",
      "sum": "The context is about answering hard questions, which is not related to the query about the capital of France.",
      "info": "Include information about France or its capital in the context.",
      "data": {
        "query": "What is the capital of France?",
        "answer": "Paris",
        "prompt": "You are an expert at answering hard questions.",
        "context": ["Paris is the capital of France."]
      },
      "gen_ans": "Paris",
      "is_similar": "1",
      "summary": "The query asks for the capital of France, which is a straightforward question. Given the context that the assistant is an expert at answering hard questions, it is logical to deduce that the assistant should know basic geographical facts such as the capital of France. Therefore, the answer to the query is 'Paris'."
    }
  ]
}
```
