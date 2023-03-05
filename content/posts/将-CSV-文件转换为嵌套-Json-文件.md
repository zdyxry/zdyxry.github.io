---
title: 将 CSV 文件转换为嵌套 Json 文件
date: 2018-07-07 15:40:01
tags:
- Python
---

## 使用方法

```shell
master ✗ $ python csv2json.py --help                                             
Usage: csv2json.py [OPTIONS]

  Convert csv file to json file.

Options:
  --csv_file TEXT   Input csv file abspath
  --json_file TEXT  Output json file abspath
  --help            Show this message and exit.
```

如果执行成功，命令行输出会像下面示例一样。

```shell
master ✗ $ python csv2json.py --csv_file ./test.csv --json_file ./yiran-test.json
Convert csv file success, json file path is ./yiran-test.json
```

如果执行失败，则会提示具体失败原因。如：csv 文件无法找到。

```shell
master ✗ $ python csv2json.py --csv_file ./tes.csv --json_file ./yiran-test.json 
Failed to convert csv file with error [Errno 2] No such file or directory: u'./tes.csv'
```

---

## 转换效果

test.csv
```shell
name,age (years),weight (kg),birth day,birth month,birth year,adopted_a,adopted_since,adopted_finish
Tommy,5,3.6,11,April,2011,TRUE,2012,2015
Clara,2,8.2,6,May,2015,FALSE,N/A,N/A
Catnip,6,3.3,21,August,2011,TRUE,2017,2020
Ciel,3,3.1,18,January,2015,TRUE,2018,2021
```

test.json
```json
[
    {
        "weight (kg)": "3.6", 
        "birth": {
            "year": "2011", 
            "day": "11", 
            "month": "April"
        }, 
        "name": "Tommy", 
        "adopted": {
            "a": "TRUE", 
            "since": "2012", 
            "finish": "2015"
        }, 
        "age (years)": "5"
    }, 
    {
        "weight (kg)": "8.2", 
        "birth": {
            "year": "2015", 
            "day": "6", 
            "month": "May"
        }, 
        "name": "Clara", 
        "adopted": {
            "a": "FALSE", 
            "since": "N/A", 
            "finish": "N/A"
        }, 
        "age (years)": "2"
    }, 
    {
        "weight (kg)": "3.3", 
        "birth": {
            "year": "2011", 
            "day": "21", 
            "month": "August"
        }, 
        "name": "Catnip", 
        "adopted": {
            "a": "TRUE", 
            "since": "2017", 
            "finish": "2020"
        }, 
        "age (years)": "6"
    }, 
    {
        "weight (kg)": "3.1", 
        "birth": {
            "year": "2015", 
            "day": "18", 
            "month": "January"
        }, 
        "name": "Ciel", 
        "adopted": {
            "a": "TRUE", 
            "since": "2018", 
            "finish": "2021"
        }, 
        "age (years)": "3"
    }
]
```

---

## 具体实现

