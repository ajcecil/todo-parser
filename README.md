# todo-parser
 Generate Task Lists in csv format from comments starting with TODO


 ## Installation

```bash
pip install todo-parser
```

## Function Usage
The primary beneficial usage of this library would currently be the "generate_list()" function which will generate a todo list from the comments and directly store it as a csv in the same folder as the given script the other two functions are intermediates that could be useful for exporting the TODO items in another format.


```python
todos = extract_todos(script_path) # finds all comments listed as "TODO" and compiles them into a dataframe

write_todos_to_csv(todos, csv_path) # Takes todo dataframe and exports to csv

generate_list(script_path) # Uses both above function to generate csv file from only the script path
```

### Python file comment structure

For this to work comments should be set up as below, the script is not case sensitive so "Todo" can be written in any way.

``` python
# TODO: Complete a function to do more with this script

print("Hello World")

# TODO: Tell everyone how great I am.
