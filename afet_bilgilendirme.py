import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# CSV dosyasının bilgisayardaki konumunu file_path değişkenine atadık.
file_path = r"C:\Users\excalibur\Desktop\pythonodev\natural_disasters_2024 (1).csv"

# CSV dosyasını olası hata durumu olunca yakalamak için try-except bloğu ile yakalıyoruz.
try:
    # Dosyayı pandas ile okuyoruz
    data = pd.read_csv(file_path)
    print("Dosya başarıyla yüklendi!")
    print(data.head())  # Veri setinin ilk 5 satırını head() metodu ile yazdırıyoruz.
except FileNotFoundError:
    print("Hata: Dosya yolu bulunamadı. Lütfen yolu ve dosya adını kontrol edin.")
    exit()  # Eğer dosya bulunamazsa programı sonlandırıyoruz

# Veri İncelemesi Sorgularını yapıyoruz.  
print("Veri setinin ilk 5 satırı:")
print(data.head())  # İlk 5 satırı yazdırıyoruz  !!Sorgu
print("\nVeri setinin genel bilgileri:")
data.info()  # Veri setinin yapısını ve her sütunun tipini yazdırıyoruz  !!Sorgu
print("\nEksik değerlerin sayısı:")
print(data.isnull().sum())  # Eksik değerlerin sayısını kontrol ediyoruz  !!Sorgu

# Eksik verileri dolduruyoruz (varsayılan olarak '**' ile)
data.fillna("**", inplace=True)

# 1. En Sık Görülen Afet Türleri (Yatay Çubuk Grafiği)
print("\nEn sık görülen afet türleri (Yatay Çubuk Grafiği):")
disaster_counts = data["Disaster_Type"].value_counts()  # Afet türlerinin sıklığını hesaplıyoruz  !!Sorgu
plt.figure(figsize=(10, 8))  # Grafiğin boyutunu ayarlıyoruz
sns.barplot(x=disaster_counts.values, y=disaster_counts.index, palette="viridis", orient='h')  # Yatay çubuk grafiği çiziyoruz
plt.title("En Sık Görülen Afet Türleri")
plt.xlabel("Sayısı")
plt.ylabel("Afet Türü")
plt.show()  
# Açıklama: Bu grafik, her afet türünün ne kadar sık meydana geldiğini gösteren yatay bir çubuk grafik olarak sunuluyor. 
# Afet türlerinin sıklığı "Disaster_Type" sütununa göre hesaplanmaktadır.

# 2. Afet Büyüklüğüne Göre Ölümler
print("\nAfet büyüklüğüne göre ölümlerin dağılımı:")
plt.figure(figsize=(10, 6))
sns.scatterplot(x="Magnitude", y="Fatalities", data=data, hue="Disaster_Type", palette="viridis")  # Dağılım grafiği oluşturuyoruz
plt.title("Afet Büyüklüğüne Göre Ölümler")
plt.xlabel("Büyüklük")
plt.ylabel("Ölümler")
plt.legend(title="Afet Türü", bbox_to_anchor=(1.05, 1), loc="upper left")  # Grafiğe açıklama ekliyoruz
plt.show()
# Açıklama: Bu grafik, afetlerin büyüklüğüne (Magnitude) göre ölümlerin (Fatalities) dağılımını bir noktalarla (scatter plot) gösteriyor.
# Afet türleri farklı renklerle ayırt ediliyor. Bu, afet büyüklüğü ile ölüm sayısı arasındaki ilişkiyi gözlemlemeye olanak tanır.

# 3. Tarihe Göre Afetlerin Büyüklüğü
print("\nTarihe göre afetlerin büyüklüğü:")
data["Date"] = pd.to_datetime(data["Date"], format="%Y-%m-%d %H:%M:%S")  # Tarih sütununu datetime formatına çeviriyoruz
plt.figure(figsize=(12, 6))
sns.lineplot(x="Date", y="Magnitude", data=data, ci=None)  # Zaman serisi çiziyoruz
plt.title("Tarihe Göre Afetlerin Büyüklüğü")
plt.xlabel("Tarih")
plt.ylabel("Büyüklük")
plt.show()
# Açıklama: Bu grafik, afetlerin büyüklüğünü zamanla (Tarih) nasıl değiştiğini gösteren bir çizgi grafiğidir.
# Zaman içinde büyüklüklerin trendini inceleyerek afetlerin sıklığı ve şiddetindeki değişimleri gözlemleyebilirsiniz.