```Python
#!/usr/bin/python

# MIT License

# Copyright (c) 2018 CK

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

import click
import copy
import json
from contextlib import contextmanager


class JsonUtils(object):

    @staticmethod
    def save_json(json_struct, json_file):
        with open(json_file, "w") as f:
            json.dump(json_struct, f, indent=4)


class CSVUtils(object):

    def __init__(self, csv_file):
        self._file = csv_file

    @contextmanager
    def open_csv_file(self, mode="rb"):
        with open(self._file, mode) as f:
            if f:
                yield f
            else:
                raise NotImplementedError

    def parse_row(self, row):
        row = row.strip()
        cells = []
        quote_flag = False
        split_index = 0

        for index, value in enumerate(row):
            if value == '"':
                quote_flag = not quote_flag
            elif value == ',':
                if not quote_flag:
                    cells.append(row[split_index:index])
                    split_index = index + 1
        if split_index != len(row):
            cells.append(row[split_index:])

        cells = [cell.strip(' "') for cell in cells]
        return cells

    def get_column_names(self):
        with self.open_csv_file() as f:
            cols = self.parse_row(f.readline())
        return cols

    def get_data_rows(self):
        data_rows = []
        with self.open_csv_file() as f:
            f.readline()
            while True:
                row = f.readline()
                if row != '':
                    data_rows.append(self.parse_row(row))
                else:
                    break
        return data_rows


class CSV2Json(object):

    def __init__(self, csv_file):
        self.delimit_chars = [",", "_", " "]
        self.csv = CSVUtils(csv_file)

    def is_valid_prefix(self, prefix, base):
        if base.startswith(prefix):
            if base[len(prefix)] in self.delimit_chars:
                return True
        return False

    def clean_split(self, split):
        i = len(split) - 1
        while i >= 0:
            c = split[i]
            if c not in self.delimit_chars:
                return split[0:i + 1]
            i -= 1
        return split

    def get_leaves(self, structure, path="", result={}):
        for key, value in structure.items():
            if type(value) is dict:
                self.get_leaves(value, path + "['" + key + "']", result)
            else:
                result[value] = path + "['" + key + "']"
        return result

    def get_split_suffix(self, split, column_name=""):
        suffix = column_name[len(split) + 1:]
        for index, value in enumerate(suffix):
            if value not in self.delimit_chars:
                return suffix[index:]

    def get_valid_splits(self, column_name):
        splits = []
        i = len(column_name) - 1
        while i >= 0:
            c = column_name[i]
            if c in self.delimit_chars:
                split = self.clean_split(column_name[0:i])
                splits.append(split)
            i -= 1
        return sorted(list(set(splits)))

    def generate_structure(self, column_names=None, parent_structure=None):
        if parent_structure and not column_names:
            column_names = list(parent_structure.keys())
        visited = set()
        structure = {}
        sorted(column_names, reverse=True)
        for c1 in column_names:
            if c1 in visited:
                continue
            splits = self.get_valid_splits(c1)
            for split in splits:
                nodes = {split: {}}
                if split in column_names:
                    continue
                for c2 in column_names:
                    if c2 not in visited and self.is_valid_prefix(split, c2):
                        if parent_structure:
                            nodes[split][self.get_split_suffix(split, c2)] = parent_structure[c2]
                            visited.add(c2)
                        else:
                            nodes[split][self.get_split_suffix(split, c2)] = c2
                if len(nodes[split].keys()) > 1:
                    structure[split] = self.generate_structure(parent_structure=nodes[split])
                    for val in nodes[split].values():
                        visited.add(val)
            if c1 not in visited:
                if parent_structure:
                    structure[c1] = parent_structure[c1]
                else:
                    structure[c1] = c1
        return structure

    def populate_structure_with_data(self, structure, column_names, data_rows):
        json_struct = []
        num_columns = len(column_names)
        mapping = self.get_leaves(structure)
        for row in data_rows:
            json_row = copy.deepcopy(structure)
            i = 0
            while i < num_columns:
                cell = row[i]
                column_name = column_names[i]
                key_path = mapping[column_name]
                exec("json_row" + key_path + "=" + "'" + cell + "'")
                i += 1
            json_struct.append(json_row)
        return json_struct

    def convert(self):
        column_names = self.csv.get_column_names()
        data = self.csv.get_data_rows()
        column_schema = self.generate_structure(column_names)
        json_struct = self.populate_structure_with_data(column_schema, column_names, data)
        return json_struct


@click.command()
@click.option('--csv_file', default=None, help='Input csv file abspath')
@click.option('--json_file', default=None, help='Output json file abspath')
def main(csv_file, json_file):
    """Convert csv file to json file."""
    try:
        csv2json = CSV2Json(csv_file)
        JsonUtils.save_json(csv2json.convert(), json_file)
        print "Convert csv file success, json file path is %s" % json_file
    except Exception as error:
        print "Failed to convert csv file with error %s" % error


if __name__ == '__main__':
    main()
```

---

### 参考链接
* https://github.com/chamkank/hone
* https://stackoverflow.com/questions/35969611/csv-to-nested-json
* https://stackoverflow.com/questions/43757965/convert-csv-to-json-tree-structure
