import os
import PyPDF2
import csv
import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages




def function1():
	os.chdir('B:\\Travel\\US\\USF_Course\\EIS')

	data_frame1 = pd.read_csv('icr.csv')
	data_frame1.columns = data_frame1.columns.str.replace(' ','_').str.replace('.','_')
	#print(data_frame1)
	#data_frame2 = pd.read_csv('icr2.csv')
	data_frame3 = pd.read_csv('icr3.csv')
	data_frame3.columns = data_frame3.columns.str.replace(' ','_').str.replace('.','_')
	data_frame4 = pd.read_csv('icr4.csv')
	data_frame5 = pd.read_csv('icr5.csv')
	data_frame5.columns = data_frame5.columns.str.replace(' ','_').str.replace('.','_')
	data_frame5.List_Price = data_frame5.List_Price.apply(lambda x: x.replace('$',''))
	# print(data_frame5.List_Price)
	#print(data_frame2)
	# data_frame2['new_column'] = data_frame2['Pfmn-expected']
	# data_frame2.to_csv('icr1.csv')
	
	data_frame_t = data_frame1[data_frame1.Primary_Segment == 'Trad']
	data_frame_l = data_frame1[data_frame1.Primary_Segment == 'Low']
	data_frame_h = data_frame1[data_frame1.Primary_Segment == 'High']
	data_frame_p = data_frame1[data_frame1.Primary_Segment == 'Pfmn']
	data_frame_s = data_frame1[data_frame1.Primary_Segment == 'Size']
	data_frame_icr = data_frame4[data_frame4.Round == 3]
	#From icr3.csv
	data_frame_t1 = data_frame3[data_frame3.Primary_Segment == 'Trad']
	data_frame_l1 = data_frame3[data_frame3.Primary_Segment == 'Low']
	data_frame_h1 = data_frame3[data_frame3.Primary_Segment == 'High']
	data_frame_p1 = data_frame3[data_frame3.Primary_Segment == 'Pfmn']
	data_frame_s1 = data_frame3[data_frame3.Primary_Segment == 'Size']
	#From icr5.csv Segment Analysis Report
	data_frame_t5 = data_frame5[data_frame5.Primary_Segment == 'Trad']
	data_frame_t5_Able = data_frame_t5[data_frame_t5.Name == 'Able']
	data_frame_l5 = data_frame5[data_frame5.Primary_Segment == 'Low']
	data_frame_l5_Acre = data_frame5[data_frame5.Name == 'Acre']
	data_frame_h5 = data_frame5[data_frame5.Primary_Segment == 'High']
	data_frame_h5_Adam = data_frame5[data_frame5.Name == 'Adam']
	data_frame_p5 = data_frame5[data_frame5.Primary_Segment == 'Pfmn']
	data_frame_p5_Aft = data_frame5[data_frame5.Name == 'Aft']
	data_frame_s5 = data_frame5[data_frame5.Primary_Segment == 'Size']
	data_frame_s5_Agape = data_frame5[data_frame5.Name == 'Agape']

	#print(data_frame_t)
	#print(data_frame_icr)
	#print(data_frame_h5)
	#TRADITIOAL: What's important for traditional: Age 47%, Price 23%, Pfmn-Size 21%, Rel 9%
	# print(data_frame_t.Age_Dec_31.min())
	# print(data_frame_t.Price.min())
	# print(data_frame_t.Pfmn_Coord.max())
	# print(data_frame_t.Size_Coord.min())

	te_Pfmn_max = data_frame_icr['Pfmn-t']
	te_Size_min = data_frame_icr['Size-t']
	# te_Awareness = 97 - data_frame_t1['Awareness_%'] * 0.67
	# te_Accessibility = 97 - data_frame_t1['Accessibility_%'] * 0.67
	te_Awareness = 90 - data_frame_t1.iat[0,10]*0.67
	te_Accessibility = 90 - data_frame_t1.iat[0,11]*0.67
	te_Total_Demand = data_frame_t1.iat[0,13]
	te_Growth_Rate = 1 + (data_frame_t1.iat[0,14]/100)
	te_total_score = 0.0
	te_total_score = float(data_frame_t5.Dec_Cust_Survey.sum())
	te_able_score = data_frame_t5_Able.iat[0,15]
	te_able_sc_pc = te_able_score / te_total_score
	te_forecast = te_Total_Demand * te_Growth_Rate * te_able_sc_pc
	te_price_range = str(data_frame_t1.iat[0,2]) + str("_")+str(data_frame_t1.iat[0,3])
	te_capacity = ((te_forecast * (te_Growth_Rate**3)) / 2)
	te_avg_price = data_frame_t5.List_Price.astype(float).mean()
	# print(te_Total_Demand)
	# print(te_Growth_Rate)
	# # print(te_Awareness)
	# # print(te_Accessibility)
	# print(te_total_score)
	# print(te_able_score)
	# print(te_able_sc_pc)
	# print(te_forecast)
	# print(te_price_range)
	#print(te_capacity)
	# print(te_avg_price)

	


	data_frame_exp = pd.DataFrame({'Primary_Segment':['Trad'],
								  'Age-Suggested':[0],
								  'Price-Suggested':[0],
								  'Pfmn_Coord-Suggested':[0.0],
								  'Size_Coord-Suggested':[0.0],
								  'Rel-Suggested':[0],
								  'Importance':'Age 47%, Price 23%, Pfmn-Size 21%, Rel 9%',
								  'Pfmn_Coord-Suggested-max':te_Pfmn_max,
								  'Size_Coord-Suggested-min':te_Size_min,
								  'Awareness-Increase-suggested':te_Awareness,
								  'Accessibility-Increase-suggested':te_Accessibility,
								  'Forecast-suggested':te_forecast,
								  'Price-Range':te_price_range,
								  'Capacity-Suggested':te_capacity,
								  'Average_Price':te_avg_price})
								  #index=['Trad', 'Low'])

	data_frame_exp['Primary_Segment'] = 'Trad'
	data_frame_exp['Age-Suggested'] = data_frame_t.Age_Dec_31.min()
	data_frame_exp['Price-Suggested'] = data_frame_t.Price.min()
	data_frame_exp['Pfmn_Coord-Suggested'] = data_frame_t.Pfmn_Coord.max()
	data_frame_exp['Size_Coord-Suggested'] = data_frame_t.Size_Coord.min()
	data_frame_exp['Rel-Suggested'] = data_frame_t.MTBF.min()
	data_frame_exp['Pfmn_Coord-Suggested-max'] = te_Pfmn_max
	data_frame_exp['Size_Coord-Suggested-min'] = te_Size_min
	#print(data_frame_exp)
	#TRADITIONAL

	#LOW END: What's important for Low end: Price 53%, Age 24%, Pfmn-Size 16%, Rel 7%
	# print(data_frame_l.Age_Dec_31.min())
	# print(data_frame_l.Price.min())
	# print(data_frame_l.Pfmn_Coord.max())
	# print(data_frame_l.Size_Coord.min())
	le_age = data_frame_l.Age_Dec_31.min()
	le_price = data_frame_l.Price.min()
	le_Pfmn = data_frame_l.Pfmn_Coord.max()
	le_Size = data_frame_l.Size_Coord.min()
	le_MTBF = data_frame_l.MTBF.min()
	le_imp = 'Price 53%, Age 24%, Pfmn-Size 16%, Rel 7%'
	le_Pfmn_max = data_frame_icr['Pfmn-l']
	le_Size_min = data_frame_icr['Size-l']
	# le_Awareness = 97 - data_frame_l1['Awareness_%'] * 0.67
	# le_Accessibility = 97 - data_frame_l1['Accessibility_%'] * 0.67
	# le_forecast = data_frame_l1.Total_Demand * (data_frame_l1.Market_share/100) * (1 + (data_frame_l1.Growth_Rate / 100)) * 1.1
	# le_score = ( data_frame_l5_Acre.Dec_Cust_Survey / data_frame_t5.Dec_Cust_Survey.sum() + 1 )
	# le_forecast = data_frame_t1.Total_Demand * (data_frame_t1.Growth_Rate / 100) * le_score
	# print(le_score)
	# print(le_forecast)
	le_Awareness = 90 - data_frame_l1.iat[0,10]*0.67
	le_Accessibility = 90 - data_frame_l1.iat[0,11]*0.67
	le_Total_Demand = data_frame_l1.iat[0,13]
	le_Growth_Rate = 1 + (data_frame_l1.iat[0,14]/100)
	le_total_score = 0.0
	le_total_score = float(data_frame_l5.Dec_Cust_Survey.sum())
	le_acre_score = data_frame_l5_Acre.iat[0,15]
	le_acre_sc_pc = le_acre_score / le_total_score
	le_forecast = le_Total_Demand * le_Growth_Rate * le_acre_sc_pc
	le_price_range = str(data_frame_l1.iat[0,2]) + str("_")+str(data_frame_l1.iat[0,3])
	le_capacity = ((le_forecast * (le_Growth_Rate**3)) / 2)
	le_avg_price = data_frame_l5.List_Price.astype(float).mean()
	# print(le_Total_Demand)
	# print(le_Growth_Rate)
	# print(le_total_score)
	# print(le_acre_score)
	# print(le_acre_sc_pc)
	# print(le_forecast)
	#print(le_price_range)

	data_frame_exp1 = data_frame_exp.append({'Primary_Segment': 'Low', 'Age-Suggested': le_age, 'Price-Suggested':le_price, 'Pfmn_Coord-Suggested':le_Pfmn, 'Size_Coord-Suggested':le_Size, 'Rel-Suggested': le_MTBF, 'Importance':le_imp, 'Pfmn_Coord-Suggested-max':le_Pfmn_max, 'Size_Coord-Suggested-min':le_Size_min, 'Awareness-Increase-suggested':le_Awareness, 'Accessibility-Increase-suggested':le_Accessibility, 'Forecast-suggested':le_forecast, 'Price-Range':le_price_range, 'Capacity-Suggested':le_capacity, 'Average_Price':le_avg_price}, ignore_index=True)
	#print(data_frame_exp1)
	#LOW END

	#HIGH END: What's important for High end: Pfmn-Size 43%, Age 29%, Rel 19%, Price 7%
	# print(data_frame_l.Age_Dec_31.min())
	# print(data_frame_l.Price.min())
	# print(data_frame_l.Pfmn_Coord.max())
	# print(data_frame_l.Size_Coord.min())
	he_age = data_frame_h.Age_Dec_31.min()
	he_price = data_frame_h.Price.min()
	he_Pfmn = data_frame_h.Pfmn_Coord.max()
	he_Size = data_frame_h.Size_Coord.min()
	he_MTBF = data_frame_h.MTBF.min()
	he_imp = 'Pfmn-Size 43%, Age 29%, Rel 19%, Price 7%'
	he_Pfmn_max = data_frame_icr['Pfmn-h']
	he_Size_min = data_frame_icr['Size-h']
	# he_Awareness = 97 - data_frame_h1['Awareness_%'] * 0.67
	# he_Accessibility = 97 - data_frame_h1['Accessibility_%'] * 0.67
	# he_forecast = data_frame_h1.Total_Demand * (1 + data_frame_h1.Market_share/100) * (data_frame_h1.Growth_Rate / 100) * 1.1
	he_Awareness = 90 - data_frame_h1.iat[0,10]*0.67
	he_Accessibility = 90 - data_frame_h1.iat[0,11]*0.67
	he_Total_Demand = data_frame_h1.iat[0,13]
	he_Growth_Rate = 1 + (data_frame_h1.iat[0,14]/100)
	he_total_score = 0.0
	he_total_score = float(data_frame_h5.Dec_Cust_Survey.sum())
	he_adam_score = data_frame_h5_Adam.iat[0,15]
	he_adam_sc_pc = he_adam_score / he_total_score
	he_forecast = he_Total_Demand * he_Growth_Rate * he_adam_sc_pc
	he_price_range = str(data_frame_h1.iat[0,2]) + str("_")+str(data_frame_h1.iat[0,3])
	he_capacity = ((he_forecast * (he_Growth_Rate**3)) / 2)
	he_avg_price = data_frame_h5.List_Price.astype(float).mean()
	#print(he_Total_Demand)
	#print(he_Growth_Rate)
	#print(he_total_score)
	#print(he_adam_score)
	#print(he_adam_sc_pc)
	#print(he_forecast)

	data_frame_exp2 = data_frame_exp1.append({'Primary_Segment': 'High', 'Age-Suggested': he_age, 'Price-Suggested':he_price, 'Pfmn_Coord-Suggested':he_Pfmn, 'Size_Coord-Suggested':he_Size,'Rel-Suggested': he_MTBF, 'Importance':he_imp, 'Pfmn_Coord-Suggested-max':he_Pfmn_max, 'Size_Coord-Suggested-min':he_Size_min, 'Awareness-Increase-suggested':he_Awareness, 'Accessibility-Increase-suggested':he_Accessibility, 'Forecast-suggested':he_forecast, 'Price-Range':he_price_range, 'Capacity-Suggested':he_capacity, 'Average_Price':he_avg_price}, ignore_index=True)
	#print(data_frame_exp2)
	#HIGH END

	#PFMN: What's important for Pfmn: Rel 43%, Pfmn-Size 29%, Price 19%, Age 9%
	# print(data_frame_l.Age_Dec_31.min())
	# print(data_frame_l.Price.min())
	# print(data_frame_l.Pfmn_Coord.max())
	# print(data_frame_l.Size_Coord.min())
	hp_age = data_frame_p.Age_Dec_31.min()
	hp_price = data_frame_p.Price.min()
	hp_Pfmn = data_frame_p.Pfmn_Coord.max()
	hp_Size = data_frame_p.Size_Coord.min()
	hp_MTBF = data_frame_p.MTBF.max()
	hp_imp = 'Rel 43%, Pfmn-Size 29%, Price 19%, Age 9%'
	hp_Pfmn_max = data_frame_icr['Pfmn-P']
	hp_Size_min = data_frame_icr['Size-P']
	# hp_Awareness = 97 - data_frame_p1['Awareness_%'] * 0.67
	# hp_Accessibility = 97 - data_frame_p1['Accessibility_%'] * 0.67
	# hp_forecast = data_frame_p1.Total_Demand * (1 + data_frame_p1.Market_share/100) * (data_frame_p1.Growth_Rate / 100) * 1.1
	hp_Awareness = 90 - data_frame_p1.iat[0,10]*0.67
	hp_Accessibility = 90 - data_frame_p1.iat[0,11]*0.67
	hp_Total_Demand = data_frame_p1.iat[0,13]
	hp_Growth_Rate = 1 + (data_frame_p1.iat[0,14]/100)
	hp_total_score = 0.0
	hp_total_score = float(data_frame_h5.Dec_Cust_Survey.sum())
	hp_aft_score = data_frame_p5_Aft.iat[0,15]
	hp_aft_sc_pc = hp_aft_score / hp_total_score
	hp_forecast = hp_Total_Demand * hp_Growth_Rate * hp_aft_sc_pc
	hp_price_range = str(data_frame_p1.iat[0,2]) + str("_")+str(data_frame_p1.iat[0,3])
	hp_capacity = ((hp_forecast * (hp_Growth_Rate**3)) / 2)
	hp_avg_price = data_frame_p5.List_Price.astype(float).mean()
	print(hp_Total_Demand)
	print(hp_Growth_Rate)
	print(hp_total_score)
	print(hp_aft_score)
	print(hp_aft_sc_pc)
	print(hp_forecast)

	data_frame_exp3 = data_frame_exp2.append({'Primary_Segment': 'Pfmn', 'Age-Suggested': hp_age, 'Price-Suggested':hp_price, 'Pfmn_Coord-Suggested':hp_Pfmn, 'Size_Coord-Suggested':hp_Size, 'Rel-Suggested': hp_MTBF, 'Importance':hp_imp, 'Pfmn_Coord-Suggested-max':hp_Pfmn_max, 'Size_Coord-Suggested-min':hp_Size_min, 'Awareness-Increase-suggested':hp_Awareness, 'Accessibility-Increase-suggested':hp_Accessibility, 'Forecast-suggested':hp_forecast, 'Price-Range':hp_price_range, 'Capacity-Suggested':hp_capacity, 'Average_Price':hp_avg_price}, ignore_index=True)
	#print(data_frame_exp3)
	#PFMN

	#SIZE: What's important for Size: Pfmn-Size 43%, Age 29%, Rel 19%, Price 7%
	# print(data_frame_l.Age_Dec_31.min())
	# print(data_frame_l.Price.min())
	# print(data_frame_l.Pfmn_Coord.max())
	# print(data_frame_l.Size_Coord.min())
	hs_age = data_frame_s.Age_Dec_31.min()
	hs_price = data_frame_s.Price.min()
	hs_Pfmn = data_frame_s.Pfmn_Coord.max()
	hs_Size = data_frame_s.Size_Coord.min()
	hs_MTBF = data_frame_s.MTBF.min()
	hs_imp = 'Pfmn-Size 43%, Age 29%, Rel 19%, Price 7%'
	hs_Pfmn_max = data_frame_icr['Pfmn-S']
	hs_Size_min = data_frame_icr['Size-S']
	# hs_Awareness = 97 - data_frame_s1['Awareness_%'] * 0.67
	# hs_Accessibility = 97 - data_frame_s1['Accessibility_%'] * 0.67
	# hs_forecast = data_frame_s1.Total_Demand * (1 + data_frame_s1.Market_share/100) * (data_frame_s1.Growth_Rate / 100) * 1.1
	hs_Awareness = 90 - data_frame_s1.iat[0,10]*0.67
	hs_Accessibility = 90 - data_frame_s1.iat[0,11]*0.67
	hs_Total_Demand = data_frame_s1.iat[0,13]
	hs_Growth_Rate = 1 + (data_frame_s1.iat[0,14]/100)
	hs_total_score = 0.0
	hs_total_score = float(data_frame_s5.Dec_Cust_Survey.sum())
	hs_agape_score = data_frame_s5_Agape.iat[0,15]
	hs_agape_sc_pc = hs_agape_score / hs_total_score
	hs_forecast = hs_Total_Demand * hs_Growth_Rate * hs_agape_sc_pc
	hs_price_range = str(data_frame_s1.iat[0,2]) + str("_")+str(data_frame_s1.iat[0,3])
	hs_capacity = ((hs_forecast * (hs_Growth_Rate**3)) / 2)
	hs_avg_price = data_frame_s5.List_Price.astype(float).mean()
	print(hs_Total_Demand)
	print(hs_Growth_Rate)
	print(hs_total_score)
	print(hs_agape_score)
	print(hs_agape_sc_pc)
	print(hs_forecast)

	data_frame_exp4 = data_frame_exp3.append({'Primary_Segment': 'Size', 'Age-Suggested': hs_age, 'Price-Suggested':hs_price, 'Pfmn_Coord-Suggested':hs_Pfmn, 'Size_Coord-Suggested':hs_Size, 'Rel-Suggested': hs_MTBF, 'Importance':hs_imp, 'Pfmn_Coord-Suggested-max':hs_Pfmn_max, 'Size_Coord-Suggested-min':hs_Size_min, 'Awareness-Increase-suggested':hs_Awareness, 'Accessibility-Increase-suggested':hs_Accessibility, 'Forecast-suggested':hs_forecast, 'Price-Range':hs_price_range, 'Capacity-Suggested':hs_capacity, 'Average_Price':hs_avg_price}, ignore_index=True)
	#print(data_frame_exp4)
	#SIZE
	data_frame_exp4.to_csv('suggested.csv')

