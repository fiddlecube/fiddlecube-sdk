from fiddlecube.fiddlecube import FiddleCube

fc = FiddleCube(api_key="cabaa6b5-4c58-467a-9471-c3433555795e")
dataset = fc.generate(
    [
        "The cat did not want to be petted.",
        "The cat was not happy with the owner's behavior.",
    ],
    10,
)
print("==dataset==", dataset)

debug = [
    {
        "query": "What is the capital of France?",
        "answer": "Paris",
        "prompt": "You are an expert at answering hard questions.",
        "context": ["Paris is the capital of France."],
    }
]
diagnosis = fc.diagnose(debug)
print("==diagnosis==", diagnosis)
