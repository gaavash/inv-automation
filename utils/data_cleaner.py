import pandas as pd


class DataCleaner:
    """
    Handles data loading and cleaning for inventory workflows.
    """

    def __init__(self):
        pass

    def load_csv(self, file_path):
        """
        Load CSV file into pandas DataFrame.
        """
        try:
            df = pd.read_csv(file_path)
            print(f"Loaded data from {file_path}")
            return df

        except Exception as e:
            print(f"Error loading file: {e}")
            return None

    def remove_duplicates(self, df):
        """
        Remove duplicate rows.
        """
        before = len(df)

        df = df.drop_duplicates()

        after = len(df)

        print(f"Removed {before - after} duplicate rows")

        return df

    def fill_missing_values(self, df):
        """
        Fill missing values depending on column type.
        """

        for column in df.columns:

            # Numeric columns
            if df[column].dtype in ['int64', 'float64']:
                df[column] = df[column].fillna(0)

            # Text columns
            else:
                df[column] = df[column].fillna("Unknown")

        print("Filled missing values")

        return df

    def standardize_column_names(self, df):
        """
        Standardize column names.
        """

        df.columns = (
            df.columns
            .str.strip()
            .str.lower()
            .str.replace(" ", "_")
        )

        print("Standardized column names")

        return df

    def clean_product_names(self, df, column_name="product_name"):
        """
        Clean product name formatting.
        """

        if column_name in df.columns:

            df[column_name] = (
                df[column_name]
                .astype(str)
                .str.strip()
                .str.title()
            )

            print("Cleaned product names")

        return df

    def clean_data(self, file_path):
        """
        Full cleaning pipeline.
        """

        df = self.load_csv(file_path)

        if df is None:
            return None

        df = self.standardize_column_names(df)

        df = self.remove_duplicates(df)

        df = self.fill_missing_values(df)

        df = self.clean_product_names(df)

        return df
