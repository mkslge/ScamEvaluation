#AUTHOR: SHASHANK THIRUMALE
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score

# Load the uploaded CSV file
data = pd.read_csv('fraud_email_evaluated.csv')

# Extract the true labels and predicted labels
y_true = data['Class']
y_pred = data['EvaluatedLabel']

# Create the confusion matrix
cm = confusion_matrix(y_true, y_pred)

accuracy = accuracy_score(y_true, y_pred)
precision = precision_score(y_true, y_pred, average='weighted')
recall = recall_score(y_true, y_pred, average='weighted')
f1 = f1_score(y_true, y_pred, average='weighted')
print("ChatGPT 4o")
print(f'Accuracy: {accuracy:.2f}')
print(f'Precision: {precision:.2f}')
print(f'Recall: {recall:.2f}')
print(f'F1 Score: {f1:.2f}')

# Visualize the confusion matrix
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=set(y_pred), yticklabels=set(y_true))
plt.xlabel('Predicted Labels')
plt.ylabel('True Labels')
plt.title('Confusion Matrix')
plt.show()

# Accuracy Bar Plot
plt.subplot(1, 2, 2)
plt.bar(['Accuracy', 'Precision', 'Recall', 'F1 Score'],
        [accuracy, precision, recall, f1], color='skyblue')
plt.ylim(0, 1)
plt.ylabel('Score')
plt.title('Model Performance Metrics')

plt.tight_layout()
plt.show()
