import pandas as pd
import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import confusion_matrix, accuracy_score, precision_score, recall_score, f1_score
# --- DATASET & PREPROCESSING ---
data = {
    'Age': [55, 40, 65, 30, 50, 45, 70, 38, 62, 58, 52, 35, 60, 42, 68, 45, 55, 30],
    'HighBP': [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 0, 1],
    'Cholesterol': [240, 180, 290, 170, 250, 190, 310, 200, 270, 260, 210, 185, 280, 195, 305, 220, 230, 160],
    'GenHealth': [0, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 1, 0, 1, 1, 0],
    'Target': [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0] 
}
df = pd.DataFrame(data)
# --- TRAIN-TEST SPLIT ---
X = df[['Age', 'HighBP', 'Cholesterol', 'GenHealth']]
y = df['Target']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
# --- IMPLEMENT NAÏVE BAYES ---
model = GaussianNB()
model.fit(X_train, y_train)
# --- PERFORMANCE REPORTING ---
def show_metrics():
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    # ---CONFUSION MATRIX---
    perf_win = tk.Toplevel(root)
    perf_win.title("Performance Data")
    perf_win.geometry("350x250")
    tk.Label(perf_win, text="CONFUSION MATRIX", font=("Arial", 12, "bold")).pack(pady=10)
    matrix_frame = tk.Frame(perf_win, bg="white", bd=1, relief="solid")
    matrix_frame.pack(pady=5)
    # Table Labels
    tk.Label(matrix_frame, text="Pred: Healthy", bg="#d1e7ff", width=12).grid(row=0, column=1)
    tk.Label(matrix_frame, text="Pred: Sick", bg="#d1e7ff", width=12).grid(row=0, column=2)
    tk.Label(matrix_frame, text="Actual: Healthy", bg="#eeeeee", width=12).grid(row=1, column=0)
    tk.Label(matrix_frame, text="Actual: Sick", bg="#eeeeee", width=12).grid(row=2, column=0)
    # Matrix Values from your cm result
    tk.Label(matrix_frame, text=str(cm[0][0]), font=("Arial", 10, "bold")).grid(row=1, column=1)
    tk.Label(matrix_frame, text=str(cm[0][1])).grid(row=1, column=2)
    tk.Label(matrix_frame, text=str(cm[1][0])).grid(row=2, column=1)
    tk.Label(matrix_frame, text=str(cm[1][1]), font=("Arial", 10, "bold")).grid(row=2, column=2)
    tk.Label(perf_win, text=f"Overall Accuracy: {acc*100:.0f}%", fg="green", font=("Arial", 10, "bold")).pack(pady=10)
    tk.Button(perf_win, text="View Bar Chart", command=lambda: [plt.bar(['Accuracy', 'Precision', 'Recall', 'F1'], [acc, prec, rec, f1], color='teal'), plt.title("Performance Summary"), plt.ylim(0, 1.1), plt.show()]).pack()
# ---LIVE DEMO UI ---
def run_demo():
    try:
        p_age = float(entry_age.get())
        p_bp = 1 if var_bp.get() == "Yes" else 0
        p_chol = float(entry_chol.get())
        p_health = 1 if var_health.get() == "Good" else 0
        patient = pd.DataFrame([[p_age, p_bp, p_chol, p_health]], 
                               columns=['Age', 'HighBP', 'Cholesterol', 'GenHealth'])
        pred = model.predict(patient)[0]
        prob = model.predict_proba(patient)[0][pred]
        result = "HEART DISEASE LIKELY" if pred == 1 else "NO DISEASE DETECTED"
        msg = (f"Result: {result}\n"
               f"Posterior Probability: {prob:.2f}\n\n"
               f"Decision Support: This probability helps doctors prioritize "
               f"high-risk patients for further clinical testing.")
        messagebox.showinfo("Bayesian Diagnosis", msg)
    except:
        messagebox.showerror("Error", "Please enter valid numerical values.")
# UI Setup
root = tk.Tk()
root.title("Heart Disease Diagnostic System")
root.geometry("350x420")
tk.Label(root, text="Patient Input", font=("Arial", 12, "bold")).pack(pady=10)
tk.Label(root, text="Age:").pack()
entry_age = tk.Entry(root); entry_age.pack()
tk.Label(root, text="High Blood Pressure?").pack()
var_bp = tk.StringVar(root); var_bp.set("No")
tk.OptionMenu(root, var_bp, "Yes", "No").pack()
tk.Label(root, text="Cholesterol Level:").pack()
entry_chol = tk.Entry(root); entry_chol.pack()
tk.Label(root, text="General Health Status:").pack()
var_health = tk.StringVar(root); var_health.set("Good")
tk.OptionMenu(root, var_health, "Good", "Poor").pack()
tk.Button(root, text="Results", command=run_demo, bg="blue", fg="white").pack(pady=10)
tk.Button(root, text="Show Performance Graph", command=show_metrics, bg="green", fg="white").pack()
root.mainloop()
