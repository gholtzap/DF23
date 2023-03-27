# Mapping The Meltdown
**Python packages used**
* pandas
* geopandas
* matplotlib
* zipcodes


![TitleSlide](https://cdn.discordapp.com/attachments/660884610313486346/1089682978638155906/image.png)

Our team investigated the effects of education, family and children, health and disability, housing and homelessness, income maintenance, individual rights, employment status, and other internal and external factors on an individual’s income level based on clients that needed legal advice provided by the American Bar Association (ABA).<br />
<br />
To analyze the effect of these factors on the individuals that go to the ABA for legal advice, we first parsed the annual income of each client from the clients.csv file to see which clients disclosed their annual income. If clients did not disclose their annual income due to confidentiality of personal data, indicated as ‘NULL’, these clients were not included in the final collection of annual income data. Using the annual income data, we created a heat map using the Python matplotlib package, the Python geopandas package, and the 2014 US map from the US Census to visualize the spectrum of income distributions of many regions of the United States (US). As the ABA provides pro bono online services in some states and territories, only 36 states were considered in this data analysis; the states with no income data are colored white. To find the concentration of individuals in certain regions of the US where they face at least one of the effects of education, family and children, health and disability, housing and homelessness, income maintenance, individual rights, employment status, and other internal and external factors, we created a heat map for each of these factors based off of specific keywords describing common issues from clients from certain states to lawyers. These heat maps are superimposed onto the original income heat map so that the data visually depict potential reasons why certain regions of low or high income may be experiencing certain issues in their area.
<br /><br />Our initial intuition was that if clients had a lower income, then those clients would not be able to afford a house or be able to pay their mortgages on their current 
house. Thus, we deduced that housing and homelessness is the factor that most reflected an individual’s income level. We used the Python pandas package to analyze the 
income data, the Python matplotlib to analyze the housing data, and the Python geopandas package to create the heatmaps of home retentions by state to visualize the spectrum of housing retention of many regions of the US.
Although we intuitively reasoned that housing and homelessness was the main factor in qualitatively determining an individual’s income level, by conducting the random 
forest machine learning algorithm on the client data, questions data, and question posts data, we found a different conclusion. To conduct this machine learning algorithm,
first the clients.csv, questions.csv, and questionposts.csv files were parsed for the annual income, state, and county of each client. Then, the clients’ annual income 
and their state and county of residence were used to implement a random forest machine learning algorithm using the Python sklearn library and the Python pandas library 
to generate a confusion matrix and predict what may be the common problems clients are communicating to lawyers from the ABA. We found that this machine learning 
algorithm predicts that family and children issues most reflect an individual’s income level.<br />
<br />
Although this is not an exhaustive list of all potential patterns and trends we see from all of the data, we took the most relevant and important pieces of information to conclude that
Clients from Florida mostly voice their issues about housing and homelessness to lawyers.
In general, family and children are the main issues that clients communicate about to lawyers across the US.
In an attempt to remedy these issues from this data analysis, practicing lawyers in law school should be well-versed in communicating and responding professionally and empathetically about housing issues in Florida and family and children issues across the US.

![TitleSlide](https://cdn.discordapp.com/attachments/660884610313486346/1089683037731684363/image.png)

![TitleSlide](https://cdn.discordapp.com/attachments/660884610313486346/1089683091490086912/image.png)
