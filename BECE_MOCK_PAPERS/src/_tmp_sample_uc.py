import sqlite3
c = sqlite3.connect(r'data\metadata\catalog.db'); c.row_factory = sqlite3.Row
for src in ['Computing_ICT_uc_13a23797.pdf','Computing_ICT_uc_3582a795.pdf','Computing_ICT_uc_5703e827.pdf','Computing_ICT_uc_9956ee66.pdf','Computing_ICT_uc_c43e1959.pdf','Computing_ICT_uc_d45488d0.pdf','Computing_ICT_uc_f7c5c685.pdf','Computing_ICT_BestBrain_Solve_BECE_Computing_Questions_&_Answers_29e249ff.txt','Computing_ICT_Download_Computing_Questions_and_Answers_b9c5bf93.txt','Computing_ICT_2025_SUPER-MOCK-B-COMPUTING-MARKING-SCHEME_01ac21ac.pdf','Computing_ICT_2012_BECE_ICT_Pasco_questions_with_answe_fae362a3.txt','Computing_ICT_2021_ICT-2019_f2cdf945.docx']:
    print('='*20, src)
    n = 0
    for r in c.execute("select question_text from extracted_questions where subject='Computing_ICT' and source_file=? limit 3", (src,)):
        print('  >', (r[0] or '')[:110].replace('\n',' '))
        n += 1
    if n == 0:
        print('  (none)')
