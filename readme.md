

# todo:
- cli script to process input csv
- parallelism option with cli arguments for setting worker numbers
- add docs
- add tests




---
# notes from client

"+ use of type hints
+ concise easy to understand functions
+ detailed explanation of the code (comments are overused, maybe because this is a test. Should use docstrings wherever possible)
+ provided 3 different solutions with
+ has tests
- tests use same file as running program
- unclear distinction between time and space complexity when explaining the big O analysis
- for each pass of a unique department, all the rows are read
- file paths hardcoded into code
- data “column” names should be string constants
- pending TODO in solution
- little exception handling, assumed happy path scenario
Verdict: This is a straightforward solution using the pandas package. It however does not improve on the basic implementation as demonstrated by other candidates."



---





### pandas approach is too boring to implement, but here it is just in case.

```python
def get_total_sales(filepath: str) -> pd.DataFrame:
    """Counts total sales.

    :param filepath: full path to csv file with sale entries
    :return: :class: <pandas.DataFrame> total sales per department
    """
    sales = pd.DataFrame()
    with pd.read_csv(filepath, chunksize=settings.chunk_size) as reader:
        for chunk in reader:
            sales = sales.append(chunk)
            sales = sales.groupby('Department Name')["Number of sales"].sum().reset_index(name ='Total Amount')
    return sales
```