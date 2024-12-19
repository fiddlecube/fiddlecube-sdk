> [!Note]
> This repository is now archived. Thanks to all the users who have supported us so far!
> We are working on the next version of our product based on your valuable feedback.
> Watch this space for new, interesting developments in the future.

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

## Generate the Dataset

```python
from fiddlecube import FiddleCube

fc = FiddleCube(api_key="<api-key>")
dataset = fc.generate(
    [
        "Wheat is mainly grown in the midlands and highlands of Ethiopia.",
        "Wheat covers most of the country's agricultural land next to teff, corn and sorghum and in the 2009/10 crop season 1.69 million hectares were covered by wheat crops",
        "46.42 million quintals of production was obtained and the average yield was 26.75 quintals per hectare.",
        "Bread wheat (Triticum aestivum L) and durum wheat (Triticum turgidum var durum L) are the types of wheat that are mainly produced in our country, and durum wheat is one of the native wheat crops.",
        "Ethiopia is known to be the primary source of durum wheat and a source of its biodiversity.",
        "Durum wheat is grown in high and medium altitude areas and clay and light soils, and its industrial demand is increasing from time to time.",
    ], # data chunks
    3, # number of rows to generate
)
```

## Diagnose your data generated

```python
from fiddlecube import FiddleCube
fc = FiddleCube(api_key="<api-key>")
result = fc.diagnose(
    [{
        "query": "Can you explain supply and demand with an example?",
        "answer": "Supply and demand is a fundamental economic principle. For instance, consider concert tickets. If a popular band announces a show, demand for tickets is high. Initially, supply is limited, so prices are high. As the concert date approaches, if tickets remain unsold, prices might drop to increase demand. Conversely, if demand outstrips supply, prices may rise further.",
        "prompt": "Explain the concept of supply and demand in economics using a real-world example. Your answer should be between 50-75 words",
        "context": [
            "The evolution of the music industry, much like any other industry, is a story of innovation, disruption, and adaptation. From the early days of sound recording to the streaming age, how we consume and engage with music have transformed profoundly, often reflecting broader societal shifts in technology, culture, and economy. The invention of the phonograph by Thomas Edison in 1877 marked the beginning of a new era for music. Before this, music was primarily experienced live, at concerts, dance halls, or in homes. The phonograph allowed sound to be captured, stored, and replayed, giving birth to the recorded music industry. Initially, these recordings were made on wax cylinders. However, by the 20th century, flat disc records made of shellac began to dominate, paving the way for what would be commonly known as vinyl records."
        ]
    }]
)
```

## Ideal QnA datasets for testing, eval and training LLMs

Testing, evaluation or training LLMs requires an ideal QnA dataset aka the golden dataset.

This dataset needs to be diverse, covering a wide range of queries with accurate responses.

Creating such a dataset takes significant manual effort.

As the prompt or RAG contexts are updated, which is nearly all the time for early applications, the dataset needs to be updated to match.

## FiddleCube generates ideal QnA from vector embeddings

- The questions cover the entire RAG knowledge corpus.
- Complex reasoning, safety alignment and 5 other question types are generated.
- Filtered for correctness, context relevance and style.
- Auto-updated with prompt and RAG updates.

## Roadmap

- [x] Question-answers, complex reasoning from RAG
- [ ] Multi-turn conversations
- [ ] Evaluation Setup - Integrate metrics
- [ ] CI setup - Run as part of CI/CD pipeline
- [x] Diagnose failures - step-by-step analysis of failed queries

## More Questions?

[Book a demo](https://cal.com/kaushiks/fc)  
Contact us at [founders@fiddlecube.ai](mailto:founders@fiddlecube.ai) for any feature requests, feedback or questions.
