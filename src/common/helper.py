
class ProjectHelper:
    @staticmethod
    def convert_db_data_with_response(db_data,column_indexes):
        result_data = []
        for each in db_data:
            print(type(each))
            record = {}
            for key, col in enumerate(column_indexes):
                record[col] = each.col
            result_data.append(record)
        return result_data

