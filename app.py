from collections import defaultdict
import numpy as np
import joblib
import warnings
import pandas as pd

base_model_0 = joblib.load('base_model_0.pkl')

base_model_1 = joblib.load('base_model_1.pkl')

base_model_2 = joblib.load('base_model_2.pkl')

all_columns = ['Ad Placement Method__direct through outlet', 'Ad Placement Method__media placement vendor', 'Ad Placement Method__non-profit', 'Ad Placement Method__other', 'Ad Placement Method__placement vendor', 'Type of Media (MOECM)__digital', 'Type of Media (MOECM)__other', 'Type of Media (MOECM)__print', 'Type of Media (MOECM)__radio', 'Type of Media (MOECM)__tv', 'Outlet Channel (Agency submission)__digital', 'Outlet Channel (Agency submission)__digital media', 'Outlet Channel (Agency submission)__digital out of home', 'Outlet Channel (Agency submission)__digital screens', 'Outlet Channel (Agency submission)__job board', 'Outlet Channel (Agency submission)__journal (print)', 'Outlet Channel (Agency submission)__magazine (digital)', 'Outlet Channel (Agency submission)__magazine (print)', 'Outlet Channel (Agency submission)__newsletter (digital)', 'Outlet Channel (Agency submission)__newsletter (print)', 'Outlet Channel (Agency submission)__newspaper', 'Outlet Channel (Agency submission)__newspaper (digital)', 'Outlet Channel (Agency submission)__newspaper (print)', 'Outlet Channel (Agency submission)__newspaper digital', 'Outlet Channel (Agency submission)__other', 'Outlet Channel (Agency submission)__out of home', 'Outlet Channel (Agency submission)__out of home advertisment', 'Outlet Channel (Agency submission)__program', 'Outlet Channel (Agency submission)__programmatic', 'Outlet Channel (Agency submission)__radio', 'Outlet Channel (Agency submission)__radio chanel', 'Outlet Channel (Agency submission)__radio channel', 'Outlet Channel (Agency submission)__radio show', 'Outlet Channel (Agency submission)__radio station', 'Outlet Channel (Agency submission)__social media', 'Outlet Channel (Agency submission)__streaming radio', 'Outlet Channel (Agency submission)__streaming video', 'Outlet Channel (Agency submission)__television', 'Outlet Channel (Agency submission)__television channel', 'Outlet Channel (Agency submission)__television show', 'Outlet Channel (Agency submission)__tv', 'Outlet Channel (Agency submission)__webpage (digital)', 'Outlet Channel (Agency submission)__website (digital)', 'Language__a - adserving', 'Language__african', 'Language__albanian', 'Language__arabic', 'Language__bambara', 'Language__bengali', 'Language__bengali (bangla)', 'Language__cantonese', 'Language__chinese', 'Language__chinese (cantonese)', 'Language__chinese (mandarin)', 'Language__chinese (simplified)', 'Language__chinese (traditional)', 'Language__english', 'Language__english-caribbean', 'Language__english-hindi', 'Language__filipino', 'Language__french', 'Language__french-creole', 'Language__fulani', 'Language__greek', 'Language__gujarati', 'Language__haitian creole', 'Language__hindi', 'Language__italian', 'Language__japanese', 'Language__jewish', 'Language__jewish english', 'Language__korea', 'Language__korean', 'Language__mandarin', 'Language__multiple', 'Language__n', 'Language__pakistani', 'Language__polish', 'Language__punjabi', 'Language__russian', 'Language__simplified chinese', 'Language__south asian', 'Language__spanish', 'Language__spanish and chinese', 'Language__traditional bengali', 'Language__traditional chinese', 'Language__unknown', 'Language__urdu', 'Language__varies per location', 'Language__wolof', 'Language__yiddish', 'Purpose__9', 'Purpose__advertisement', 'Purpose__benefits', 'Purpose__city administration', 'Purpose__civic engagement', 'Purpose__education', 'Purpose__elections', 'Purpose__executive order', 'Purpose__housing', 'Purpose__legal notices', 'Purpose__other', 'Purpose__public health', 'Purpose__public hearing', 'Purpose__public notice', 'Purpose__public safety', 'Purpose__quality of life', 'Purpose__recruitmant', 'Purpose__recruitment', 'Purpose__social services', 'Spend Amount']

