# The Refined Data Playbook

## Table of Contents  
- [The Problem](#the-problem)  
- [What is Data Refinement?](#what-is-data-refinement)  
- [Historical Examples](#historical-examples)  
  - [Optum Healthcare AI Bias (2019)](#optum-healthcare-ai-bias-2019)  
  - [Zillow AI Collapse (2021)](#zillow-ai-collapse-2021)  
  - [Google Photos Gorillas Incident (2015)](#google-photos-gorillas-incident-2015)  

## What is Data Refinement?
Traditional "data cleaning" focuses on handling missing values and fixing typos, but real-world AI failures show that this is **not enough.** Many AI models fail not because of bad architecture but because their **data was not properly structured, balanced, or scaled.**  

### We're Having an Industrial Revolution, and AI is the Combustion Engine.
The world is undergoing another Industrial Revolution, with AI playing the role that the combustion engine did in the 19th and 20th centuries. But just like engines are with crude oil, AI cannot function properly without clean, structured, and properly processed data.

This playbook expands the definition of **data cleaning** into a broader concept called **Data Refinement**, which includes:  

- **Balancing Datasets** – Desampling (downsampling) overrepresented classes and upsampling underrepresented ones.  
- **Scaling & Normalization** – Ensuring that features do not dominate due to magnitude differences (Z-score, Min-Max, IQR).  
- **Outlier Handling** – Removing or transforming extreme values to prevent them from skewing model performance.  
- **Feature Engineering** – Structuring and transforming data to improve predictive power.  

Just as crude oil must go through multiple **processing stages** before it becomes gasoline, AI data must go through **scaling, balancing, and structuring** before it becomes useful for machine learning models.  

Data Refinement is not just about removing NaNs or fixing formatting issues—it is about making data truly usable for AI.

## The Problem:
AI models are notoriously difficult to deploy into the real world. A lot of the industry sees their models performing well in the lab, but when they're deployed, they break.

The hypothesis presented in this playbook is that this **isn't** because of *bad models*, but *bad data*.

## Historical Examples:

### Optum Healthcare AI Bias (2019) – A Data Scaling Failure

<details>
  <summary>Click to expand</summary>

In 2019, *Science* published a critical analysis of an Optum Healthcare AI system, which is widely used in U.S. hospitals to identify patients who might need extra medical care. The AI assigned risk scores to patients, (numerical values predicting future healthcare needs), but these scores favored white patients over Black patients.

Why? Because one of the factors used to determine risk score dominated all the others, healthcare spending.

- Healthcare spending was measured in the pure dollar amount (e.g. 10000, 20000, etc.).
- Diagnosis was measured using a binary amount, (a 1 if they had the diagnosis, a 0 if they didn't).
- Since Healthcare spending was in the tens of thousands, but diagnosis was measured with either a 0 or a 1, the algorithm thought that a 1 dollar increase in healthcare spending was as significant as a 1 used to differentiate diagnoses.
- This dominated the distribution, resulting in massive biases.

The solution? min-max or z-score normalization, which would have allowed for the algorithmn to understand that a 1 dollar increase of healthcare spending is weighed less than a 1 used to differentiate diagnoses.

The **model** wasn't flawed, the **lack of data refinement was**.

[Read More Here](https://www.science.org/doi/10.1126/science.aax2342)

</details>


### Zillow AI Collapse (2021) – A Textbook Normalization Failure

<details>
  <summary>Click to expand</summary>

In 2021, Zillow shut down its home-buying algorithm, *Zillow Offers*, after losing $500 million due to bad data preprocessing, not a bad model. The AI was designed to estimate home values, but instead, it overpaid for thousands of houses, assuming prices would keep rising. When the market corrected, Zillow was stuck with overvalued properties it couldn’t sell at a profit.

Why? Because they didn't use proper data scaling and normalization.

- The evidence suggests that home price features were not properly scaled, or Zillow used Min-Max Scaling, which caused outliers to dominate the distribution.  
- COVID-era home prices were treated as normal, despite being market anomalies.  
- Luxury homes and speculative market spikes ($1M-$3M+) skewed the model, distorting predictions for average-priced homes ($250K-$400K).  
- Since extreme home prices weren’t normalized, the model learned an unrealistic trend: assuming home values would continue rising indefinitely.  

The solution? IQR-based scaling and proper normalization techniques, which would have allowed the algorithm to understand that extreme price spikes should not outweigh typical home values.

The **model** wasn't flawed, the **lack of data refinement was**.

[Read More Here](https://www.bloomberg.com/news/articles/2021-11-02/zillow-shuts-down-home-flipping-business-after-racking-up-losses)

</details>

### Google Photos "Gorillas" Incident (2015) – A Data Imbalance Failure

<details>
  <summary>Click to expand</summary>

In 2015, Google’s image recognition AI mislabeled Black people as “gorillas.” The mistake was not due to a flawed model but rather a lack of representative data. The training dataset contained far fewer images of darker-skinned individuals compared to lighter-skinned individuals, causing the AI to generalize poorly when classifying non-white faces.

Why? Because the dataset was imbalanced, leading to poor generalization for underrepresented groups.

- The AI was trained on significantly more images of lighter-skinned individuals, making it highly accurate in recognizing those faces but unreliable for others.  
- The dataset lacked sufficient diversity, meaning the model did not learn robust decision boundaries for darker-skinned individuals.  
- Instead of correcting the dataset and retraining the model, Google initially attempted a quick fix by blocking the labels "gorilla," "chimpanzee," and "monkey" altogether, avoiding the core issue rather than addressing it.  

The solution? Proper dataset balancing techniques such as upsampling underrepresented classes, downsampling overrepresented ones, and synthetic data augmentation. Ensuring equal class representation in training data would have significantly reduced misclassification errors.

The model wasn’t flawed, the lack of data refinement was.

[Read More Here](https://www.nytimes.com/2018/01/11/technology/google-racism.html)

</details>