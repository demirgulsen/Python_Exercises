######################################################################
# Kural Tabanlı Sınıflandırma ile  Potansiyel Müşteri Getirisi Hesaplama
######################################################################
# İş Problemi
######################################################################
# Gezinomi yaptığı satışların bazı özelliklerini kullanarak seviye tabanlı
# (level based) yeni satış tanımları oluşturmak ve bu yeni satış
# tanımlarına göre segmentler oluşturup bu segmentlere göre yeni
# gelebilecek müşterilerin şirkete ortalama ne kadar kazandırabileceğini
# tahmin etmek istemektedir.
# Örneğin:
# Antalya’dan Herşey Dahil bir otele yoğun bir dönemde gitmek isteyen
# bir müşterinin ortalama ne kadar kazandırabileceği belirlenmek
# isteniyor.
######################################################################
# Veri Seti Hikayesi
######################################################################
# gezinomi_miuul.xlsx veri seti Gezinomi şirketinin yaptığı satışların fiyatlarını ve bu
# satışlara ait bilgiler içermektedir. Veri seti her satış işleminde oluşan kayıtlardan
# meydana gelmektedir. Bunun anlamı tablo tekilleştirilmemiştir. Diğer bir ifade ile
# müşteri birden fazla alışverişyapmış olabilir.
######################################################################
# Değişkneler:
######################################################################
# SaleId: Satış id
# SaleDate : Satış Tarihi
# Price: Satış için ödenen fiyat
# ConceptName:Otel konsept bilgisi
# SaleCityName: Otelin bulunduğu şehir bilgisi
# CheckInDate:Müşterinin otelegirişitarihi
# CInDay:Müşterinin otele giriş günü
# SaleCheckInDayDiff: Check in ile giriş tarihi gün farkı
# Season:Otele giriş tarihindeki sezon bilgisi
######################################################################
import numpy as np
import pandas as pd
import seaborn as sns

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)
######################################################################
# Görev 1: Aşağıdaki Soruları Yanıtlayınız
######################################################################
# Soru1 : miuul_gezinomi.xlsx dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.
df = pd.read_excel('Python_Programming/datasets/miuul_gezinomi.xlsx')
df.head()
df.shape
df.info()
df.isnull().sum()

# Soru 2:Kaç unique şehir vardır? Frekansları nedir?
df['SaleCityName'].nunique()
df['SaleCityName'].value_counts()

# Soru 3:Kaç unique Concept vardır?
df['ConceptName'].nunique()

# Soru4: Hangi Concept’den kaçar tane satış gerçekleşmiş?
df['ConceptName'].value_counts()

# Soru5: Şehirlere göre satışlardan toplam ne kadar kazanılmış?
df.groupby('SaleCityName')['Price'].sum()

# Soru6:Concept türlerine göre göre ne kadar kazanılmış?
df.groupby('ConceptName')['Price'].sum()

# Soru7: Şehirlere göre PRICE ortalamaları nedir?
df.groupby('SaleCityName')['Price'].mean()

# Soru 8:Conceptlere göre PRICE ortalamaları nedir?
df.groupby('ConceptName')['Price'].mean()

# Soru 9: Şehir-Concept kırılımında PRICE ortalamaları nedir?
df.groupby(['SaleCityName', 'ConceptName'])['Price'].mean()

######################################################################
# Görev 2: SaleCheckInDayDiff değişkenini EB_Score adında yeni bir kategorik değişkene çeviriniz.
######################################################################
# • SaleCheckInDayDiff değişkeni müşterinin CheckIn tarihinden ne kadar önce satin alımını tamamladığını gösterir.
# • Aralıkları ikna edici şekilde oluşturunuz.
#   Örneğin: '0_7’, '7_30', '30_90', '90_max' aralıklarını kullanabilirsiniz.
# • Bu aralıklar için "Last Minuters", "Potential Planners", "Planners", "Early Bookers" isimlerini kullanabilirsiniz.

df['SaleCheckInDayDiff'].value_counts()

max_val = df['SaleCheckInDayDiff'].max()
bins = [0, 7, 30, 90, max_val]
labels = ["Last Minuters", "Potential Planners", "Planners", "Early Bookers"]
df['EB_Score'] = pd.cut(df['SaleCheckInDayDiff'], bins=bins, labels=labels, include_lowest=True)