# 4. En Çok Ölüm Yaşanan Ülkeler  !!Sorgu
print("\nEn çok ölüm yaşanan ülkeler:")
fatalities_by_location = data.groupby("Location")["Fatalities"].sum().sort_values(ascending=False)  # Ülkelere göre ölümleri topluyoruz
print(fatalities_by_location.head(10))  # İlk 10 ülkeyi yazdırıyoruz
# Açıklama: Bu sorgu, her bir ülke için toplam ölüm sayısını hesaplar ve en fazla ölüm yaşanan 10 ülkeyi listeler.

# Pasta grafiği ile en çok ölüm yaşanan ülkeler   !!Sorgu
print("\nEn çok ölüm yaşanan ülkeler (Pasta Grafiği):")
top_10_fatalities = fatalities_by_location.head(10)
plt.figure(figsize=(10, 10))
top_10_fatalities.plot(kind='pie', autopct='%1.1f%%', startangle=90, shadow=True, colors=sns.color_palette("Set3"))
plt.title("En Çok Ölüm Yaşanan Ülkeler")
plt.ylabel('')
plt.show()
# Açıklama: Bu pasta grafiği, en fazla ölüm yaşanan 10 ülkeyi ve her birinin yüzdelik payını gösterir. 
# Verilerin görselleştirilmesi, her bir ülkenin ölüm oranının daha kolay anlaşılmasını sağlar.

# 5. Ülkelere Göre Toplam Ekonomik Kayıplar (Yatay Çubuk Grafiği)  !!Sorgu
print("\nÜlkelere göre toplam ekonomik kayıplar (Yatay Çubuk Grafiği):")
economic_loss_by_location = data.groupby("Location")["Economic_Loss($)"].sum().sort_values(ascending=False)  # Ülkelere göre ekonomik kayıpları topluyoruz
plt.figure(figsize=(10, 8))
sns.barplot(x=economic_loss_by_location.values, y=economic_loss_by_location.index[:10], palette="YlOrRd", orient='h')
plt.title("Ülkelere Göre En Yüksek Ekonomik Kayıplar")
plt.xlabel("Toplam Ekonomik Kayıp ($)")
plt.ylabel("Ülke")
plt.show()
# Açıklama: Bu grafik, ülkelere göre toplam ekonomik kayıpları sıralar ve ilk 10 ülkeyi yatay çubuk grafiğiyle gösterir.
# Böylece hangi ülkelerin afetler sonucunda daha fazla ekonomik zarar gördüğü görsel olarak analiz edilir.

# 6. Her Afet Türü İçin Ortalama Ekonomik Kayıp  !!Sorgu
print("\nHer afet türü için ortalama ekonomik kayıp:")
mean_loss_by_disaster = data.groupby("Disaster_Type")["Economic_Loss($)"].mean()  # Afet türlerine göre ortalama kaybı hesaplıyoruz
print(mean_loss_by_disaster)
# Açıklama: Bu sorgu, her afet türü için ortalama ekonomik kaybı hesaplar ve her türdeki kaybın büyüklüğünü gösterir.

# 7. En Düşük Büyüklükteki 5 Afet !!Sorgu
print("\nEn düşük büyüklükteki 5 afet:")
lowest_magnitude_disasters = data.nsmallest(5, "Magnitude")  # En küçük büyüklükteki 5 afet
print(lowest_magnitude_disasters)
# Açıklama: Bu sorgu, büyüklük açısından en küçük 5 afetin verilerini çıkarır. Genellikle, küçük büyüklükteki afetler daha az hasar bırakabilir.

