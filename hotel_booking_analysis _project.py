#!/usr/bin/env python
# coding: utf-8

# In[37]:


# Importing libraries


# In[24]:


import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')


# In[25]:


# lOading the datasets


# In[26]:


df = pd.read_csv('hotel_booking.csv.zip')


# In[27]:


df


# In[28]:


# Exploratory Data Analysis and Data Cleaning


# In[29]:


df.head()


# In[30]:


df.tail()


# In[32]:


df.shape


# In[33]:


df1 = df.drop(columns = {'name','phone-number','email','credit_card'},axis = 1)
df1


# In[34]:


df1.shape


# In[35]:


df1.columns


# In[36]:


df1.dtypes


# In[37]:


df1.info()


# In[38]:


df1['reservation_status_date'] = pd.to_datetime(df1['reservation_status_date'])


# In[39]:


df1.info()


# In[40]:


df.describe(include = 'object')


# In[41]:


for col in df.describe(include = 'object').columns:
    print(col)
    print(df[col].unique())
    print('-'*50)


# In[42]:


df1.isnull().sum()


# In[43]:


df1.drop(['company','agent'],axis = 1 ,inplace = True)


# In[44]:


df1.isnull().sum()


# In[45]:


df1.dropna(inplace = True)
df1.isnull().sum()


# In[46]:


df1.describe()


# In[47]:


df['adr'].plot(kind =  'box')


# In[48]:


df1 = df1[df1['adr']<5000]


# In[49]:


df1.describe()


# In[35]:


# Data Analysis and Visualizations


# In[50]:


cancelled_per = df1['is_canceled'].value_counts(normalize = True)
cancelled_per


# In[52]:


cancelled_per = df1['is_canceled'].value_counts(normalize = True)
print(cancelled_per)

plt.figure(figsize = (5,4))
plt.title('Reservation status count')
plt.bar(['Not canceled','canceled'],df1['is_canceled'].value_counts(),edgecolor = 'k',width = 0.7)
plt.show()


# In[53]:


plt.figure(figsize =  (8,4))
ax1 = sns.countplot(x = 'hotel', hue = 'is_canceled', data = df, palette = 'Blues')
legend_labels = ax1.get_legend_handles_labels()
ax1.legend(bbox_to_anchor = (1,1))
plt.title('Reservation status in different hotels',size = 20)
plt.xlabel('hotel')
plt.ylabel('number of reservation')


# In[54]:


resort_hotel = df1[df1['hotel'] == 'Resort Hotel']
resort_hotel['is_canceled'].value_counts(normalize = True)


# In[55]:


city_hotel = df1[df1['hotel'] == 'City Hotel']
city_hotel['is_canceled'].value_counts(normalize = True)


# In[56]:


resort_hotel = resort_hotel.groupby('reservation_status_date')[['adr']].mean()
city_hotel = city_hotel.groupby('reservation_status_date')[['adr']].mean()


# In[57]:


plt.figure(figsize = (20,8))
plt.title('Average Daily Rate in City and Resort Hotel',fontsize = 30)
plt.plot(resort_hotel.index,resort_hotel['adr'],label = 'Resort hotel')
plt.plot(city_hotel.index,city_hotel['adr'],label = 'City hotel')
plt.legend(fontsize = 20)
plt.show()


# In[58]:


df1['month'] = df1['reservation_status_date'].dt.month
plt.figure(figsize = (16,8))
ax1 = sns.countplot(x = 'month',hue = 'is_canceled' ,data = df1,palette = 'bright' )
legend_label = ax1.get_legend_handles_labels()
ax1.legend(bbox_to_anchor = (1,1))
plt.title('Reservation status per month',size = 20)
plt.xlabel('month')
plt.ylabel('number of reservation')
plt.legend(['not canceled','canceled'])
plt.show()


# In[59]:


plt.figure(figsize = (15,8))
plt.title('ADR per month',fontsize = 30)
sns.barplot('month','adr',data = df1[df1['is_canceled']==1].groupby('month')[['adr']].sum().reset_index())

plt.show()


# In[60]:


canceled_data = df1[df1['is_canceled']==1]
top_10_country = canceled_data['country'].value_counts()[:10]
plt.figure(figsize = (8,8))
plt.title('Top 10 countries with reservation cancelled')
plt.pie(top_10_country,autopct = '%.2f',labels = top_10_country.index)
plt.show()


# In[61]:


df1['market_segment'].value_counts()


# In[62]:


df1['market_segment'].value_counts(normalize = True)


# In[63]:


canceled_data['market_segment'].value_counts(normalize = True)


# In[64]:


canceled_df_adr = canceled_data.groupby('reservation_status_date')[['adr']].mean()
canceled_df_adr.reset_index(inplace = True)
canceled_df_adr.sort_values('reservation_status_date',inplace = True)

not_canceled_data = df1[df1['is_canceled']==0]
not_canceled_df_adr = not_canceled_data.groupby('reservation_status_date')[['adr']].mean()
not_canceled_df_adr.reset_index(inplace = True)
not_canceled_df_adr.sort_values('reservation_status_date',inplace = True)


plt.figure(figsize = (20,6))
plt.title('Average Daily Rate')
plt.plot(not_canceled_df_adr['reservation_status_date'],not_canceled_df_adr['adr'],label = 'not cancelled')
plt.plot(canceled_df_adr['reservation_status_date'],canceled_df_adr['adr'],label = ' cancelled')
plt.legend()
plt.show()


# In[65]:


cancelled_df_adr = canceled_df_adr[(canceled_df_adr['reservation_status_date'] >'2016') & (canceled_df_adr['reservation_status_date'] < '2017-09')]
not_cancelled_df_adr = not_canceled_df_adr[(not_canceled_df_adr['reservation_status_date'] >'2016') & (not_canceled_df_adr['reservation_status_date'] < '2017-09')]                                                                                                        


# In[67]:


plt.figure(figsize = (20,6))
plt.title('Average Daily Rate',fontsize = 30)
plt.plot(not_cancelled_df_adr['reservation_status_date'],not_cancelled_df_adr['adr'],label = 'not cancelled')
plt.plot(cancelled_df_adr['reservation_status_date'],cancelled_df_adr['adr'],label = ' cancelled')
plt.legend()
plt.show()


# # Suggestions

# In[ ]:


1-cancellation rates rise as the prices does.In order to prevent cancellations of reservation,hotels could work on their pricing
strategies and try to lower the rates for specific hotel based on locations.
2- In the month of January,hotels can start campaigns or marketing with a reasonable amount to increase their revenue as the the
cancellation is the highest in this month.

