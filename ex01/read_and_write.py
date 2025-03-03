def read_csv(path: str = './ds.csv') -> str:
    with open(path) as file:
        txt = file.read()
        lst = []

        for row in txt.split('\n'):
            if row:
                row = row.replace('","', '***').replace('",', '***').replace(',"', '***')
                lst.append(row.strip('"').split('***'))

        result_lst = []

        for row in lst:
            result_row = []
            for col_n, col in enumerate(row):
                if col_n == 3:
                    result_row.extend(col.split(','))
                else:
                    result_row.append(col)

            result_lst.append(result_row)

    result_txt = '\n'.join(['\t'.join(row) for row in result_lst])

    return result_txt


def write_tsv(text: str, path: str = './ds.tsv') -> None:
    with open(path, 'w') as file:
        file.write(text)


if __name__ == "__main__":
    res = read_csv()
    write_tsv(res)
