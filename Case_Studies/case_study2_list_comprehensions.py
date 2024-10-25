import numpy as np
import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
# pd.set_option('display.max_rows', 300)
pd.set_option('display.width', 500)

########## List Comprehension  #########

##############################################################################
# Görev 1: List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.
##############################################################################
# NOT:  Numeric olmayan değişkenlerin de isimleri büyümeli.
# Tek bir list comprehension yapısı kullanılmalı.
df = sns.load_dataset('car_crashes')
df.columns
df.info()

['NUM_' + col.upper() if df[col].dtype != 'O' else col.upper() for col in df.columns]

##############################################################################
# Görev 2: List Comprehension yapısı kullanarak car_crashes verisinde isminde "no" barındırmayan değişkenlerin isimlerinin sonuna "FLAG" yazınız.
##############################################################################
# NOT: Tüm değişkenlerin isimleri büyük harf olmalı.
# Tek bir list comprehension yapısı ile yapılmalı.
[col.upper() + '_FLAG' if 'no' not in col else col.upper() for col in df.columns]

##############################################################################
# Görev 3: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.
##############################################################################
# NOT: Önce verilen listeye göre list comprehension kullanarak new_cols adında yeni liste oluşturunuz.
# Sonra df[new_cols] ile bu değişkenleri seçerek yeni bir df oluşturunuz ve adını new_df olarak isimlendiriniz.
og_list = ['abbrev', 'no_previous']

new_cols = [col for col in df.columns if col not in og_list]
new_df = df[new_cols]


##############################################################################
###########   Pandas Alıştırmalar    ##########

##############################################################################
# Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
##############################################################################
df = sns.load_dataset('titanic')
df.head()

##############################################################################
# Görev 2: Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
##############################################################################
df['sex'].value_counts()

##############################################################################
# Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.
##############################################################################
df[df.columns].nunique()

# Alternatif çözüm
for col in df.columns:
    print(df[col].name + " --> " + str(df[col].nunique()))

##############################################################################
# Görev 4: pclass değişkeninin unique değerlerinin sayısını bulunuz.
##############################################################################
df['pclass'].nunique()

##############################################################################
# Görev 5: pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
##############################################################################
df[['pclass', 'parch']].nunique()

##############################################################################
# Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz ve tekrar kontrol ediniz.
##############################################################################
df['embarked'].dtype
df['embarked'] = df['embarked'].astype('category')

##############################################################################
# Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz.
##############################################################################
df[df['embarked'] == 'C']

##############################################################################
# Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.
##############################################################################
df[df['embarked'] != 'S']

##############################################################################
# Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
##############################################################################
# age değişkeninde boş değerler olduğu için onları önce sex ve survived değişkenlerine göre gruplayıp, yaşlarının ortalamasına göre doldurmayı tercih ettim.
# (Başka yöntemler de denenebilir)

df['age'] = df['age'].fillna(df.groupby(['sex', 'survived'])['age'].transform('mean'))
df[(df['age'] < 30) & (df['sex'] == 'female')]

##############################################################################
# Görev 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.
##############################################################################
df[(df['age'] > 70) | (df['fare'] > 500)]

##############################################################################
# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.
##############################################################################
df.isnull().sum()

##############################################################################
# Görev 12: who değişkenini dataframe’den çıkarınız.
##############################################################################
df.drop('who', axis=1, inplace=True)

##############################################################################
# Görev 13: deck değişkenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.
##############################################################################
df['deck'] = df['deck'].fillna(df['deck'].mode()[0])

##############################################################################
# Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurunuz.
##############################################################################
df['age'] = df['age'].fillna(df['age'].median())

##############################################################################
# Görev 15: survived değişkeninin pclass ve cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.
##############################################################################
df.groupby(['sex', 'pclass'])['survived'].agg(['sum', 'count', 'mean'])

##############################################################################
# Görev 16: 30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazın. Yazdığınız fonksiyonu kullanarak titanik veri
# setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)
##############################################################################
def age(age):
    if age < 30:
        return 1
    else:
        return 0

df['age_flag'] = df['age'].apply(lambda x: age(x))

### Alternatif çözüm
df['age_flag'] = df['age'].apply(lambda x: 1 if (x < 30) else 0)
df.sample(10)

##############################################################################
# Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.
##############################################################################
df = sns.load_dataset('tips')
df.head()

##############################################################################
# Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
##############################################################################
df.groupby('time')['total_bill'].agg(['sum', 'min', 'max', 'mean'])

##############################################################################
# Görev 19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
##############################################################################
df.groupby(['day', 'time'])['total_bill'].agg(['sum', 'min', 'max', 'mean'])

##############################################################################
# Görev 20: Lunch zamanına ve kadın müşterilere ait total_bill ve tip değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.
##############################################################################
df[(df['time'] == 'Lunch') & (df['sex'] == 'Female')].groupby('day').agg({'total_bill': ['sum', 'min', 'max', 'mean'],
                                                                          'tip': ['sum', 'min', 'max', 'mean']})

new_df = df[(df['time'] == 'Lunch') & (df['sex'] == 'Female')]
new_df.groupby('day').agg({'total_bill': ['sum', 'min', 'max', 'mean'],
                           'tip': ['sum', 'min', 'max', 'mean']})

##############################################################################
# Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir? (loc kullanınız)
##############################################################################

# df.loc[(df['size'] < 3) & (df['total_bill'] > 10)]['total_bill'].mean()
df.loc[(df['size'] < 3) & (df['total_bill'] > 10), 'total_bill'].mean()

##############################################################################
# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturunuz. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.
##############################################################################
df['total_bill_tip_sum'] = df['total_bill'] + df['tip']
df.head()

##############################################################################
# Görev 23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.
##############################################################################
new_df = df.sort_values('total_bill_tip_sum', ascending=False)
new_df.head(30)
