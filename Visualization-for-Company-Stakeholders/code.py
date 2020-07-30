# --------------
#Importing header files
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


#Reading the file
data=pd.read_csv(path)

#Code starts here

# Step 1 
#Reading the file
loan_status=data['Loan_Status'].value_counts()
plt.bar(loan_status.index,loan_status)
plt.show()

#Creating a new variable to store the value counts


#Plotting bar plot



# Step 2
#Plotting an unstacked bar plot
property_and_loan=data.groupby(['Property_Area','Loan_Status']).size().unstack()
property_and_loan.plot(kind='bar', stacked=False)
plt.xlabel('Property Area')
plt.ylabel('Loan Status')
#Rotating the ticks of X-axis
plt.xticks(rotation=45)
# Step 3
#Plotting a stacked bar plot
#Changing the x-axis label
#Changing the y-axis label
#Rotating the ticks of X-axis
# Step 4 
#Subsetting the dataframe based on 'Education' column
education_and_loan=data.groupby(['Education','Loan_Status']).size().unstack()
education_and_loan.plot(kind='bar', stacked=True)
#Subsetting the dataframe based on 'Education' column
plt.xlabel('Education Status')
plt.ylabel('Loan Status')
plt.xticks(rotation=45)
#Plotting density plot for 'Graduate'

graduate=data[data['Education']=='Graduate']
#Plotting density plot for 'Graduate'
not_graduate=data[data['Education']=='Not Graduate']
graduate['LoanAmount'].plot(kind='density', label='Graduate')
not_graduate['LoanAmount'].plot(kind='density', label='Not Graduate')
#Code ends here
#For automatic legend display
plt.legend()

# Step 5
#Setting up the subplots

fig, (ax_1,ax_2,ax_3)=plt.subplots(3,1)
#Plotting scatter plot
data.plot.scatter('ApplicantIncome','LoanAmount',ax=ax_1)
ax_1.set_xlabel('Application Income')
#Setting the subplot axis title
data.plot.scatter(x='CoapplicantIncome',y='LoanAmount', ax=ax_2)
ax_2.set_xlabel('Coapplicant Income')


data['TotalIncome'] = data['ApplicantIncome']+data['CoapplicantIncome']
data.plot.scatter(x='TotalIncome',y='LoanAmount', ax=ax_3)
ax_3.set_xlabel('Total Income')




