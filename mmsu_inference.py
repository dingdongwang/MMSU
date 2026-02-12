import os
import argparse
import json
from tqdm import tqdm
from datasets import load_dataset


def main():
    parser = argparse.ArgumentParser(description="MMSU Inference Script (HF version)")
    parser.add_argument('--output_jsonl', type=str, required=True, help="Path to save output JSONL file")
    parser.add_argument('--split', type=str, default="train", help="Dataset split (default: train)")
    args = parser.parse_args()

    output_file = args.output_jsonl
    split = args.split

    # ============================
    # Step 1: Load HuggingFace Dataset
    # ============================
    dataset = load_dataset("ddwang2000/MMSU", split=split)

    # ============================
    # Step 2: Build your model
    # ============================
    # model = ...
    # model.eval()

    with open(output_file, "w") as fout:
        for item in tqdm(dataset):

            audio = item["audio"]
            audio_array = audio["array"]         
            sampling_rate = audio["sampling_rate"]
            audio_path = audio["path"]           

            task_name = item["task_name"]

            # ============================
            # Step 3: Construct Prompt
            # ============================
            question = item["question"]

            question_prompts = (
                "Choose the most suitable answer from options A, B, C, and D. "
                "You must respond with only A, B, C, or D."
            )

            choice_a = item["choice_a"]
            choice_b = item["choice_b"]
            choice_c = item.get("choice_c", "")
            choice_d = item.get("choice_d", "")

            choices = (
                f"A. {choice_a}\n"
                f"B. {choice_b}\n"
                f"C. {choice_c}\n"
                f"D. {choice_d}"
            )

            instruction = f"{question_prompts}\n\nQuestion: {question}\n\n{choices}"

            # ============================
            # Step 4: Run Model Inference
            # ============================
            # output = model.infer(
            #     prompt=instruction,
            #     audio=audio_array,
            #     sampling_rate=sampling_rate,
            # )

            output = "Model response here"  # Placeholder response

            # ============================
            # Step 5: Save result
            # ============================
            result = {
                "id": item["id"],
                "audio_path": audio_path,
                "question": question,
                "choice_a": choice_a,
                "choice_b": choice_b,
                "choice_c": choice_c,
                "choice_d": choice_d,
                "answer_gt": item["answer_gt"],
                "response": output,
                "task_name": task_name,
                "category": item["category"],
                "sub-category": item["sub-category"],
                "sub-sub-category": item["sub-sub-category"],
                "linguistics_sub_discipline": item["linguistics_sub_discipline"],
            }

            fout.write(json.dumps(result, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    # python mmsu_inference.py --output_jsonl /path/to/output.jsonl
    main()