def function1a():
	os.chdir('B:\\Travel\\US\\USF_Course\\EIS\\Rounds\\Round1')

	#Buying Criteria
	df_bc = pd.read_csv('buyingcriteria.csv')
	df_bc.columns = df_bc.columns.str.replace(' ','_').str.replace('.','_')
	#Industry Conditions Report
	df_icr = pd.read_csv('icr.csv')
	df_icr.columns = df_icr.columns.str.replace(' ','_').str.replace('.','_')
	#Production Analysis
	df_pa = pd.read_csv('production.csv')
	df_pa.columns = df_pa.columns.str.replace(' ','_').str.replace('.','_')
	#Segment Analysis
	df_sa = pd.read_csv('segmentanalysis.csv')
	df_sa.columns = df_sa.columns.str.replace(' ','_').str.replace('.','_')
	#Check
	# print(df_bc.info())
	# print(df_icr.info())
	#print(df_pa.info())
	# print(df_sa.info())
	#Transform columns
	#col_str = df_pa.Price.str.replace('^$', '', case=False)
	#df.sa1 = df.sa.replace(to_replace=r'^ba.$', value='new', regex=True)
	df_pa['Price'] = df_pa['Price'].replace({'\$':''}, regex=True).astype(float)
	df_pa['Material_Cost'] = df_pa['Material_Cost'].replace({'\$':''}, regex=True).astype(float)
	df_pa['Labor_Cost'] = df_pa['Labor_Cost'].replace({'\$':''}, regex=True).astype(float)
	df_pa['Units_Sold'] = df_pa['Units_Sold'].replace({',':''}, regex=True).astype(int)/100
	df_pa['Contr_Marg'] = df_pa['Contr_Marg'].replace({'%':''}, regex=True).astype(float)
	df_pa['Overtime'] = df_pa['Overtime'].replace({'%':''}, regex=True).astype(float)
	df_pa['Plant_Utiliz'] = df_pa['Plant_Utiliz'].replace({'%':''}, regex=True).astype(float)/10
	df_pa['Capacity_Next_Round'] = df_pa['Capacity_Next_Round'].replace({',':''}, regex=True).astype(float)		
	#print(df_pa['Price'])
	#print(df_pa['Units_Sold'])
	#print(df_pa['Overtime'])
	#print(col_str.head(3))
	#print(df_pa)
	#print(df_pa.info())

	#Filter dataframe by Segment
	df_pa_t = df_pa[df_pa.Primary_Segment == 'Trad']
	df_bc_t = df_bc[df_bc.Primary_Segment == 'Trad']
	df_icr_t = df_icr[df_icr.Round == 4]
	df_sa_t = df_sa[df_sa.Primary_Segment == 'Trad']
	#print(df_pa_t)

	#Draw the plots
	with PdfPages('Round1.pdf') as pdf:
		ax = df_pa_t.plot.bar(x='Name', y=['Units_Sold', 'Price', 'Pfmn_Coord', 'Size_Coord', 'Age_Dec_31', 'Automation_Next_Round', 'Plant_Utiliz'], rot=0, fontsize=5, grid=True)
		mean = df_pa_t['Price'].mean()
		age_exp = df_bc_t['Age_Exp'].sum()
		price_low = df_bc_t['Price_Low_Exp'].sum()
		price_high = df_bc_t['Price_High_Exp'].sum()
		pfmn_exp = df_icr_t['Pfmn_t'].max()
		size_exp = df_icr_t['Size_t'].min()
		ax.axhline(mean, linestyle='-', linewidth=0.5)
		ax.axhline(age_exp, linestyle='-', linewidth=0.7, color='purple')
		ax.axhline(price_low, linestyle='-', linewidth=0.7, color='orange')
		ax.axhline(price_high, linestyle='-', linewidth=0.7, color='orange')
		ax.axhline(pfmn_exp, linestyle='-', linewidth=0.7, color='green')
		ax.axhline(size_exp, linestyle='-', linewidth=0.7, color='red')
		ax.set_title(('Traditional Segment Pos 21%, Age 47%, Price 23%, Rel 9%'), fontsize=10)
		ax.set_yticks(np.arange(0,40, step=1))
		ax.grid(color='g', linestyle='-', linewidth=0.5)
		ax.legend(loc=2, prop={'size':6})
		#second data frame

		pdf.savefig()
		plt.close()
		#plt.show()
		# ax1 = df_pa_t.plot.bar(x='Name', y='Price', rot=0)
		# plt.show()
	print('ok')

