# Evaluating LLMs for Scam Detection: Safeguarding Older Adults Against Online Threats

## Overview
This project explores the capabilities of two advanced large language models (LLMs), OpenAI’s GPT-4.0 and Google’s Gemini-1.5-Pro, in detecting email scams. The study focuses on how these models can safeguard older adults, a group particularly vulnerable to online threats, by providing accurate and accessible scam detection solutions. This paper is the result of our final project for our CMSC396H class

## Abstract
With the rise in online scams, especially targeting older adults, this research compares the performance of GPT-4.0 and Gemini-1.5-Pro in identifying fraudulent emails. By analyzing metrics such as accuracy, precision, recall, and F1 score, this work sheds light on the potential and limitations of these models in real-world applications.

## Methodology
The research follows a systematic approach to evaluate the models:
- **Data Collection**: A dataset of emails labeled as either “fraudulent” or “non-fraudulent” was used.
- **Model Selection**: GPT-4.0 and Gemini-1.5-Pro were chosen for their advanced natural language processing capabilities.
- **Testing Process**: Both models processed the dataset to classify emails and generate new labeled outputs, which were compared with the original labels to calculate metrics.
- **Evaluation Metrics**:
  - **Accuracy**: Proportion of correct classifications.
  - **Precision**: Proportion of true positives among predicted positives.
  - **Recall**: Proportion of true positives among actual positives.
  - **F1 Score**: Harmonic mean of precision and recall.

## Results
The performance of both models was summarized using confusion matrices and key performance metrics.

### Confusion Matrices
#### GPT-4.0
(Include the image for GPT-4.0 confusion matrix here)

#### Gemini-1.5-Pro
(Include the image for Gemini-1.5-Pro confusion matrix here)

### Performance Metrics
#### GPT-4.0
- **Accuracy**: 0.84
- **Precision**: 0.85
- **Recall**: 0.84
- **F1 Score**: 0.83
![gpt_matrix](https://github.com/user-attachments/assets/f9e7958d-cba5-4d08-9437-d725c44f11fe)

![gpt_performance](https://github.com/user-attachments/assets/2065711e-e20e-47f8-bdad-06a8f37996a3)


#### Gemini-1.5-Pro
- **Accuracy**: 0.87
- **Precision**: 0.87
- **Recall**: 0.87
- **F1 Score**: 0.87

  ![gemini_matrix](https://github.com/user-attachments/assets/b5a743d8-67b8-4081-b79f-30bc558cc807)

![gemini_evaluation](https://github.com/user-attachments/assets/32885bce-9da7-478d-96c4-d3b9faac6393)


### Comparative Performance Visualization
(Include performance comparison charts for both models here)

## Key Findings
- **Superior Model**: Gemini-1.5-Pro outperformed GPT-4.0 across all metrics.
- **Challenges**: False positives and false negatives remain significant issues.
- **Impact**: Both models provide insights into improving scam detection, with implications for protecting older adults.

## Conclusion
The study demonstrates the potential of LLMs in enhancing online safety but also highlights the need for further refinements to ensure reliable and precise scam detection.

## Authors
- Harshil Agarwal  
- Jude Lwin  
- Mark Seeliger  
- Shashank Thirumale  
- Shiqi Wu  

