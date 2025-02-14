# The Refined Data Playbook 

## Table of Contents  
- [What is Data Refinement?](#what-is-data-refinement)  
- [AI is like an Engine, It Needs Refined Fuel](#ai-is-like-an-engine-it-needs-refined-fuel)  
- [The Scope of Data Refinement](#the-scope-of-data-refinement)  
- [The Problem](#the-problem)  
- [Technical Scope](#technical-scope)  
- [Case Studies](#case-studies)  
  - [Optum Healthcare AI Bias (2019)](#optum-healthcare-ai-bias-2019)  
  - [Zillow AI Collapse (2021)](#zillow-ai-collapse-2021)  
  - [Google Photos Gorillas Incident (2015)](#google-photos-gorillas-incident-2015)  

## What is Data Refinement?  
"Data cleaning" is often reduced to removing duplicates and NaN values, but it encompasses much more. Scaling, normalization, and feature engineering are critical steps that shape model performance.  

Because of its depth and impact, this playbook uses the term **"Data Refinement"** to emphasize its importance beyond basic cleaning.  

### AI is like an Engine, It Needs Refined Fuel
AI is transforming industries just like the combustion engine did. But just like crude oil, data needs refinement before it becomes usable by machine learning algorithms. *(Garbage in, Garbage out.)*   

### The Scope of Data Refinement  
Data Refinement generally includes, but is not limited to:  

- **Balancing Datasets** – Addressing imbalanced classes through upsampling/downsampling.  
- **Scaling & Normalization** – Preventing numerical features from dominating due to magnitude differences.  
- **Outlier Handling** – Adjusting extreme values that distort model performance.  
- **Feature Engineering** – Structuring and transforming data for better predictive power.

Refined data is critical to ensuring competent, reliable AI systems.

## The Problem:
AI models perform well in controlled environments but often **fail in real-world deployment**—not because of bad models, but **because they are trained on raw, unrefined data.**  



## Technical Scope  
This repository is structured into two key parts:  

- **Case Studies** – Real-world examples where AI failures were caused by poor data handling.  
- **Experiments** – Testing the impact of **data refinement techniques** on model performance, including:  
  - Normalization (Z-score, Min-Max, IQR)  
  - Scaling & Feature Engineering  
  - Handling Outliers & Imbalanced Data  
  - Desampling and Upsampling  

Performance will be measured using **accuracy, F1-score, and recall.**  


## Case Studies:

### Optum Healthcare AI Bias (2019) – A Data Scaling Failure

<details>
  <summary>Click to expand</summary>

In 2019, *Science* published a critical analysis of an Optum Healthcare AI system, which is widely used in U.S. hospitals to identify patients who might need extra medical care. The AI assigned risk scores to patients, (numerical values predicting future healthcare needs), resulting in an unintended bias where Black patients received lower risk scores than white patients.

Why? Because one of the factors used to determine risk score dominated all the others, healthcare spending.

- Healthcare spending was measured in the pure dollar amount (e.g. 10000, 20000, etc.).
- Diagnosis was measured using a binary amount, (a 1 if they had the diagnosis, a 0 if they didn't).
- Since Healthcare spending was in the tens of thousands, but diagnosis was measured with either a 0 or a 1, the algorithm thought that a 1 dollar increase in healthcare spending was as significant as a 1 used to differentiate diagnoses.
- This dominated the distribution, resulting in massive biases.

The solution? Min-max or z-score normalization, which would have helped the algorithm recognize that a $1 increase in healthcare spending should not be treated as equivalent to a binary diagnosis value.

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
- Google’s initial response was to block the labels "gorilla," "chimpanzee," and "monkey," which prevented further misclassification but did not resolve the underlying dataset imbalance.

The solution? Proper dataset balancing techniques such as upsampling underrepresented classes, downsampling overrepresented ones, and synthetic data augmentation. Ensuring equal class representation in training data would have significantly reduced misclassification errors.

The model wasn’t flawed, the lack of data refinement was.

[Read More Here](https://www.nytimes.com/2018/01/11/technology/google-racism.html)

</details>