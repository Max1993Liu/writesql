from writesql.utils import as_template_function, render_template


def count(table_name, cols=None):
    cols = cols or []
    if isinstance(cols, str):
        cols = [cols]
    return render_template('count',
                           table_name=table_name, cols=cols)


def find_duplicates(table_name, cols, min_count=1):
    if isinstance(cols, str):
        cols = [cols]
    return render_template('find_duplicates',
                           table_name=table_name, cols=cols, min_count=min_count)


if __name__ == '__main__':
    # print(find_duplicates(table_name='table_name', cols=['cert_no', 'seq_no'], min_count=5))
    print(6)