df[['SaleCheckInDayDiff', 'EB_Score']].head(30)

######################################################################
# Görev 3: Şehir-Concept-EB_Score, Şehir-Concept- Sezon, Şehir-Concept-CInDay kırılımında ortalama ödenen ücret ve yapılan işlem sayısı cinsinden inceleyiniz?
######################################################################

df.groupby(['SaleCityName', 'ConceptName', 'EB_Score']).agg({'Price': ['mean', 'count']})
df.groupby(['SaleCityName', 'ConceptName', 'Seasons']).agg({'Price': ['mean', 'count']})
df.groupby(['SaleCityName', 'ConceptName', 'CInDay']).agg({'Price': ['mean', 'count']})

######################################################################
# Görev 4: City-Concept-Season kırılımının çıktısını PRICE'a göre sıralayınız.
######################################################################
# Elde ettiğiniz çıktıyı agg_df olarak kaydediniz.
agg_df = df.groupby(['SaleCityName', 'ConceptName', 'Seasons']).agg({'Price': 'mean'}).sort_values('Price', ascending=False)
agg_df.head(10)

######################################################################
# Görev 5: Indekste yer alan isimleri değişken ismine çeviriniz.
######################################################################
# Üçüncü sorunun çıktısında yer alan PRICE dışındaki tüm değişkenler index isimleridir. Bu isimleri değişken isimlerine çeviriniz.
agg_df = agg_df.reset_index()
agg_df.head()

######################################################################
# Görev 6: Yeni seviye tabanlı müşterileri (persona) tanımlayınız.
######################################################################
# Yeni seviye tabanlı satışları tanımlayınız ve veri setine değişken olarak ekleyiniz.
# • Yeni eklenecek değişkenin adı: sales_level_based
# • Önceki soruda elde edeceğiniz çıktıdaki gözlemleri bir araya getirerek sales_level_based değişkenini oluşturmanız gerekmektedir.
agg_df['sales_level_based'] = agg_df[['SaleCityName', 'ConceptName', 'Seasons']].agg(lambda x: '_'.join(x).upper(), axis=1)
agg_df.head()

######################################################################
# Görev 7: Yeni müşterileri (personaları) segmentlere ayırınız.
######################################################################
# • Yeni personaları PRICE’a göre 4 segmente ayırınız.
# • Segmentleri SEGMENT isimlendirmesi ile değişken olarak agg_df’e ekleyiniz.
# • Segmentleri betimleyiniz (Segmentlere göre group by yapıp price mean, max, sum’larını alınız).
labels = ['D', 'C', 'B', 'A']
agg_df['SEGMENT'] = pd.qcut(agg_df['Price'], 4, labels=labels)
agg_df.head()

agg_df.groupby('SEGMENT').agg({'Price': ['mean', 'max', 'sum']})

######################################################################
# Görev 8: Yeni gelen müşterileri sınıflandırıp, ne kadar gelir getirebileceklerini tahmin ediniz.
######################################################################
# • Antalya’da herşey dahil ve yüksek sezonda tatil yapmak isteyen bir kişinin ortalama ne kadar gelir kazandırması beklenir?
# • Girne’de yarım pansiyon bir otele düşük sezonda giden bir tatilci hangi segmentte yer alacaktır?

# 1. ortalama getirisi?
# SaleCityName = Antalya
# ConceptName = Herşey Dahil Yarım Pansiyon
# Seasons = High

# 2. segment?
# SaleCityName = Girne
# ConceptName =
# Seasons = Low

agg_df[agg_df['sales_level_based'] == 'ANTALYA_YARIM PANSIYON_HIGH']

def calculated_customer_yield(df, new_user):
    return df[df['sales_level_based'] == new_user]

new_user = 'ANTALYA_HERŞEY DAHIL_HIGH'
result = calculated_customer_yield(agg_df, new_user)
avg_customer_revenue = result['Price'].mean()
print(round(avg_customer_revenue, 2))


new_user2 = 'GIRNE_YARIM PANSIYON_LOW'
customer_segment = calculated_customer_yield(agg_df,new_user2)
print(customer_segment['SEGMENT'].item())

