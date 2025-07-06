from datasets import Dataset
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM, Trainer, TrainingArguments
import pandas as pd

# Load data
df = pd.read_csv("qa_data.csv")

# Format into HuggingFace dataset
data = [{"input": f"Question: {row['Question']} Answer:", "output": row["Answer"]} for _, row in df.iterrows()]
dataset = Dataset.from_list(data)

# Load tokenizer/model
tokenizer = AutoTokenizer.from_pretrained("google/flan-t5-small")
model = AutoModelForSeq2SeqLM.from_pretrained("google/flan-t5-small")

# Preprocess
def preprocess(examples):
    inputs = tokenizer(examples["input"], truncation=True, padding="max_length", max_length=64)
    outputs = tokenizer(examples["output"], truncation=True, padding="max_length", max_length=64)
    inputs["labels"] = outputs["input_ids"]
    return inputs

tokenized_dataset = dataset.map(preprocess, batched=False)

# Training setup
training_args = TrainingArguments(
    output_dir="./math_tutor_model",
    per_device_train_batch_size=2,
    num_train_epochs=5,
    logging_steps=10,
    save_steps=10,
    save_total_limit=2,
)

trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_dataset,
)

# Train your model!
trainer.train()

# Save model
model.save_pretrained("./math_tutor_model")
tokenizer.save_pretrained("./math_tutor_model")

question = "What is the area of a circle with radius 5?"
inputs = tokenizer(f"Question: {question} Answer:", return_tensors="pt")

outputs = model.generate(**inputs, max_length=64, do_sample=False)
print(tokenizer.decode(outputs[0], skip_special_tokens=True))
