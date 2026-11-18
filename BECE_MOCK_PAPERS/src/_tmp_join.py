import sqlite3
c = sqlite3.connect(r'data\metadata\catalog.db'); c.row_factory = sqlite3.Row
# test join coverage
r = c.execute("""
select count(*) n, sum(case when eq.year is not null then 1 else 0 end) tagged
from questions q
left join question_occurrences qo on qo.question_id = q.id
left join extracted_questions eq on eq.id = qo.original_id
where q.subject='Computing_ICT'""").fetchone()
print('join coverage:', r['n'], 'with eq.year:', r['tagged'])
for x in c.execute("""
select q.id, q.migrated_from, qo.original_id, eq.id eqid, eq.year
from questions q left join question_occurrences qo on qo.question_id=q.id
left join extracted_questions eq on eq.id=qo.original_id
where q.subject='Computing_ICT' limit 5"""):
    print(dict(x))
