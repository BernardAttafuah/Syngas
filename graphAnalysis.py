import matplotlib.pyplot as plt
import seaborn as sns

def distp_plot(df):
    for col in df.columns:
        import matplotlib.pyplot as plt
        import seaborn as sns
        plt.figure(figsize=(10,5))
        plt.subplot(1,1,1)
        sns.distplot(df[col])
        plt.show()


def box_plot(df):
    for col in df.columns:
        plt.figure(figsize=(10,5))
        plt.subplot(1,1,1)
        sns.boxplot(df[col])
        plt.show()