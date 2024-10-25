###############################################
# Fonksiyonlara Özellik Ekleme ve Docstring Ekleme
###############################################
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
##############################################################################################
# GÖREV 1: Fonksiyonlara Özellik Ekleme
##############################################################################################
# cat_summary() fonksiyonuna 1 özellik ekleyiniz. Bu özellik argumanla biçimlendirilebilir olsun.
# Var olan özelliği de argumandan kontrol edilebilir hale getirebilirsiniz.

# Arguman eklemeden önce
def cat_summary(dataframe, col_name):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        'Ratio': 100* dataframe[col_name].value_counts() / len(dataframe)}))

    print('**************************************************')


df = sns.load_dataset('titanic')
for col in df.columns:
    cat_summary(df, col)

# Arguman ekledikten sonra
def cat_summary(dataframe, col_name, plot=False):
    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        'Ratio': 100 * dataframe[col_name].value_counts() / len(dataframe)}))

    print('**************************************************')
    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)


df = sns.load_dataset('titanic')
cat_summary(df, 'embarked', True)

# Eğer kategorik değişkenleri liste halinde fonksiyona göndermek istersek, bu veri seti için öncelikle null kayıtlar silinmeli ve kategorik değişkenler belirlenmelidir.
# Not: Bu işlemler sadece fonksiyonun çalışması için gereken azami işlemlerdir.
# Hangisini isterseniz onu kullanarak fonksiyonu deneyebilirsiniz.

# 1. Tüm null değerler silinir ve kategorik değişkenler belirlenip fonksiyona gönderilir
df = df.dropna()
cat_vals = [col for col in df.columns if df[col].dtype not in ['int64', 'float64', 'bool']]

for col in cat_vals:
    cat_summary(df, col, True)


# 2. null değer içermeyen kategorik değişkenler belirlenip fonksiyona gönderilir
not_null_cols = df.loc[:, ~df.isnull().any()].columns
cat_vals = [col for col in df[not_null_cols] if df[col].dtype not in ['int64', 'float64', 'bool']]

for col in cat_vals:
    cat_summary(df, col, True)

##############################################################################################
# GÖREV 2: check_df() ve cat_summary() fonksiyonlarına 4 bilgi (uygunsa) barındıran numpy tarzı docstring yazınız.
# (task, params, return, example)
##############################################################################################

def check_df(dataframe, head=10):
    """
    Bu fonksiyon veri seti hakkında ilk 5 gözlem, gözlem sayısı, boş değer saysısı gibi genel bilgileri verir

    Parameters
    ----------
    dataframe: dataframe
    Özellikleri getirilecek ilgili veri setidir

    head: int, optional
    İlk kaç gözlemin getirileceğini ifade eder

    Returns
    -------
    None

    """
    print("######### Head #########")
    print(dataframe.head(head))
    print("######### Shape #########")
    print(dataframe.shape)
    print("######### Info #########")
    print(dataframe.info())
    print("######### NA #########")
    print(dataframe.isnull().sum())
    print("######### Quantiles #########")
    print(dataframe.describe([0, 0.05, 0.50, 0.95, 0.99, 1]).T)



def cat_summary(dataframe, col_name, plot=False):
    """
     Kategorik değişkenlerin eşsiz değer sayılarını, bunların veri setindeki oranlarını
     ve tercihe bağlı olarak da countplot grafiklerini getirir

    Parameters
    ----------
    dataframe: dataframe
    İşleme alınacak ilgili veri setidir

    col_name: str
    Veri setindeki herbir değişkeni/sütunu ifade eder

    plot: bool, optional
    İlgili değişken ile ilgili grafik bilgisinin gösterilip gösterilmeyeceğini belirler

    Returns
    -------
    None

    """

    print(pd.DataFrame({col_name: dataframe[col_name].value_counts(),
                        'Ratio': 100 * dataframe[col_name].value_counts() / len(dataframe)}))

    print('**************************************************')
    if plot:
        sns.countplot(x=dataframe[col_name], data=dataframe)
        plt.show(block=True)
