import sqlite3, collections
c = sqlite3.connect(r'data\metadata\catalog.db'); c.row_factory = sqlite3.Row
print('--- questions.year ---')
for r in c.execute("select year, count(*) from questions where subject='Computing_ICT' group by year"): print(r[0], r[1])
print('--- extracted_questions.year ---')
for r in c.execute("select year, count(*) from extracted_questions where subject='Computing_ICT' group by year"): print(r[0], r[1])
print('--- occurrences.year (distinct qids) ---')
for r in c.execute("""select qo.year, count(distinct qo.question_id) from question_occurrences qo
 join questions q on q.id=qo.question_id where q.subject='Computing_ICT' group by qo.year"""): print(r[0], r[1])
print('--- extracted source_file breakdown ---')
sf = collections.Counter()
for r in c.execute("select source_file, year, count(*) from extracted_questions where subject='Computing_ICT' group by source_file, year"):
    print(r[0], 'year=', r[1], 'n=', r[2])
print('--- source_file column looks what? sample ---')
for r in c.execute("select distinct source_file from extracted_questions where subject='Computing_ICT' limit 25"):
    print(r[0])
