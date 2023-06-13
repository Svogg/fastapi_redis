## sql task

### Problem:
You have 2 tables like (name text, status integer).\
First one has name without extensions - name = name1, status = 0\
Another has name like name1.zip\
There no duplicates names with different extensions, number of extension - random\

You need to move satus from one table to another with minimum amount of queries


### Solution:

these are all required steps to move data from short_names table to full_names:
* create all tables
* create indexes for these table. Indexes make searching faster
* fill tables with random values
* update table using bare sql or python script

#### 1) Create all tables
```sql
create table if not exists short_names (
    name text,
    status integer
);

create table if not exists full_names (
    name text,
    status integer
);
```
#### 2) Create indexes for these table
```sql
create index if not exists
short_names_name_idx on short_names (name);

create index if not exists
full_name_name_idx on full_names (name);
```

#### 3) fill tables with random values 
```sql
insert into short_names (name, status)
select 'nazvanie' || generate_series(1, 700000),
case
	when random() <= 0.5 then 0
	else 1
end;

insert into full_names (name, status)
select 'nazvanie' || generate_series(1, 500000) || '.' || ((array['txt', 'mp3', 'png'])[floor(random() * 3 + 1)]), 0
```
#### 4.1) update table using bare sql
```sql
update full_names
set status = short_names.status
from short_names
where short_names.name = left(full_names.name, strpos(full_names.name, '.') - 1)    
```
#### 4.2) update table using python script
```commandline
cd sql
python update_table.py
```
