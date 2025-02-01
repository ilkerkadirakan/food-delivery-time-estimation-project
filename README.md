# 📦 Teslimat Süresi Tahmin Uygulaması

Bu proje, bir kargo sisteminde, kurye, hava durumu, trafik durumu ve araç türü gibi faktörlere dayanarak teslimat süresini tahmin etmek için geliştirilmiş bir makine öğrenmesi modelini kullanmaktadır.

## 🚀 Başlangıç

Projeyi yerel bilgisayarınızda çalıştırmak için aşağıdaki adımları takip edebilirsiniz.

### 1. Gerekli Kütüphanelerin Yüklenmesi

Projenin çalışması için gereken Python kütüphanelerini yüklemek için:

```bash
pip install -r streamlit_app/requirements.txt
```

### 2. Model Eğitimi ve Veri Seti

Modelin nasıl eğitildiğini görmek için **food_delivery_estimation.ipynb** dosyasına göz atabilirsiiz. Bu dosya, modelin eğitim sürecini, veri seti ile yapılan ön işleme adımlarını ve modelin doğruluğunu açıklamaktadır. Kullanılan veri setini görmek için ise **Food_Delivery_Times**  dosyasına göz atabilirsiniz.

### 3. Modelin Yüklenmesi

Proje,  yukarıda bahsedilen dosyadaki eğitilmiş modeli (`model.pkl`) kullanır. Modeli yüklemek için:

```python
import joblib
model = joblib.load('streamlit_app/model.pkl')
```

### 4. Web Uygulaması (Streamlit)

Proje kullanıcıların çeşitli teslimat parametrelerine göre tahmin yapmalarını sağlayan bir web uygulaması (Streamlit) barındırıyor. Uygulamayı başlatmak için:

```bash
streamlit run streamlit_app/food_delivery.py
```

### 5. Kullanıcı Girdileri

Streamlit arayüzü üzerinden aşağıdaki girdileri sağlayarak teslimat süresi tahmininizi alabilirsiniz:
- **Mesafe (km)**: Teslimat mesafesi
- **Hava Durumu**: Seçilebilecek hava durumu seçenekleri (Rüzgarlı, Açık, Sisli, Yağmurlu, Karlı)
- **Trafik Seviyesi**: Düşük, Orta, Yüksek
- **Günün Saati**: Öğle, Akşam, Gece, Sabah
- **Araç Türü**: Skuter, Motor, Araba
- **Hazırlık Süresi (dk)**: Teslimat öncesi hazırlık süresi
- **Kurye Deneyimi (yıl)**: Kurye deneyimi (yıl olarak)

Uygulama, girilen veriye göre tahmini teslimat süresini hesaplar ve kullanıcıya gösterir.

## ⚙️ Kullanılan Yöntemler

### 1. **Makine Öğrenmesi Modelleri**
Projede, **Ridge Regression** (Eğik Regresyon) kullanılarak, teslimat süresi tahmin edilmiştir.

### 2. **Özellikler ve Veri Manipülasyonu**
Veri seti, çeşitli faktörlere (trafik, hava durumu, araç tipi vb.) göre özelliklerle zenginleştirilmiştir. Bu özellikler:
- **Traffic_Time_Impact**: Trafik yoğunluğunun, teslimat süresi üzerindeki etkisi.
- **Weather_Traffic_Impact**: Hava durumu ve trafik yoğunluğunun birleşik etkisi.
- **Expected_Speed**: Araç türüne göre beklenen hız.

### 3. **Streamlit ile Web Uygulaması**
Streamlit kullanarak, kullanıcılara etkileşimli bir arayüz sağlanmış ve tahmin işlemleri kolayca yapılabilir hale getirilmiştir.

## 📊 Sonuçlar

Projenin tahmin sonuçları, modelin doğruluğuna dayanmaktadır. Model, çeşitli parametreleri göz önünde bulundurarak, kullanıcıların daha hızlı ve doğru teslimat planları yapmalarını sağlar.

## 📝 Lisans

Bu proje, [MIT Lisansı](https://opensource.org/licenses/MIT) ile lisanslanmıştır.
