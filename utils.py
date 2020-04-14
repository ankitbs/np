

def rename_columns(source_df, column_name_mapping):
    """
    Returns dataframe with updated column name in accordance with the database schema

    Params
    =======
    source_df : Dataframe : Master dataframe which needs the column name updated.
    column_name_mapping : Dataframe : dataframe with column name mapping which would
                          be updated to store in the database table.
    """

    # Read Mapping from main function
    source_df.columns = source_df.columns.str.lower()
    source_df.columns = source_df.columns.str.replace(" ", "")
    column_name_mapping.column_name = column_name_mapping.column_name.str.lower()
    column_name_mapping.column_name = column_name_mapping.column_name.str.replace(" ", "")
    column_name_validate = validate_columns(source_df, column_name_mapping)
    # print(column_name_validate)
    sql_col_mapping = dict(zip(column_name_mapping.column_name,
                               column_name_mapping.mapping_name))
    try:
        column_name_validate.rename(columns=sql_col_mapping, inplace=True)
    # source_df.rename(columns=sql_col_mapping, inplace=True)
        return column_name_validate
    except:
        return column_name_validate


def validate_columns(source_df, column_name_mapping):
    count=0
    not_present_col =[]
    column_name_map = list(column_name_mapping.column_name)
    for col in source_df.columns:  #checking column name present in our csv file column_name
        if col not in column_name_map:
            not_present_col.append(col)
        else:
            count+=1
    if(count==len(column_name_mapping.column_name)): #check for total columns present or not
        return source_df
    else:
        return not_present_col