def function1b():
	os.chdir('B:\\Travel\\US\\USF_Course\\EIS\\Rounds\\Round')

	#Buying Criteria
	df_bc = pd.read_csv('buyingcriteria.csv')
	df_bc.columns = df_bc.columns.str.replace(' ','_').str.replace('.','_')
	#Industry Conditions Report
	df_icr = pd.read_csv('icr.csv')
	df_icr.columns = df_icr.columns.str.replace(' ','_').str.replace('.','_')
	#Production Analysis
	df_pa = pd.read_csv('production.csv')
	df_pa.columns = df_pa.columns.str.replace(' ','_').str.replace('.','_')
	#Segment Analysis
	df_sa = pd.read_csv('segmentanalysis.csv')
	df_sa.columns = df_sa.columns.str.replace(' ','_').str.replace('.','_')

	#set column object types for production
	df_pa['Price'] = df_pa['Price'].replace({'\$':''}, regex=True).astype(float)
	df_pa['Material_Cost'] = df_pa['Material_Cost'].replace({'\$':''}, regex=True).astype(float)
	df_pa['Labor_Cost'] = df_pa['Labor_Cost'].replace({'\$':''}, regex=True).astype(float)
	df_pa['Units_Sold'] = df_pa['Units_Sold'].replace({',':''}, regex=True).astype(int)/100
	df_pa['Contr_Marg'] = df_pa['Contr_Marg'].replace({'%':''}, regex=True).astype(float)
	df_pa['Overtime'] = df_pa['Overtime'].replace({'%':''}, regex=True).astype(float)
	df_pa['Plant_Utiliz'] = df_pa['Plant_Utiliz'].replace({'%':''}, regex=True).astype(float)/10
	df_pa['Capacity_Next_Round'] = df_pa['Capacity_Next_Round'].replace({',':''}, regex=True).astype(float)
	#set column object types for segment analysis
	df_sa['Market_Share'] = df_sa['Market_Share'].replace({'%':''},regex=True).astype(int)
	df_sa['Cust_Awareness'] = df_sa['Cust_Awareness'].replace({'%':''}, regex=True).astype(int)/10
	df_sa['Cust_Accessibility'] = df_sa['Cust_Accessibility'].replace({'%':''}, regex=True).astype(int)/10
	df_sa['Dec_Cust_Survey'] = df_sa['Dec_Cust_Survey'] / 10

	#Merge production analysis and segment analysis data frames
	df_pa_sa = pd.merge(df_pa, df_sa, on=['Name'])
	#print(df_pa_sa.info())

	#Filter dataframe by Segment
	round_number = input("Enter the Next Round number:")
	df_icr_round = df_icr[df_icr.Round == round_number]
	#Traditional
	df_pa_sa_t = df_pa_sa[df_pa_sa.Primary_Segment == 'Trad']
	df_bc_t = df_bc[df_bc.Primary_Segment == 'Trad']
	#print(df_pa_t)

	#Lowend
	df_pa_sa_l = df_pa_sa[df_pa_sa.Primary_Segment == 'Low']
	df_bc_l = df_bc[df_bc.Primary_Segment == 'Low']

	#Highend
	df_pa_sa_h = df_pa_sa[df_pa_sa.Primary_Segment == 'High']
	df_bc_h = df_bc[df_bc.Primary_Segment == 'High']

	#Performance
	df_pa_sa_p = df_pa_sa[df_pa_sa.Primary_Segment == 'Pfmn']
	df_bc_p = df_bc[df_bc.Primary_Segment == 'Pfmn']

	#Size
	df_pa_sa_s = df_pa_sa[df_pa_sa.Primary_Segment == 'Size']
	df_bc_s = df_bc[df_bc.Primary_Segment == 'Size']

	#Traditional
	#Forecast
	demand = df_icr_round['Total_demand_t'].min()/100
	tot_score = df_pa_sa_t.Dec_Cust_Survey.sum()
	prod_score = df_pa_sa_t[df_pa_sa_t.Name == 'Able'].Dec_Cust_Survey.sum().astype(float)
	score_pc = prod_score / tot_score
	growth = 1 + (df_bc_t.Growth_Rate_Pc.min()/100)
	forecast = (demand * score_pc * growth)
	capacity_4_rounds = forecast * (growth ** 3)
	#print(capacity_4_rounds)
	
	df_pa_sa_t['Forecast'] = 0
	df_pa_sa_t['Capacity_4_Rounds'] = 0
	df_pa_sa_t.loc[df_pa_sa_t['Name'] == 'Able', ['Forecast']] = forecast
	df_pa_sa_t.loc[df_pa_sa_t['Name'] == 'Able', ['Capacity_4_Rounds']] = capacity_4_rounds
	#df_pa_sa_t['Forecast'].loc[df_pa_sa_t.Name == 'Able'] = forecast

	#print(tot_score)
	#print(able_score)
	#print(score_pc)
	#print(growth)
	#print(forecast)
	#print(df_pa_sa_t.Forecast)

	#Lowend
	#Forecast
	demand = df_icr_round['Total_demand_l'].min()/100
	tot_score = df_pa_sa_l.Dec_Cust_Survey.sum()
	prod_score = df_pa_sa_l[df_pa_sa_l.Name == 'Acre'].Dec_Cust_Survey.sum().astype(float)
	score_pc = prod_score / tot_score
	growth = 1 + (df_bc_l.Growth_Rate_Pc.min()/100)
	forecast = (demand * score_pc * growth)
	capacity_4_rounds = forecast * (growth ** 3)
	#print(capacity_4_rounds)
	df_pa_sa_l['Forecast'] = 0
	df_pa_sa_l['Capacity_4_Rounds'] = 0
	df_pa_sa_l.loc[df_pa_sa_l['Name'] == 'Acre', ['Forecast']] = forecast
	df_pa_sa_l.loc[df_pa_sa_l['Name'] == 'Acre', ['Capacity_4_Rounds']] = capacity_4_rounds

	#Highend
	#Forecast
	demand = df_icr_round['Total_demand_h'].min()/100
	tot_score = df_pa_sa_h.Dec_Cust_Survey.sum()
	prod_score = df_pa_sa_h[df_pa_sa_h.Name == 'Adam'].Dec_Cust_Survey.sum().astype(float)
	score_pc = prod_score / tot_score
	growth = 1 + (df_bc_h.Growth_Rate_Pc.min()/100)
	forecast = (demand * score_pc * growth)
	capacity_4_rounds = forecast * (growth ** 3)
	#print(capacity_4_rounds)
	df_pa_sa_h['Forecast'] = 0
	df_pa_sa_h['Capacity_4_Rounds'] = 0
	df_pa_sa_h.loc[df_pa_sa_h['Name'] == 'Adam', ['Forecast']] = forecast
	df_pa_sa_h.loc[df_pa_sa_h['Name'] == 'Adam', ['Capacity_4_Rounds']] = capacity_4_rounds

	#Performance
	#Forecast
	demand = df_icr_round['Total_demand_p'].min()/100
	tot_score = df_pa_sa_p.Dec_Cust_Survey.sum()
	prod_score = df_pa_sa_p[df_pa_sa_p.Name == 'Aft'].Dec_Cust_Survey.sum().astype(float)
	score_pc = prod_score / tot_score
	growth = 1 + (df_bc_p.Growth_Rate_Pc.min()/100)
	forecast = (demand * score_pc * growth)
	capacity_4_rounds = forecast * (growth ** 3)
	#print(capacity_4_rounds)
	df_pa_sa_p['Forecast'] = 0
	df_pa_sa_p['Capacity_4_Rounds'] = 0
	df_pa_sa_p.loc[df_pa_sa_p['Name'] == 'Aft', ['Forecast']] = forecast
	df_pa_sa_p.loc[df_pa_sa_p['Name'] == 'Aft', ['Capacity_4_Rounds']] = capacity_4_rounds

	#Size
	#Forecast
	demand = df_icr_round['Total_demand_s'].min()/100
	tot_score = df_pa_sa_s.Dec_Cust_Survey.sum()
	prod_score = df_pa_sa_s[df_pa_sa_s.Name == 'Agape'].Dec_Cust_Survey.sum().astype(float)
	score_pc = prod_score / tot_score
	growth = 1 + (df_bc_s.Growth_Rate_Pc.min()/100)
	forecast = (demand * score_pc * growth)
	capacity_4_rounds = forecast * (growth ** 3)
	#print(capacity_4_rounds)
	df_pa_sa_s['Forecast'] = 0
	df_pa_sa_s['Capacity_4_Rounds'] = 0
	df_pa_sa_s.loc[df_pa_sa_s['Name'] == 'Agape', ['Forecast']] = forecast
	df_pa_sa_s.loc[df_pa_sa_s['Name'] == 'Agape', ['Capacity_4_Rounds']] = capacity_4_rounds

	#Draw the plots
	filename = str(round_number)+'.pdf'
	#with PdfPages('Round1.pdf') as pdf:
	with PdfPages(filename) as pdf:
		#Traditional
		ax = df_pa_sa_t.plot.bar(x='Name', y=['Units_Sold', 'Price', 'Pfmn_Coord_x', 'Size_Coord_x', 'Age_Dec_31_x', 'Cust_Awareness', 'Cust_Accessibility', 'Dec_Cust_Survey', 'Forecast', 'Capacity_4_Rounds'], rot=0, fontsize=5, grid=True, width=0.7)
		mean = df_pa_sa_t['Price'].mean()
		age_exp = df_bc_t['Age_Exp'].max()
		price_low = df_icr_round['Price_low_t'].min()
		price_high = df_icr_round['Price_high_t'].max()
		pfmn_exp = df_icr_round['Pfmn_t'].max()
		size_exp = df_icr_round['Size_t'].min()
		
		
		ax.axhline(mean, linestyle='-', linewidth=0.5)
		ax.axhline(age_exp, linestyle='-', linewidth=0.7, color='purple')
		ax.axhline(price_low, linestyle='-', linewidth=0.7, color='orange')
		ax.axhline(price_high, linestyle='-', linewidth=0.7, color='orange')
		ax.axhline(pfmn_exp, linestyle='-', linewidth=0.7, color='green')
		ax.axhline(size_exp, linestyle='-', linewidth=0.7, color='brown')
		ax.set_title(('Traditional Segment Pos 21%, Age 47%, Price 23%, Rel 9%'), fontsize=10)
		ax.set_yticks(np.arange(0,40, step=1))
		ax.grid(color='g', linestyle='-', linewidth=0.5)
		ax.legend(loc=1, prop={'size':6})
		#second data frame
		pdf.attach_note("Multiply Units Sold, Forecast and Capacity by 100, Customer Awareness, Accessibility and Dec Cust Survey Score by 10")

		pdf.savefig()
		plt.close()

		#Lowend
		ax = df_pa_sa_l.plot.bar(x='Name', y=['Units_Sold', 'Price', 'Pfmn_Coord_x', 'Size_Coord_x', 'Age_Dec_31_x', 'Cust_Awareness', 'Cust_Accessibility', 'Dec_Cust_Survey', 'Forecast', 'Capacity_4_Rounds'], rot=0, fontsize=5, grid=True, width=0.7)
		mean = df_pa_sa_l['Price'].mean()
		age_exp = df_bc_l['Age_Exp'].max()
		price_low = df_icr_round['Price_low_l'].min()
		price_high = df_icr_round['Price_high_l'].max()
		pfmn_exp = df_icr_round['Pfmn_l'].max()
		size_exp = df_icr_round['Size_l'].min()
		
	
		ax.axhline(mean, linestyle='-', linewidth=0.5)
		ax.axhline(age_exp, linestyle='-', linewidth=0.7, color='purple')
		ax.axhline(price_low, linestyle='-', linewidth=0.7, color='orange')
		ax.axhline(price_high, linestyle='-', linewidth=0.7, color='orange')
		ax.axhline(pfmn_exp, linestyle='-', linewidth=0.7, color='green')
		ax.axhline(size_exp, linestyle='-', linewidth=0.7, color='brown')
		ax.set_title(('Lowend Segment Pos 16%, Age 24%, Price 53%, Rel 7%'), fontsize=10)
		ax.set_yticks(np.arange(0,40, step=1))
		ax.grid(color='g', linestyle='-', linewidth=0.5)
		ax.legend(loc=1, prop={'size':6})
		#second data frame

		pdf.savefig()
		plt.close()

		#Highend
		ax = df_pa_sa_h.plot.bar(x='Name', y=['Units_Sold', 'Price', 'Pfmn_Coord_x', 'Size_Coord_x', 'Age_Dec_31_x', 'Cust_Awareness', 'Cust_Accessibility', 'Dec_Cust_Survey', 'Forecast', 'Capacity_4_Rounds'], rot=0, fontsize=5, grid=True, width=0.7)
		mean = df_pa_sa_h['Price'].mean()
		age_exp = df_bc_h['Age_Exp'].max()
		price_low = df_icr_round['Price_low_h'].min()
		price_high = df_icr_round['Price_high_h'].max()
		pfmn_exp = df_icr_round['Pfmn_h'].max()
		size_exp = df_icr_round['Size_h'].min()
		
		
		ax.axhline(mean, linestyle='-', linewidth=0.5)
		ax.axhline(age_exp, linestyle='-', linewidth=0.7, color='purple')
		ax.axhline(price_low, linestyle='-', linewidth=0.7, color='orange')
		ax.axhline(price_high, linestyle='-', linewidth=0.7, color='orange')
		ax.axhline(pfmn_exp, linestyle='-', linewidth=0.7, color='green')
		ax.axhline(size_exp, linestyle='-', linewidth=0.7, color='brown')
		ax.set_title(('Highend Segment Pos 43%, Age 29%, Price 9%, Rel 19%'), fontsize=10)
		ax.set_yticks(np.arange(0,40, step=1))
		ax.grid(color='g', linestyle='-', linewidth=0.5)
		ax.legend(loc=1, prop={'size':6})
		#second data frame

		pdf.savefig()
		plt.close()

		#Performance
		ax = df_pa_sa_p.plot.bar(x='Name', y=['Units_Sold', 'Price', 'Pfmn_Coord_x', 'Size_Coord_x', 'Age_Dec_31_x', 'Cust_Awareness', 'Cust_Accessibility', 'Dec_Cust_Survey', 'Forecast', 'Capacity_4_Rounds'], rot=0, fontsize=5, grid=True, width=0.7)
		mean = df_pa_sa_p['Price'].mean()
		age_exp = df_bc_p['Age_Exp'].max()
		price_low = df_icr_round['Price_low_p'].min()
		price_high = df_icr_round['Price_high_p'].max()
		pfmn_exp = df_icr_round['Pfmn_p'].max()
		size_exp = df_icr_round['Size_p'].min()
		
		
		ax.axhline(mean, linestyle='-', linewidth=0.5)
		ax.axhline(age_exp, linestyle='-', linewidth=0.7, color='purple')
		ax.axhline(price_low, linestyle='-', linewidth=0.7, color='orange')
		ax.axhline(price_high, linestyle='-', linewidth=0.7, color='orange')
		ax.axhline(pfmn_exp, linestyle='-', linewidth=0.7, color='green')
		ax.axhline(size_exp, linestyle='-', linewidth=0.7, color='brown')
		ax.set_title(('Performance Segment Pos 29%, Age 9%, Price 19%, Rel 43%'), fontsize=10)
		ax.set_yticks(np.arange(0,40, step=1))
		ax.grid(color='g', linestyle='-', linewidth=0.5)
		ax.legend(loc=1, prop={'size':6})
		#second data frame

		pdf.savefig()
		plt.close()

		#Size
		ax = df_pa_sa_s.plot.bar(x='Name', y=['Units_Sold', 'Price', 'Pfmn_Coord_x', 'Size_Coord_x', 'Age_Dec_31_x', 'Cust_Awareness', 'Cust_Accessibility', 'Dec_Cust_Survey', 'Forecast', 'Capacity_4_Rounds'], rot=0, fontsize=5, grid=True, width=0.7)
		mean = df_pa_sa_s['Price'].mean()
		age_exp = df_bc_s['Age_Exp'].max()
		price_low = df_icr_round['Price_low_s'].min()
		price_high = df_icr_round['Price_high_s'].max()
		pfmn_exp = df_icr_round['Pfmn_s'].max()
		size_exp = df_icr_round['Size_s'].min()
		
		
		ax.axhline(mean, linestyle='-', linewidth=0.5)
		ax.axhline(age_exp, linestyle='-', linewidth=0.7, color='purple')
		ax.axhline(price_low, linestyle='-', linewidth=0.7, color='orange')
		ax.axhline(price_high, linestyle='-', linewidth=0.7, color='orange')
		ax.axhline(pfmn_exp, linestyle='-', linewidth=0.7, color='green')
		ax.axhline(size_exp, linestyle='-', linewidth=0.7, color='brown')
		ax.set_title(('Size Segment Pos 43%, Age 29%, Price 9%, Rel 19%'), fontsize=10)
		ax.set_yticks(np.arange(0,40, step=1))
		ax.grid(color='g', linestyle='-', linewidth=0.5)
		ax.legend(loc=1, prop={'size':6})
		#second data frame

		pdf.savefig()
		plt.close()


	print('ok')


