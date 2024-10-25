########################################################################
# Kural Tabanlı Sınıflandırma ile Potansiyel Müşteri Getirisi Hesaplama
########################################################################
# İş Problemi:

# Bir oyun şirketi müşterilerinin bazı özelliklerini kullanarak
# seviye tabanlı (level based) yeni müşteri tanımları (persona)
# oluşturmak ve bu yeni müşteri tanımlarına göre segmentler
# oluşturup bu segmentlere göre yeni gelebilecek müşterilerin
# şirkete ortalama ne kadar kazandırabileceğini tahmin etmek
# istemektedir.
# Örneğin:
# Türkiye’den IOS kullanıcısı olan 25 yaşındaki bir erkek
# kullanıcının ortalama ne kadar kazandırabileceği belirlenmek
# isteniyor.
######################################
# Veri Seti Hikayesi

# Persona.csv veri seti uluslararası bir oyun şirketinin sattığı ürünlerin fiyatlarını ve bu
# ürünleri satın alan kullanıcıların bazı demografik bilgilerini barındırmaktadır. Veri
# seti her satış işleminde oluşan kayıtlardan meydana gelmektedir. Bunun anlamı
# tablo tekilleştirilmemiştir. Diğer bir ifade ile belirli demografik özelliklere sahip bir
# kullanıcı birden fazla alışveriş yapmış olabilir.
#######################################
# Değişkenler

# PRICE :  Müşterinin harcama tutarı
# SOURCE : Müşterinin bağlandığı cihaz türü
# COUNTRY : Müşterinin ülkesi
# SEX : Müşterinin cinsiyeti
# AGE : Müşterinin yaşı

###################################################################
import pandas as pd
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

###################################################################
# Görev 1: Aşağıdaki Soruları Yanıtlayınız
###################################################################
# Soru 1: persona.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.
df = pd.read_csv('Python_Programming/datasets/persona.csv')
df.head()
df.shape
df.info()
df.isnull().sum()
df.describe().T

###################################################################
# Soru 2: Kaç unique SOURCE vardır? Frekansları nedir?
df['SOURCE'].unique()
df['SOURCE'].nunique()
df['SOURCE'].value_counts()


###################################################################
# Soru 3: Kaç unique PRICE vardır?
df['PRICE'].unique()
df['PRICE'].nunique()

###################################################################
# Soru 4: Hangi PRICE'dan kaçar tane satış gerçekleşmiş?
df['PRICE'].value_counts()

###################################################################
# Soru 5: Hangi ülkeden kaçar tane satış olmuş?
df['COUNTRY'].value_counts()

# df.groupby('COUNTRY')['PRICE'].count()
# İkisi de aynı sonucu verir

###################################################################
# Soru 6: Ülkelere göre satışlardan toplam ne kadar kazanılmış?
df.groupby('COUNTRY')['PRICE'].sum()

###################################################################
# Soru 7: SOURCE türlerine göre satış sayıları nedir?
df['SOURCE'].value_counts()

# df.groupby('SOURCE')['PRICE'].count()
# İkisi de aynı sonucu verir

###################################################################
# Soru 8: Ülkelere göre PRICE ortalamaları nedir?
df.groupby('COUNTRY')['PRICE'].mean()

###################################################################
# Soru 9: SOURCE'lara göre PRICE ortalamaları nedir?
df.groupby('SOURCE')['PRICE'].mean()

###################################################################
# Soru 10: COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?
df.groupby(['COUNTRY', 'SOURCE'])['PRICE'].mean()

###################################################################
# Görev 2: COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?
###################################################################
df.groupby(['COUNTRY', 'SOURCE', 'SEX', 'AGE'])['PRICE'].mean()

###################################################################
# Görev 3: Çıktıyı PRICE’a göre sıralayınız.
###################################################################
# • Önceki sorudaki çıktıyı daha iyi görebilmek için sort_values metodunu azalan olacak şekilde PRICE’a göre uygulayınız.
# • Çıktıyı agg_df olarak kaydediniz.
agg_df = df.groupby(['COUNTRY', 'SOURCE', 'SEX', 'AGE']).agg({'PRICE': 'mean'}).sort_values('PRICE', ascending=False)
agg_df.head()

