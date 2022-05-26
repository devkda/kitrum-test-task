# Backend Engineer test
- [x] Command line interface
- [x] Docker image
- [x] Tests

## usage
Command line interface accepts 2 arguments `src` and `dest`(optional) of corresponding files.
Where src is absolute path to input data and dest is destination path for results.
```bash
$ python cli.py --help

Usage: cli.py [OPTIONS]

  Command line interface for salescalc.

Options:
  --src PATH                      absolute path of input file
  --dest PATH                     absolute path of output file
```

Examples:

```bash
$ python cli.py --src data/input.csv --dest data/results.csv
```
or
```
$ python -m salescalc --src data/input.csv --dest data/results.csv
```


## configuration
There are several environment variables which can be set to configure the application:
```
FILE_CHUNK_SIZE - amount of bytes to read per iteration
CSV_DELIMITER - string delimiter for input csv file
```

## additional
Tests can be run by pytest command.
```
$ pytest
```


## algorithm description
#### TLDR;

- Time complexity: O(n), where `n` is the total number of lines(entries) in csv.
- Space complexity: O(m) where `m` is the total number of departments.

The main logic is powered by `SalesMap` data structure and `salescalc.usecases.calculate_total_sales` function.

### `SalesMap`
Sales data is stored in dictionary, where the keys are department names and values are total salaes of dept.
In other words, we use additional space to store all the names of departments.

Appending new sales data can be done in multiple ways, but in our case we will consider the `.add_entry()` method which just
updates the total value of sales of specific department by summarizing two numbers of sales:
```
self.sales[entry.department] += entry.sales
```
So that is a constant operation which is invoked for each entry(sales data) in our function `salescalc.usecases.calculate_total_sales`.


## memory efficiency
During the runtime, operations to calculate the total sales are performed only on the chunk of the file which
is defined by env. variable `FILE_CHUNK_SIZE`.
Therefore, even for big files it will allocate only the memory needed to store the specific part of the csv file.


# bonus: pandas approach.
Using pandas of course will be much shorter, simpler and faster(C bindings) and in production environment, it looks better to use.

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