from fiddlecube.fiddlecube import FiddleCube

fiddlecube = FiddleCube(api_key="cabaa6b5-4c58-467a-9471-c3433555795e")
dataset = fiddlecube.generate(
    [
        "The cat did not want to be petted.",
        "The cat was not happy with the owner's behavior.",
    ],
    10,
)
print("==dataset==", dataset)
