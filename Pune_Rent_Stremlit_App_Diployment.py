import streamlit as st
import pandas as pd
import numpy as np
import warnings
warnings.filterwarnings('ignore')

locality=['AWHO Hadapsar Colony', 'Adarsh Nagar Kiwale',
       'Adarsh Nagar Lohgaon', 'Agalambe', 'Akurdi', 'Akurdi Chowk',
       'Alandi', 'Amar Srushti', 'Ambegaon 1', 'Ambegaon Budruk',
       'Ambegaon Pathar', 'Ambegaon PuneMumbai Hwy', 'Anand Nagar',
       'Anand Tirth Nagar', 'Ashok Nagar', 'Aundh', 'Aundh Gaon',
       'Awhalwadi', 'BT Kawade Road', 'BT Kawde', 'Baderaj Colony',
       'Bakhori', 'Bakori Road', 'Balaji Nagar', 'Balewadi',
       'Balewadi Gaon', 'Balewadi High Street', 'Balewadi Phata', 'Baner',
       'Baner Hill Trail', 'Baner Pashan Link Road', 'Baner Road',
       'Baramati', 'Bavdhan', 'Bhairav Nagar', 'Bhandarkar Road',
       'Bharati Vidyapeeth', 'Bharati Vidyapeeth Campus',
       'Bhau Patil Road', 'Bhawani Peth', 'Bhegade Aali', 'Bhelkenagar',
       'Bhoirwadi', 'Bhosari', 'Bhugaon', 'Bhukum',
       'Bhumkar Das Gugre Road', 'Bhusari colony left',
       'Bhusari colony right', 'Bibwewadi', 'Bibwewadi Kondhwa Road',
       'Blue Ridge   Paranjpe Schemes', 'Boat Club Road', 'Bodkewadi',
       'Bopdev Ghat', 'Bopkhel', 'Bopodi', 'Budhwar Peth', 'Bund Garden',
       'Camp', 'Chakan', 'Chandan Nagar', 'Chandani Chowk', 'Chandkhed',
       'Charholi Budruk', 'Chhatrapati Sambhaji Nagar', 'Chikhali',
       'Chikhali Sector 16', 'Chinchwad', 'Chinchwad Gaon', 'DP Road',
       'Dadachi Wasti', 'Dahanukar Colony', 'Dange Chowk', 'Dapodi',
       'Dashrath Nagar Bhekrai Nagar', 'Dattanagar', 'Dattavadi',
       'Dattwadi', 'Daund', 'Deccan Gymkhana', 'Dehu', 'Dehu Phata',
       'Dehu Road Cantonment', 'Deshmukhwadi', 'Dhamalwadi Bhekrai Nagar',
       'Dhanakwadi', 'Dhankawadi', 'Dhankawadi Police Station Road',
       'Dhankawadi Road', 'Dhanori', 'Dhanukar Colony', 'Dhayari',
       'Dhayari Phata', 'Dhaygude Wada', 'Dhole Patil Road',
       'Digambar Nagar', 'Dighi', 'EON Free Zone', 'Eklavya Colony',
       'Elite 27', 'Empire Estate Phase 1', 'Erandwane', 'Fatima Nagar',
       'Fursungi', 'Gahunje', 'Gananjay Society',
       'Gananjay Society Chaitanya Nagar', 'Ganesh Nagar', 'Ganesh Peth',
       'Ganj Peth', 'Garmal', 'Ghorapdi', 'Ghorpadi', 'Ghule Vasti',
       'Giridhar Nagar', 'Gokhalenagar', 'Gujrat Colony',
       'Gulab Nagar Pune', 'Gultekdi', 'Gururaj Society', 'Guruwar Peth',
       'Hadapsar', 'Hadapsar Gaon', 'Handewadi', 'Handewadi Road',
       'Hanuman Nagar', 'Happy Colony', 'Hingne Budrukh', 'Hinjewadi',
       'Hinjewadi Phase 1', 'ITI road', 'Ideal Colony', 'Indrayani Nagar',
       'Indrayani Nagar Sector 2', 'Indryani nagar', 'Jambhe', 'Jambhul',
       'Jambhulwadi', 'Jambhulwadi Road', 'Jangali Maharaj Road',
       'Jawalkar Nagar', 'Junnar', 'Kale Padal', 'Kalewadi',
       'Kalewadi Pandhapur Road', 'Kalewadi Phata PimpriChinchwad',
       'Kalwad', 'Kalyani Nagar', 'Kamshet', 'Kanhe', 'Karegaon',
       'Karve Nagar', 'Karve Road Erandwane', 'Karve Road Kothrud',
       'Kasarwadi', 'Kasba Peth', 'Kaspate Vasti', 'Kaspate Vasti Road',
       'Katraj', 'Kausar Baugh', 'Keshav Nagar', 'Khadakwasla', 'Khadki',
       'Kharadi', 'Kharadi bypass', 'Kirkatwadi', 'Kiwale', 'Kokane Mala',
       'Kolhewadi', 'Kolte Patil', 'Kolwadi', 'Kondhawe Dhawade',
       'Kondhwa', 'Kondhwa Budruk', 'Kondhwa Budrukh', 'Kondhwa Khurd',
       'KondhwaUndriSaswad Road', 'Kondwa khurd road', 'Koregaon Bhima',
       'Koregaon Park', 'Koregaon Park Annexe', 'Kothrud',
       'Kothrud Bus Stand Road', 'Kothrud Depot Road', 'Kranti Nagar',
       'Kunal Icon Road', 'Kutwal Colony', 'L&T Labour Colony',
       'Law College Road', 'Laxman Nagar', 'Laxmi Chowk Road', 'Lohegaon',
       'Lokmanya Nagar', 'Loni Kalbhor', 'Lonikand', 'Lulla Nagar',
       'MAE Campus', 'MG Road', 'Maan', 'Madhala Vada', 'Madhav Nagar',
       'Magarpatta', 'Mahalunge', 'Mahalunge Ingale', 'Mamurdi',
       'Manaji Nagar', 'Mangawadi', 'Mangdewadi', 'Manjari',
       'Manjari Budruk', 'Manjari Khurd', 'Manjri Village Road',
       'Market yard', 'Marunji', 'Marunji Road', 'Marvel Fria Road',
       'Maval', 'Mayur Nagari', 'Megapolis Sunway Internal Road',
       'Model Colony', 'Modi Colony', 'Mohammed wadi', 'Mohan Nagar',
       'Mohan Nagar MIDC', 'Morwadi', 'Moshi', 'Mukai Nagar',
       'Mukesh Nagar', 'Mukund Nagar', 'Mulshi', 'Mundhwa',
       'Mundhwa Kharadi Road', 'Mundhwa Manjari Road', 'Munjaba Basti',
       'Munjaba Vasti', 'Murlidhar Housing Society', 'NIBM',
       'NIBM Annex Mohammadwadi', 'NIBM Annexe', 'Nanded', 'Nanded Phata',
       'Narayan Peth', 'Narayangaon', 'Narhe', 'National Society',
       'Nehru Nagar', 'Nere', 'Nerhe', 'Netaji Nagar', 'New DP Road',
       'New Kalyani Nagar', 'New Sangavi', 'New Sanghvi', 'Nigdi',
       'Nigdi Sector 24', 'Nigdi Sector 26', 'Nimbalkar Nagar Lohgaon',
       'Old Sanghvi', 'Old Sangvi', 'Olkaiwadi', 'Om Colony', 'Padmavati',
       'Pan Card Club Road', 'Pandav Nagar', 'Pandhari Nagar', 'Pangoli',
       'Parvati Darshan', 'Pashan', 'Pashan Sus Road', 'Paud Road',
       'Perugate', 'Phase 2', 'Phursungi Village Road', 'Pimple Gurav',
       'Pimple Nilakh', 'Pimple Saudagar', 'Pimpri', 'Pimpri Chinchwad',
       'Pirangut', 'Pisoli', 'Pisoli Road', 'Porwal Rd',
       'Pradhikaran Nigdi', 'Pratik Nagar', 'Punawale', 'Pune Cantonment',
       'Pune Nagar Road', 'Pune Satara Rd', 'Pune Satara Road',
       'Pune Solapur Road', 'Pune Station', 'Purnanagar', 'Rahatani',
       'Rajas Society', 'Rajgurunagar', 'Ram Nagar', 'Rambaug Colony',
       'Ramkrishna Paramhans Nagar', 'Ramtekdi Industrial Area',
       'Ranjangaon', 'Rasta Peth', 'Ravet', 'Raviwar Peth',
       'Renuka Nagar', 'SNBP School Road', 'Sadashiv Peth',
       'Sadhu Vaswani Chowk', 'Sahakar Nagar', 'Sahakar Nagar II',
       'Saibaba Nagar', 'Sainath Nagar', 'Sakal Nagar', 'Salisbury Park',
       'Salunke Vihar', 'Salunke Vihar Road', 'Sanaswadi', 'Sangamvadi',
       'Sanjay Park', 'Sant Nagar', 'Sant tukaram Nagar',
       'Santhosh Nagar', 'Sasane Nagar', 'Saswad', 'Satar Nagar',
       'Satara road', 'Satavwadi',
       'Satyapuram Co operative Housing Society', 'Sector 27 Pradhikaran',
       'Sector 29', 'Sector No1 Bhosari', 'Senapati Bapat Road',
       'Shaniwar Peth', 'Shankar Sheth Rd', 'Shankarseth Road',
       'Shantiban Society', 'Sharad Nagar', 'Shastri Nagar',
       'Shedge Vasti PimpriChinchwad', 'Sheela Vihar Colony',
       'Shewalewadi', 'Shikrapur', 'Shikshak nagar', 'Shinde Vasti',
       'Shindenagar', 'Shirgaon', 'Shirur', 'Shivaji Nagar',
       'Shivajinagar', 'Shivane', 'Shivtirth Nagar',
       'Shree Sant Eknath Nagar', 'Shree Sidhivinayaka Nagri',
       'Shukrawar Peth', 'Siddartha Nagar', 'Siddharth nagar',
       'Sinhagad Fort', 'Sinhgad Road', 'Sky Water Road', 'Somatane',
       'Someshwarwadi', 'Somwar Peth', 'Sopan Baug', 'Subhas Nagar',
       'Sukhsagar Nagar', 'Sunarwadi', 'Sus', 'Swargate', 'Talegaon',
       'Talegaon Dabhade', 'Talegaon Dhamdhere', 'Taljai Road', 'Talwade',
       'Tapodham', 'Tathawade', 'Teen Hatti Chowk Road', 'Thergaon',
       'Tilak Road', 'Tilekar Nagar', 'Tingre Nagar', 'Tukai Darshan',
       'Tukaram Nagar', 'Tulaja Bhawani Nagar', 'Ubale Nagar',
       'Udyog Nagar', 'Undri', 'Uruli Devachi', 'Uttam Nagar', 'Vadgaon',
       'Vadgaon Budruk', 'Vadgaon Sheri', 'Vadgoan Sheri Rajendri Nagar',
       'Vakil Nagar', 'Vallabh Nagar', 'Valvan Lonavla',
       'Vanaz Corner Pedestrian Crossing', 'Vanaz corner', 'Varale Pune',
       'Vardhaman Township Sasane Nagar', 'Varsha Park Society',
       'Vasant Vihar', 'Veerbhadra Nagar', 'Vijay Nagar', 'Vikas Nagar',
       'Viman Nagar', 'Vishal Nagar', 'Vishal Nagar Main',
       'Vishal nagar square new dp road', 'Vishrantwadi', 'Vittalvadi',
       'Vitthal Wadi', 'Wadarvadi', 'Wadegaon', 'Wadgaon Budruk',
       'Wadgaon Sheri', 'Wagholi', 'Wagholi Kesnand Wadegaon Road',
       'Wagholi Road', 'Wakad', 'Wakad Chowk Road', 'Wakad Pune',
       'Wakadkar Wasti', 'Walhekarwadi Chinchwad', 'Walvekar Nagar',
       'Wanawadi Gaon', 'Wanowrie', 'Wanwadi', 'Warje', 'Warje Malwadi',
       'Yamuna Nagar', 'Yashwant Nagar', 'Yashwantnagar',
       'Yashwantrao Chavan Nagar', 'Yerawada', 'Yerwada Village',
       'Yewalewadi', 'aranyeshwar', 'bavdhan patil nagar',
       'bhekarai nagar', 'bhusari colony', 'chintamani park',
       'hingne Khurd', 'katraj kondhwa road', 'kesnand', 'maharshi nagar',
       'mandai', 'wadebolhai']

