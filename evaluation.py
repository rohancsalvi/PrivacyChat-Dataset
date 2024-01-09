import pandas as pd
def calculate_precision(tp, fp):
  return tp / (tp + fp)

def calculate_recall(tp, fn):
  return tp / (tp + fn)

def calculate_f1(x,y):
  return x / y

def read_excel_files(gold_standard_file, prediction_file):
  gold_standard_df = pd.read_excel(gold_standard_file)
  prediction_df = pd.read_excel(prediction_file)
  return gold_standard_df, prediction_df

def calculate_precision_recall(gold_standard_df, prediction_df,c):
  tp = 0
  tn = 0
  fp = 0
  fn = 0
  exact_matches = 0
  for i in range(0,len(gold_standard_df)):
    gold = gold_standard_df[c][i]
    pred = prediction_df[c][i]
    if gold == 'None':
      if pred == gold:
        tn = tn + 1
      else:
        fp = fp + 1
    else:
      if pred == gold:
        tp = tp + 1
        exact_matches = exact_matches + 1
      else:
        if pred == 'None':
          fn = fn + 1
        else:
          tp = tp + 1
  precision = calculate_precision(tp, fp)
  recall = calculate_recall(tp, fn)
  f1_score = calculate_f1(2 * precision * recall, precision + recall)
  exact_match = exact_matches / len(gold_standard_df)
  return precision, recall,f1_score,exact_match
def main():
  gold_standard_file = 'gold_standard.xlsx'
  prediction_file = 'predictions_iconf.xlsx'
  gold_standard_df, prediction_df = read_excel_files(gold_standard_file, prediction_file)
  columns = ['Q1','Q2','Q3','Q4']
  for c in columns:
    print(f'For column {c}')
    precision, recall, f1_score, exact_match = calculate_precision_recall(gold_standard_df, prediction_df, c)
    print(f'Precision: {precision}')
    print(f'Recall: {recall}')
    print(f'F1 score: {f1_score}')
    print(f'Exact match: {exact_match}')
if __name__ == '__main__':
  main()