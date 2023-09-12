## Generate a sample dataset from seed:
```bash
$ fc generate -s s3://fiddlecube-demo-datasets/floworks/classification.json
# Generates gen_data_sample.json
```

Double-check the data and fix any issues that you see.
Your feedback will be used to generate the right data.

## Run the pipeline to get a model
```bash
$ fc pipeline gen_data_sample.json hello-world
# Creates a model labeled 'hello-world'
```

## Call an API to invoke inference.
https://fiddlecube.ai/floworks/hello-world
```json
{
  "prompt": "Hi, how are you?"
}
```

## Generate the fine-tuning dataset.
Use the sample generated in the previous step.
```bash
$ fc generate gen_data_sample.json
# Generates gen_data.json
```

## Fine-tune a model
```bash
fc sft gen_data.json meta-llama/Llama-2-7b-hf hello-world
# Fine-tune a base model on the generated data
```

## Deploy the model
```bash
fc deploy hello-world
```