###################################################################
# Görev 4: Indekste yer alan isimleri değişken ismine çeviriniz.
###################################################################
# Üçüncü sorunun çıktısında yer alan PRICE dışındaki tüm değişkenler index isimleridir. Bu isimleri değişken isimlerine çeviriniz.
agg_df.reset_index(inplace=True)
agg_df.head()

###################################################################
# Görev 5: Age değişkenini kategorik değişkene çeviriniz ve agg_df’e ekleyiniz.
###################################################################
# • Age sayısal değişkenini  kullanarak yeni bir kategorik değişken ekleyin (AGE_CAT isminde).
# • Aralıkları ikna edici şekilde oluşturunuz.
# • Örneğin: ‘0_18', ‘19_23', '24_30', '31_40', '41_70'
bins = [0, 18, 23, 30, 40, agg_df['AGE'].max()]
label = ['0_18', '19_23', '24_30', '31_40', '41_' + str(agg_df['AGE'].max())]
agg_df['AGE_CAT'] = pd.cut(agg_df['AGE'], bins=bins, labels=label)  # include_lowest=True

agg_df.head(50)

###################################################################
# Görev 6: Yeni seviye tabanlı müşterileri (persona) tanımlayınız
###################################################################
# • Yeni seviye tabanlı müşterileri (persona) tanımlayınız ve veri setine değişken olarak ekleyiniz.
# • Yeni eklenecek değişkenin adı: customers_level_based
# • Önceki soruda elde edeceğiniz çıktıdaki gözlemleri bir araya getirerek customers_level_based değişkenini oluşturmanız gerekmektedir.
# Dikkat! List comprehension ile customers_level_based değerleri oluşturulduktan sonra bu değerlerin tekilleştirilmesi gerekmektedir.
# Örneğin birden fazla şu ifadeden olabilir: USA_ANDROID_MALE_0_18. Bunları groupby'a alıp price ortalamalarını almak gerekmektedir.
cols = ['COUNTRY', 'SOURCE', 'SEX', 'AGE_CAT']
agg_df['customers_level_based'] = agg_df[cols].agg(lambda x: '_'.join(x).upper(), axis=1)
agg_df.head()

agg_df = agg_df[['customers_level_based', 'PRICE']]
agg_df.head()

agg_df = agg_df.groupby('customers_level_based')['PRICE'].mean()
agg_df = agg_df.reset_index()
agg_df.head()

###################################################################
# Görev 7: Yeni müşterileri (personaları) segmentlere ayırınız.
###################################################################
# • Yeni müşterileri (Örnek: USA_ANDROID_MALE_0_18) PRICE’a göre 4 segmente ayırınız.
# • Segmentleri SEGMENT isimlendirmesi ile değişken olarak agg_df’e ekleyiniz.
# • Segmentleri betimleyiniz (Segmentlere göre group by yapıp price mean, max, sum’larını alınız).

agg_df['SEGMENT'] = pd.qcut(agg_df['PRICE'], 4, ['D', 'C', 'B', 'A'])

agg_df.groupby('SEGMENT').agg({'PRICE': ['mean', 'max', 'sum']})

###################################################################
# Görev 8: Yeni gelen müşterileri sınıflandırıp, ne kadar gelir getirebileceklerini tahmin ediniz.
###################################################################
# • 33 yaşında ANDROID kullanan bir Türk kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?
# • 35 yaşında IOS kullanan bir Fransız kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?

new_user = 'TUR_ANDROID_FEMALE_31_40'
result = agg_df[agg_df['customers_level_based'] == new_user]
avg_customer_revenue = result['PRICE'].mean()

###
new_user2 = 'FRA_IOS_FEMALE_31_40'
result = agg_df[agg_df['customers_level_based'] == new_user2]
avg_customer_revenue = result['PRICE'].mean()
customer_segment = result['SEGMENT'].item()

###
# Alternatif Çözüm
# agg_df[agg_df['customers_level_based'] == new_user]['PRICE'].mean()
# agg_df[agg_df['customers_level_based'] == new_user2]['SEGMENT'].item()
# agg_df[agg_df['customers_level_based'] == new_user2]['PRICE'].mean()