Area=st.sidebar.number_input('Area in Sqft',value=0.00)
st.write('Area=',Area,'Sqft')

BedRooms=st.sidebar.selectbox('No of BedRooms',[1,2,3,4,5,6,7,8])
st.write('No of BedRooms=',BedRooms)

Seller_Type_Cat=['BUILDER','OWNER']

Seller_Type_select=st.sidebar.selectbox('Seller_Type',['BUILDER','OWNER'])
st.write('Seller_Type=',Seller_Type_select)

#Seller_Type_Encoding
Seller_Type_Encoding=[]
for s in Seller_Type_Cat:
    if (Seller_Type_select==s):
        Seller_Type_Encoding.append(1)
    else:
        Seller_Type_Encoding.append(0)
#print(Seller_Type_Encoding)

#Property_Type_Encoding
Property_Type_Cat=['Independent Floor','Independent House', 'Penthouse','Studio Apartment','Villa']

Property_Type_select=st.sidebar.selectbox('Property_Type',Property_Type_Cat)
st.write('Property_Type =',Property_Type_select)

Property_Type_Encoding=[]
for p in Property_Type_Cat:
    if (Property_Type_select==p):
        Property_Type_Encoding.append(1)
    else:
        Property_Type_Encoding.append(0)
#print(Property_Type_Encoding)


