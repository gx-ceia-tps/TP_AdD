import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def plot_feature_histogram(dataframe, cols_to_plot):
    # Number of columns for the subplot
    n_cols = 3
    n_rows = (len(cols_to_plot) // n_cols) + 1
    assert (len(cols_to_plot) <= n_cols * n_rows)

    # Create subplots
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(n_cols * 4, n_rows * 4))
    axes = axes.flatten()  # Flatten the axes array for easy indexing

    i = 0  # Initialize index for axes
    for column in cols_to_plot:
        if column in dataframe.columns:
            data = dataframe[column].dropna()

            if not data.empty:
                sns.histplot(data, bins=30, kde=True, ax=axes[i])  # Plot on the corresponding axis
                axes[i].set_title(f'Histograma de {column}')
                axes[i].set_xlabel(column)
                axes[i].set_ylabel('Frecuencia')
                axes[i].grid(True)
                i += 1  # Increment index for the next valid plot
            else:
                print(f"La columna {column} no tiene datos válidos para graficar.")
        else:
            print(f"La columna {column} no está presente en el DataFrame.")

    # Hide any remaining empty subplots
    for j in range(i, len(axes)):
        axes[j].axis('off')

    plt.tight_layout()  # Adjust layout
    plt.show()


def plot_feature_boxplot(dataframe, cols_to_plot):
    # Number of columns for the subplot
    n_cols = 3
    n_rows = (len(cols_to_plot) // n_cols) + 1
    assert (len(cols_to_plot) <= n_cols * n_rows)

    # Create subplots
    fig, axes = plt.subplots(n_rows, n_cols, figsize=(n_cols * 4, n_rows * 4))
    axes = axes.flatten()  # Flatten the axes array for easy indexing

    i = 0  # Initialize index for axes
    for column in cols_to_plot:
        if column in dataframe.columns:
            data = dataframe[column].dropna()

            if not data.empty:
                sns.boxplot(y=data, ax=axes[i])  # Plot vertical boxplot on the corresponding axis
                axes[i].set_title(f'Boxplot de {column}')
                axes[i].set_ylabel(column)
                axes[i].grid(True)
                i += 1  # Increment index for the next valid plot
            else:
                print(f"La columna {column} no tiene datos válidos para graficar.")
        else:
            print(f"La columna {column} no está presente en el DataFrame.")

    # Hide any remaining empty subplots
    for j in range(i, len(axes)):
        axes[j].axis('off')

    plt.tight_layout()  # Adjust layout
    plt.show()

def add_space_before_second_uppercase(s):
    uppercase_count = 0
    result = []
    for char in s:
        if char.isupper():
            uppercase_count += 1
            if uppercase_count == 2:
                result.append(' ')
        result.append(char)

    return ''.join(result)