grouped_features = defaultdict(list)
for f in all_columns:
    if '__' in f:
        key, val = f.split('__', 1)
        grouped_features[key.strip()].append(val.strip())

opsi_apm =  grouped_features["Ad Placement Method"]
opsi_type_of_media = grouped_features["Type of Media (MOECM)"]
opsi_outlet_channel = grouped_features["Outlet Channel (Agency submission)"]
opsi_language = grouped_features["Language"]
opsi_purpose = grouped_features["Purpose"]

def validate_input(options, input_str, feature_name):
    """Validasi input dan beri peringatan jika tidak sesuai"""
    input_lower = input_str.lower()
    valid_options = [opt.lower() for opt in options]
    
    if input_lower not in valid_options:
        warnings.warn(f"⚠️ Peringatan: Input '{input_str}' tidak valid untuk {feature_name}! Pilihan yang tersedia: {options}")
        return False
    return True

print("\n=== INPUT DATA ===")
print("\n🔹 Ad Placement Method:")
for i, opt in enumerate(opsi_apm, 1):
    print(f"{i}. {opt}")
Ad_Placement_Method = input("Pilih (masukkan teks): ")
while not validate_input(opsi_apm, Ad_Placement_Method, "Ad Placement Method"):
    Ad_Placement_Method = input("Coba lagi: ")
a = f"Ad Placement Method__{Ad_Placement_Method.lower()}"

print("\n🔹 Type of Media (MOECM):")
for i, opt in enumerate(opsi_type_of_media, 1):
    print(f"{i}. {opt}")
Type_of_Media = input("Pilih (masukkan teks): ")
while not validate_input(opsi_type_of_media, Type_of_Media, "Type of Media"):
    Type_of_Media = input("Coba lagi: ")
b = f"Type of Media (MOECM)__{Type_of_Media.lower()}"

print("\n🔹 Outlet Channel:")
for i, opt in enumerate(opsi_outlet_channel, 1):
    print(f"{i}. {opt}")
Outlet_Channel = input("Pilih (masukkan teks): ")
while not validate_input(opsi_outlet_channel, Outlet_Channel, "Outlet Channel"):
    Outlet_Channel = input("Coba lagi: ")
c = f"Outlet Channel (Agency submission)__{Outlet_Channel.lower()}"

print("\n🔹 Language:")
for i, opt in enumerate(opsi_language, 1):
    print(f"{i}. {opt}")
Language = input("Pilih (masukkan teks): ")
while not validate_input(opsi_language, Language, "Language"):
    Language = input("Coba lagi: ")
d = f"Language__{Language.lower()}"

print("\n🔹 Purpose:")
for i, opt in enumerate(opsi_purpose, 1):
    print(f"{i}. {opt}")
Purpose = input("Pilih (masukkan teks): ")
while not validate_input(opsi_purpose, Purpose, "Purpose"):
    Purpose = input("Coba lagi: ")
e = f"Purpose__{Purpose.lower()}"

print("\n🔹 Spend Amount:")
while True:
    Spend_Amount = input("Masukkan jumlah (angka): ")
    try:
        Spend_Amount = float(Spend_Amount)
        break
    except ValueError:
        print("❌ Error: Harap masukkan angka yang valid!")


selected_features = {a, b, c, d, e}
feature = [1 if i in selected_features else 0 for i in all_columns]
feature[-1] = Spend_Amount

with warnings.catch_warnings():
    warnings.simplefilter("always")
    X_test = pd.DataFrame([feature], columns=all_columns) 
    y_pred_0 = base_model_0.predict(X_test)
    y_pred_1 = base_model_1.predict(X_test)
    y_pred_2 = base_model_2.predict(X_test)

    y_pred = np.column_stack((y_pred_0, y_pred_1, y_pred_2))
    y_pred = [[int(val) for val in row] for row in y_pred]
    y_pred_ku = np.argmax(y_pred, axis=1)

print("\n=== HASIL PREDIKSI ===")
if y_pred_ku[0] == 0 :
    x = "iklan  yang mana akan memiliki jangkauan luas"
elif y_pred_ku[0] == 1 :
    x = "iklan sedang yang cukup masif"
elif y_pred_ku[0] == 2 :
    x = "iklan ini cocok untuk kawasan lokal"
     
print(f"🎯 Hasil akhir: {x}")

warnings.filterwarnings("default", category=UserWarning)
