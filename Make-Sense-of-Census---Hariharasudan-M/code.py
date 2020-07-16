# --------------
# Importing header files
import numpy as np
import warnings

warnings.filterwarnings('ignore')

#New record
new_record=[[50,  9,  4,  1,  0,  0, 40,  0]]

#Reading file
data = np.genfromtxt(path, delimiter=",", skip_header=1)
print(data.shape)
census=np.concatenate((data,new_record),axis=0)
print(census.shape)
#age
age=census[:,0]
max_age=age.max()
min_age=age.min()
age_mean=age.mean()
age_std=age.std()
print('Max Age=',max_age)
print('Min Age=',min_age)
print('Mean of ages=',age_mean)
print('Standard deviation of ages=',age_std)
#Race
race=census[:,2]
mask_0=race==0
race_0=np.array(race[mask_0])
len_0=len(race_0)
print('No. of Person in Race 0=',len_0)
mask_1=race==1
race_1=np.array(race[mask_1])
len_1=len(race_1)
print('No. of Person in Race 1=',len_1)
mask_2=race==2
race_2=np.array(race[mask_2])
len_2=len(race_2)
print('No. of Person in Race 2=',len_2)
mask_3=race==3
race_3=np.array(race[mask_3])
len_3=len(race_3)
print('No. of Person in Race 3=',len_3)
mask_4=race==4
race_4=np.array(race[mask_4])
len_4=len(race_4)
print('No. of Person in Race 4=',len_4)
len_of_each_race=np.array([len_0,len_1,len_2,len_3,len_4])
print(len_of_each_race)
minority_race=np.argmin(len_of_each_race, axis=0)
print('Minority race=',minority_race)
#senior_Citizens
senior_citizens=census[census[:,0]>60]
senior_citizens_len=len(senior_citizens)
working_hours_sum=sum(senior_citizens[:,6])
print('working hours sum=',working_hours_sum)
avg_working_hours=(working_hours_sum/senior_citizens_len)
print('average working hours',avg_working_hours)
#Income based on education: true or false
high=census[census[:,1]>10]
low=census[census[:,1]<=10]
avg_pay_high=np.mean(high[:,7])
avg_pay_low=np.mean(low[:,7])
print('Avg pay high=',avg_pay_high)
print('Avg pay low=',avg_pay_low)
compare=np.array_equal(avg_pay_high,avg_pay_low)
print(compare)