def function2():
	#basic rules

	print('ok')

def main():
	#function1()
	#function1a()
	function1b()
	function2()

main()

#Read the practice round values and predict the values other teams might set. 
#Use the round values to predict the maximum extent teams may go. Use the practice round movements to estimate the possible values.
#
#How are we doing on the investments when compared to others? More bang for buck - check Capstone courier SG&A / Sales
#How are we doing on contribution margin? Changes to product vs sales margin? 
#Hows our sales compared to others? % of sales
#How to increase Book value, P/E, Stock price
#


#references
#https://medium.com/@chaimgluck1/working-with-pandas-fixing-messy-column-names-42a54a6659cd
#https://cmdlinetips.com/2018/02/how-to-subset-pandas-dataframe-based-on-values-of-a-column/
#https://pythonforbiologists.com/when-to-use-aggregatefiltertransform-in-pandas/
#https://thispointer.com/python-pandas-how-to-add-rows-in-a-dataframe-using-dataframe-append-loc-iloc/
#https://www.shanelynn.ie/select-pandas-dataframe-rows-and-columns-using-iloc-loc-and-ix/
#https://towardsdatascience.com/5-methods-to-remove-the-from-your-data-in-python-and-the-fastest-one-281489382455
#Clean up data in columns: https://towardsdatascience.com/seven-clean-steps-to-reshape-your-data-with-pandas-or-how-i-use-python-where-excel-fails-62061f86ef9c
#Replace data, $, % in columns https://stackoverflow.com/questions/43096522/remove-dollar-sign-from-entire-python-pandas-dataframe?rq=1
#https://stackoverflow.com/questions/34347145/pandas-plot-doesnt-show
#https://stackoverflow.com/questions/42128467/matplotlib-plot-multiple-columns-of-pandas-data-frame-on-the-bar-chart
#https://stackoverflow.com/questions/46828689/adding-avg-line-to-bar-plot-using-read-excel-pandas-matplotlib
#https://stackoverflow.com/questions/35484458/how-to-export-to-pdf-a-graph-based-on-a-pandas-dataframe
#Set bar values: https://matplotlib.org/examples/api/barchart_demo.html
#Set bar values: http://composition.al/blog/2015/11/29/a-better-way-to-add-labels-to-bar-charts-with-matplotlib/
#Set y xis intervals or yticks https://matplotlib.org/api/_as_gen/matplotlib.pyplot.yticks.html
#Set grid width: https://matplotlib.org/api/_as_gen/matplotlib.axes.Axes.grid.html
#Plot inputs: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.plot.html
#size of legend: https://stackoverflow.com/questions/7125009/how-to-change-legend-size-with-matplotlib-pyplot
#Update an element using .iloc: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.loc.html
#Write plots to PDF https://matplotlib.org/gallery/misc/multipage_pdf.html
#Get keyboard input: https://www.python-course.eu/python3_input.php



# Python Operator	Pandas Method(s)
# +	add()
# -	sub(), subtract()
# *	mul(), multiply()
# /	truediv(), div(), divide()
# //	floordiv()
# %	mod()
# **	pow()