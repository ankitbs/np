def validate_columns(source_df, column_name_mapping):
    print(source_df.columns,column_name_mapping.column_name)
    if (source_df.columns == column_name_mapping.column_name):
        print(source_df.columns,column_name_mapping.column_name)
        return True
    else:
        return false