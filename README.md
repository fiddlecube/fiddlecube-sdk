# FiddleCube - Generate golden evaluation datasets for RAG

Test and evaluate your RAG system, get actionable diagnosis of the top problems.
Systematically improve the prompt, RAG and data points in the RAG storage.

## Evaluation dilemma - scale vs effectiveness

Evals are either highly effective - human evaluation and manual QA.
Or they scale well while being unreliable - LLM as a judge.

## Data driven evaluation

Evaluating an LLM effectively needs:
1. An accurate representation of possible queries and usages of the LLM and RAG DB.
2. Gold-standard responses to the queries, grounded in knowledge.
3. Evaluate the outputs based on subjective rules and business logic
4. Scale to accomodate fast-paced dev teams - ideally as a part of CI/CD

## Evaluating using a golden dataset - step by step
1. Pass a list of chunks from your vector DB to the fiddlecube generate API.
2. FiddleCube generates a wide range of queries and answers across 7 question type.
   Includes multi-turn conversations, QA and complex reasoning.
3. Use the golden dataset to evaluate real user interactions with your LLM.
4. FiddleCube will diagnose failed queries providing a step by step analysis of the failure.
5. Step by step analysis of the output.
6. Pinpoint the exact root cause of the failure
7. Actionable prompt improvement or RAG updates.

## Installation

```bash
pip3 install fiddlecube
```

## Usage

### Generate data

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
print(dataset)
```

```json
{
   "results":[
      {
         "query":"Question: Why did the cat not want to be petted?",
         "contexts":[
            "The cat did not want to be petted."
         ],
         "answer":"The cat did not want to be petted because it was not in the mood for physical affection at that moment.",
         "score":0.8,
         "question_type":"SIMPLE"
      },
      {
         "query":"Was the cat pleased with the owner's actions?",
         "contexts":[
            "The cat was not happy with the owner's behavior."
         ],
         "answer":"No, the cat was not pleased with the owner's actions.",
         "score":0.8,
         "question_type":"NEGATIVE"
      }
   ],
   "status":"COMPLETED",
   "num_tokens_generated":44,
   "rate_limited":false
}
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
diagnosis = fc.diagnose({
        "query": "What is the capital of France?",
        "answer": "Paris",
        "prompt": "You are an expert at answering hard questions.",
        "context": ["Paris is the capital of France."],
    })
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
