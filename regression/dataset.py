import pandas as pd

class Dataset:
    def __init__(self, data):
        self.data = data  # Initialize with a Pandas DataFrame

    def get(self, columns=None, conditions=None):
        """
        Retrieve data based on specified columns and conditions.

        Parameters:
        - columns (list or None): A list of column names to select. If None, all columns are selected.
        - conditions (dict or None): A dictionary of conditions to filter the data.
            For example, {'column_name': condition} will filter rows where 'column_name' meets 'condition'.

        Returns:
        - pd.DataFrame: A DataFrame containing the selected data.
        """
        if columns is not None:
            selected_data = self.data[columns].copy()
        else:
            selected_data = self.data.copy()

        if conditions is not None:
            for column, condition in conditions.items():
                selected_data = selected_data[selected_data[column] == condition]

        return selected_data

# # Example usage:
# data = pd.DataFrame({
#     'A': [1, 2, 3, 4, 5],
#     'B': [10, 20, 30, 40, 50],
#     'C': ['X', 'Y', 'X', 'Z', 'Y']
# })

# dataset = Dataset(data)

# # Retrieve all columns with no conditions
# result = dataset.get()
# print("All columns with no conditions:")
# print(result)

# # Retrieve specific columns with no conditions
# result = dataset.get(columns=['A', 'B'])
# print("Specific columns with no conditions:")
# print(result)

# # Retrieve data with conditions
# conditions = {'C': 'X', 'A': 3}
# result = dataset.get(columns=['A', 'C'], conditions=conditions)
# print("Data with conditions:")
# print(result)
