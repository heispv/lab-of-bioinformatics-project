#!/usr/bin/env python3
import argparse
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def compute_cm(preds, th):
    cm = np.zeros((2, 2))
    for pred in preds:
        p = 0 if pred[1] > th else 1
        cm[p][pred[2]] += 1
    return cm

def get_metrics(cm):
    tp, tn = cm[1][1], cm[0][0]
    fn, fp = cm[0][1], cm[1][0]
    accuracy = (tn + tp) / np.sum(cm)
    mcc = (tp * tn - fp * fn) / np.sqrt((tp + fp) * (tp + fn) * (tn + fp) * (tn + fn))
    tpr = tp / (tp + fn)
    ppv = tp / (tp + fp)
    f1 = 2 * ppv * tpr / (ppv + tpr)
    return accuracy, mcc, tpr, ppv, f1

def evaluate_thresholds(predfile, threshold):
    print("Reading data from file...")
    preds = []
    with open(predfile, "r") as f:
        for line in f:
            seq_id, e_value, label = line.rstrip().split()
            preds.append((seq_id, float(e_value), int(label)))
    print("Data reading completed.")

    print("Computing final metrics with the threshold...")
    cm = compute_cm(preds, threshold)
    accuracy, mcc, tpr, ppv, f1 = get_metrics(cm)

    print("Final results:")
    print(f"Threshold: {threshold}")
    print(f"Accuracy: {accuracy:.4f}")
    print(f"MCC: {mcc:.4f}")
    print(f"TPR (Recall): {tpr:.4f}")
    print(f"PPV (Precision): {ppv:.4f}")
    print(f"F1 Score: {f1:.4f}")

    print("Plotting the confusion matrix...")
    sns.set(style="whitegrid")
    plt.figure(figsize=(6, 5))
    sns.heatmap(cm, annot=True, fmt=".1f", cmap="Blues", xticklabels=['Negative', 'Positive'], yticklabels=['Negative', 'Positive'])
    plt.xlabel('Actual')
    plt.ylabel('Predicted')
    plt.title(f'Confusion Matrix (Threshold: {threshold})')
    plt.show()

def find_optimal_threshold(predfile, initial_range=(1e-10, 1.0), tol=1e-10, max_iter=100):
    print("Reading data for optimization...")
    preds = []
    with open(predfile, "r") as f:
        for line in f:
            seq_id, e_value, label = line.rstrip().split()
            preds.append((seq_id, float(e_value), int(label)))

    low, high = initial_range
    best_th, best_f1 = low, 0

    for _ in range(max_iter):
        mid = (low + high) / 2
        cm = compute_cm(preds, mid)
        f1 = get_f1_score(cm)

        print(f"Threshold {mid}: F1 Score = {f1:.4f}")

        if f1 > best_f1:
            best_f1 = f1
            best_th = mid

        if high - low < tol:
            break

        if f1 > best_f1:
            low = mid
        else:
            high = mid

    print(f"Optimal threshold found: {best_th} with F1 Score = {best_f1:.4f}")
    return best_th

def main():
    parser = argparse.ArgumentParser(description='Evaluate thresholds or find an optimal threshold for predictions.')
    parser.add_argument('predfile', help='Prediction file path.')
    parser.add_argument('--threshold', type=float, help='Evaluate using this specific threshold.')
    parser.add_argument('--optimize', action='store_true', help='Find the optimal threshold.')

    args = parser.parse_args()

    if args.threshold is not None:
        evaluate_thresholds(args.predfile, args.threshold)
    elif args.optimize:
        find_optimal_threshold(args.predfile)
    else:
        print("No action specified. Use --threshold to evaluate or --optimize to find optimal threshold.")

if __name__ == "__main__":
    main()
