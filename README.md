# The Refined Data Playbook

## The Problem:
AI models are notoriously difficult to deploy into the real world. A lot of the industry sees their models performing well in the lab, but when they're deployed, they break.

The hypothesis presented in this playbook is that this **isn't** because of *bad models*, but *bad data*.

## Historical Examples:

### Optum Healthcare AI Bias (2019) – A Data Scaling Failure

In 2019, Science published a critical analysis of an Optum Healthcare AI system, which is widely used in U.S. hospitals to identify patients who might need extra medical care. The AI assigned risk scores to patients, (numerical values predicting future healthcare needs), but these scores favored white patients over Black patients.

Why? Because one of the factors used to determine risk score dominated all the others, healthcare spending.

- Healthcare spending was measured in the pure dollar amount (e.g. 10000, 20000, etc.).
- Diagnosis was measured using a binary amount, (a 1 if they had the diagnosis, a 0 if they didn't).
- Since Healthcare spending was in the tens of thousands, but diagnosis was measured with either a 0 or a 1, the algorithm thought that a 1 dollar increase in healthcare spending was as significant as a 1 used to differentiate diagnoses.
- This dominated the distribution, resulting in massive biases.

The solution? min-max or z-score normalization, which would have allowed for the algorithmn to understand that a 1 dollar increase of healthcare spending is weighed less than a 1 used to differentiate diagnoses.

The **model** wasn't flawed, the **lack of data refinement was**.

[Check Here](https://www.science.org/doi/10.1126/science.aax2342)