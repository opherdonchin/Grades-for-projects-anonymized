#!/usr/bin/env python3
import pandas as pd
import argparse

def convert_scores(input_path, output_path):
    # Read the Excel file
    df = pd.read_excel(input_path)

    # Assume the first column is the project number
    id_col = df.columns[0]

    df[id_col] = df[id_col].ffill()

    # Identify judge-name and grade columns by their prefixes (Hebrew or English)
    judge_cols = [col for col in df.columns if col.startswith('בוחנ/ת') or 'Judge' in col]
    grade_cols = [col for col in df.columns if col.startswith('ציון') or 'Grade' in col]

    # Sort columns by their numeric suffix
    def suffix_num(col, stub):
        try:
            return int(col.replace(stub, '').strip())
        except:
            return 0

    judge_cols = sorted(judge_cols, key=lambda x: suffix_num(x, 'בוחנ/ת'))
    grade_cols = sorted(grade_cols, key=lambda x: suffix_num(x, 'ציון'))

    # Melt the wide format into long format
    records = []
    for jcol, gcol in zip(judge_cols, grade_cols):
        temp = df[[id_col, jcol, gcol]].copy()
        temp.columns = ['Project', 'Judge', 'Grade']
        temp = temp.dropna(subset=['Judge', 'Grade'])
        records.append(temp)

    df_long = pd.concat(records, ignore_index=True)

    # Optionally drop rows where judge name is missing
    df_long = df_long.dropna(subset=['Judge'])

    # Write to CSV with UTF-8 signature for Excel compatibility
    df_long.to_csv(output_path, index=False, encoding='utf-8-sig')
    print(f"Converted {len(df_long)} rows and saved to {output_path}")

def main():
    parser = argparse.ArgumentParser(description='Convert scores from wide to long format.')
    parser.add_argument('input', help='Input Excel file (e.g., ציונים מצגות (1).xlsx)')
    parser.add_argument('output', help='Output CSV file (e.g., long_format_grades.csv)')
    args = parser.parse_args()
    convert_scores(args.input, args.output)

if __name__ == '__main__':
    main()
