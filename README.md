# User Activity Data Analysis for SalesTech StartUp ELTROPY

### A little about ELTROPY
Eltropy empowers financial services companies to engage clients and sell financial products over Text Messaging.
A once-in-a-generation communication revolution is underway: a shift from emails, phone calls to Messaging. 95% of text messages are opened and read within 3 minutes, and responded to within 90 seconds.
Eltropy’s technology allows client-facing teams to leverage Messaging platforms like iMessage, SMS, Facebook Messenger etc. to engage prospects and clients in a whole new way. Which results in an 11x increase in client engagement and Sales conversion metrics.

### Data as a door to find customers' behavior
1. What does the data tell us?
2. Does the behavior of the customer differ based on geographical locations, industry type, time of day, day of week, month?
3. Can we identify on-the-fence customers? How soon can we do that?
4. Are there any underlying "View" patterns specific to a certain industry type? Can we   generalize for all customers?
5. Can we use insights from one industry for another?
6. What can help the business leaders in focusing and prioritizing efforts and brain power?
7. Recommendation for future data collection efforts.

### Data Format
Data was from four customers of Eltropy, from varying industries, of user activities "Share" and "View". The data had about 12 features, all but one ("Time spent in seconds") being categorical features. Each row is an activity. The features being in the following format.
https://github.com/UrmiM/Capstone/blob/master/Data/Data_Format_Example.png

### Truth about the Data
1. The data has 6000 rows but information is for only 600 users. It is not possible to get good predictions since no information is available about the content. The only feature with good signal is "Time Spent In Seconds".
2. Also, there is no conversion data, therefore classification was not possible.
3. Linear Regression was implemented to predict the "Time Spent per View" with dummified features for month, day of week, viewing device, browser type, time of day etc. but the r2 for the model is very low.
4. Random Forest Regressor was implemented as well for the same feature set, but there was no improvement seen in the prediction. Cross Validation using the train_test_split.
5. Fitted a Logistic Classification Model, by assuming 20% randomly selected users with number of views greater than the mean converted, accuracy of about 85%.
6. Gives indication that if the content type, size was known and adding varied weights on the content files can give us prediction for possible conversion.

### Some Insights
1. The distribution of the view time across the industries varies from a mean of 1 minute to 4 minutes.
2. The maximum views happened during the weekdays across all the industries except one which had an unusual pattern of the views peaking on Thursdays.
3. Study in-depth why this pattern exists and whether it increases view rate.
4. Future data collection should include more content and conversion information.

### Company's Response
1. Very excited to see the data visualization of user activity for all customers compared to each other.
2. This analysis will help them show their customers what can be done with the data.
3. Could potentially convince the customers to release more data for more predictive analyses in future.  
