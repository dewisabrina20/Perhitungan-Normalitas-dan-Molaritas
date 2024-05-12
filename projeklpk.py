import streamlit as st 

#Tampilan Halaman Web
add_selectbox = st.sidebar.selectbox("Menu :mag:", ("Beranda", "Perhitungan Normalitas", "Perhitungan Molaritas"))

#Halaman Beranda
if add_selectbox == "Beranda" :
    st.title(":blue[Tentang Aplikasi]")
    st.markdown('Web aplikasi ini dibuat untuk mempermudah dan mempercepat perhitungan normalitas dan molaritas.')
    
    
    st.title(":blue[Normalitas]")
    st.markdown('Normalitas (N) menyatakan jumlah mol ekuivalen zat terlarut dalam 1 liter larutan.')
    
    st.title(":blue[Rumus Normalitas]")
    st.image('https://hal255.files.wordpress.com/2024/05/blue-simple-keep-calm-desktop-wallpaper-1.png?w=1024')
    st.markdown('''Keterangan :\n
    N = Normalitas larutan \n 
    mg sampel = massa titrat yang ditimbang \n
    mL titran = volume yang didapat saat titrasi \n 
    BE = bobot ekuivalen sampel \n 
    fp = faktor pengali \n''')
    
    
    st.title(":blue[Molaritas]")
    st.markdown('Molaritas (M) menyatakan jumlah mol suatu zat per liter larutan.')
    
    st.title(':blue[Rumus Molaritas]')
    st.image('https://hal255.files.wordpress.com/2024/05/whatsapp-image-2024-05-12-at-20.33.20.jpeg?w=1024')
    st.markdown('''Keterangan :\n
    M = Molaritas larutan \n 
    mg sampel = massa titrat yang ditimbang \n
    mL titran = volume yang didapat saat titrasi \n 
    BM = bobot molekul sampel \n 
    fp = faktor pengali \n''')


#Halaman Perhitungan Normalitas
if add_selectbox == "Perhitungan Normalitas":
    
    st.title(':green[Perhitungan Normalitas]')
    mg = st.number_input("Masukkan nilai massa titrat (mg)", min_value= 0.01 )
    mL = st.number_input("Masukkan nilai volume titran (mL)", min_value= 0.01)
    fp = st.number_input("Masukkan nilai faktor pengali", min_value= 1.00 ) 
    BE = st.number_input("Masukkan nilai bobot ekuivalen (mg/mgrek)", min_value= 0.01)
    
    #Perhitungan Normalitas
    if st.button("Normalitas"):
        Normalitas_Larutan = (mg/(BE*mL*fp))
        st.success (f"Normalitas Larutan Adalah  {Normalitas_Larutan} N")
        
        
#Halaman Perhitungan Molaritas
if add_selectbox == "Perhitungan Molaritas":
    
    st.title(':green[Perhitungan Molaritas]')
    mg = st.number_input("Masukkan nilai massa titrat (mg)", min_value= 0.01 )
    mL = st.number_input("Masukkan nilai volume titran (mL)", min_value= 0.01)
    fp = st.number_input("Masukkan nilai faktor pengali", min_value= 1.00)
    BM = st.number_input("Masukkan nilai bobot molekul (mg/mmol)", min_value= 0.01)
    
    #Perhitungan Molaritas
    if st.button("Molaritas"):
        Molaritas_Larutan = (mg/(BM*mL*fp))
        st.success (f"Molaritas Larutan Adalah {Molaritas_Larutan} M")