Locality_select=st.sidebar.selectbox('Locality',locality)
st.write('Locality =',Locality_select)
# LOCALITY_ENCODING
locality_encoding=[]
for L in locality:
    if (L==Locality_select):
        locality_encoding.append(1)
    else:
        locality_encoding.append(0)

#print(locality_encoding)

furnish_type=['Semi-Furnished','Unfurnished']

furnish_type_select=st.sidebar.selectbox('furnish_type',furnish_type)
st.write('Furnish_type =',furnish_type_select)
# furnish_type_ENCODING
furnish_type_encoding=[]
for F in furnish_type:
    if (F==furnish_type_select):
        furnish_type_encoding.append(1)
    else:
        furnish_type_encoding.append(0)
#print(furnish_type_encoding)
      
#Bathroom_Encoding
Bathroom_encoding=[]
Bathroom_Cat=['2 ','3 ', '4 ','5', '6 ', '8']

No_of_Bathrooms_select=st.sidebar.selectbox('No.of Bathrooms',Bathroom_Cat)
st.write('No.of Bathrooms =',No_of_Bathrooms_select)


for B in Bathroom_Cat:
    if (B==No_of_Bathrooms_select):
        Bathroom_encoding.append(1)
    else:
        Bathroom_encoding.append(0)
#print(Bathroom_encoding)

#Final_Encoding
Final_Encoding=[]
Final= [Area]+[BedRooms]+Seller_Type_Encoding+Property_Type_Encoding+locality_encoding+furnish_type_encoding+Bathroom_encoding
print(Final)

import pickle
from sklearn.ensemble import RandomForestRegressor

Machine_learning_model=pickle.load(open('Pune_Rent_App.pkl',"rb"))
Random_Forest=Machine_learning_model[0].predict([Final])[0]
print(round(Random_Forest,2))

st.write('__House Rent Will be Approximately:__',' #',round(Random_Forest,2),'Rs')
st.success('Success')

#print(len([Area]),len([BedRooms]),len(Seller_Type_Encoding),len(Property_Type_Encoding),len(locality_encoding),len(furnish_type_encoding),len(Bathroom_encoding))