# En düşük büyüklükteki afet türlerinin dağılımı (Pasta Grafiği) !!Sorgu
print("\nEn düşük büyüklükteki afetlerin türlerinin dağılımı:")  
plt.figure(figsize=(8, 8))
lowest_magnitude_disasters["Disaster_Type"].value_counts().plot(kind="pie", autopct="%1.1f%%", startangle=140, colors=sns.color_palette("pastel"))
plt.title("En Düşük Büyüklükteki Afet Türleri")
plt.ylabel("")
plt.show()
# Açıklama: Bu pasta grafiği, en düşük büyüklükteki afet türlerinin dağılımını gösterir.
# Bu, küçük afetlerin hangi türde daha sık meydana geldiğini anlamamıza yardımcı olur.

# 8. Ölümlerle Ekonomik Kayıplar Arasındaki İlişki !!Sorgu
print("\nÖlümlerle ekonomik kayıplar arasındaki ilişki:")
plt.figure(figsize=(10, 6))
sns.regplot(x="Fatalities", y="Economic_Loss($)", data=data, scatter_kws={'alpha':0.5}, line_kws={"color":"red"})  # Regresyon çizgisi
plt.title("Ölümler ve Ekonomik Kayıplar Arasındaki İlişki")
plt.xlabel("Ölümler")
plt.ylabel("Ekonomik Kayıp ($)")
plt.show()
# Açıklama: Bu grafik, ölümlerle ekonomik kayıplar arasındaki ilişkiyi incelemek için bir regresyon grafiği sunar.
# Grafik, ölümler arttıkça ekonomik kayıpların nasıl değiştiğini görsel olarak ortaya koyar.

# 9. Afet Büyüklüklerinin Dağılımı (Histogram) !!Sorgu
print("\nAfet büyüklüklerinin dağılımı (Histogram):")
plt.figure(figsize=(10, 6))
sns.histplot(data['Magnitude'], kde=True, bins=30)  # Histogram ve kernel yoğunluk tahmini
plt.title("Afet Büyüklüklerinin Dağılımı")
plt.xlabel("Büyüklük")
plt.ylabel("Frekans")
plt.show()
# Açıklama: Bu histogram, afet büyüklüklerinin dağılımını gösterir. 
# Kernel yoğunluk tahmini (KDE) ile büyüklüklerin nasıl yayılış gösterdiğini ve hangi büyüklüklerin daha sık meydana geldiğini inceleyebiliriz.

# 10. Afet Türlerine Göre Ekonomik Kayıp (Box Plot)  !!Sorgu
print("\nAfet türlerine göre ekonomik kayıp (Box Plot):")
plt.figure(figsize=(12, 6))
sns.boxplot(x='Disaster_Type', y='Economic_Loss($)', data=data)  # Box plot ile dağılımı gösteriyoruz
plt.title("Afet Türlerine Göre Ekonomik Kayıp")
plt.xlabel("Afet Türü")
plt.ylabel("Ekonomik Kayıp ($)")
plt.xticks(rotation=90)  # X eksenindeki etiketleri döndürüyoruz
plt.show()
# Açıklama: Bu box plot, afet türlerine göre ekonomik kayıpların dağılımını ve uç değerlerini gösterir.
# Ekonomik kayıpların hangi afet türlerinde daha fazla ya da daha az olduğunu görselleştirir.

# 11. Ay Bazında Afet Sayısı  !!Sorgu
print("\nAy bazında afet sayısı:")
data['Month'] = data['Date'].dt.month  # Tarihten ay bilgisini çıkarıyoruz
monthly_disaster_count = data['Month'].value_counts().sort_index()  # Ay bazında afet sayısını hesaplıyoruz
plt.figure(figsize=(10, 6))
sns.barplot(x=monthly_disaster_count.index, y=monthly_disaster_count.values, palette="coolwarm")
plt.title("Ay Bazında Afet Sayısı")
plt.xlabel("Ay")
plt.ylabel("Afet Sayısı")
plt.xticks(ticks=range(12), labels=['Ocak', 'Şubat', 'Mart', 'Nisan', 'Mayıs', 'Haziran', 'Temmuz', 'Ağustos', 'Eylül', 'Ekim', 'Kasım', 'Aralık'])
plt.show()
# Açıklama: Bu grafik, her ay için afet sayısını gösteren bir çubuk grafiğidir.
# Aylar arasındaki afet sıklığını kıyaslayarak hangi aylarda daha fazla afet yaşandığını gözlemleyebilirsiniz.
