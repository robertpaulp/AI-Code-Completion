# Code Generation with Tiny StarCoder

## Project overview

* `create_dataset`: A script to create a dataset from code files by extracting prefix, current, and suffix code segments.
* `generate_code`: Uses a model (Tiny StarCoder) to generate current code segments based on prefix and suffix.
* `metrics`: Measures the quality of generated code segments using various metrics.

## Step-by-step thought process

### Creating the dataset
In the `data/raw/` directory there is a python file which contains a set of simple functions (e.g. merge_sort,is_prime). Based on this file, the **create_dataset** program parses the file, takes each function defined with `def` and separate the prefix, middle and suffix based on a simulate cursor_pos. This way the cursor can be in the middle of the function, writing a comment, simulating real-life situations.

### Model code generation
After the dataset is created, the **generate_code** program takes the dataset, parse it, use the model to generate code and create a dataset with a new collumn attached.

### Labelling
The labelling process had me thinking of a confusion matrix and I've decided to go for 4 labels:
    - perfect : the generated code is exactly the same
    - high : the generated code is nearly the same
    - low : the generated code has some similarity but the model hallucinated
    - fail : the generated code is nowhere near

### Score Metrics
The metrics used:

* Exact Match: Compares the generated current segment with the reference segment for an exact character match.
* Character-Level F-Score (ChrF): Measures the similarity of character n-grams between reference and generated code.
* Levenshtein Distance: Computes normalized edit distance to measure similarity.
* CodeBLEU: Calculates BLEU-based metrics tailored for code structure and syntax.
* ROUGE: Measures the overlap of n-grams between the reference and generated code, focusing on recall.

I would say the metric which correlates the best is CodeBLEU because it considers the syntactic and semantic structure of the code, making it more sensitive to meaningful differences between the generated and reference code segments.

## **Interesting Findings & Learnings**

Initially, I used code files that I had written myself. However, I noticed that the model struggled to understand my codebase due to the presence of custom libraries and imports from other files. This led to poor completion results. After switching to a simpler file with standard functions, the model's accuracy improved significantly.

While working with **Tiny StarCoder**, I observed that the generated code was sometimes an exact match to the original. However, in other cases, the model would **hallucinate**, copying the suffix and adding extra content that was not relevant.

### **Key Observations**
- **High Success Rate** – The model achieved a **62% success rate**, producing either a perfect or high-quality match for most code completions.
- **Failure Cases** – About **16% of cases failed**, highlighting areas where the model could be improved.
- **Strengths** – The model performs well with **structured, common coding patterns**, making it particularly effective for algorithmic and function-based code completion.
- **Challenges with Edge Cases** – It struggles with **edge cases and non-standard syntax**, often generating incorrect completions.
- **Repetitions and Hallucinations** – Some failures were due to **code repetitions or hallucinated completions**, which could be reduced with **fine-tuning, improved dataset preprocessing, or better in-context learning techniques**.

These findings highlight the model's strengths in structured code generation while identifying areas for improvement in handling complex or unconventional coding patterns.